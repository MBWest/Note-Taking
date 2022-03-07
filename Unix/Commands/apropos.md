# apropos

`apropos [OPTION..] KEYWORD...`

- **apropos *compress***- Suppose you don’t know how to compress a file then you could type the following command in terminal and it will show all the related command and its short description or functionality.

**Options**
- **-v** - Print verbose warning messages
- **-e** - Search each keyword for exact match
- **-w** - This option is used when the keyword(s) contain wildcards
- **-d** - Emit debugging messages
- **-a, –and** - When we want all the keywords to match
- **-l, –long** - Output is trimmed to the terminal width
    - This option becomes handy when we don’t want the result to be truncated
- **-r, –regex** - Interpret each keyword as a regex(regular expression)
- **-C** - Don’t want to use the default(/manpath) but user configuration file
- **-L** -  Define the locale for this search
- **-m, –systems** - This option use manual pages from other systems
    - This option is helpful when we want to search the man page description of other accessible operating system
- **-M, –manpath** - Set search path for manual pages to PATH rather than the default $MANPATH
- **-s, –sections, –section** - This option is used when we want to search only particular sections (colon-separated) that are given in the argument
