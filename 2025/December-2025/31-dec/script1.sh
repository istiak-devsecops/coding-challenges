#!/bin/bash

# --- THE SAFETY HEADER ---
# e: exit on error | u: exit on unset variables | o pipefail: catch errors in pipes
set -euo pipefail

# --- THE CLEANUP CREW ---
# This ensures that even if the script crashes, we leave the system clean.
cleanup() {
    echo "Cleaning up temporary files..."
    rm -f /tmp/nginx_config_test
}
trap cleanup EXIT

# --- CONSTANTS ---
readonly NGINX_CONF="/etc/nginx/sites-available/default"
readonly SOURCE_CONF="./my_config"

# --- HELPER: LOGGING ---
# Lead Approach: Standardized output makes it easy for Datadog/Splunk to read.
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')] [$1] $2"
}

# --- FUNCTION: INSTALL NGINX ---
install_nginx() {
    # Idempotency: Check if nginx is already installed
    if command -v nginx &> /dev/null; then
        log "INFO" "Nginx already installed. Skipping."
    else
        log "INFO" "Installing Nginx..."
        apt-get update -y && apt-get install nginx -y
    fi
}

# --- FUNCTION: SYNC CONFIG ---
configure_nginx() {
    # Idempotency: Check if the config actually needs changing
    # We compare the local file to the system file using 'diff'
    if diff -q "$SOURCE_CONF" "$NGINX_CONF" &> /dev/null; then
        log "INFO" "Config is already up to date. No restart needed."
    else
        log "INFO" "Updating Nginx configuration..."
        cp "$SOURCE_CONF" "$NGINX_CONF"
        
        # Fail-Fast: Test the config before restarting
        nginx -t &> /dev/null || { log "ERROR" "Invalid Nginx config!"; exit 1; }
        
        systemctl restart nginx
        log "INFO" "Nginx restarted successfully."
    fi
}

# --- MAIN EXECUTION ---
main() {
    # Pre-flight check: Must be root
    if [[ $EUID -ne 0 ]]; then
       log "ERROR" "This script must be run as root"
       exit 1
    fi

    install_nginx
    configure_nginx
    log "INFO" "Deployment complete."
}

main "$@"