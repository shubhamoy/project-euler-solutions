var sum = 0;
var num1 = 1, num2 = 2, temp = 1;

while(num2 <= 4000000)
{
	if(num2 % 2 === 0)
	{
		sum += num2;
	}
	temp = num1;
	num1 = num2;
	num2 += temp;
}

document.write("<h2>Solution to Problem 2: "+sum+"</h2>");
