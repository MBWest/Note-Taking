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

- *Exmaple* > (echo $((10+7)))

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

## Permissions

### Groups

On Unix systems, a single user may be the owner of files and directories, meaning that they have control over their access. 
Additionally, users can belong to groups which are given access to particular files and folders by their owners. 
- **whoami** - Shows current terminal user

### User and Group IDs

When a new user account is made, it is assigned a user ID. The user is also assigned a group ID. 
These user IDs are stored in /etc/passwd, and the group IDs are stored in /etc/group.
- **id** - View Users and Group IDs

### File Attributes

#### File Type
- **-** - Regular File
- **d** - Directory
- **c** - Special File or Device
- **l** - Symbolic Link
- **b** - Block Device
- **s** - Socket
- **p** - Named Pipe

|Owner|Group|World|
|---|---|---|
|rwx|rwx|rwx|

| Character | Effect On Files | Effect On Directories |
|--|--|--|
| r | file can be read | directory's contents can be listed |
| w | file can be modified | directory's contents can be modified (create new files, rename files/folders) but only if the executable attribute is also set |
| x | file can be treated as a program to be executed |  allows a directory to be entered or "cd"ed into |
| - | file cannot be read, modified, or executed depending on the location of the - character  | directory contents cannot be shown, modified, or cd'ed into depending on the location of the - character |

#### Examples

|Owner|Group|World|
|---|---|---|
|rw-|- - -|- - -|

- In the above example, we see that the file's owner has read and write permissions but NOT execute permissions. No one else has any access.

|Owner|Group|World|
|---|---|---|
|rwx|- - -|- - -|

- In the above example, we see that the file's owner has read, write, AND execute permissions. No one else has any access.

|Owner|Group|World|
|---|---|---|
|rw-|r- -|r- -|

- In the above example, we see that the file's owner has read, and write BUT NOT execute permissions. Members of the file's owner group can only read the file. Everyone else can read the file too.

|Owner|Group|World|
|---|---|---|
|rwx|rwx|- - -|

- In the above example, we see that the directory's owner AND member's of the owner group can enter the directory, rename, and remove files from within the directory. 


|Owner|Group|World|
|---|---|---|
|rwx|- -x|- - -|

- In the above example, we see that the directory's owner can enter the directory, rename, and remove files from within the directory. Members of the owner group can enter the directory but
cannot create, delete, or rename files.

### The Sticky Bit 
The sticky bit is to tell the OS to run the executable as its owner. Indicated by the ‘s’ instead of ‘x’
- **-rwsrwx---**
- This is very important to configure correctly. If you have a root based executable with the sticky bit set for everyone then anyone can run it as root!

#### Permission Commands

- **chmod** - To change the permissions of a file or directory, we can use the chmod command
	- To use chmod to alter permissions we need to tell it: ***Who, What, Which***
		- *Who:*
			- **u** - User (The owner of the file)
			- **g** - Group (Members of the group the file belongs to)
			- **o** - Others (The 'World')
			- **a** - All of the above
		- *What:*
			- **Minus Sign (-)** - Removes the permission
			- **Plus Sign (+)** - Grants the permission
			- **Equal Sign (=)** - Set a permission and removes others
		- *Which:*
			- **r** - The read permissions
			- **w** - The write permissions
			- **x**- The execute permissions
	*Examples:*
	**Add write permissions to the group**
	chmod g+w file.txt
	**Remove write permissions from all**
	chmod a-w file.txt

- **chmod octals** - Chmod also supports octal number (base 8). Each digit in an octal number represents 3 binary digits

|Octal  | Binary  | File Mode  |
|--|--|--|
|  0| 000 | - - - |
|1  | 001 | - -x |
| 2 |  010| -w- |
|  3|  011| -wx |
|  4|  100| r- - |
|  5| 101 |r-x |
|  6|110  |rw-  |
|  7| 111  |rwx  |


- **chown** - Changes the owner or the group owner of a file or directory
	- *Example* > chown bojack file.txt
		- Makes bojack the owner of file.txt 
	- *Example* > chown :horses file.txt
		- Makes the file.txt group owner horses
