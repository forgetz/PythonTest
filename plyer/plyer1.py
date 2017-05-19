#!/usr/bin/env python
# -- coding: utf-8 --
from plyer import notification,battery

batpercent = battery.status['percentage']

messages = "แบตเตอรี่ เหลือ %s percent." % batpercent
messages = unicode(messages, "utf-8")
notification.notify(title='TEST', message=messages, app_name='MyPythonApp', app_icon='', timeout=10)

print(battery.status)
print(battery.status['percentage'])