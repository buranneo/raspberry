#!/bin/sh
set -e

killall start_ibecon.sh
killall ibeacon

for h in `hciconfig | grep hci | cut -d':' -f1`; do
	hciconfig $h reset
done