- **sudo** - Execute a command as another user (chown USER[:GROUP] FILE(s))
	- *Example* >  sudo -l
		- Shows all commands that the current user can run as the super user
- **addgroup** - Add a Group
- **adduser** - Add a User
- **su** - Substitute user as another user. 
	- *Example* > su - hermione
		- Createes a new login shell for the user hermione. You would need to entire hermione's password.
	- To leave the session type, exit. 

## Enviorment

### Viewing the Environment

- **printenv** or **env** - Prints out standard environmental information

### Parameter Expansion

If you write out the name of an enviornment variable prefixed with a dollar sign ($) the shell will replace it with the actual value

### Defining Variables

To define a cariable, use the syntax **variable=value**
	- To make a variable a global variable, prefix the variable with **export**

### Startup Files

**Login Session**
- **/etc/profile**- Global config for all users
- **~/.bash_profile** - user's personal config file
- **~/.bash_login** - read if bash_profile isn't found
- **~/.profile** - used if previous two aren't found

**Non-login Session**
For non-login session (typical session when you launch the terminal via the GUI):
- **etc/bash.bashrc** - Global config for all users
- **~/.bashrc** - Specific settings for each user. This is where you can define your own settings and configurations

## Scripting

### Writing a Basic Script

#### The Basic Steps
1. Write a script in a file and save it
2. Make the script executable using chmod
3. Verify that the shell can find your script

#### Shebang! (First Line of Script)

The first line of our script shoudl read ***"#!/bin/bash"***

The **"#!"** is called the shebang, and it's used to tell the OS which interpreter it shoud use when parsing this file. 

#### Comments (#)

Lines that begine with **"#"** will not be read by the shell. 

#### Commands

You can write any of the commands that are normally run from the command line. 

#### Executing the Script

We can execute the script the 'long way' by running **bash PathToFile**

#### Locating Commands

If we want the shell to find our own programs, we need to make sure we put them in a folder that is in the PATH variable

A common place to put user-defined programs is in a bin folder located in the user's home directory. 
	- *Example* >  /home/colt/bin
- If that directory is not yet part of your path, you can add it by putting PATH="$HOME/bin:$PATH" in your .bashrc file

#### Making it Executable 

Make sure the file containing our script is executable. 
	- *Example* > chmod a+x FileName 
		- Grants executable permissions to everyone

### The PATH Variable

### Writing our first script

#!/bin/bash

#This is my first script

echo "Hello there, $USER"
echo "Today is $(date)"
echo "last ran hi at $(date)" >> hi.log

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

### Cron

The cron service allows you to schedule commands to run at regular intervals

#### Editing the crontab

To set up a cron job, we need to edit the crontab configuration file. Rather than edit the files directly it is best to use the **crontab -e** command.

#### Cron Syntax (https://crontab.guru/)

| a|b  |c  |d  |e  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

- asteric(*) - Any Value
- 5,6 - List of values (5 and 6)
- 1-4 - Range of values (1 to 4)
- */5 - Step values (every 5)

#### Examples

1. Run a job at minute 30, every hour (everytime the clock shows x:30)
| 30|*  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

2. Run a job every day at midnight (when hour is 0 and minute is 0)

| 30|6  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

3. Run a job every monday at 6:30AM

| 30|6  |*  |*  |1  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

4. Run a job every monday in April at 6:30AM

| 30|6  |*  |4  |1  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

5. Run a job at midnight on the first of every month

| 0|0  |1  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

6. Run a job at midnight every weekday (monday-friday)

| 0|0  |*  |*  |1-5  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

7. Run a job every 5 minutes

| */5 |*  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

### Locate Command

The locate command references a pre-generated database file rather than searching the entire matchine. Update this database using the **updatedb** command.

The **locate** command performs a search of pathnames across the machine that match a given substring and then prints out any matching names
- *Example* > locate chick
	- Locates all files and directories with the name 'chick' in them
