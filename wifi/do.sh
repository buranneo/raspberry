#!/usr/bin/env bash
set -eu

dump_list_macs() {
    tcpdump.sh $1 | parse_tcpdump_list.py
}

dump_seen_macs() {
    tcpdump.sh $1 | parse_tcpdump.py /home/pi/logs/macs_wlan$1.tsv
}

$@


