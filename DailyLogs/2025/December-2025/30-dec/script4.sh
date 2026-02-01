#!/bin/bash

red="\e[31m"
green="\e[32m"
yellow="\e[33m"
reset="\e[0m"

passed=0
warned=0
failed=0

audit_directory() {
    local path="$1"

    # 1. First, check it exists
    if [[ ! -d "$path" ]]; then
        echo -e "${red}[FAILED]${reset} Directory $path is missing."
        return 1
    fi

    # 2. If it exists, count the items
    local count=$(ls -1 "$path" 2> /dev/null | wc -l)

    # 3. Use the count to decide the return code
    if [[ $count -eq 0 ]]; then
        echo -e "${yellow}[WARNING]${reset} $path is empty."
        return 2
    else
        echo -e "${green}[SUCCESS]${reset} $path found. Items: $count"
        return 0
    fi
}

for dir in "$@"; do
    audit_directory "$dir"
    status=$?  # Save it immediately so we don't lose it!

    if [[ $status -eq 0 ]]; then
        ((passed++))
    elif [[ $status -eq 2 ]]; then
        ((warned++)) 
    else
        ((failed++))
        echo "$dir" >> error.log
    fi
done

echo "Final Report: $passed Passed, $failed Failed., $warned Warned"