#!/bin/bash

##changes the 
dir=image_cache 
cd $dir
dir_files=($(ls -d *))
echo "${#dir_files[@]}"

##checking to see if there are any files in the cache 
if [[ "${#dir_files[@]}" > 0 ]]
then 
    ##deleting the files in image cache 
    ##should probably add more checks here lol 
    rm * 
else 
    echo there is nothing to empty 
fi 


