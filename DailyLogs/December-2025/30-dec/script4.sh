#!/bin/bash

red="\e[31m"
green="\e[32m"
reset="\e[0m"

audit_directory() {
    local path="$1"

    if [[ -d "$path" ]]; then
        local count=$(ls -1 "$path" | wc -l)
        echo -e "${green}[SUCCESS]${reset} Directory $path found. Total items: $count"
    else
        echo -e "${red}[FAILED]${reset} Directory $path is missing or invalid."
    fi
}

for dir in "$@"; do
    audit_directory "$dir"
done