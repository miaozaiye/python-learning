
# practice str2float
# -*- coding : utf-8 -*-

from functools import reduce

def fn(x, y):
    return x*10 + y

def mut(n):
	x = 1.0
	while n>0:
		x = x*10
		n = n-1
	return x

def str2float(s):
	s1,s2 = s.split('.')
	return reduce(fn,map(int,s1))+reduce(fn,map(int,s2))/mut(len(s2))

print str2float('123.456')



