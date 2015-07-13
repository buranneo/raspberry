#!/usr/bin/env bash
set -eu

ifconfig wlan${1:-0} | perl -ne 'print $1 if m{HWaddr ([\w\:]+)}'

