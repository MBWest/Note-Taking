# Linux - Accounts and Security Administration

> ## **groupadd [options] group**
- Creates a new group account using the values specified on the command line plus the default values from the system

```
[guru@CentOS ~]$ sudo groupadd rebel-alliance

[guru@CentOS ~]$ sudo groupadd galactic-empire

[guru@CentOS ~]$ grep -e rebel -e empire /etc/group
rebel-alliance:x:601:
galactic-empire:x:602:
```

---

> ## **groupmod [options] group**
- Modifies the definition of the specified group by modifying the appropriate entry in the group database
- `-g GID`      - change Group ID (GID) of the given group
- `-n NEWGROUP` - change name of the group to NEWGROUP

```
[guru@CentOS ~]$ grep rebel /etc/group
rebel-alliance:x:601:

[guru@CentOS ~]$ sudo groupmod -g 600 -n rebels rebel-alliance

[guru@CentOS ~]$ grep rebel /etc/group
rebels:x:600:
```

---

> ## **groupdel [options] group**
- Modifies the system account files, deleting all entries that refer to group
- You cannot remove primary groups of existing users; you must remove the user before you can remove the primary group of the same name

```
[guru@CentOS ~]$ sudo groupdel galactic-empire
[guru@CentOS ~]$ grep empire /etc/group
```

---

> ## **useradd [options] LOGIN || useradd -D [options]**
- Creates a new user account using the values specified on the command line plus the default values from the system
- `-D` - display or update default system values
- `-d HOMEDIR` - value for the user’s login directory
- `-s SHELL`   - absolute path of the user’s login shell 
- `-g GROUP`   - group name or GID of the user’s login group
- `-G GROUP[,GROUP2...]` - list of supplementary groups of which the user is also a member 

```
[guru@CentOS ~]$ sudo useradd -G rebels -s /bin/sh chewbacca

[guru@CentOS ~]$ grep chewbacca /etc/passwd
chewbacca:x:502:603::/home/chewbacca:/bin/sh

[guru@CentOS ~]$ sudo useradd -G rebels han-solo

[guru@CentOS ~]$ grep rebels /etc/group
rebels:x:600:chewbacca,han-solo

[guru@CentOS ~]$ ll /home/
total 12
drwx------ 2 chewbacca chewbacca 4096 Jan  7 11:34 chewbacca
drwx------ 5 guru      guru      4096 Jan  6 01:52 guru
drwx------ 2 han-solo  han-solo  4096 Jan  7 11:38 han-solo
```

---

> ## **passwd [options] [username]**
- Update a user’s authentication token
- `-l | -u` - lock or unlock an account
- `-n`- set min password lifetime in days
- `-x`- set max password lifetime in days

```
[guru@CentOS ~]$ sudo passwd chewbacca
Changing password for user chewbacca.
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.

[guru@CentOS ~]$ sudo grep -e chewbacca -e han /etc/shadow
chewbacca:$6$fgHPthJN$EUDDLXgsTb.56p0JgN1asGkqe555zBnH4CgLtdW.HiMwAYqq0xaLUOchXA.iUX4.k92O4rcrXCMQ31dCl6stu0:17173:0:99999:7:::
han-solo:!!:17173:0:99999:7:::

[guru@CentOS ~]$ sudo passwd -l chewbacca
Locking password for user chewbacca.
passwd: Success

[guru@CentOS ~]$ sudo grep -e chewbacca /etc/shadow
chewbacca:!!$6$fgHPthJN$EUDDLXgsTb.56p0JgN1asGkqe555zBnH4CgLtdW.HiMwAYqq0xaLUOchXA.iUX4.k92O4rcrXCMQ31dCl6stu0:17173:0:99999:7:::

[guru@CentOS ~]$ sudo usermod -p Rrrrrrr-ghghghghgh chewbacca

[guru@CentOS ~]$ sudo grep -e chewbacca /etc/shadow
chewbacca:Rrrrrrr-ghghghghgh:17173:0:99999:7:::
```

---

> ## **usermod [options] LOGIN**
- Modifies the system account files to reflect the changes that are specified on the command line
- Very similar options to the useradd command
- `-l NEWLOGIN` - change the user’s login name
- `-L | -U` - lock or unlock a user’s password

```
[guru@CentOS ~]$ sudo usermod -l chewie chewbacca

[guru@CentOS ~]$ grep chewie /etc/passwd
chewie:x:502:603::/home/chewbacca:/bin/sh

[guru@CentOS ~]$ sudo usermod -m -d /home/chewie chewie

[guru@CentOS ~]$ ll /home/
drwx------ 2 chewie   chewbacca 4096 Jan  7 11:34 chewie
drwx------ 5 guru     guru      4096 Jan  6 01:52 guru
drwx------ 2 han-solo han-solo  4096 Jan  7 11:38 han-solo
```

---

> ## **userdel [options] LOGIN**
- Modifies the system account files, deleting all entries that refer to LOGIN
- `-f` - force removal, even if user is logged in
- `-r` - recursively deletes user’s home directory

```
[guru@CentOS ~]$ sudo userdel -r han-solo

[guru@CentOS ~]$ grep han /etc/passwd

[guru@CentOS ~]$ ll /home/
total 8
drwx------ 2 chewie chewbacca 4096 Jan  7 11:34 chewie
drwx------ 5 guru   guru      4096 Jan  6 01:52 guru
```

---

> ## **chage [options] LOGIN**
- Changes the number of days between password changes and the date of the last password change
- `-l` - list account aging information
- `-d LASTDAY`    - set # of days since last password change
- `-E EXPIREDATE` - set expiration date of the user’s account
- `-m MINDAYS`    - set min # days between password change
- `-M MAXDAYS`    - set max # days which a password is valid
- `-W WARNDAYS`  - set # of warning days before expiration

```
[guru@CentOS ~]$ sudo chage -m 7 -M 60 -W 15 chewie

[guru@CentOS ~]$ sudo chage -l chewie
Last password change					: Jan 07, 2017
Password expires						: Mar 08, 2017
Password inactive						: never
Account expires						: never
Minimum number of days between password change		: 7
Maximum number of days between password change		: 60
Number of days of warning before password expires		: 15
```

> ## **su [OPTION]... [-] [USER [ARG]...]**
- Change the EUID and effective group ID (EGID) to that of USER
- If USER is not given, root is assumed
- `-l` or `-` - make the shell a login shell 
    - Clears all environment variables
    - Initializes HOME, SHELL, USER, LOGNAME, and PATH 
    - Changes to USER’s home directory
- `-m` or `-p` - preserve environment (do not reset vars above)

```
[root@CentOS tmp]# pwd
/tmp

[root@CentOS tmp]# su -m chewie
bash: /root/.bashrc: Permission denied

bash-4.1$ echo $HOME $SHELL $PATH
/root /bin/bash /usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

bash-4.1$ pwd
/tmp

[root@CentOS tmp]# su -l guru

[guru@CentOS ~]$ echo $HOME $SHELL $PATH
/home/guru /bin/bash /usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/guru/bin

[guru@CentOS ~]$ pwd
/home/guru
```