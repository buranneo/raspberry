#!/bin/sh -eu

if [ ! -f $1 ]; then
    echo "#!/usr/bin/env python" > $1
    echo >> $1
    echo >> $1
    chmod +x $1
fi

vim +3 $1
