#!/bin/sh

tcpdump -tt -nei mon${1:-0}
