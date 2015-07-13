#!/bin/sh -eu

if [ ! -f $1 ]; then
    echo "#!/usr/bin/env bash" > $1
    echo "set -eu" >> $1
    echo >> $1
    echo >> $1
    chmod +x $1
fi

#mcedit +4 $1
vim +4 $1

