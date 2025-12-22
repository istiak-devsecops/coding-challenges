
#!/bin/bash


service_list="nginx docker mysql"
dir_path="/var/lib/"

for service in $service_list; do
    if [[ -d "$dir_path/$service" ]]; then
        echo "Service $service: Configured"
    else
        echo "Service $service: Missing"
    fi
done

