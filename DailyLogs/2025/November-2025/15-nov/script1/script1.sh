#!/bin/bash

FILE="script1.txt"

while IFS= read -r line

do 
    IP=$(echo "$line" | grep -Eo "^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$" | sort -u)
    if [[ -n "$IP" ]]; then 
        echo "$IP"
    fi 
done < "$FILE"