#!/bin/bash

filename="$1"


while IFS="," read -r server_name ip_address; do 
    if [[ "$server_name" == *"db"* ]]; then
        echo -e "[DATABASE] Name: $server_name | IP: $ip_address"
    else
        echo -e "[SERVER] Name: $server_name | IP: $ip_address"
    fi
done < "$filename"
