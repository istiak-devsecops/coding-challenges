# check if a text exist in side a string

#!/bin/bash

TEXT="I love bash script. I like to play with bash script"

if [[ $TEXT =~ ([a-z]+)\ bash ]]; then 
    echo "The word bash found"
else 
    echo "No match found"
fi

# extract all the valid email

STRING="Hello Command, please reach out to us at support@devsecops.io for any assistance."
REGEX="([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})"

if [[ $STRING =~ $REGEX ]]; then
    echo "Email: ${BASH_REMATCH[0]}" # - capture groups from your regex. $BASH_REMATCH[0] means entire match
else
    echo "No match found"
fi
