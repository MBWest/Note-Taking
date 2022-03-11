# Loops

## Looping through directory listing

    for i in $( ls ); do
	  echo item: $i
    done


## Loop through a file (dirs.txt) with a list of directories and copy

    #!/bin/bash
    while read p; do
      echo $p
      cp PRODUCT_INFO.md $p
    done < dirs.txt

## Range

    for i in {0..40}; do wget http://10.10.10.245/data/${i}; done

## Infinite loop

    while true; do nc -w0 -v 10.10.10.10 514 <<< "Hello There"; sleep 2; done