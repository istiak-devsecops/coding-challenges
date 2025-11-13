# check if a file is readable and writable

FILE="/home/bash_script.sh"

# check if its readable
if [ -r "$FILE" ]; then
    echo "The $FILE is readable"
else
    echo "The $FILE is not readable"
fi


#check if its writable
if [ -w "$FILE" ]; then 
    echo "The $FILE is writable"
else
    echo "The $FILE is not writable"
fi

# check if file has both permission
if [[ -r "$FILE" && -w "$FILE" ]]; then
    echo "The $FILE is readable and writable"
else
    echo "The $FILE is not readable and writable"
fi

