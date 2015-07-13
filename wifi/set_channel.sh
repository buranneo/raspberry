#!/bin/sh

ifconfig wlan${1:-0} down
iw mon${1:-0} set channel ${2:-2}
ifconfig mon${1:-0} up


