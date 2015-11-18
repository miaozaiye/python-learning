'''
from datetime import datetime
now = datetime.now() # acquire current datetime
print (now)

# try regular expression

import re

s = re.split(r'[\s]', str(now))
print (s)

m = re.match(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',s[0])

print (m.group(0),m.group(1),m.group(2),m.group(3))

dt = datetime(2015,4,19,12,20)
print (dt)

print (dt.timestamp())

from datetime import timedelta,timezone

tz_utc_8 = timezone(timedelta(hours = 8))
now = datetime.now()
print (now)

dt = now.replace(tzinfo = tz_utc_8)
print (dt)

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)

print (utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print (bj_dt)

t = dt.timestamp()
print (datetime.fromtimestamp(t))

print (datetime.utcfromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print (cday)

now = datetime.now()
print (now + timedelta(hours = -10))
print (now + timedelta(days = 1))

'''
# -*- coding:utf-8 -*-


import re
from datetime import datetime, timezone, timedelta



def to_timestamp(dt_str, tz_str):
  utct = int(re.split(r'\:',tz_str)[0][3:])
  utc = timezone(timedelta(hours=utct))
  res = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc)
  return res.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')



