<?php
	$sum = 0;
	$i = 0;
	
	while($i<1000)
	{
		if(($i%3==0) or ($i%5==0))
		{
			$sum = $sum+$i;
		}
		$i++;
	}
	echo $sum;
?>
