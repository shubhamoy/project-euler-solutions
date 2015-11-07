<?php
	//Identify a prime number by RegEx (http://stackoverflow.com/a/24769490/2365052)
	function is_prime($number) {
		return !preg_match('/^1?$|^(11+?)\1+$/x', str_repeat('1', $number));
	}	

	$n = 600851475143;
	$b = sqrt($n);
	
	for($i=2;$i<$b;$i++){
		if(is_prime($i) == 1){
			if($n % $i == 0){
				echo $i;
				echo "\n";
			}
		}	
	}
?>
