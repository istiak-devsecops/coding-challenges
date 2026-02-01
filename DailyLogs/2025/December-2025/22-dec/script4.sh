# the log filer

#!/bin/bash

log_file="$1"
error_count=0

# check if the filename exist
if [[ -z "$1" ]]; then
    echo "ERROR: Usage:: $0 <file_name>"
    exit 1
fi

# 1. Check if the file exists first (Always do this!)
if [[ ! -f "$log_file" ]]; then
    echo "File not found!"
    exit 1
fi

# 2. Start the while loop
while read -r line; do
    # 3. Check if "ERROR" is in the line
    if [[ "$line" == *"ERROR"* ]]; then
        echo "ALERT: Found an issue -> $line"
        # 4. Increment your counter here
        ((error_count++))
        exit 0
    fi
done < "$log_file"

# 5. Print the final total
echo "Total errors found: $error_count"