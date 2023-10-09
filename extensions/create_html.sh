#!/bin/bash

#loop 10 times
for i in {1..10}; do
    #for every other name html or htm
    if (( $i % 2 == 0 )); then
        #name the file with .htm
        touch data/file_"$i".htm
    else
        #name the file with .html
        touch data/file_"$i".html
    fi
done