#!/bin/bash


filename="$1"
delete_counter=0

# check if the file exist
if [[ ! -f "$filename" ]]; then
    echo "Error: CSV list $filename not found."
    exit 1
fi

while IFS="," read -r file action; do
    if [[ -f "$file" ]]; then
        if [[ "${action^^}" == *"DELETE"* ]]; then
            echo -e "Removing [$file]..."
            rm "$file"
            ((delete_counter++))
        elif [[ "${action^^}" == *"KEEP"* ]]; then
            echo -e "preserving: [$file]."
        else 
            echo -e "Action not performable."
        fi
    else
        echo -e "Skip: [$file] already gone or never existed."
    fi
done < "$filename"

echo -e "Total file removed: $delete_counter"
        
