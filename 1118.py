# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
#now = datetime.now()
#print (now)
#print (type(now))

#print (now.timestamp())

from datetime import datetime,timedelta
import re

def to_timestamp(dt_str, tz_str):
	#获取时区数字
    tz_num = re.match(r'^(\w{3})[\+|\-](\d+)\:(00)$',tz_str)
    tzn = int(tz_num.group(2))
    print (tzn)
    #获取输入的当地时间
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print ('cday is:',cday)
    utctime = cday - timedelta(hours = tzn)
    print ('utctime is: ',utctime)

    print (utctime.timestamp())

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
