#!/bin/bash

# safety header
set -euo pipefail # saftey header

log_file="audit.log"

log() {
    local level="${1^^}"
    local message="$2"
    local timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    echo "[$timestamp] [$level] $message" >> "$log_file"

    case "$level" in 
        "INFO") echo -e "[INFO] $message";;
        "WARN") echo -e "[WARN] $message";;
        "ERROR") echo -e "[ERROR] $message" >&2;;

    esac
}


check_log() {
    local file="$1"
    local keyword="$2"

    # check if file exist
    if [[ ! -f "$file" ]]; then
        return 1
    fi

    if grep -q "$keyword" "$file" 2> /dev/null; then 
        return 0
    else
        return 2
    fi
}

log "INFO" "Starting log hunter audit..."

read -p "Enter keyword to search for: " KEYWORD

touch "$log_file"

# check if the log file has write permission if doesn't change the permission
if [[ ! -w "$log_file" ]]; then
    echo -e "[ERROR] Can't write to $log_file. Please run: chmod +w $log_file" >&2
    exit 1
fi

for logfile in "$@"; do
    status=0
    check_log "$logfile" "$KEYWORD" || status=$?

    case $status in
        0) log "INFO" "Keyword $KEYWORD found in: $logfile";;
        1) log "ERROR" "Target file missing: $logfile";;
        2) log "WARN" "keyword $KEYWORD not found in: $logfile";;
    esac
done

log "INFO" "Audit completed. Detailed logs available in $log_file"






