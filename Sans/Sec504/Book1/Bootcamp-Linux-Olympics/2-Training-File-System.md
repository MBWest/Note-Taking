# Bootcamp: Linux Olympics

    bootcamp

Welcome to the Linux Olympics! 🏅 Select a training event below to prepare you for the Linux Olympic main event.

✅ Training: Common Commands (3:05)

❎ Training: File System (0:00)

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

    2

## 2 - Training: File System (find, path navigation)

Welcome to the File System event for the Linux Olympics!
In this event you will exercise your skills at the Linux command line when navigating the file system. 🏅

Ready to begin? [Y]es: 
    
    Y

File System (1)
The Linux file system uses absolute and relative path references. Absolute paths always start with a '/'.
Change to the /var/tmp/badminton directory using an absolute path.

    olympian@bc-filesystem:~$ cd /var/tmp/badminton

File System (2)
Display the badminton fact in the /var/tmp/badminton directory.

    olympian@bc-filesystem:/var/tmp/badminton$ cat badmintonfact1.txt 
    Badminton is an Olympic sport since 1992 with five events

File System (3)
Relative paths can also be used in Linux without a leading '/'.
Change to the ../badminton2 directory using a relative path.

    olympian@bc-filesystem:/var/tmp/badminton$ cd ../badminton2

File System (4)
Display the badminton fact in the /var/tmp/badminton2 directory.

    olympian@bc-filesystem:/var/tmp/badminton2$ cat badmintonfact2.txt 
    Sixteen feathers are needed to make a shuttlecock. The best shuttles are made
    from the feathers from the left wing of a goose.

File System (5)
Relative paths can use multiple '..' indicators to travel up several directories.
Change to the ../../../tmp directory using a relative path.

    olympian@bc-filesystem:/var/tmp/badminton2$ cd ../../../tmp/

File System (6)
Display the badminton fact in the /tmp directory.

    olympian@bc-filesystem:/tmp$ cat badmintonfact3.txt 
    Badminton is the fastest racket sport with shuttle clocking speed in excess of
    200 MPH.

File System (7)
The find command uses the basic syntax 'find [starting directory] -name "wildcard"'.
Use the find command to list all files matching *.txt in /home.

    olympian@bc-filesystem:/tmp$ find /home *.txt
    /home
    /home/olympian
    /home/olympian/HELP
    /home/olympian/.fact
    /home/olympian/.fact/badmintonfact4.txt
    /home/olympian/Documents
    /home/olympian/Documents/Badmintonfact6.Txt
    /home/olympian/.bashrc
    /home/jhashman
    /home/jhashman/BADMINTONFACT5.TXT
    /home/snehwal
    /home/snehwal/badmintonfact8.text
    /home/init
    /home/init/.bash_logout
    /home/init/.profile
    /home/init/.bashrc
    /home/init/mysession.yaml
    /home/init/.tmux.conf
    /home/init/bottom_pane
    /home/init/top_pane
    /home/init/questions_answers.json
    badmintonfact3.txt

File System (8)
Repeat the 'find' command, this time displaying all files ending in .TXT in /home.

    olympian@bc-filesystem:/tmp$ find /home *.TXT
    /home
    /home/olympian
    /home/olympian/HELP
    /home/olympian/.fact
    /home/olympian/.fact/badmintonfact4.txt
    /home/olympian/Documents
    /home/olympian/Documents/Badmintonfact6.Txt
    /home/olympian/.bashrc
    /home/jhashman
    /home/jhashman/BADMINTONFACT5.TXT
    /home/snehwal
    /home/snehwal/badmintonfact8.text
    /home/init
    /home/init/.bash_logout
    /home/init/.profile
    /home/init/.bashrc
    /home/init/mysession.yaml
    /home/init/.tmux.conf
    /home/init/bottom_pane
    /home/init/top_pane
    /home/init/questions_answers.json
    find: ‘*.TXT’: No such file or directory

File System (9)
Repeat the 'find' command, this time displaying all files ending in any case combination of .TXT in /home.

    olympian@bc-filesystem:/tmp$ find /home -iname *.TXT
    /home/olympian/.fact/badmintonfact4.txt
    /home/olympian/Documents/Badmintonfact6.Txt
    /home/jhashman/BADMINTONFACT5.TXT

File System (10)
Repeat the 'find' command, this time displaying all files ending in any case combination of .TXT in /home or in /tmp.

    olympian@bc-filesystem:/tmp$ find /home /tmp -iname *.TXT
    /home/olympian/.fact/badmintonfact4.txt
    /home/olympian/Documents/Badmintonfact6.Txt
    /home/jhashman/BADMINTONFACT5.TXT
    find: ‘/tmp/tmux-1050’: Permission denied
    find: ‘/tmp/_MEIayWFsb’: Permission denied
    /tmp/.badmintonfact7.txt
    find: ‘/tmp/_MEIbVwTgC’: Permission denied
    /tmp/badmintonfact3.txt

