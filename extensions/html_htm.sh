#!/bin/bash

#loop through files in thid directory
for file in data/*; do
    # save extension
    extension="${file##*.}"
    #if ends in htm
    if [[ "$extension" == "htm" ]]; then
        #save base name
        name=$(basename "$file" .htm)
        #change file extension
        mv "$file" data/$name.html
        echo Changed:  "$file" to $name.html
    #if ends in html
    elif [[ "$extension" == "html" ]]; then
        #save base name
        name=$(basename "$file" .html)
        #change file extension
        mv "$file" data/$name.htm
        echo Changed:  "$file" to $name.htm
    #if neither print file name
    else
        echo "$file is not htm or html"
    fi
#end original loop
done
