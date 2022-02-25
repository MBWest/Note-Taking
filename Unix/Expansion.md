## Expansion

**(*)** - Represents zero or more characters in a filename
**(?)** - Represent one character in a filename
**[A-Z]** - Represents a range of characters in a filename ([A-Z], [a-z], [0-9])
**[^A-Z]** - Represents a range of characters to **NOT** match ([^A-Z], [^a-z], [^0-9])

### Pathname Expansion (*)

- *Example* > echo press * to speak to operator
	- The **(*)** will be replaced by all files that are in the current directory
- *Example* > ls *html
	- Matches any files that end with .html
*Example* > cat blue*
	- Matches any files that start with "blue"

### Brace Expansion {}

Brace expansion is used to generate arbitrary strings. 

**{1,2,3}**
- *Example* > touch page{1,2,3}
	- Generates three new files: page1.txt, page2.txt, page3.txt
**{1..3}**
- *Example* > touch page{1..3}
	- Generates three new files: page1.txt, page2.txt, page3.txt
**{2..10..2}**
- *Example* > touch page{2..10..2}
	- Generates five new files: page2.txt, page4.txt, page6.txt, page8.txt, page10.txt
**{A..E}**
- *Example* > touch page{A..E}
	- Generates five new files: pageA.txt, pageB.txt, pageC.txt, pageD.txt, pageE.txt

### Quoting 

If you wrap text in a double quote ("wrapped"), the shell will respect spacing and ignore special characters except: Dollar Sign ($), backslash (\), and backtick (`).

If you wrap text in a single quote ('wrapped') you will suppress all forms of subsitution. 

### Command Substitution]

You can use the **$(command)** syntax to dispay the output of another command
- *Example* > echo "today is $(date)"
	- This will echo out to the terminal "today is Thu 01 May 2021 03:10:31 PM PDT"
- You can use the `command` syntax to dispay the output of another command
- *Example* > echo today is `date`
	- This will echo out to the terminal "today is Thu 01 May 2021 03:10:31 PM PDT"


### Arithmetic Expansion

The shell will perform arithmetic via expansion using the **$((expression))** syntax. Inside the parentheses the user can write artithmetic expression using:
- + Addition
- - Subtraction
- * Multiplication
- / Division
- ** Exponentiation
- % Modulo

- *Example* > (echo $((10+7)))

### Tilde Expansion

- *Example* > echo **~**
	- Returns the current users home directory 
- *Example* > echo **~User**
	- Returns the specific users home directory 

### Parameter Expansion

If you write out the name of an enviornment variable prefixed with a dollar sign ($) the shell will replace it with the actual value