
#!/bin/bash

FILE="script1.txt" # store file in FILE variable

while IFS= read -r line     # seperate the each line and read them one by one

do 
    EMAIL=$(echo "$line" | grep -Eo '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | sort -u)  # extract only the unique email address and store them in email variable
    if [[ -n "$EMAIL" ]]; then
        echo "$EMAIL"
    fi 
done < "$FILE"  # restart the loop again
