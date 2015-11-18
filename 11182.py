from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print (p.x)

isinstance(p,Point)

Circle = namedtuple('Circle',['x','y','r'])

from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print (q)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print (dd['key1'])
print (dd['key2'])

from collections import OrderedDict

from collections import Counter
c = Counter()
for ch in 'programming':
	print (ch, c[ch])

	c[ch] = c[ch] + 1

print (c)