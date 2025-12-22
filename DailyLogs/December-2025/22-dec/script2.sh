# The Input Loop
#!/bin/bash

for i in {1..3}; do
    read -p "Enter username: $i: " current_user

    if [[ -z "$current_user" ]]; then
        echo "ERROR: username cannot be empty."
        continue
    fi

    if [[ "$current_user" == "admin" ]]; then
        echo "Warning: Root-level access requested for $current_user!"
    else
        echo "User $current_user added to the queue."
    fi
done

echo "All users processed."