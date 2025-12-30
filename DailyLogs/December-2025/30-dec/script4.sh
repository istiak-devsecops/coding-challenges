#!/bin/bash

red="\e[31m"
green="\e[32m"
reset="\e[0m"

passed=0
failed=0

audit_directory() {
    local path="$1"

    if [[ -d "$path" ]]; then
        local count=$(ls -1 "$path" | wc -l)
        echo -e "${green}[SUCCESS]${reset} Directory $path found. Total items: $count"
        return 0
    else
        echo -e "${red}[FAILED]${reset} Directory $path is missing or invalid."
        return 1
    fi
}

for dir in "$@"; do
    audit_directory "$dir"
    if [[ $? -eq 0 ]]; then
        ((passed++))
    else
        ((failed++))
    fi
done

echo "Final Report: $passed Passed, $failed Failed."