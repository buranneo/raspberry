#!/bin/sh -eu

if [ ! -f $1 ]; then
    echo "#!/usr/bin/env perl" > $1
    echo "use strict;" >> $1
    echo >> $1
    chmod +x $1
fi

#mcedit +3 $1
vim +3 $1


