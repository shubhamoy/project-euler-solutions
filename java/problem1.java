class Problem1{
	public static void main(String args[]){
		int sum=0;
		for(int i=0; i<=999;i=i+1){
			if( i % 3 == 0 || i % 5 == 0){
				sum = sum+i;
			}
		}
		System.out.println(sum);
	}
}
