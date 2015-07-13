#!/usr/bin/env python

import threading
from time import sleep, time
import tail
import subprocess
from sys import stderr

hwaddr_list = [
    '00:13:ef:ca:02:3c', # orange ball
    '00:13:ef:c0:04:be', # 2
    '00:13:ef:c7:03:c4', # 3
    '00:13:ef:ca:07:1a', # 4
    '00:13:ef:c7:04:3c'  # 5
]

mac_list = {}
state_file_tail = tail.Tail("/home/pi/dev/flask/state_log.txt")
sec_for_rm_mac = 10

def update_mac_list(line):
    fields = line.rstrip().split()
    if len(fields) == 3:
        [time, mac, state] = fields
        if mac in mac_list:
            mac_list[mac][0] = [time, state]
        else:
            mac_list[mac] = [[time, state]] + [[0, 0, 0, 0, 0] for i in range(len(hwaddr_list))]

state_file_tail.register_callback(update_mac_list)

thread_update_mac_list = threading.Thread(target=state_file_tail.follow)
thread_update_mac_list.daemon = True

def rm_old_mac():
    while True:
        for mac in list(mac_list):
            if float(mac_list[mac][0][0]) < time() - sec_for_rm_mac:
                del(mac_list[mac])
        sleep(1)

thread_rm_old_mac = threading.Thread(target=rm_old_mac)
thread_rm_old_mac.daemon = True

tcpdump_exe = ["tcpdump", "-tt", "-nei"]

def run_tcpdump_parse(hw_id):
    mon_id = thread_tcpdump_parse[hw_id][2]
    p = subprocess.Popen(tcpdump_exe + ["mon" + str(mon_id)], stdout=subprocess.PIPE)
    thread_tcpdump_parse[hw_id][1] = True
    while True:
        for line in p.stdout:
            fields = line.rstrip().split()
            time = fields[0]
            sec = str(int(float(time)))
            macTA = ""
            db = 100
            for f in fields:
                if f.startswith("-") and f.endswith("dB"):
                    db = int(f.split("-",1)[1].split("d",1)[0])
                if f.startswith("TA:") or f.startswith("SA:"):
                    macTA = f.split(":",1)[1]
            if macTA != "":
                if macTA in mac_list:
                    rec = mac_list[macTA][1 + hw_id]
                    if sec != rec[0]:
                        rec[0] = sec
                        rec[1] = rec[3]
                        if rec[3] == 0:
                            rec[2] = 100
                        else:
                            rec[2] = float(rec[4]) / rec[3]
                        rec[3:5] = [0, 0]
                    rec[3:5] = [x + y for x, y in zip(rec[3:5], [1, db])]


        sleep(0.1)

thread_tcpdump_parse = {}
for mon_id in map(int, subprocess.check_output("iwconfig 2>/dev/null | grep mon | cut -c4-5", shell=True).split()):
    mac = subprocess.check_output("ifconfig wlan%d | grep -oP \"(\w{2}\:){5}\w{2}\"" % mon_id, shell = True).rstrip()
    for i in range(len(hwaddr_list)):
        if mac == hwaddr_list[i]:
            thread_tcpdump_parse[i] = [threading.Thread(target=run_tcpdump_parse, args=[i]), False, mon_id]
            thread_tcpdump_parse[i][0].daemon = True

thread_update_mac_list.start()
thread_rm_old_mac.start()
for thread in thread_tcpdump_parse.values():
    thread[0].start()
while True:
    sleep(1)
    print >>stderr, [t[1] for t in thread_tcpdump_parse.values()]
    for mon_id, thread in thread_tcpdump_parse.items():
        if not thread[1]:
            print >>stderr, "restart", mon_id
            thread[0].join(1)
            thread[0] = threading.Thread(target=run_tcpdump_parse, args=[mon_id])
            thread[0].daemon = True
            thread[0].start()
            continue
    break

while True:
    pool_file = open("/home/pi/position/pool.tsv", "a", 0)
    print >>stderr, mac_list
    for mac in mac_list.keys():
        rec = mac_list[mac]
        print "\t".join(map(str, [mac, rec[0]] + [[a[1], "%.2f" % a[2]] for a in rec[1:]]))
        mac_file = open("/home/pi/position/" + mac + ".pos", "a", 0)
        print >>mac_file, "\t".join(map(str, [rec[0][0]] + [[a[1], "%.2f" % a[2]] for a in rec[1:]]))

        print >>pool_file, "\t".join(map(str, \
            [time(), rec[0][1], rec[0][0], mac] + \
            ["%d\t%.2f" % (a[1], a[2]) for a in rec[1:]] \
        ))
    sleep(1)


