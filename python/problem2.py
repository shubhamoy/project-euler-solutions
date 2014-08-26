sum = 0 

num1, num2, temp = 1, 2, 1

while (num2 <= 4000000):
	if(num2%2==0):
		sum += num2
	temp = num1
	num1 = num2
	num2 += temp 

print(sum)