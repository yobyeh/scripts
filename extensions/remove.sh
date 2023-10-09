#!/bin/bash

#loop through the data dir
for file in data/*; do
    #save the extension
    extension="${file##*.}"
    #check extensions
    if [[ "$extension" == "htm" ||  "$extension" == "html" ]]; then
        rm "$file"
        echo Removed: "$file"
    fi
done
