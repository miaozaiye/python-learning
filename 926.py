def now():
	print ('2015-9-26')

f = now
print f()

print now.__name__
print f.__name__

import functools


def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call-%s():' % (func.__name__))
            func(*args, **kw)
            print ('end call')
        return wrapper
    return decorator

@log()
def now():
	print ('2015-9-26')

print now()

print now.__name__