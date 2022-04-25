#!/bin/bash
echo "Factorial Finder"
echo "Enter the value of n"
read N

fact=1
i=1
while ((i <= N))
do
    fact=$((fact*i))
    i=$((i+1))
done
echo "The factorial of the number is $fact"
