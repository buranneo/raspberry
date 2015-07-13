#!/usr/bin/env python

from flask import Flask

bState = "n/a"
logFile = open("my_log.txt", "a", 0)
print >>logFile, "start log"
app = Flask(__name__)
from app import views
