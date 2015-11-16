from math import factorial
	
x = str(factorial(100))
sum=0
for i in range(len(x)):
	sum += int(x[i])
print sum
