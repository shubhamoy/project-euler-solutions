class Problem2{
	public static void main(String args[]){
		int sum=0; 
		int num1=1; 
		int num2=2; 
		int temp=1;

		while(num2 <= 4000000){
			if(num2%2==0){
				sum+=num2;
			}
			temp = num1;
			num1 = num2;
			num2 += temp;
		}
		System.out.println(sum);
	}
}
