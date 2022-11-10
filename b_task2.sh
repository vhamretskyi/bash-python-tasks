#!/bin/bash

function add {
    sum=0
    for i in $@
    do
        sum=$((sum+i))
    done
    echo $sum
}
#substract function
function substract {
    sum=$1
    shift
    for i in $@
    do
        sum=$((sum-i))
    done
    echo $sum
}

function multiply {
    product=1
    for i in $@
    do
        product=$((product*i))
    done
    echo $product
}

function modulo {
    remainder=$(( $1 % $2 ))
    echo $remainder
}

while getopts "o:n:d" opt; do
    case $opt in
        o)
            operation=$OPTARG
            ;;
        n)
            numbers=$OPTARG
            ;;
        d)
            display=1
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac
done


shift $((OPTIND-1))


if [ $operation == "+" ]
then
    result=$(add $numbers)
elif [ $operation == "-" ]
then
    result=$(substract $numbers)
elif [ $operation == "m" ] # m is for multiply besause * is reserved for special character
then
    result=$(multiply $numbers)
elif [ $operation == "%" ]
then
    result=$(modulo $numbers)
fi

    echo "Result: $result"

if [ $display ]
then
    echo "Username: $USER"
    echo "Script name: $0"
    echo "Operation: $operation"
    echo "Numbers: $numbers"
fi