You can use expansion characters (*, ?) to narrow down the search.
- *Example* >  locate /bin/less???
	- locates all files that contain the /bin/less with exactly 3 characters afterwards.

**Options**
- -i - Option tells locate to ignore casing
- -l - Option tells locate to limit the number of entries that locate retrieves
- -e - Option will only print entries that actually exist at the time locate is run

### Find Command

By default the **find** command will list every single file and directory nested in our current working directory. You can also provide a specific folder
- *Example* > find friends/
	- Print all the files and directories inside the friends directory, including nested folders

**Options**
- **-type f** - Will limit searches to files
- **-type d** - Will limit searches to directories
- **-name "*.txt"*** - Will limit searches to files with *.txt* at the end
	- Use the ***-iname*** option for a case insensitive search
- **-size** - Find files of a specific size
	- *Example* > find -size +1G
		- Finds all files larger than 1 gigabyte
	- *Example* > find -size -50m
		- Finds all files smaller than 50 megabytes
	- *Example* > find -size 20k
		- Finds all files exactly 20 kilobytes big
- **-user** - Matches files na ddirectories that belong to a particular user
- **-empty** - Finds all empty files and folders

### Finding by Time and Types of Timestamps

Use the find command and the applicable modifiers to look for time ranges
Without these modifiers at the beggining of your numbers to specify less-than (**-**) and greater-than (**+**) your number will specify exactly 
- **find -mmin *number*** - Find by modified time
- **find -amin *number*** - Find by accessed time
- **find -cmin *number*** - Find by changed time

**Types of Timestamps**
- **mtime**, or modification time, is when a file was last modified AKA when its contents last changed. This is the default time shown when running *'ls -l'*.
- **ctime**, or change time, is when a file was last changed. This occurs anytime mtime changes but also when we rename a file, move it, or alter permissions. To see change time us the *'ls -lc'* command. 
- **atime**, or access time, is updated when a file is read by an application or a command like cat.To see access time us the *'ls -lu'* command. 

**Modifying Time Stamps Using the Touch Command**
- **-d** - Allows you to create a file and specify the timestamp
	- *Example* > touch *filename* -d "1 week ago"
		- Creates a file and sets mtime of the file to exactly 1 week ago

### Find with Logical Operators

We can also use the **-and**, **-or**, and **-not (!)** operators to create more complex queries.
- *Example* > find -name "*chick* -or -name "*kitty*"
	- Finds all files with the name chick or kitty
- *Example* > find -cmin -60 -not -name "*.log"
	- Finds all files with ctime less than 60 minutes ago and do not have *.log in their name 

### Find with Exec and User Defined Actions

We can provide find with our own actions to perform using each matching parthname. 
The syntaxx is **find -exec *command* {} ;**
- Instead of **-exec** you can use *-ok** and the terminal will ask (y/n) for each item
- The **{}** are a placeholder for the current pathname (each match), and the semicolon(;) is required to indicate the end of the command
- *Example* > find ~ -type f -empty -exec ls -l '{}' ';'
	- Find all the empty files in my home directory and run the ls -l command against each item found
- *Example* > find -type f -name "*.html" -exec cp '{}' '{}_COPY' ';'
	- Finds all files that end with .html. Then creates a copy of each using the cp command. 

### Xargs Command

When **-exec** is used, the command is executed separatley for every single element, unlike **xargs** which builds up the input into a bundle that will be provided as an arguement to the next command. 
find -name "*txt" -exec ls '{}' ';' **=EQUALS=** find -name ".txt" | xargs ls

### Grep

#### Grep Basics

The **grep** command searches for patterns in each file's content. **Grep** will print each line that matches a pattern we provide
- Example > grep "chicken" animals.txt
	- Prints each line from the animals.txt file that contains the pattern "chicken"

#### Grep Options

- **-i** - Makes grep search case insensitve
- **-w** - Ensures that grep only matches whole words rather than fragments located inside other words
- **-r** - Perfoms a recursive search, which will include all files under a directory, subdirectories, and their files, and so on 
- **-n** - Lables each line with the applicable line number
- **-c** - Counts how many times the grep commands finds the requested pattern
- **-A** - Gives x number of lines after each pattern found
- **-B** - Gives x number of lines before each pattern found
- **-C** - Gives x number of lines before and after each pattern found
- **-E** - Same as using egrep

