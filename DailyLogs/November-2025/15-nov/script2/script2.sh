#!/bin/bash

PATH_TO_DIR="C:/Users/PC/Desktop/Coding/coding-challenges/*"

count=0

for entry in $PATH_TO_DIR; do
    if [[ -d "$entry" ]]; then
        echo "$entry"
        ((count++))
    fi
done 

echo "Total directories: $count"