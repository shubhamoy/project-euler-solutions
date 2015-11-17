#!/usr/bin/python
x=0
for i in range(1, 1001):
	x += i**i
print str(x)[-10:]
