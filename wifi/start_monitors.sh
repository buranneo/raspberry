#!/bin/sh
set -e

channel=${1:-11}

iwconfig 2> /dev/null | perl -ane 'print "$1\n" if m{wlan(\d+)}' | while read wlanId; do
    echo "wlan$wlanId"
    iwconfig 2> /dev/null | grep -q mon$wlanId || ./add_monitor.sh $wlanId
    ./set_channel.sh $wlanId $channel    
done


