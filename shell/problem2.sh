#!/bin/sh
SUM=0
NUM1=1
NUM2=2
TEMP=1

while [ $NUM2 -le 4000000 ]
do
	if [[ $((NUM2 % 2)) == 0 ]]; then
		SUM=$((SUM+NUM2))
	fi
	TEMP=$NUM1
	NUM1=$NUM2
	NUM2=$((NUM2+TEMP))
done

echo $SUM

