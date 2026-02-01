#!/bin/bash

filename="$1"

green="\e[32m"
yellow="\e[33m"
reset="\e[0m"
db_counter=0

while IFS="," read -r server_name ip_address; do
    if [[ "${server_name^^}" == *"DB"* ]]; then
        echo -e "${green}[DATABASE]${reset} $server_name ($ip_address)"
        ((db_counter++))
    else
        echo -e "${yellow}[APP]${reset} $server_name ($ip_address)"
    fi
done < "$filename"

echo -e "Total DataBase found: $db_counter"