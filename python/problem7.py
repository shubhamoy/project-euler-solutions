#!/usr/bin/python
def primes_sieve(limit):
	limitn = limit+1
	not_prime = [False] * limitn
	primes = []

	for i in range(2, limitn):
		if not_prime[i]:
			continue
		for f in xrange(i*2, limitn, i):
			not_prime[f] = True

		primes.append(i)

	return primes


count = 0
length = 0
while(count < 10000):
	a = primes_sieve(length)
	count = len(a)	
	if count < 10000:
		length += 500
	else:
		print a[10000]