#### Grep and Regular Expressions
- **.**- Matches any single character
- **?**- Matches 1 or less the preceding pattern
- **^** - Matches the start of a line
- **$** - Matches the end of a line
- **[abc]** - Matches any character in the set
- **[^abc]**- Matches any character NOT in the set
- **[A-Z]** - Matches characters in a range
- **a{1}** - Matches the preceding letter repeating {x} times (a{3} =EQUALS= aaa)
- * - Repeat previous expression 0 or more times
- **\*** - Escape meta-characters

### Working with Processes

#### Get a Process ID (pidof)

- *Example* > pidof firefox
    - Returns the process id of firefox

#### Get a List of Processes (ps)

- *Example* > ps
    - Get a list of processes you have access to

- *Example* > ps aux 
    - See a list of every process being ran

- *Example* > top
    - Provides cpu memory usage and process IDs

#### Killing of Processes

- *Example* > kill -l
    - List all available ways to kill a signal

- *Example* > kill 9 2975
    - Uses the SIGKILL to kill the 2975 process

- *Example* > pkill firefox
    - Kills the firefox process

- *Example* > killall firefox
    - Kills the firefox process

#### Dealing with Open Files

- **lsof** - Identifies any open files on the system
    - *Example* > lsof +D /var/log
        - Views all sub directories to see if anything is open 
    - *Example* > lsof -u brandon
        - View open files by the user Brandon

