# Tuples

import collections
from collections import namedtuple

#Point = namedtuple('point','x y z')

Point = namedtuple('point',['x', 'y', 'z'])
newP = Point(3,4,5)
print(newP.x, newP.y, newP.z)
print(newP._asdict())
print(newP._fields)

newP = newP._replace(y=6)
print(newP)

p2 = Point._make(['a','b','c'])
print(p2)
