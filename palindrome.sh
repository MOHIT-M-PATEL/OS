#!/bin/bash

# Function to check if a string is a palindrome
check_palindrome() {
    local str="$1"
    local len=${#str}
    local i=0
    local flag=1
    
    while [ $i -lt $len ]; do
        if [ "${str:$i:1}" != "${str: -$(($i + 1)):1}" ]; then
            flag=0
            break
        fi
        i=$(($i + 1))
    done
    
    if [ $flag -eq 1 ]; then
        echo "String is a palindrome."
    else
        echo "String is not a palindrome."
    fi
}

# Accept a string from the user
read -p "Enter a string: " input

# Check if the string is not empty
if [ -z "$input" ]; then
    echo "String should not be NULL."
else
    check_palindrome "$input"
fi
