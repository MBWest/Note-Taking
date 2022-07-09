# Linux File Structure - File Management

> ## **ls [OPTION]... [FILE]...**
- List information about FILEs (the current directory by default)
    - `-a` - display all files
    - `-i` - display inode 
    - `-l` - display in a long listing format
    - `-R` - Display subdirectories recursively

```
[guru@CentOS ~]$ ls -al
drwx------  7 guru guru 4096 Jan  2 12:06 .
drwxr-xr-x. 3 root root 4096 Dec 31 12:27 ..
-rw-------  1 guru guru  806 Jan  1 18:06 .bash_history
drwxrwxr-x  2 guru guru 4096 Jan  2 12:06 Desktop
drwxrwxr-x  2 guru guru 4096 Jan  2 12:06 Downloads
```
---
> ## **cd [-L|-P] [dir]**

- Change the current directory to dir.  Default dir is the value of the HOME shell variable

---

> ## **pwd [OPTION]...**

- Print name of current/working directory

```
[guru@CentOS ~]$ pwd
/home/guru

[guru@CentOS ~]$ cd Downloads/

[guru@CentOS Downloads]$ pwd
/home/guru/Downloads
```

---
> ## **mkdir [OPTION]... DIRECTORY...**
- Create DIRECTORY(ies), if they do not already exist
- `-p`- no error if existing, make parent directories as needed

```
[guru@CentOS Downloads]$ mkdir -p These/are/new/folders

[guru@CentOS Downloads]$ ls -R These/
These/:
are
These/are:
new
These/are/new:
folders
These/are/new/folders:
```

---

> ## **rmdir [OPTION]... DIRECTORY...**
- Remove the DIRECTORY(s), if they are empty
- `-p`- remove DIRECTORY and its ancestors

```
[guru@CentOS Downloads]$ mkdir -p These/are/new/folders

[guru@CentOS Downloads]$ rmdir -p These/are/new/folders

[guru@CentOS Downloads]$ ls -R These
ls: cannot access These: No such file or directory

[guru@CentOS Downloads]$ ls
movies  music
```
---

> ## **rm [OPTION]... FILE...**
- Remove (unlink) the FILE(s)
- `-f` - ignore nonexistent files, never prompt
- `-R` or `-r` - Remove directories and their contents recursively

```
[guru@CentOS Downloads]$ touch movies/movie{1,2,3,4,5}

[guru@CentOS Downloads]$ ls movies/
movie1  movie2  movie3  movie4  movie5

[guru@CentOS Downloads]$ rm movies/*

[guru@CentOS Downloads]$ ls movies/

[guru@CentOS Downloads]$ ls
movies  music

[guru@CentOS Downloads]$ rm -r movies/

[guru@CentOS Downloads]$ ls
music
```

---

> ## **cp [OPTION]... [-T] SOURCE DEST  || cp [OPTION]... SOURCE... DIRECTORY || cp [OPTION]..**. -t DIRECTORY SOURCE...
- Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY
- `-r` or `-R` - copy directories recursively

```
[guru@CentOS ~]$ ls Desktop/
manifest.txt  passwords.txt  tools

[guru@CentOS ~]$ ls Downloads/

[guru@CentOS ~]$ cp -r Desktop/* Downloads/

[guru@CentOS ~]$ ls Downloads/
manifest.txt  passwords.txt  tools
```

---

> ## **mv [OPTION]... [-T] SOURCE DEST || mv [OPTION]... SOURCE... DIRECTORY || mv [OPTION]... -t DIRECTORY SOURCE...**
- Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY

```
[guru@CentOS ~]$ ls Documents/

[guru@CentOS ~]$ ls Downloads/
manifest.txt  passwords.txt  tools

[guru@CentOS ~]$ mv Downloads/passwords.txt Documents/

[guru@CentOS ~]$ ls Documents/
passwords.txt

[guru@CentOS ~]$ mv Documents/passwords.txt Documents/totally-not-passwords

[guru@CentOS ~]$ ls Documents/
totally-not-passwords
```

---

> ## **echo [-neE] [arg ...]**
- Display the arg(s) on STDOUT followed by a newline
- `-n` - do not output trailing newline
- `-e `- enable interpretation of escape sequences

```
[guru@CentOS ~]$ echo This is text
This is text

[guru@CentOS ~]$ echo -n no new line.
no new line.[guru@CentOS ~]$ 

[guru@CentOS ~]$ echo -e Can use escape \$400.50
Can use escape $400.50
```

---

