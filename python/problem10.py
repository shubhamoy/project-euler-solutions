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

x = primes_sieve(2000000)
sum = 0
for i in range(len(x)):
	sum += x[i]
	
print sum
