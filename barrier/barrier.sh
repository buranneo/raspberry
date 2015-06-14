#!/bin/sh
set -e

if [ $# -ge 1 ]; then
	# toggle, set/0, set/1
	wget -q -O /dev/null http://192.168.2.1/cgi-bin/led/$1
else
	while true; do
		/bin/barrier.py
		sleep 1
	done
fi


