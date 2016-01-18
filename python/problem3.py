import math

def isPrime(n):

	if n == 2: return 1
	if n == 3: return 1
	if n % 2 == 0: return 0
	if n % 3 == 0: return 0

	i = 5
	w = 2
	while i * i <= n:
		if n % i == 0:
			return 0
		i += w
		w = 6 - w
	return 1


n = 600851475143
b = math.sqrt(n)
i = 1
while(i<b):
        if(isPrime(i) == 1):
                if(n % i == 0):
                        print i
                        print '\n'
        i = i+1
