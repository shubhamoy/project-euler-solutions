#!/usr/bin/python
sosq = 0
sqos = 0
for i in range(1, 101):
	sosq += i*i
	sqos += i
diff = (sqos * sqos) - sosq
print "Sum of Squares: ", str(sosq)
print "Squares of Sum: ", str(sqos*sqos)
print "Difference: ", str(diff)
