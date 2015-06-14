# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

import bluetooth._bluetooth as bluez

n = 2
m = 1

dev_ids = [0, 1, 2]
socks = {}
try:
	for dev_id in dev_ids:
		socks[dev_id] = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

for dev_id in dev_ids:
	blescan.hci_le_set_scan_parameters(socks[dev_id])
	blescan.hci_enable_le_scan(socks[dev_id])

rssi = [[] for i in dev_ids]
while True:
	for dev_id in dev_ids:
		returnedList = blescan.parse_events(socks[dev_id], 1)
		for beacon in returnedList:
			fields = beacon.split(',')
			if fields[0] == "ea:2e:a4:78:79:26":
				rssi[dev_id].append(int(fields[5]))
				#print dev_id, beacon
	if sum([len(rssi[i]) >= m for i in dev_ids]) == len(dev_ids):
		rssi_avg = [float(sum(a)) / len(a) for a in rssi]
		avg = sum(rssi_avg) / len(rssi_avg)
		print avg, rssi_avg, rssi
		rssi = [[] for i in dev_ids]

