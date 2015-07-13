#!/bin/sh
set -e

iw dev wlan$1 interface add mon$1 type monitor
ifconfig mon$1 up
#tcpdump -nei mon$1


