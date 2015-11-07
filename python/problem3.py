import math, re

def isPrime(num):
        pattern = r'^1?$|^(11+?)\1+$'
        if re.match(pattern, '1'*num) is None:
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
