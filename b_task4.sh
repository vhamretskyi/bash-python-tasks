#!/bin/bash

while getopts "s:i:o:" opt; do
    case $opt in

        s)
            shift=$OPTARG
            ;;
        i)
            input=$OPTARG
            ;;
        o)
            output=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac

done


shift $((OPTIND-1))

if ! [[ $shift =~ ^[0-9]+$ ]]
then
    echo "Shift must be a number"
    exit 1
fi

if [ ! -f $input ]
then
    echo "Input file does not exist"
    exit 1
fi

if [ -f $output ]
then
    echo "Output file already exists"
    exit 1
fi

if [ $shift -gt 26 ]
then
    echo "Shift must be less than 26"
    exit 1
fi


while read line
do
    for (( i=0; i<${#line}; i++ ))
    do
        if [[ ${line:$i:1} =~ [a-zA-Z] ]]
        then
            if [[ ${line:$i:1} =~ [A-Z] ]]
            then
                if [ ${line:$i:1} == "Z" ]
                then
                    echo -n "A" >> $output
                elif [ ${line:$i:1} == "z" ]
                then
                    echo -n "a" >> $output
                else
                    echo -n $(printf \\$(printf '%03o' $((`printf '%d' "'${line:$i:1}"`+$shift)))) >> $output
                fi
            elif [[ ${line:$i:1} =~ [a-z] ]]
            then
                if [ ${line:$i:1} == "z" ]
                then
                    echo -n "a" >> $output
                else
                    echo -n $(printf \\$(printf '%03o' $((`printf '%d' "'${line:$i:1}"`+$shift)))) >> $output
                fi
            fi
        else
            echo -n ${line:$i:1} >> $output
        fi
    done
    echo "" >> $output
done < $input

