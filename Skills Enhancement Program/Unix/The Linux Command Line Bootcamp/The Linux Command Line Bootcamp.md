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
- **mkdir *foldername1*** - Creates a new folder in the current directory
- **mkdir *foldername1 foldername2*** - Creates multiple folders
	- Can provide an absolute path or a relative path
- **mkdir -p** - Make parent directories as needed (useful if nested folders do not already exist)
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
- **touch** - Change file timestamps/Create files
	- **touch *filename filename***... - Create multiple files at once
		- If you wish to have a space in the file name you must wrap the name in "quotation marks"
	- **touch ../*filename*** - Creates a file in the parent directory
- **file** - See what type of item a file is
	- If looking at a file with a space in the name you must wrap it in "quotation marks" or escape the space with a backslash (\)
- **rm *filename*** - Remove files from the machine
	- **DELETES FILES**, there is no undo or recycling bin to retrieve them from