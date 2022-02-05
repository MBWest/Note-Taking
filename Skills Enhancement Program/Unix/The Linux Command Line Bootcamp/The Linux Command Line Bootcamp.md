# The Linux Command Line Bootcamp: Beginner To Power User
### Resources
**- Operating Systems: Timeline and Family Tree** 
	- https://eylenburg.github.io/os_familytree.htm
**- The world of Operating Systems**
	- https://spectrum.ieee.org/the-strange-birth-and-long-life-of-unix
	- https://www.opengroup.org/membership/forums/platform/unix
**- Exploring the Original Unix**
	- https://www.bell-labs.com/usr/dmr/www/man11.pdf
	- https://www.bell-labs.com/usr/dmr/www/1stEdman.html
**- Linux, GNU, Kernes, Oh My!**
	- https://www.howtogeek.com/139287/the-great-debate-is-it-linux-or-gnulinux/

## Useful Shortcuts

- **Clear the screen** - Ctrl-l
- **Move the cursor to the beginning of the line** - Ctrl-a
- **Move the cursor to the end of the line** - Ctrl-e
- **Move the cursor foward one character** - Ctrl-f
- **Move the cursor backwards one character** - Ctrl-b
- **Move the cursor forward one word** - Alt-f
- **Move the cursor backwards one word** - Alt-b
- **Swaps the current character under the cursor with the preceding one** - Ctrl-t
- **Swaps the current word under the cursor with the preceding one** - Alt-t
- **Kill the text from the cursor until the end of the line** - Ctrl-k
- **Kill the text from the cursor until the beginning of the line** - Ctrl-u
- **Kill the text from the cursor through the end of the word** - Alt-d
- **Kill the text from the current cursor through the beginning of the word** - Ctrl-w or alt-delete
- **Kill-ring**
	- Words killed are temporarly stored in the kill-ring and can be brought back using **Ctrl-y**

## History

- **history** - View previous run commands
	- **history | less**  - Easier way to manage a long history
- **!somenumber** - Rerun a command using its line number from the history
	- *Example* > !73
		- Runs the 73rd command in the history
- **!!** - Reruns the last command
	- Useful if your last command needed sudo in front of it
- **Ctrl-r** - Search through your history
- *.bash_history* - Where the history is saved
- *$HISTFILESIZE* - Number of items stored in history
- *$HISTSIZE* - The number of item which will be shown to the user when running *history*

## Command Basics (capitalization matters!)
### Basic Command Structure
- **Command**
- **Options** - Options are prefixed by a dash '-', can be combined together
	- *Example* >  ncal -h
		- Turns off the highlighting of the current day
	- *Example* > ncal -j
		- Will print out a calendar with Julian dates
	- Long Form Options - Full words prefixed with two dashes
		- *Example* > date -u = date --universal
- **Options with Parameters** - Some options require us to pass an additional value
	- *Example* > ncal -A1
		- Prints out the current month with one month afterwards 
	- *Example* > ncal -A1 -B1
		- Prints out the current month with one month afterwards and one month before
	- *Example* > ncal july 1969 -B1 -A1 -M
		- Prints out July in the year 1969,  1 month before, 1 month after and starts the calendars on Monday
- **Arguments** - Values that we give to a command to work with or operate on
	- *Example* > ncal 1999
	- *Example* > ncal april 1999

## Arrow Keys
- **Left/Right** - Move the cursor along the command
- **Up** - Cycle through previous commands
- **Down** - Cycle through recent commands

## Man Pages (Manuals)
#### What are Man Pages?
Built-in form of documentation available on nearly all UNIX-like operating systems
#### Navigating and Searching a Man Page
- **man *command*** - Opens a man page for a command
	- *Example* > man ncal
		- Opens the ncal Man Page
- ***man -k search-term*** - Search the short description and manual page names for the search-term provided
	- *Example* >  man -k dog

#### While in a Man Page

- ***'q'*** - Exits a Man Page
- ***'Down Arrow/Up Arrow'*** - Scroll one line at a time
- ***'Space Bar'*** - Jumps down 1 page at a time
- ***'b'*** - Jumps up 1 page at a time
- ***'f'*** - Jumps down 1 page at a time
- ***'h'*** - Opens the *help* document
- ***'/???'*** - Search in a man page

