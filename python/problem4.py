#!/usr/bin/python
n1 = 999
n2 = 999
res = []
for i in range(999, 1, -1):
	for j in range(1, 1000): 
		r = n1 * n2
		if str(r) == str(r)[::-1]:
			if r not in res:
				res.append(r)
		n1 -= 1
	n2 -= 1
	n1 = 999
res.sort()
print res[-1]