File System (11)
Display the new badminton fact in the /tmp directory.

    olympian@bc-filesystem:/tmp$ cat .badmintonfact7.txt 
    The two most successful badminton countries are China and Indonesia
    which between them have won 70% of all Badminton World Federation events.

File System (12)
The find command can display output similar to the ls command using the -ls argument. Display the file list information for all badminton facts in /home.

    olympian@bc-filesystem:/tmp$ find /home -ls 
    6832396      8 drwxr-xr-x   1 root     root         4096 Aug 12  2021 /home
    6832277      8 drwxr-xr-x   1 olympian olympian     4096 Aug 12  2021 /home/olympian
    6832064      4 -rw-r--r--   1 olympian olympian      154 Aug 12  2021 /home/olympian/HELP
    6832218      8 drwxr-xr-x   1 olympian olympian     4096 Aug 12  2021 /home/olympian/.fact
    6832219      4 -rw-r--r--   1 olympian olympian       71 Aug 12  2021 /home/olympian/.fact/badmintonfact4.txt
    6832278      8 drwxr-xr-x   1 olympian olympian     4096 Aug 12  2021 /home/olympian/Documents
    6832279      4 -rw-r--r--   1 olympian olympian       93 Aug 12  2021 /home/olympian/Documents/Badmintonfact6.Txt
    6832081      4 -rw-r--r--   1 olympian olympian     3105 Aug 12  2021 /home/olympian/.bashrc
    6832247      8 drwxr-xr-x   1 olympian olympian     4096 Aug 12  2021 /home/jhashman
    6832248      4 -rw-r--r--   1 olympian olympian      158 Aug 12  2021 /home/jhashman/BADMINTONFACT5.TXT
    6832307      8 drwxr-xr-x   1 olympian olympian     4096 Aug 12  2021 /home/snehwal
    6832308      4 -rw-r--r--   1 olympian olympian       72 Aug 12  2021 /home/snehwal/badmintonfact8.text
    6832397      4 drwxr-xr-x   1 init     init         4096 Aug 12  2021 /home/init
    5656818      4 -rw-r--r--   1 init     init          220 Feb 25  2020 /home/init/.bash_logout
    5656820      4 -rw-r--r--   1 init     init          807 Feb 25  2020 /home/init/.profile
    5656819      4 -rw-r--r--   1 init     init         3771 Feb 25  2020 /home/init/.bashrc
    6832398      4 -rw-r--r--   1 root     root          323 Aug 12  2021 /home/init/mysession.yaml
    6832368      4 -rw-r--r--   1 root     root         1512 Aug 12  2021 /home/init/.tmux.conf
    6831931   6784 -rwsr-xr-x   1 root     root      6943104 Aug 12  2021 /home/init/bottom_pane
    6697286   6784 -rwsr-xr-x   1 root     root      6945152 Aug 12  2021 /home/init/top_pane
    6697194      8 -rw-r--r--   1 root     root         7890 Aug 12  2021 /home/init/questions_answers.json

File System (13)
The find command can also search for files based on size. Identify the badminton fact file in /home that is 72 bytes in size (-size 72c).

    olympian@bc-filesystem:/tmp$ find /home -size 72c
    /home/snehwal/badmintonfact8.text

File System (14)
Display all of the badminton facts in /var, /tmp, and /home using find's -exec feature and cat.

    olympian@bc-filesystem:/tmp$ cd /
    olympian@bc-filesystem:/$ find /var /tmp /home -iname *badminton* -exec cat '{}' \;
    find: ‘/var/lib/apt/lists/partial’: Permission denied
    cat: /var/tmp/badminton2: Is a directory
    Sixteen feathers are needed to make a shuttlecock. The best shuttles are made
    from the feathers from the left wing of a goose.
    cat: /var/tmp/badminton: Is a directory
    Badminton is an Olympic sport since 1992 with five events.
    find: ‘/var/cache/apt/archives/partial’: Permission denied
    find: ‘/var/cache/ldconfig’: Permission denied
    find: ‘/tmp/tmux-1050’: Permission denied
    find: ‘/tmp/_MEIayWFsb’: Permission denied
    The two most successful badminton countries are China and Indonesia
    which between them have won 70% of all Badminton World Federation events.
    find: ‘/tmp/_MEIbVwTgC’: Permission denied
    Badminton is the fastest racket sport with shuttle clocking speed in excess of
    200 MPH.
    Badminton is the second most popular sport in the world, after soccer.
    Crowds of up to 15,000 are common for major badminton tournaments in Malaysia
    and Indonesia.
    The biggest shuttle in the world can be found on the lawns of the Kansas City
    Museum 48 times larger than the real thing, 18 feet tall and weighing 5500
    lbs.
    A typical badminton player can cover more than 2 km in just one match. 

Congratulations! You have completed the File System qualifying event for the Linux Olympics! 🏅🏅🏅
You have demonstrated true skill, and are ready to compete as a true contender for the Linux gold medal.
Run 'exit' to close.

    exit