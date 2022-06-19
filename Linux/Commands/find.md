# Find Command

By default the **find** command will list every single file and directory nested in our current working directory. You can also provide a specific folder
- *Example* > find friends/
	- Print all the files and directories inside the friends directory, including nested folders

## Options

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

## Finding by Time and Types of Timestamps

Use the find command and the applicable modifiers to look for time ranges
Without these modifiers at the beggining of your numbers to specify less-than (**-**) and greater-than (**+**) your number will specify exactly 
- **find -mmin *number*** - Find by modified time
- **find -amin *number*** - Find by accessed time
- **find -cmin *number*** - Find by changed time

### Types of Timestamps
- **mtime**, or modification time, is when a file was last modified AKA when its contents last changed. This is the default time shown when running *'ls -l'*.
- **ctime**, or change time, is when a file was last changed. This occurs anytime mtime changes but also when we rename a file, move it, or alter permissions. To see change time us the *'ls -lc'* command. 
- **atime**, or access time, is updated when a file is read by an application or a command like cat.To see access time us the *'ls -lu'* command. 

### Modifying Time Stamps Using the Touch Command
- **-d** - Allows you to create a file and specify the timestamp
	- *Example* > touch *filename* -d "1 week ago"
		- Creates a file and sets mtime of the file to exactly 1 week ago

## Find with Logical Operators

We can also use the **-and**, **-or**, and **-not (!)** operators to create more complex queries.
- *Example* > find -name "*chick* -or -name "*kitty*"
	- Finds all files with the name chick or kitty
- *Example* > find -cmin -60 -not -name "*.log"
	- Finds all files with ctime less than 60 minutes ago and do not have *.log in their name 

## Find with Exec and User Defined Actions

We can provide find with our own actions to perform using each matching parthname. 
The syntaxx is **find -exec *command* {} ;**
- Instead of **-exec** you can use *-ok** and the terminal will ask (y/n) for each item
- The **{}** are a placeholder for the current pathname (each match), and the semicolon(;) is required to indicate the end of the command
- *Example* > find ~ -type f -empty -exec ls -l '{}' ';'
	- Find all the empty files in my home directory and run the ls -l command against each item found
- *Example* > find -type f -name "*.html" -exec cp '{}' '{}_COPY' ';'
	- Finds all files that end with .html. Then creates a copy of each using the cp command.

## Examples

- **find . -name 'file*.txt'** - Find all files with the pattern denoted in the 'pattern' from the current directory and all sub directories. 

`SETUID and SETGID Bits`

    find / -perm -4000 -ls 2>/dev/null