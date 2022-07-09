# apropos

> ## **Syntax** 

`apropos [OPTION..] KEYWORD...`

---

> ## **Example** 

| **Command**   | **Description**   |
| --------------|-------------------|
| **apropos** |
| `apropos *keyword*` | Show all the related commands and short descriptions or functionality. `apropos compress`. |
| **Options** |
| `-v` | Print verbose warning messages. |
| `-e` | Search each keyword for exact match.  |
| `-w` | This option is used when the keyword(s) contain wildcards. |
| `-d` | Emit debugging messages. |
| `-a, --and` | When we want all the keywords to match. |
| `-l, --long` | Output is trimmed to the terminal width. This option becomes handy when we don’t want the result to be truncated |
| `-r, --regex` | Interpret each keyword as a regex(regular expression). |
| `-C` | Don’t want to use the default(/manpath) but user configuration file. |
| `-L` | Define the locale for this search.  |
| `-m, --systems` | This option use manual pages from other systems.  This option is helpful when we want to search the man page description of other accessible operating system |
| `-M, --manpath` | Set search path for manual pages to PATH rather than the default $MANPATH.  |
| `-s, --sections, --section` | This option is used when we want to search only particular sections (colon-separated) that are given in the argument. |


