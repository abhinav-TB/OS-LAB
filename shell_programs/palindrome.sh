#!/bin/bash
echo "Enter a String : "
read x
strlen=${#x}
dec=$((strlen - 1))
counter=0
divlen=`expr $strlen / 2`
for ((i=0; i<divlen; i++))
do
    let1=${x:$i:1}
    let2=${x:$dec:1}
    if [ $let1 = $let2 ]
    then
        counter=`expr $counter + 1`
        dec=`expr $dec - 1`
    else
        echo "not palindrome"
        exit 1
    fi
done
echo "It is palindrome"