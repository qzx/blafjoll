#!/usr/bin/env python # -*- coding: utf-8 -*-
import requests 
import json

api_key = 'AVJI83ZF4RZD02YIJYGKODX36'
notification_title = 'Bláfjöll Opin'
notification_message = 'Opið er í Bláfjöllum, lets gooo!'
url = "https://www.notifymydevice.com/push"
data = {"ApiKey": api_key, "PushTitle": notification_title,"PushText": notification_message}
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)

if r.status_code == 200:
    print ('Notification sent!')
else:
    print('Error while sending notificaton!')
