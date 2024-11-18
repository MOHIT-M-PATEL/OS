#!/bin/sh
# Read the input from the user
echo "Enter a string to check if it is a palindrome:"
read input
# Initialize variables
reversed=""
length=${#input}
# Reverse the string
for (( i=$length-1; i>=0; i-- )) 
do
    reversed="${reversed}${input:$i:1}"
done
# Compare original string with reversed string
if [ "$input" = "$reversed" ] 
then
 echo "The string is a palindrome."
else
 echo "The string is not a palindrome."
fi
