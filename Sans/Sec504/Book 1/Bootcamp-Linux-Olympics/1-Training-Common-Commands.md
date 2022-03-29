# Bootcamp: Linux Olympics

    bootcamp

Welcome to the Linux Olympics! 🏅 Select a training event below to prepare you for the Linux Olympic main event.

❎ Training: Common Commands (0:00)

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

    1

## 1 - Training: Common Commands (ls, pwd, mv, mkdir, whoami)

Welcome to the qualifying event for the Linux Olympics!
In this event you will exercise your skills at the Linux command line, completing several qualifying events. 🏅

Ready to begin? [Y]es: 

    Y

Common Commands (1)
The 'ls' command is used to list files.
List the files in your home directory.

    ls

Common Commands (2)
The 'cat' command is used to display the contents of a file.
Display the contents of the fencing.txt file.

    olympian@bc-commoncommands:~$ cat fencing.txt 
    Swordplay has been practised for thousands of years, and modern day fencing began as a form of military training. 
    Fencing did not become an Olympic sport until around the 15th century.

Common Commands (3)
In Linux, files that begin with a . are hidden by default.
List the hidden and non-hidden files in your home directory using 'ls -a'.

    olympian@bc-commoncommands:~$ ls -a
    .  ..  .bash_logout  .bashrc  .fencingfact1.txt  .profile  HELP  epee  fencing.txt  foil  sabre

Common Commands (4)
Display the contents of the .fencingfact1.txt file.

    olympian@bc-commoncommands:~$ cat .fencingfact1.txt 
    The tip of the fencing weapon is the second fastest moving object in Olympic
    sports; the first is the marksman's bullet.

Common Commands (5)
The 'pwd' command prints the name of the working directory.
Identify the current directory name.

    olympian@bc-commoncommands:~$ pwd
    /home/olympian

Common Commands (6)
The 'cd' command is used to change to a new directory.
Change to the epee directory.

    olympian@bc-commoncommands:~$ cd epee/

Common Commands (7)
Display the fencing fact in the epee directory.

    olympian@bc-commoncommands:~/epee$ cat .fencingfact2.txt 
    Many of the ballet positions are derived from fencing.

Common Commands (8)
The 'mkdir' command is used to create a new directory
Create a directory called bout, then change to the new directory.

    olympian@bc-commoncommands:~/epee$ mkdir bout && cd bout

Common Commands (9)
Running 'cd' with no arguments returns to the home directory.
Return to the home directory.

    olympian@bc-commoncommands:~/epee/bout$ cd

Common Commands (10)
The 'whoami' command will display your user name.
What is your user name?

    olympian

Common Commands (11)
The 'id' command displays your user name, user ID, and group information.
What is your user ID?

    olympian@bc-commoncommands:~$ id
    uid=1051(olympian) gid=1051(olympian) groups=1051(olympian),5(tty)

Common Commands (12)
Display the fencing fact in the foil directory.

olympian@bc-commoncommands:~$ cat foil/fencingfact3.txt 
Fencing as a game goes back to as early as 1200 A.D.

Common Commands (13)
Display the final fencing fact in the sabre directory.

    olympian@bc-commoncommands:~$ cat sabre/fencingfact4.txt 
    The fencing suits are white, because in earlier times, touching was recorded
    with a piece of cotton at the tip of the weapon dipped in ink.

Common Commands (14)
The 'rm' command is used to remove files.
Remove the fencingfact4.txt file.

    olympian@bc-commoncommands:~$ rm sabre/fencingfact4.txt 

Common Commands (15)
The 'mv' command is used to move a file to a new directory.
Change to the foil directory. Move the fencingfact3.txt file to /tmp.

    olympian@bc-commoncommands:~$ cd foil && mv fencingfact3.txt /tmp 

Common Commands (16)
The 'mv' command is also used to rename files.
Change to the /tmp directory, then rename the fencingfact3.txt file to fact.txt

    olympian@bc-commoncommands:~/foil$ cd /tmp && mv fencingfact3.txt fact.txt

Congratulations! You have completed the Common Commands qualifying event for the Linux Olympics! 🏅🏅🏅
You have demonstrated true skill, and are ready to compete as a true contender for the Linux gold medal.
Run 'exit' to close.

    exit