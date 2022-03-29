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

Permissions (4)
The permission 600 indicates read/write for owner (6), no permission for group (0) and no permission for other (0).
Re-examine the permissions of the racewalkingfact1.txt file.

    olympian@bc-permissions:~$ ll
    total 884
    drwxr-xr-x 1 olympian olympian   4096 Mar  3 12:12 ./
    drwxr-xr-x 1 root     root       4096 Mar  3 12:12 ../
    -rw-r--r-- 1 olympian olympian   3105 Aug 12  2021 .bashrc
    -rw-r--r-- 1 olympian olympian    154 Aug 12  2021 HELP
    -rw------- 1 olympian olympian     49 Aug 12  2021 racewalkingfact1.txt
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

Permissions (5)
Notice how the permission information for the file has changed from ---------- to -rw-------.
Display the contents of the racewalkingfact1.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact1.txt 
    Racewalking debuted as an Olympic event in 1908.

Permissions (6)
Linux supports octal notation for permissions where 4=read, 2=write, 1=execute.
Adding the values together produces the desired permission. Change the permission for racewalkingfact2.txt so it is owner and group readable.

    olympian@bc-permissions:~$ chmod 440 racewalkingfact2.txt 

Permissions (7)
Display the contents of the racewalkingfact2.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact2.txt 
    One of the main rules of race walking is that competitors must keep at least one foot on the ground at all time.

Permissions (8)
Using octal notation (4=read, 2=write, 1=execute), change the permission of racewalkingfact3.txt so it is read/write by owner, read by group, and no permissions for other.

    olympian@bc-permissions:~$ chmod 640 racewalkingfact3.txt 

Permissions (9)
Display the contents of the racewalkingfact3.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact3.txt 
    In racewalking, the front leg must always be straight.

Permissions (10)
Using octal notation (4=read, 2=write, 1=execute), change the permission of racewalkingfact3.txt so it is read/write by owner, read/write by group, and read for other.

    olympian@bc-permissions:~$ chmod 664 racewalkingfact4.txt 

Permissions (11)
Display the contents of the racewalkingfact4.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact4.txt 
    Violations of the racewalking rules are punished by judges with a red card. If an athlete receives three of them, they are eliminated from the race.

Permissions (12)
The racewalkingfact5.py file is a Python script.
Display the contents of the racewalkingfact5.py file.

    olympian@bc-permissions:~$ chmod 777 racewalkingfact5.py 
    olympian@bc-permissions:~$ cat racewalkingfact5.py 
    #!/usr/bin/env python3
    import base64
    print(base64.b64decode("K4CduVmdlBSbrBCMyASYg4WagUGdlBXbvNGIuVWbvdFIuMHduVmdlByZul2asF2dlNWYyBSbrBCM1ACZuFGIttGIwIDIoR3biBibpBSZ0VGct92Yg4WZtBCLzNWaw1Wes9EIlhGdgQXQ"[::-1]).decode('utf-8'))

Permissions (13)
Using octal notation (4=read, 2=write, 1=execute), change the permission of racewalkingfact5.py so it is read/write/execute by owner, read/execute by group, and read/execute for other

    olympian@bc-permissions:~$ chmod 755 racewalkingfact5.py 

Permissions (14)
When a file has the execute bit set, it can be run as a program. Execute the racewalkingfact5.py script: ./racewalkingfact5.py

    olympian@bc-permissions:~$ ./racewalkingfact5.py 
    At the Olympics, men compete in both 20 km and 50 km racewalking events. Women compete in a 20 km event.

Permissions (15)
The execute permission is also used for directories.
Attempt to change to the racewalkingfact6 directory.

    olympian@bc-permissions:~$ cd racewalkingfact6/
    bash: cd: racewalkingfact6/: Permission denied

Permissions (16)
Examine the permissions for the racewalkingfact6 directory.

    olympian@bc-permissions:~$ ll
    total 884
    drwxr-xr-x 1 olympian olympian   4096 Mar  3 12:12 ./
    drwxr-xr-x 1 root     root       4096 Mar  3 12:12 ../
    -rw-r--r-- 1 olympian olympian   3105 Aug 12  2021 .bashrc
    -rw-r--r-- 1 olympian olympian    154 Aug 12  2021 HELP
    -rw------- 1 olympian olympian     49 Aug 12  2021 racewalkingfact1.txt
    ---------- 1 olympian olympian    106 Aug 12  2021 racewalkingfact10.txt
    ---------- 1 olympian olympian     52 Aug 12  2021 racewalkingfact11.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact12.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact13.txt
    -r--r----- 1 olympian olympian    113 Aug 12  2021 racewalkingfact2.txt
    -rw-r----- 1 olympian olympian     55 Aug 12  2021 racewalkingfact3.txt
    -rw-rw-r-- 1 olympian olympian    149 Aug 12  2021 racewalkingfact4.txt
    -rwxr-xr-x 1 olympian olympian    227 Aug 12  2021 racewalkingfact5.py*
    drw-r--r-- 1 olympian olympian   4096 Mar  3 12:12 racewalkingfact6/
    -rw------- 1 root     root        114 Aug 12  2021 racewalkingfact7.txt
    ---------- 1 olympian olympian    175 Aug 12  2021 racewalkingfact8.txt
    ---------- 1 olympian olympian 827896 Aug 12  2021 racewalkingfact9

Permissions (17)
Change the permissions for the racewalkingfact6 directory to mode 755.

    olympian@bc-permissions:~$ chmod 755 racewalkingfact6

