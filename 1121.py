#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self._flag = ''

    def handle_starttag(self, tag, attrs):
        if ('class','event-title') in attrs:
            self._flag = 'event-title:'
        elif ('class','event-location') in attrs:
            self._flag = 'event-location:'
        elif tag == 'time':
            self._flag = 0

    def handle_data(self,data):
        if self._flag in ('event-title:','event-location:'):
            if self._flag == 'event-title:':
                print ('-'*35)
            print (self._flag,data.strip())
            self._flag = ' '
        if isinstance(self._flag,int):
            l = ['-',',','\n']
            if self._flag<3:
                print(data.strip(),end = l[self._flag])
                self._flag +=1


parser = MyHTMLParser()
with open('index.html') as html:
    parser.feed(html.read())