**Output of lsof**
- **Command** - Name of the application ran 
- **PID** - PID of the application
- **USER** - Users context the application is running in
- **FD** - File Drescriptor
    - **Cwd** - Shows the current working directory
    - **Txt** - Shows its a text file
    - **Mem** - Data Segment or Shared Object loaded into memory
    - **Number** - This will be a digit and will show the actual file discriptor number (#u)
- **TYPE** - Tells us what type of file
    - **REG** - Regular file
    - **DIR** - Directory
    - **FIFO** - Named pipe, symbolic links, sockets, blocks
    - **UNKOWN** - Normally happens with kernel threads
- **DEVICE** - The drive, EX: sda1
- **SIZE/OFF** - Size of the file
- **NODE** - inode number
- **NAME** - Name of the file

## Kernel

- The Linux Kernel is a result of collaborative development efforts from developers accross the globe.
- Small incremental changes, also known as patches add:
    - New features
    - Make enhancements
    - Fix bugs
- A new release of Linux kernel happens every 2 to 3 months. 
    - Realeases are time based rather than feature based

### Kernel Module
- Loaded on demand
    - Become part of the kernel once loaded

**Module commands**
- **insmod** - Insert a module into the kernel
- **rmmod** - Remove a module from the kernel
- **lsmod** - List the currently loaded modules
- **modinfo** - Display information about a module
- **modprobe** - Insert or remove a module from the kernel. Unlike insmod, modprobe automatically handles module dependencies. Dependent modules will be automatically loaded or unloaded with modprobe **-a**
    - *Example* > modpro [options] modulename params
    Option
    - **c** - Show configuration file
    - **l** - List modules
    - **r** - Remove modules

## File System

- **/boot** - Holds important files during boot-up process, including Linux Kernel
- **/root** - This is the home directory of root user and should never be confused with ‘/‘
- **/dev** - Contains device files for all the hardware devices on the machine e.g., cdrom, cpu, etc
- **/etc** - Contains Application’s configuration files, startup, shutdown, start, stop script for every individual program
- **/bin -> /usr/bin** - All the executable binary programs (file) required during booting, repairing, files required to run into single-user-mode, and other important, basic commands viz., cat, du, df, tar, rpm, wc, history, etc 
- **/sbin -> /user/sbin** - Contains binary executable programs, required by System Administrator, for Maintenance. Viz., iptables, fdisk, ifconfig, swapon, reboot, etc.
- **/opt** - Optional is abbreviated as opt. Contains third party application software. Viz., Java, etc.
- **/proc** - A virtual and pseudo file-system which contains information about running process with a particular Process-id aka pid
- **/lib -> /usr/lib** - The Lib directory contains kernel modules and shared library images required to boot the system and run commands in root file system
- **/tmp** - System’s Temporary Directory, Accessible by users and root. Stores temporary files for user and system, till next boot
- **/home** - Home directory of the users. Every time a new user is created, a directory in the name of user is created within home directory which contains other directories like Desktop, Downloads, Documents, etc.
- **/var** - Stands for variable. The contents of this file is expected to grow. This directory contains log, lock, spool, mail and temp files
- **/run** - System daemons that start very early to store temporary runtime files like PID files
- **/mnt** - Temporary mount directory for mounting file system
- **/media** - Temporary mount directory is created for removable devices viz., media/cdrom.
- **/lost+found** - This Directory is installed during installation of Linux, useful for recovering files which may be broken due to unexpected shut-down
- **/run** - This directory is the only clean solution for early-runtime-dir problem
- **/srv** - Service is abbreviated as ‘srv‘. This directory contains server specific and service related files
- **/sys** - Modern Linux distributions include a /sys directory as a virtual filesystem, which stores and allows modification of the devices connected to the system
- **/usr** - Contains executable binaries, documentation, source code, libraries for second level program

**Linux is a complex system which requires a more complex and efficient way to start, stop, maintain and reboot a system unlike Windows. There is a well defined configuration files, binaries, man pages, info files, etc. for every process in Linux.** (https://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/)

- **/boot/vmlinuz **- The Linux Kernel file
- **/dev/hda** - Device file for the first IDE HDD (Hard Disk Drive)
- **/dev/hdc** - Device file for the IDE Cdrom, commonly
- **/dev/null** - A pseudo device, that don’t exist. Sometime garbage output is redirected to /dev/null, so that it gets lost, forever
- **/etc/bashrc** - Contains system defaults and aliases used by bash shell
- **/etc/crontab** - A shell script to run specified commands on a predefined time Interval
- **/etc/exports** - Information of the file system available on network
- **/etc/fstab** - Information of Disk Drive and their mount point
- **/etc/group** - Information of Security Group
- **/etc/grub.conf** - grub bootloader configuration file
- **/etc/init.d** - Service startup Script
- **/etc/lilo.conf** - lilo bootloader configuration file
- **/etc/hosts** - Information of Ip addresses and corresponding host names
- **/etc/hosts.allow** - List of hosts allowed to access services on the local machine
- **/etc/host.deny** - List of hosts denied to access services on the local machine
- **/etc/inittab** - INIT process and their interaction at various run level
- **/etc/issue** - Allows to edit the pre-login message
- **/etc/modules.conf** - Configuration files for system modules
- **/etc/motd** - motd stands for Message Of The Day, The Message users gets upon login
- **/etc/mtab** - Currently mounted blocks information
- **/etc/passwd** - Contains password of system users in a shadow file, a security implementation.
- **/etc/printcap** - Printer Information
- **/etc/profile** - Bash shell defaults
- **/etc/profile.d** - Application script, executed after login
- **/etc/rc.d** - Information about run level specific script
- **/etc/rc.d/init.d** - Run Level Initialisation Script
- **/etc/resolv.conf** - Domain Name Servers (DNS) being used by System
- **/etc/securetty** - Terminal List, where root login is possible
- **/etc/skel** - Script that populates new user home directory
- **/etc/termcap** - An ASCII file that defines the behaviour of Terminal, console and printers
- **/etc/X11** - Configuration files of X-window System
- **/usr/bin** - Normal user executable commands
- **/usr/bin/X11** - Binaries of X windows System
- **/usr/include** - Contains include files used by ‘c‘ program
- **/usr/share** - Shared directories of man files, info files, etc
- **/usr/lib** - Library files which are required during program compilation
- **/usr/sbin** - Commands for Super User, for System Administration
- **/proc/cpuinfo** - CPU Information
- **/proc/filesystems** - File-system Information being used currently
- **/proc/interrupts** - Information about the current interrupts being utilised currently
- **/proc/ioports** - Contains all the Input/Output addresses used by devices on the server
- **/proc/meminfo** - Memory Usages Information
- **/proc/modules** - Currently using kernel module
- **/proc/mount** - Mounted File-system Information
- **/proc/stat** - Detailed Statistics of the current System
- **/proc/swaps** - Swap File Information
- **/version** - Linux Version Information
- **/var/log/lastlog** - log of last boot process
- **/var/log/messages** - log of messages produced by syslog daemon at boot
- **/var/log/wtmp** - list login time and duration of each user on the system currently




## Processes

### Program vs. Process
- **Program** - Is an executable file on the disk
    - **Process** - Is an instance of that program or is a program or application that is in execution

### Types of Processes

#### Foreground Process

Also known as an interactive process. Terminal for example or web browser. 

#### Background Process

Also known as a non-interactive process. These are not normally connected to any foreground process and don't expect any user input. 

### User and System Processes
- They dont actuall run simultaneously
- The OS split time between each process and the CPU

### Process IDs

- **PID** (Process ID) When a program is started it is assigned a PID
    - *Kernel* PID 0
- **PPID** (Parent Process ID)
    - init.d PID 1, PPID 0 
- **Process Tree**
    - Starts at PID 0

### States of a Process

- **Running** - Either actively running or waiting for a CPU core to be assigned to it
- **Waiting** - In this state the process is waiting for 1 of 2 things
    - Event to happen such as user input, etc
    - Systems resources to become available
    - ***Two Types of Waiting***
        - **Interrupted** - Some hardware based conditions would cause this
        - **Uninterruptible** - This process cannot be stopped by any event or signal
- **Stopped** - The process has been stopped by some means
    - This can be a signal to stop from the user or system
    - Can also be in this state during the time a debugger is attached to it
- Zombie/Orphan - The process is no longer alive or AKA dea
    - The reason it is still showing as a 'Zombie' or 'z' is due to still being on the process entry table in the kernel

### Signals

A system message sent from one process to another, not usually used to transfer data but instead of used to remotely command the partnered process.

When a process receives a Signal, either of the **three** things can happen:
- **Default** - Process excecute the default action of the signal.
    - *Example* > When process receives SIGTERM signal, process is terminated by default
- **Customized** -  Process executes customized processing on receiving the singal by executing the *signal handler routine* (Special function which is invoked when the process receives a signal. Executed at the highest priority)
    - *Example* > When process receives the SIGTERM signa, process might want to print the Goodbye msg on the screen, or write its internal data structure in a file for offline debugging before it dies out
- **Ignore** - Process ignore the signal

#### Well Known Linux Signals

- **SIGINT** - Interrupt (i.e., Ctrl-C)
- **SIGUSR1 and SIGUSR2** - User defined signals
- **SIGKILL** - Sent to the process from kernel when kill -9 is invoked on a PID. 
    - This signal cannot be caught by the process.
- **SIGABRT** - Raised by abort() by the process itself. Cannot be blocked. The process is terminated. 
- **SIGTERM** - Raised when *kill* is invoked. Can be caught by the process to execute user defined actions.  
- **SIGSEGV** - Segmentation fault, raised by the kernel to the process when illegal memory is referenced.
- **SIGCHILD** - Whenever a child terminates, this is the signal sent to the parent. 

## Network File Sharing (NFS)



### Network File System (NFS) 
- Default Port 2049
- Remote access to file system
- Supported by Linux, UNIX, Windows
- Packages
- Name Resolution

### NFS Server Configuration
- **/etc/exports/** - Which file systems are exported, permissions and which host may mount them
- **/etc/host.allow** - Which hosts are permitted to mount exported file systems
- **/etc/host.deny** - Which host are explicity denied permissions to mount exported file systems

### Mounting
Mount an NFS file system to access it
     - *Example* > mount -t nfs computer:fs /mount_point

