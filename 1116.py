import threading

#creat global ThreadLocal obj
local_school = threading.local()


s = 'ABC\\-001'

import re
print (re.match(r'^\d{3}\-\d{3,8}$','010-12345'))

print ('a b   c'.split(' '))
print (re.split(r'\s+','a b  c'))

print (re.split(r'[\s\,\;]+','a,b;; c d'))

m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print (m)
print (m.group(0))
print (m.group(1))

mail = re.match (r'^([0-9a-zA-Z\_]+)@([0-9a-zA-Z]+).(com)','miaozaiye@proginn.com')

print (mail.group(0))
print (mail.group(1))
print (mail.group(2))