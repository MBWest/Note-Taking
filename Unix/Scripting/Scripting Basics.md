# Scripting

## Writing a Basic Script

## The Basic Steps
1. Write a script in a file and save it
2. Make the script executable using chmod
3. Verify that the shell can find your script

## Shebang! (First Line of Script)

The first line of our script shoudl read ***"#!/bin/bash"***

The **"#!"** is called the shebang, and it's used to tell the OS which interpreter it shoud use when parsing this file. 

## Comments (#)

Lines that begine with **"#"** will not be read by the shell. 

## Commands

You can write any of the commands that are normally run from the command line. 

## Executing the Script

We can execute the script the 'long way' by running **bash PathToFile**

## Locating Commands

If we want the shell to find our own programs, we need to make sure we put them in a folder that is in the PATH variable

A common place to put user-defined programs is in a bin folder located in the user's home directory. 
	- *Example* >  /home/colt/bin
- If that directory is not yet part of your path, you can add it by putting PATH="$HOME/bin:$PATH" in your .bashrc file

## Making it Executable 

Make sure the file containing our script is executable. 
	- *Example* > chmod a+x FileName 
		- Grants executable permissions to everyone

### The PATH Variable

## Writing our first script

	#!/bin/bash

	#This is my first script

	echo "Hello there, $USER"
	echo "Today is $(date)"
	echo "last ran hi at $(date)" >> hi.log