#!/bin/bash

# check if a file exist
FILE="/etc/passwd"

if [ -f "$FILE" ]; then
    echo "File $FILE exist"
else 
    echo "File $FILE doesn't exist"
fi

# check if a directory exist
DIR="/etc"

if [ -d "$DIR" ]; then 
    echo "Directory $DIR exist"
else 
    echo "Directory $DIR doesn't exist"
fi