package main

import "fmt"

func main(){
	
	sum := 0
	num1 := 1
	num2 := 2
	temp := 1

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
