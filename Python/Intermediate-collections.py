#Collections

import collections
from collections import Counter

#Containers
#list
#set
#dict
#tuple - inmutable

#Types
#1 counter
#2 deque
#3 namedTuple()
#4 orderdDict
#5 defaultdict


'''
c = Counter('gallad')
print(c)
c = Counter(['a','a','b','c','c'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats=4, dogs=7)
print(c)

print(list(c.elements()))
print(c.most_common(2))
'''
c = Counter(a=4,b=2,c=0,d=-2)
d = Counter(['a','b','b','c'])
c.subtract(d)
print(c+d)
print(c-d)
#c.update(d) adds 1
#c.clear()
#print(c)

print(c & d) #intersection
print(c | d) #union