Permissions (18)
Change to the racewalkingfact6 directory, display the race walking fact, then change back to your home directory using a relative path.

    olympian@bc-permissions:~$ cd racewalkingfact6/ 
    olympian@bc-permissions:~/racewalkingfact6$ cat racewalkingfact6.txt 
    Women's racewalking competition didn't debut until the 1992 Olympics in Barcelona.
    olympian@bc-permissions:~/racewalkingfact6$ cd ~

Permissions (19)
Display the permissions for the racewalkingfact7.txt file.

    olympian@bc-permissions:~$ ll
    total 884
    drwxr-xr-x 1 olympian olympian   4096 Mar  3 12:12 ./
    drwxr-xr-x 1 root     root       4096 Mar  3 12:12 ../
    -rw-r--r-- 1 olympian olympian   3105 Aug 12  2021 .bashrc
    -rw-r--r-- 1 olympian olympian    154 Aug 12  2021 HELP
    -rw------- 1 olympian olympian     49 Aug 12  2021 racewalkingfact1.txt
    ---------- 1 olympian olympian    106 Aug 12  2021 racewalkingfact10.txt
    ---------- 1 olympian olympian     52 Aug 12  2021 racewalkingfact11.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact12.txt
    ---------- 1 olympian olympian     85 Aug 12  2021 racewalkingfact13.txt
    -r--r----- 1 olympian olympian    113 Aug 12  2021 racewalkingfact2.txt
    -rw-r----- 1 olympian olympian     55 Aug 12  2021 racewalkingfact3.txt
    -rw-rw-r-- 1 olympian olympian    149 Aug 12  2021 racewalkingfact4.txt
    -rwxr-xr-x 1 olympian olympian    227 Aug 12  2021 racewalkingfact5.py*
    drwxr-xr-x 1 olympian olympian   4096 Mar  3 12:12 racewalkingfact6/
    -rw------- 1 root     root        114 Aug 12  2021 racewalkingfact7.txt
    ---------- 1 olympian olympian    175 Aug 12  2021 racewalkingfact8.txt
    ---------- 1 olympian olympian 827896 Aug 12  2021 racewalkingfact9

Permissions (20)
File ownership is controlled by the chown command.
Attempt to change the ownership of the racewalkingfact7.txt file to the olympian user with the chown command.

    olympian@bc-permissions:~$ chown olympian racewalkingfact7.txt 
    chown: changing ownership of 'racewalkingfact7.txt': Operation not permitted

Permissions (21)
Only the root user can change the ownership of a file. Repeat the last chown command, this time adding the sudo command to the beginning of the command.

    olympian@bc-permissions:~$ sudo chown olympian racewalkingfact7.txt 

Permissions (22)
Display the contents of the racewalkingfact7.txt file.

    olympian@bc-permissions:~$ cat racewalkingfact7.txt 
    Athletes from the now defunct Soviet Union have won the most race walking events at the Olympics, with 13 medals.

Permissions (23)
Unlike ownership, a user can change a group assignment to any other group where they are a member.
Change the group of racewalkingfact8.txt to athlete using the chgrp command.

    olympian@bc-permissions:~$ chgrp athlete racewalkingfact8.txt 

Permissions (24)
Display the contents of the racewalkingfact8.txt file.

    olympian@bc-permissions:~$ chmod 777 racewalkingfact8.txt 
    olympian@bc-permissions:~$ cat racewalkingfact8.txt 
    In racewalking, the stride length is reduced, so to achieve competitive speeds, race walkers must attain pace rates comparable to those achieved by Olympic 400-meter runners.

Permissions (25)
The racewalkingfact9 file is a compiled program. Change the file so that it is read/write/executable for the owner, read/executable for group and other.

    olympian@bc-permissions:~$ chmod 755 racewalkingfact9

Permissions (26)
Execute the racewalkingfact9 program.

    olympian@bc-permissions:~$ ./racewalkingfact9
    Hello olympian. Your effective user ID is 1051.

Permissions (27)
The permission 755 implies a leading zero: 0755. When you set the leading 0 to 4, the file is SETUID, and will run with the permissions of the owner, not the user running the program.
Change the owner of racewalkingfact9 to root.

    olympian@bc-permissions:~$ sudo chown root racewalkingfact9

Permissions (28)
SETUID files can be dangerous on the file system, since they grant privileges of the file owner.
Change the permission of racewalkingfact9 to 4755 to make it SETUID.

    olympian@bc-permissions:~$ sudo chmod 4755 racewalkingfact9

Permissions (29)
Execute the racewalkingfact9 program as a normal user.

    olympian@bc-permissions:~$ ./racewalkingfact9
    Hello root. Your effective user ID is 0. Also, I have a fact for you:.

    The racewalking violation of having both feet off the ground is known as flying.

Permissions (30)
An attacker with root access can use SETUID permissions to create a backdoor.
Copy the /bin/bash file to /tmp/backdoor.

    olympian@bc-permissions:~$ cp /bin/bash /tmp/backdoor

Permissions (31)
An attacker with root access can use SETUID permissions to create a backdoor.
Change the ownership of /tmp/backdoor to root.

    olympian@bc-permissions:~$ sudo chown root /tmp/backdoor 

Permissions (32)
An attacker with root access can use SETUID permissions to create a backdoor.
Change the permissions of /tmp/backdoor to 4755 (SETUID).

    olympian@bc-permissions:~$ sudo chmod 4755 /tmp/backdoor

Permissions (33)
An attacker with root access can use SETUID permissions to create a backdoor.
We have revoked your sudo access, but you can still get root access by running the backdoor command with the -p argument.

    olympian@bc-permissions:/tmp$ backdoor

Congratulations! You have completed the Linux Permissions qualifying event for the Linux Olympics! 🏅🏅🏅
You have demonstrated true skill, and are ready to compete as a true contender for the Linux gold medal.
Run 'exit' to close.
