#!/bin/bash

read -p "what is the directory name: " DIR_NAME

# check if the directory exists
if [[ -d "$DIR_NAME" ]]; then
    echo "Directory exists. Listing .log files."

    for file in "$DIR_NAME"/*.log; do
        [ -e "$file" ] && echo "Found: $file"
        done
else
    mkdir "$DIR_NAME"
    # check if the first execution was successful
    if [ $? -eq 0 ]; then
        echo "$DIR_NAME has been created"
    else
        echo "Failed to create directory!"
        exit 1
    fi 
fi