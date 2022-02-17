#Questions

## Unix

### Unix Shells and Scripting

1. How would you view the manual page for SSH? ** man ssh**

2. What is the standard shell that most other shell versions are based off of? **Bourne Shell**

3. What is root's default shell for FreeBSD? **tcsh**

4. In one line, write a find command that: Finds all files on the machine named "config" using case insensitive search and redirects STDERR to /dev/null. **find / -iname config 2>/dev/null**

5. What symbol is used to redirect STDOUT and STDERR to the same place? **>&**

6. Write a command that will count the number of lines in /etc/passwd and write the result to /tmp/lines. **wc -l /etc/passwd > /tmp/lines**

7. On one line write two commands that will assign the value /bin/bash to a variable called myshell and then print the value of myshell.

8. Write a command that will promote the variable myshell to an environment variable and reassign the value to /bin/sh.

9. What should be the first line in a bash script? **#!/bin/bash**

### Unix Filesystems

1. Which directory stores critical system and configuration files? **/etc**

2. Where is the file that contains the OS kernel usually located? **/boot**


3. Which directory contains on-line manual pages? **/usr/share/man**

4. Which of the following are stored as regular files?

Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Links
    B. Sockets
    C. Executables
    D. Configuration Files
    E. Device Files
    F. Text Files
    G. Libraries`

5. A link that has the same inode number as the original file is a:
Format: Multiple Choice, Letter only
**A. Hard Link**
B. Symbolic Link

6. (T/F) Hard links can be used across filesystems, while soft links cannot. **False**

7. Write a command that will create a symbolic link named /tmp/log to /var/log/secure. **ln -s /var/log/secure /tmp/log**

8. Which of the following correctly describes a partition?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. System that aggregates physical devices to form pools

    B. Determines where and how file contents are stored

    C. Is used to increase reliability by duplicating data across disks

    **D. Is a fixed-size subsection of a storage device**

    **E. Has its own device file**

9.

10.

11.
