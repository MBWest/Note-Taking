# sort

- **sort *filename*** - Outputs the contents of a file alphabetically
	- Lowercase letters come before uppercase letters
- **sort -r *filename*** - Alpabetically reverses the output of a file
	- *--reverse* - Equal to -r
- **sort -n *filename*** - Sorts the numeric value
	- *--numeric* - Equal to -n
- **sort -u *filname*** - Sorts unique values only
	- *--unique* - Equal to -u
- **sort  *filename* -k*cloumnnumber*** - Specifies a particular column to sort by
	- *Example* > sort data.txt -n -k2
		- Sorts the data.txt file 2nd column by their numeric value. 