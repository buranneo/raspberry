#!/bin/sh -eu

if [ ! -f $1 ]; then
    echo "#!/bin/sh -eu" > $1
    echo >> $1
    echo >> $1
    chmod +x $1
fi

mcedit +3 $1
