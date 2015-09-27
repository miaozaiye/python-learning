print int('1000',2)

import functools
int2 = functools.partial(int,base=2)
print int2('100010')