#### Parsing Man Page Synopsis
-  ***[optional]*** - Anything in [brackets] is optional 
- ***[short-option]...*** - One or more strings can be provided
- ***[string]...*** - One or more options can be provided
- ***OPTIONS*** - Must pass along options that are not in [brackets]

#### Manual Sections

**Different sections of Man Pages**
- Using the corresponding number below you can look at certain section of man pages
	- *Example* > man 2 printf
		- This will look at the *System Calls* section of the printf command

1. User Commands
2. System Calls
3. C Library Functions
4. Special Files
5. File Forms
6. Games
7. Miscellaneous
8. System Admin Commands

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

### Command Substitution]

### Arithmetic Expansion

### Tilde Expansion

- *Example* > echo **~**
	- Returns the current users home directory 
- *Example* > echo **~User**
	- Returns the specific users home directory 

## Directories

### Relative Path/Absolute Path
**Relative Path** - Paths that specify a directory/file relative to the current directory
**Absolute Path** - Paths that specify a directory/files full path so it works in any directory

### Root Directory
**/** - Starting point of the entire Directory, called the root directory (Top Level Directory)
- Not the actual folder with the name "root"
### Home Directory
**/home** - Contains a home folder for each user on the system
- *Example* > /home/west
	- My home folder
- The home directory can be accessed using the 'tilde ~' key
	- *Example* > cd ~

### Directory Manipulation

#### mkdir

- **mkdir *foldername1*** - Creates a new folder in the current directory
- **mkdir *foldername1 foldername2*** - Creates multiple folders
	- Can provide an absolute path or a relative path
- **mkdir -p** - Make parent directories as needed (useful if nested folders do not already exist)

#### rm


- **rm -d *foldername***- Deletes empty directories
- **rmdir *foldername*** - Deletes empty directories
- **rm -r *foldername*** - Removes directories and their contents recursively
	- **rm -i** - Interactive optionsl, prompts user (y or n)



## Commands

### Type of Commands
1. **Executable program** - Compiled binary files
	- Usually stored in /bin,  /usr/bin, /usr/local/bin
2. **Built-in shell command** - Part of the shell
	- ***help* command** - Similar to Man Pages but for built-in shell commands
3. **Shell Function**
4. **Alias**

### Redirection

*Standard Input* -> **Command** -> *Standard Output* or -> *Standard Error*

The **>** operator default to 1 as the file descriptor number which is why we dont need to specify **1>** to redirect standard output. 
The **<** operator uses a default file descriptor number of 0, so we dont ned to specify **0<** to redirect to standard input, although you can. 

#### Standard Input

Standard input is where a program or command get its input from. By default, the shell directs standard input from the keyboard
- The input information could come from a keyboard, a file, or even from another command. 

#### Standard Output

Standard output is a place to which a program or command can send information.
- The information could go to a screen to be displayed, to a file, or even to a printer or other device

#### Standard Error

Commands and programs also have a destination to send error messages: Standard Error
- By default, the shell directs standard error information to the screen for the user to read, but this destination can be changed if needed. 
- If you have standard output and standard error in the same command you must redirect standard output first and then standard error. 

#### Redirecting Output (>)

The redirect output symbol (**>**) tells the shell to redirect the output of a command to a specific file instead of the screen. 
- By default, the **date** command will print the current date to the screen. If we instead run **date > output.txt** the output will be redirected to a file called output.txt

The append output symbol (**>>**) tells the shell to redirect the output SSof a command to a specific file instead of the screen.
- To instead keep the existing contents in the file and add new content to the end of the file, use (**>>**) when redirecting. 

#### Redirecting Standard Input (<)

To pass contents of a file to standard input use the (**<**) symbol followed by the filename. 
- *Example* > cat < filename.txt

#### Redirecting Standard Input and Output at the Same Time

- *Example* > cat **<** original.txt *>* output.txt

#### Redirecting Standard Error (2>)

By default, error messages are output top the screen. The standard error redirection operator is **2>**
- *Example* > ls notrealfolder 2> errorlog.txt
	- Redirects the error text to the errorlog.txt file

#### Redirecting Standard Output and Error at the Same Time (&>)

Newer versions of bash allow for (&>) to redirect both standard output and standard error to the same file

### Piping

#### Piping vs Redirecting

**>** Connects a command to some file

**|** Connets a command to another command

#### Piping (|)

Pipe the standard output from one command into the standard input of another command using the (**|**) 

#### tr

