#!/bin/bash

file_name="$1"

# check if argument is missing
if  [[ -z "$file_name" ]]; then
        echo "Usage: $0 <file_path>"
        exit 1
fi

# chcek if file exist
if  [[ ! -f "$file_name" ]]; then
        echo "Error: '$file_name' doesn't exist or not a regular file."
        exit 1
fi

# check if a file has write permission
if  [[ ! -w "$file_name" ]]; then
        echo "Error: $file_name doesn't have write permission."
        exit 1
fi

# check if the file is not empty
if  [[ ! -s "$file_name" ]]; then 
        echo "Error: $file_name is empty."
        exit 1
fi

echo "Backup performed on $(date)" >> "$file_name"
echo "Success: message appended on $file_name"
exit 0

