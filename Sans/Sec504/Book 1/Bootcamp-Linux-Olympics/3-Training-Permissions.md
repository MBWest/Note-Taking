# Bootcamp: Linux Olympics

    bootcamp

Welcome to the Linux Olympics! 🏅 Select a training event below to prepare you for the Linux Olympic main event.

✅ Training: Common Commands (3:05)

✅ Training: File System (5:10)

❎ Training: Permissions (0:00)

❎ Training: Processes (0:00)

❎ Training: Networking (0:00)

❎ Training: File Processing (0:00)

❎ Training: JSON File Processing (0:00)

⭕️ Final Olympic Event (0:00)

1 - Training: Common Commands (ls, pwd, mv, mkdir, whoami)

2 - Training: File System (find, path navigation)

3 - Training: Permissions (chown, chmod, chgrp, sudo)

4 - Training: Processes (ps, kill, jobs)

5 - Training: Networking (ip, ping, netstat, ss)

6 - Training: File Processing (echo, cat, grep, cut, sort, uniq)

7 - Training: JSON File Processing (jq)

8 - Final Olympic Event 

9 - Exit

    3

## 3 - Training: Permissions (chown, chmod, chgrp, sudo)

Welcome to the Linux Permissions event for the Linux Olympics!
In this event you will exercise your skills at the command line when working with Linux permissions. 🏅

Ready to begin? [Y]es: 

    Y

Permissions (1)
Linux uses discretionary permissions on all files for the owner, the group, and other.
Identify the owner of the racewalkingfact1.txt file.

    olympian@bc-permissions:~$ ll
    total 876
    drwxr-xr-x 1 olympian olympian   4096 Mar  3 12:12 ./
    drwxr-xr-x 1 root     root       4096 Mar  3 12:12 ../
    -rw-r--r-- 1 olympian olympian   3105 Aug 12  2021 .bashrc
    -rw-r--r-- 1 olympian olympian    154 Aug 12  2021 HELP
    ---------- 1 olympian olympian     49 Aug 12  2021 racewalkingfact1.txt
    ---------- 1 olympian olympian    106 Aug 12  2021 racewalkingfact10.txt
    ---------- 1 olympian olympian     52 Aug 12  2021 racewalkingfact11.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact12.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact13.txt
    ---------- 1 olympian olympian    113 Aug 12  2021 racewalkingfact2.txt
    ---------- 1 olympian olympian     55 Aug 12  2021 racewalkingfact3.txt
    ---------- 1 olympian olympian    149 Aug 12  2021 racewalkingfact4.txt
    ---------- 1 olympian olympian    227 Aug 12  2021 racewalkingfact5.py
    drw-r--r-- 1 olympian olympian   4096 Mar  3 12:12 racewalkingfact6/
    -rw------- 1 root     root        114 Aug 12  2021 racewalkingfact7.txt
    ---------- 1 olympian olympian    175 Aug 12  2021 racewalkingfact8.txt
    ---------- 1 olympian olympian 827896 Aug 12  2021 racewalkingfact9

Permissions (2)
Attempt to examine the contents of the racewalkingfact1.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact1.txt 
    cat: racewalkingfact1.txt: Permission denied

Permissions (3)
You cannot examine the racewalkingfact1.txt file since you don't have permissions to read the file.
Change the file permissions by running 'chmod 600 racewalkingfact1.txt'.

    olympian@bc-permissions:~$ chmod 600 racewalkingfact1.txt 