**tr** - Translate, squeeze, and/or delete characters from standard input, writing to standard output
- *Example* > cat somefile | tr s $
	- Replaces all lower case s's with a dollar sign ($) then outputs the results to the terminal 
- Can use both ranges (*a-z, A-Z*) or character sets *[:alpha:]*, *[:blank:]*...

#### tee

The tee program rads standard input and copies it both to standard output AND to a file. This allows the user to capture information part of the way through a pipeline, without interrupting the flow.
- *Example* > command1 | **tee** file.txt | command2

### Basic Commands
- **type** - Shows the type of a command and its location
- **which** - Finds the exact location of an executable
- **pwd** - shows the present working directory, stands for 'print working directory'
- **ls** - Lists the contents of the directory
	- **-a** - Shows 'hidden' folders/files (folders/files beginning with a '.')
	- **-l** - Shows a long list of folders/files with more information
	- **--sort=size/time/version/extension** - Sorts the file by the designated descriptor 
- **cd** - Change to a different directory
	- *Example* > cd /home/matt
		- Change the directory to Matt's home folder
- **..** (Two Periods) - Goes up one level in the filepath, to the parent directory
	- **.** (Single Period) - Represents the current directory

### Date Commands
- **date** - Shows current date and time
- **ncal** - Shows  new calendar
- **cal** - Shows calendar

### File Manipulation

#### touch

- **touch** - Change file timestamps/Create files
	- **touch *filename filename***... - Create multiple files at once
		- If you wish to have a space in the file name you must wrap the name in "quotation marks"
	- **touch ../*filename*** - Creates a file in the parent directory

#### file

- **file** - See what type of item a file is
	- If looking at a file with a space in the name you must wrap it in "quotation marks" or escape the space with a backslash (\)

#### rm

- **rm *filename*** - Remove files from the machine
	- **DELETES FILES**, there is no undo or recycling bin to retrieve them from

#### mv

- **mv *source destination*** - When you specify a file(s) as the source and a directory as the destination, you are moving the files into the directory
	- *Example* > mv app.css styles/
		- Will move the app.css file into the styles directory
- **mv *fileone filetwo filethree destination/*** - Moves multiple files into one directory
- **mv *folderone/ foldertwo/*** - Moves the first directory into the second directory
	- If *foldertwo/* does not exist it will rename *folderone/* into foldertwo/

#### cp

- **cp *filename newfile*** - Copies filename into another file called newfile
- **cp *filename destination/newfilename*** - Copies filename into another directory called newfilename
- **cp *filename filename1 destination/*** - Copies filename and filename1 into another directory
- **cp -r *directory/ copyofdirectory*** - Recursively copies directory into a copyofdirectory

#### cat

- **cat *filename*** - Con*cat*enates and prints the contents of a file
	- **cat *filename1 filename2** - Displays the contents of both filename1 and filename2
- **cat *filename.txt* -n** - Displays the contents of the file with each line having a number assosiated with it


#### less

- **less *filename*** - Opens a file in the less program
	- **less navigation**
		- *space* or *f* - Go to the next page
		- *b* - Go back to the previous page
		- *Enter* or *Down Arrow* - Scroll down by one
		- */* - Search followed by a pattern
		- *q* - Quit

#### head

- **head *filename*** - Prints a portion of a file starting at the beginning of the file (Default 10 lines)
- **head -n 21 *filename*** - Prints the first 21 lines of the file
	- **--lines 21** - Equal to *-n 21*
	- **-21** - Equal to *--lines 21* or *-n 21*
- **head -c 8 *filename*** - Prints the first 8 bytes of the file

#### sort

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

#### tail

- **tail *filename*** - Prints a portion of a file starting at the end of the file (Default 10 lines)
- **tail -n 21 *filename*** - Prints the first 21 lines of the file
	- **--lines 21** - Equal to *-n 21*
	- **-21** - Equal to *--lines 21* or *-n 21*
- **tail -c 8 *filename*** - Prints the last 8 bytes of the file
- **tail -f *filename*** - Continue to output data from a file
	- *--follow* - Equal to -f

#### tac

- **tac *filename*** - Concatenate and print file in reverse

#### rev

- **rev *filename*** - Prints out each letter in a file in reverse

#### wc

- **wc *filename*** - Ouputs the number of words, lines or bytes in a file
	- **-l** - Limit the output to the number of lines
	- **-w** - Limit the output to the number of words
	- **-m** - Limit the output to the number of characters
	- **-c** - Limit the output to the number of bytes
