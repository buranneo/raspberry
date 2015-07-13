#!/usr/bin/env python

from time import time
import subprocess

stateFile = open("state_log.txt", "a", 0)
print >>stateFile, time(), "start"

def getState(mac, real_state):
    state = "0"
    if mac == "none":
        state = "-1"

    if subprocess.Popen("[ -f /home/pi/position/" + mac + ".pos ]", shell=True).wait() == 0:
        state = subprocess.check_output("tail -1 /home/pi/position/" + mac + ".pos | cut -b8- | tr '\t' ' ' | perl -pe \"s/\[\d+, \'(\d+.\d+)\'\]/\$1/g\"", shell=True)
    else:
        state = "1"

    print >>stateFile, time(), mac, real_state
    return state


