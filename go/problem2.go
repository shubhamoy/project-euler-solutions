package main

import "fmt"

func main(){
	
	var sum int = 0
	var num1 int = 1
	var num2 int = 2
	var temp int = 1

	for num2 <= 4000000 {
		if( num2%2==0 ){
			sum += num2
		}
		temp = num1
		num1 = num2
		num2 += temp
	}
	
	fmt.Println(sum)
}
