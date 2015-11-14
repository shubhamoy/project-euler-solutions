#!/usr/bin/python

#http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
def gcd(a, b):
	"""Return greatest common divisor using Euclid's Algorithm."""
	while b:      
		a, b = b, a % b
	return a

def lcm(a, b):
	"""Return lowest common multiple."""
	return a * b // gcd(a, b)

def lcmm(*args):
	"""Return lcm of args."""   
	return reduce(lcm, args)
	
print lcmm(*range(1,20))
