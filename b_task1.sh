#!/bin/bash





echo "Write how many fib you want to see:"
read n
echo "Fib series:"
a=0
b=1

for((i=0;i<n;i++))
do
echo "$a"
fn=$((a+b))
a=$b
b=$fn
done




