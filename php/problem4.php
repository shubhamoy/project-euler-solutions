<?php
	$n1 = 999;
	$n2 = 999;
	$res = array();
	for($i=999;$i>0;$i--){
		for($j=1;$j<=1000;$j++){
			$r = $n1 * $n2;
			if(strrev($r) == $r){
				$res[] = $r;
			}
			$n1--;
		}
		$n2--;
		$n1=999;
	}
	sort($res);
	echo $res[count($res)-1];
