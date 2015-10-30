#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('/Users/Jane/PycharmProjects/python-learning/test.txt','w') as f:
	print (f.write('Hello, world! I love you'))


with open('/Users/Jane/PycharmProjects/python-learning/test.txt','r') as f:
	print (f.read())


with open('/Users/Jane/PycharmProjects/python-learning/gbk.txt','r',encoding = 'gbk') as f:
	print (f.read())