#8 collections deque

import collections
from collections import deque
'''
d = deque("hello")

d.append('4')
d.append(5)
d.appendleft(5)
d.pop()
d.popleft()
d.clear()
d.extend('456')
d.extend('hello')
d.extend([1,2,3])
d.extendleft('hey')
d.rotate(1)
print(d)
'''

d = deque("hello", maxlen=5)
print(d)
d.append(1)
d.extend([1,2,3])
print(d)
