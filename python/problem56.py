#!/usr/bin/python
def digitSum(n):
	n = str(n)
	sum = 0
	for i in range(len(n)):
		sum += int(n[i])
	return sum

big = 0
for i in range(1,100):
	for j in range(1,100):	
		s = i**j
		ds = digitSum(s)
		if big < ds:
			big = ds
print big
