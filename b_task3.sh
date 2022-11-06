#!/bin/bash



for((i=0;i<=100;i++))
do

if [ $i == 0 ]; then
echo "$i"

elif [ $[$i % 3] == 0 -a $[$i % 5] == 0 ];then
echo "FizzBuzz"

elif [ $[$i % 3] == 0 ]; then
echo "Fizz"

elif [ $[$i % 5] == 0 ];then
echo "Buzz"

else
echo "$i"

fi



done
