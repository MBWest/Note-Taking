# Command Basics (capitalization matters!)

## Basic Command Structure

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

## Alias

### Format

alias name=`value`

### Examples

- **alias ll=`ls -alF`** - Typing 'll' into the command line will instead execute the `value` listed
- **alias del=`rm -rfi`** - Typing 'del' into the command line will instead execute the `value` listed
	- This alias is common for individuals to manually add to force the command prompt to ask if you want to delete a file
- **alias c=`clear`** -Typing 'c' into the command line will instead execute the `value` listed

### .bsahrc

When updating the .bashrc file with alias' you must run `source .bashrc` command if you want the current shell to recognize the new alias`