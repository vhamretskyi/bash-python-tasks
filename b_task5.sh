#!/bin/bash

if [[ $1 != "-i" ]] || [[ $3 != "-o" ]] ; then
        echo "Invalidt tet"
fi

if [ ! -f $2 ]; then
        echo "Input file does not exist"
        exit 1
fi

if [ -f $4 ]; then
        echo "Output file already exists"
        exit 1
fi

if [[ $5 == "-v" ]]; then
        tr -s '[:upper:]' '[:lower:]' < $2 > $4
        tr -s '[:lower:]' '[:upper:]' < $4 > $2
        exit 0
fi

if [[ $5 == "-s" ]]; then
        sed "s/$6/$7/g" < $2 > $4
        exit 0
fi

if [[ $5 == "-r" ]]; then
        tac < $2 > $4 
        exit 0
fi

if [[ $5 == "-l" ]]; then
        tr '[:upper:]' '[:lower:]' < $2 > $4
        exit 0
fi
 if -u tag is passed

if [[ $5 == "-u" ]]; then
        tr '[:lower:]' '[:upper:]' < $2 > $4
        exit 0
fi

if [ $# -eq 4 ]; then
        cp $2 $4
        exit 0
fi

if [ $# -gt 5 ]; then
        echo "Invalid syntax. Please use -i <input file> -o <output file> tags"
        exit 1
fi
