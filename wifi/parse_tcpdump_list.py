#!/usr/bin/python

from sys import stdin, stdout, stderr, argv
from os import fdopen

mac_logout_time = 100

mac_hash = {}
sumDb = 0
nDb = 0
lastSec = "0"

ub_stdout = fdopen(stdout.fileno(), 'w', 0)

#ub_mac_logout = open(argv[1], "a", 0)

for line in stdin:
    fields = line.rstrip().split()
    time = fields[0]
    sec = time.split(".",1)[0]

    macTA = ""
    db = 100
    for f in fields:
        if f.startswith("-") and f.endswith("dB"):
            db = int(f.split("-",1)[1].split("d",1)[0])
        if f.startswith("TA:") or f.startswith("SA:"):
            macTA = f.split(":",1)[1]

    if int(sec) - int(lastSec) >= mac_logout_time:
        for mac in mac_hash.keys():
            [nDb_prn, sumDb_prn] = mac_hash[mac]
            avgDb_prn = float(sumDb_prn) / nDb_prn
            #ub_stdout.write("\t".join(map(str, [sec, mac, nDb_prn, "%.2f" % avgDb_prn])) + "\n")
            #ub_mac_logout.write("\t".join(map(str, [sec, mac, nDb_prn, "%.2f" % avgDb_prn])) + "\n")
        mac_hash = {}
        lastSec = sec

    if macTA != "":
        if macTA not in mac_hash:
            mac_hash[macTA] = [0, 0]
        mac_hash[macTA] = [x + y for x, y in zip(mac_hash[macTA], [1, db])]

    if macTA == "bc:f5:ac:e1:e0:06":
        if lastSec != sec and lastSec > 0 and nDb > 0:
            avgDb = float(sumDb) / nDb
            ub_stdout.write("\t".join(map(str, [sec, nDb, "%.2f" % avgDb])) + "\n")
            sumDb = 0
            nDb = 0
        sumDb += db
        nDb += 1
        lastSec = sec



