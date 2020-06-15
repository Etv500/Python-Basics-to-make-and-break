# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:08:03 2017

@author: elvis
"""
#while in while
m = 0
x = 1
while x < 4:
    y = 1
    while y < 3:
        m = m + x + y
        y = y + 1
    x = x + 1
print(m)


#for in while
print("")
m = 0
x = 10
y=1
while x > 8:
    for y in range(1,3):
        m = m + 1
    x = x - 1
print(m)

#for in for
print("")
m = 1
x=1
y=4
for x in [1,2,3]:
    x=x+1
    for y in [4,5,6]:
        y=y+1
        if x != y:
            m = m+1
print (m)


