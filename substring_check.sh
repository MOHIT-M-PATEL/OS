#!/bin/bash

# Function to check if a substring exists
substring_check() {
    local str1="$1"
    local str2="$2"
    
    if [[ "$str1" == *"$str2"* ]]; then
        echo "Substring exists."
        echo "Positions: "
        
        # Find and display all positions of substring
        local pos=0
        local temp_str="$str1"
        local len_str2=${#str2}
        
        while [[ "$temp_str" == *"$str2"* ]]; do
            pos=$((${#str1} - ${#temp_str} + $(expr index "$temp_str" "$str2")))
            echo "$pos"
            temp_str=${temp_str#*"$str2"}
        done
    else
        echo "Substring does not exist."
    fi
}

# Accept two strings from the user
read -p "Enter the main string: " str1
read -p "Enter the substring: " str2

# Check if strings are not empty
if [ -z "$str1" ]; then
    echo "First string should not be NULL."
else
    substring_check "$str1" "$str2"
fi
