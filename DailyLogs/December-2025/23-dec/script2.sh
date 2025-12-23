# user access simulation

#!/bin/bash

admin_user="root"
admin_ip="192.168.1.1"

read -p "Enter your username: " user
read -p "Enter your ip address: " ip

if [[ "$user" == "$admin_user" && "$ip" == "$admin_ip" ]]; then
    echo "[ACCESS GRANTED]"
elif [[ "$user" == "$admin_user"  "$ip" != "$admin_ip" ]]; then
    echo "[SECURITY ALERT] Wrong IP for Root."
else
    echo "ACCESS DENIED"
fi