> ## **touch [OPTION]... FILE...**
- Update the access and modification times of each FILE to the current time
    - If FILE does not exist, it is created
- `-r FILE` - Use this file's timestamps instead of current time

```
[guru@CentOS ~]$ touch file1 file2

[guru@CentOS ~]$ ls file*
file1  file2

[guru@CentOS ~]$ ls -l /etc/passwd
-rw-r--r-- 1 root root 889 Jan  1 13:13 /etc/passwd

[guru@CentOS ~]$ touch -r /etc/passwd file2

[guru@CentOS ~]$ ls -l file2 
-rw-rw-r-- 1 guru guru 0 Jan  1 13:13 file2
```

---

> ## **cat [OPTION]... [FILE]...**
- Concatenate FILE(s), or STDIN, to STDOUT
    - If FILE does not exist, it is created
- `-n` - number all output lines
- `-A` - show all nonprinting characters

```
[guru@CentOS ~]$ cat -n /etc/group
     1	root:x:0:
     2	bin:x:1:bin,daemon

[guru@CentOS ~]$ cat -A SNCOPDS-file-from-windows.txt
^ISNCO^M$
^IProfessional Enhancement Seminar^M$
^I^ISablich Center (Bldg. 701) Room 108B^M$
```

---

> ## **less [OPTION]... [FILE]...**
- Allows backward movement in the file as well as forward movement.
- Commands are based on vi
    - `/pattern` - search forward through the document for pattern
    - `?pattern `- search backward through the document for pattern
        - `n` - repeat previous search forward
        - `N` - repeat previous search backward
    - `q` - exit less
    - `ctrl + f` - page forward through the document (^f)
    - `ctrl + b` - page backward through the document (^b)	
    - `v` - invokes an editor to edit the current file being viewed

---

> ## **head [OPTION]... [FILE]...**
- Print the first 10 lines of each FILE to STDOUT
- `-n [-]K` - print the first K lines instead of the first 10
    - When the leading - is used, print all but the last K lines of each file

```
[guru@CentOS ~]$ head -n 5 /etc/group
root:x:0:
bin:x:1:bin,daemon
daemon:x:2:bin,daemon
sys:x:3:bin,adm
adm:x:4:adm,daemon
```

---

> ## **tail [OPTION]... [FILE]...**
- Print the last 10 lines of each FILE to STDOUT
- `-n [+]K` - print the last K lines instead of the last 10
    - When the leading + is used, print from the Kth line to the bottom of each file
- `-f` - output appended data as the file grows

```
[guru@CentOS ~]$ tail -n 5 /etc/group
postdrop:x:90:
postfix:x:89:
sshd:x:74:
cgred:x:499:
guru:x:500:
```

---

> ## **ln [OPTION]... [-T] TARGET LINK_NAME (1) || ln [OPTION]... TARGET (2) || ln [OPTION]... TARGET... DIRECTORY (3) || ln [OPTION]... -t DIRECTORY TARGET...	(4)**

- Make links between files
    - Creates hard links by default
- `(1)` - Create a link to TARGET with the name LINK_NAME
- `(2)` - Create a link to TARGET in the current directory
- `(3) & (4)` - Create links to each TARGET in DIRECTORY
- `-s` - make symbolic links instead of hard links

```
[guru@CentOS ~]$ ls -i /etc/passwd
130302 /etc/passwd

[guru@CentOS ~]$ ln /etc/passwd

[guru@CentOS ~]$ ls -i
517200 Desktop  517203 Documents  517199 Downloads  517204 file1  517205 file2  130302 passwd

[guru@CentOS ~]$ ln -s /etc/passwd passwd.symlnk

[guru@CentOS ~]$ ls -i passwd*
130302 passwd  517206 passwd.symlnk

[guru@CentOS ~]$ ls -li passwd*
130302 -rw-r--r-- 2 root root 889 Jan  1 13:13 passwd
517206 lrwxrwxrwx 1 guru guru  11 Jan  4 01:31 passwd.symlnk -> /etc/passwd 
```

---

> ## **file [OPTION]... FILE...**

- Tests each FILE in an attempt to classify its type
- Uses magic to determine file type

```
[guru@CentOS ~]$ file /etc/passwd
/etc/passwd: ASCII text

[guru@CentOS ~]$ file passwd
passwd: ASCII text

[guru@CentOS ~]$ file passwd.symlnk 
passwd.symlnk: symbolic link to `/etc/passwd'

[guru@CentOS ~]$ file my-script.py 
my-script.py: a /usr/bin/python script text executable
```
