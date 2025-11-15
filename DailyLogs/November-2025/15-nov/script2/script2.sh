#!/bin/bash

PATH_TO_DIR="C:/Users/PC/Desktop/Coding/coding-challenges/*"

count=0

for DIR in $PATH_TO_DIR; do
    if [[ -d "$DIR" ]]; then
        echo "$DIR"
        ((count++))
    fi
done 

echo "Total directories: $count"