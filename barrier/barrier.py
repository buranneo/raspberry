#!/usr/bin/python


import time
import json, requests


api_host = 'http://app.dapoint.ru'
pointId = 'c04a021a-8c3b-4d5a-b5d0-16023444916d'
secret  = 'abc'

url = api_host + '/api/v1/heartbeat/' + pointId

open_url = 'http://192.168.2.1/cgi-bin/led/set/1'
close_url = 'http://192.168.2.1/cgi-bin/led/set/0'

while 1:
    try:
        print('Loading url', url)
        data = { 'secret': secret }
        resp = requests.post(url=url, data=data)

        print resp

        data = json.loads(resp.text)
        if data['result'] == 'open':
            print '======== Open barrier'
            requests.get(url=open_url)
            time.sleep(10)
            requests.get(url=close_url)
        else:
            print data
    except Exception, e:
        print e
        time.sleep(5)
    finally:
        pass
