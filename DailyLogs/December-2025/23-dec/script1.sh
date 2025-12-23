# Disk space monitor

#!/bin/bash

# creating file with content
# echo -e "/etc\n/tmp\n/home\n/invalid_folder" > paths.txt

file_name="$1"
missing_count=0

# check if there is an arguments
if [[ -z "$file_name" ]]; then
    echo "Error: Usage:: $0 <file_name>"
    exit 1
fi

# check if the file exist
if [[ ! -f "$file_name" ]]; then
    echo "Error: File doesn't exist"
    exit 1
fi

# check if the file has writting and reading permission
if [[ ! -w "$file_name" ]]; then
    echo "Error: File doesn't have writting permission"
    exit 1
fi

while read -r lines; do
    if [[ -d "$lines" ]]; then
        echo "Path: $lines"
    else
        echo "Error: Path:: $lines not found!"
        ((missing_count++))
    fi
done < "$file_name"

if [[ $missing_count -gt 0 ]]; then
    echo "Total missing directory: [$missing_count]"
    exit 1
else
    echo "Every directory found!"
    exit 0
fi


