#!/bin/sh

dpkg -l > logs/dpkg_$1.log
python -c "help(\"modules\")" > logs/python_modules_$1.log


