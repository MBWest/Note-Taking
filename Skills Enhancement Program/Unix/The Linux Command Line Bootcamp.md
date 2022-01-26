## The Linux Command Line Bootcamp: Beginner To Power User
### Introduction
#### Resources
- Operating Systems: Timeline and Family Tree 
	- https://eylenburg.github.io/os_familytree.htm
- The world of Operating Systems
	- https://spectrum.ieee.org/the-strange-birth-and-long-life-of-unix
	- https://www.opengroup.org/membership/forums/platform/unix
- Exploring the Original Unix
	- https://www.bell-labs.com/usr/dmr/www/man11.pdf
	- https://www.bell-labs.com/usr/dmr/www/1stEdman.html
- Linux, GNU, Kernes, Oh My!
	- https://www.howtogeek.com/139287/the-great-debate-is-it-linux-or-gnulinux/

### Command Basics (capitalization matters!)
#### Basic Command Structure
- **Command**
- **Options** - Options are prefixed by a dash '-', can be combined together
	- *Example* >  ncal -h
		- Turns off the highlighting of the current day
	- *Example* > ncal -j
		- Will print out a calendar with Julian dates
	- Long Form Options - Full words prefixed with two dashes
		- *Example* > date -u = date --universal
- **Arguments** - Values that we give to a command to work with or operate on
	- *Example* > ncal 1999
	- *Example* > ncal april 1999

### Arrow Keys
- **Left/Right** - Move the cursor along the command
- **Up** - Cycle through previous commands
- **Down** - Cycle through recent commands

#### Date Commands
- **date** - Shows current date and time
- **ncal** - Shows  new calendar
- **cal** - Shows calendar

### File Manipulation
- rm
- sort