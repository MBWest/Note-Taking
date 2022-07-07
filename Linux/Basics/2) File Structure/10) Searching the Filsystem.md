# Linux File Structure - Searching the Filesystem

> ## **whatis [-dlv?V] [-r|-w] [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] name...**
- Display one-line manual page descriptions

```
[guru@CentOS ~]$ whatis passwd
passwd	(1)  		- update user's authentication tokens
passwd	(5)  		- password file
passwd [sslpasswd](lssl)	- compute password hashes
```

---

> ## **which [options] programname [...]**

- Prints the full path of the executable that would have been executed had the argument been entered at a shell prompt
- Searches for an executable/script in the directories listed in the PATH environment variable

```
[guru@CentOS ~]$ which passwd
/usr/bin/passwd

[guru@CentOS ~]$ which bash
/bin/bash
```

---

> ## **whereis [option] name...**
- Locate the binary, source, and manual pages for a command

```
[guru@CentOS ~]$ whereis passwd
passwd: /usr/bin/passwd /etc/passwd /usr/share/man/man1/passwd.1.1gz /usr/share/man/man5/passwd.5.gz

[guru@CentOS ~]$ whereis -m passwd
passwd: /usr/share/man/man1/passwd.1.1gz /usr/share/man/man5/passwd.5.gz
```

---

> ## **locate [OPTION]... PATTERN...**
- Searches for files in databases prepared by updatedb
- Use `updatedb` to update the database information
- `-i` - ignore case
- `-r REGEX` - search for a basic regular expression
- `--regex`  - interpret PATTERN(s) as extended regular expressions

```
[guru@CentOS ~]$ locate file1
/home/guru/file1

[guru@CentOS ~]$ locate my-script.py 
/home/guru/my-script.py

[guru@CentOS ~]$ touch file4

[guru@CentOS ~]$ locate file4

[guru@CentOS ~]$ sudo updatedb

[guru@CentOS ~]$ locate file4
/home/guru/file4
```

---

> ## **find [path...] [expression]**
- Search for files in a directory based on specific criteria and potentially perform actions on those files
- An expression is made up of OPTIONS, TESTS, and ACTIONS all separated by operators (-and is - assumed if no operator is specified)
- OPTIONS:
    - `-maxdepth N`- descend at most N levels of directories 
    - `-mount` - do not descend directories on other filesystems

> ## **find [path...] [expression][actions]**
- TESTS:
    - `-name PATTERN` - base of filename matches PATTERN
    - `-iname`  - same as above, but not case sensitive
    - `-perm`   - match on file permissions (multiple invocations)
    - `-type C`- match on file type (C describes different file types)
- ACTIONS:
    - `-delete` - delete files
    - `-exec COMMAND {} +` - execute command 
        - {} is replaced by current file name being processed

```
[guru@CentOS ~]$ find / -name file 2>/dev/null
/usr/bin/file
/usr/share/file

[guru@CentOS ~]$ find / -iname file 2>/dev/null
/usr/lib/perl5/File
/usr/bin/file
/usr/share/perl5/File
/usr/share/file

[guru@CentOS ~]$ ls -l my-script.py 
-rw-rw-r-- 1 guru guru 30 Jan  4 01:41 my-script.py

[guru@CentOS ~]$ find -name "*.py" -exec cat {} + 

#!/usr/bin/python
print('hi')
```