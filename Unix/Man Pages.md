# Man Pages (Manuals)

## What are Man Pages?
Built-in form of documentation available on nearly all UNIX-like operating systems

## Navigating and Searching a Man Page
- **man *command*** - Opens a man page for a command
	- *Example* > man ncal
		- Opens the ncal Man Page
- ***man -k search-term*** - Search the short description and manual page names for the search-term provided
	- *Example* >  man -k dog

## While in a Man Page

- ***'q'*** - Exits a Man Page
- ***'Down Arrow/Up Arrow'*** - Scroll one line at a time
- ***'Space Bar'*** - Jumps down 1 page at a time
- ***'b'*** - Jumps up 1 page at a time
- ***'f'*** - Jumps down 1 page at a time
- ***'h'*** - Opens the *help* document
- ***'/???'*** - Search in a man page

## Parsing Man Page Synopsis
-  ***[optional]*** - Anything in [brackets] is optional 
- ***[short-option]...*** - One or more strings can be provided
- ***[string]...*** - One or more options can be provided
- ***OPTIONS*** - Must pass along options that are not in [brackets]

## Manual Sections

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