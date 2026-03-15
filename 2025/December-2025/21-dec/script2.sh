#!/bin/bash

DIR_PATH="$1"

if [[ -z "$1" ]]; then
    echo "Usage: $0 <directory_path>"
    exit 1 # Exit because we can not continue without a path
fi

if [[ -d "$DIR_PATH" ]]; then 
    echo "Cleaning logs in $DIR_PATH..."

    for file in "$DIR_PATH"/*.log; do
        if  [[ -f "$file" ]]; then
            > "$file"
            echo  "Cleared: $file"
        fi
    done
else
    echo "Error: $DIR_PATH is not a valid directory"
    exit 1
fi