from app import app, bState, logFile, scripts
from scripts import *
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return 'hello world.\n'

@app.route('/ping')
def ping():
    return 'pong\n'

@app.route('/state')
def state():
    mac = request.args.get('mac', 'none')
    real_state = request.args.get('real', 'none')
    state = getState(mac, real_state)
    return state + "\n"

@app.route('/barrier/close')
def barrier_close():
    bState = 'closed\n'
    return 'ok\n'

@app.route('/barrier/open')
def barrier_open():
    bState = 'open\n'
    return 'ok\n'

@app.route('/barrier/toggle')
def barrier_toggle():
    bState = 'open\n'
    return 'ok\n'

