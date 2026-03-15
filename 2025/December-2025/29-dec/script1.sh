#!/bin/bash

filename="$1"
red="\e[31m"
yellow="\e[33m"
green="\e[32m"
reset="\e[0m"

critical="CRITICAL"
error="ERROR"
critical_counter=0
error_counter=0

if [[ -z "$filename" ]]; then
    echo "${red} Arguments Missing! ${reset}"
    exit 1
fi

if [[ ! -f "$filename" ]]; then
    echo -e "${red}Error: $filename missing! ${reset}"
    exit 1
fi

if [[ -r "$filename" && ! -s "$filename" ]]; then
    echo -e "${yellow} Log is empty, skipping scan ${reset}"
    exit 0
fi

while read -r line; do
    if  [[ "$line" == *"$critical"* && "$line" == *"SUDO"* ]]; then
            echo -e "${red}[SECURITY ALERT]${reset} Critical sudo action detected!"
                ((critical_counter++))
    elif    [[ "$line" == *"$critical"* ]]; then 
                ((critical_counter++))
    elif    [[ "$line" == *"$error"* ]]; then
                ((error_counter++))    
    fi
done < "$filename"

if ((critical_counter + error_counter > 5)); then
    echo -e "${red}[STATUS] System Unstable. ${reset}"
    exit 1
else
    echo -e "${green}[STATUS] System Healthy.${reset}"
    exit 0
fi
    


