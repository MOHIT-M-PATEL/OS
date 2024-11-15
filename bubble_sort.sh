#!/bin/bash

# Function to perform bubble sort
bubble_sort() {
    local array=("$@")
    local n=${#array[@]}
    
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < n-i-1; j++)); do
            if [ "${array[j]}" -gt "${array[$((j+1))]}" ]; then
                # Swap elements
                temp="${array[j]}"
                array[j]="${array[$((j+1))]}"
                array[$((j+1))]="$temp"
            fi
        done
    done
    
    echo "Sorted array: ${array[*]}"
}

# Accept the number of elements to be sorted
read -p "Enter number of elements: " n

# Accept the elements into an array
echo "Enter the elements:"
for ((i = 0; i < n; i++)); do
    read num[$i]
done

# Perform bubble sort
bubble_sort "${num[@]}"
