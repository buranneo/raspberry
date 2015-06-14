#!/bin/sh
set -ex

run() {
	bdaddr -r -i hci$1 $2
	sleep 1
	ibeacon $4 $3 $5 $6 -29 $1
}

if [ "$#" -eq "0" ]; then
  run 0 00:1A:7D:DA:71:00 e2c56db5dffb48d2b060d0f5a71096e0 100 0 0 > hci0.log 2> hci0.errlog &
  run 1 00:1A:7D:DA:71:01 e2c56db5dffb48d2b060d0f5a71096e1 100 1 0 > hci1.log 2> hci1.errlog &
  run 2 00:1A:7D:DA:71:02 e2c56db5dffb48d2b060d0f5a71096e2 100 2 0 > hci2.log 2> hci2.errlog &
else
  run $@
fi
