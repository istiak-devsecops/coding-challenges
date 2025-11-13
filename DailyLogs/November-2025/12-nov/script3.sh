# check if a text exist in side a string

#!/bin/bash

TEXT="I love bash script. I like to play with bash script"

if [[ "$TEXT" =~ ([a-z]+)\ bash ]]; then 
    echo "The word bash found"
else 
    echo "No match found"
fi