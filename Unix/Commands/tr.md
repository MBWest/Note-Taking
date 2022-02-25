# tr

**tr** - Translate, squeeze, and/or delete characters from standard input, writing to standard output
- *Example* > cat somefile | tr s $
	- Replaces all lower case s's with a dollar sign ($) then outputs the results to the terminal 
- Can use both ranges (*a-z, A-Z*) or character sets *[:alpha:]*, *[:blank:]*...