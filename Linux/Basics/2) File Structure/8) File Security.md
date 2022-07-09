# Linux File Structure - File Security

> ## **chmod [OPTION]... MODE[,MODE]... FILE...**
- Change the file mode bits of each given file according to MODE
- Set via octal (leading zeros are assumed if not present)

| **Command**   | **Description**   |
| --------------|-------------------|
| **chmod** |
| `chmod` | Change the permissions of a file or directory. |
| **who** |
| `u` | User (The owner of the file). |
| `g` | Group (Members of the group the file belongs to). |
| `o` | Others (The 'World'). |
| `a` | All of the above. |
| **What** |
| `Minus Sign (-)` | Removes the permission. |
| `Plus Sign (+)` | Grants the permission. |
| `Equal Sign (=)` | Set a permission and removes others. |
| **Which** |
| `r` | The read permissions. |
| `w` | The write permissions. |
| `x` | The execute permissions. |

---
---

> ## **Examples**

| **Command**   | **Description**   |
| --------------|-------------------|
| **Examples** |
| `chmod a= hello.txt` | Remove all permissions for all users. |
| `chmod g+w file.txt` | Add write permissions to the group. |
| `chmod a-w file.txt` | Remove write permissions from all. |

---

> ## **chmod octals**

Chmod also supports octal number (base 8). Each digit in an octal number represents 3 binary digits

| **R** | **W**  | **X**  |
|-------|--------|--------|
| `2^2`| `2^1` | `2^0` |
|  4| 2 | 1 |

| **Octal**  | **Binary**  | **File Mode**  |
|------------|-------------|----------------|
|`0`| 000 | - - - |
|`1`| 001 | - -x |
|`2`|  010| -w- |
|`3`|  011| -wx |
|`4`|  100| r- - |
|`5`| 101 |r-x |
|`6`|110  |rw-  |
|`7`| 111  |rwx  |

---

> ## **umask [-p] [-S] [mode]**
- Set file mode mask to mode or display current mode

```
[guru@CentOS tmp]$ umask
0002
[guru@CentOS tmp]$ touch stuff 

[guru@CentOS tmp]$ mkdir things

[guru@CentOS tmp]$ ll -d stuff things/
-rw-rw-r-- 1 guru guru    0 Jan  8 13:03 stuff\
drwxrwxr-x 2 guru guru 4096 Jan  8 13:03 things/

[guru@CentOS tmp]$ umask 022

[guru@CentOS tmp]$ umask
0022

[guru@CentOS tmp]$ touch other-stuff

[guru@CentOS tmp]$ mkdir other-things

[guru@CentOS tmp]$ ll -d other*
-rw-r--r-- 1 guru guru    0 Jan  8 13:07 other-stuff
drwxr-xr-x 2 guru guru 4096 Jan  8 13:07 other-things
```

---

> ## **chown [OPTION]... [OWNER][:[GROUP]] FILE...**
- Changes the user and/or group ownership of each given file

```
[genosians@CentOS ~]$ touch death-star-plans

[genosians@CentOS ~]$ sudo chown palpatine:galactic-empire death-star-plans 

[genosians@CentOS ~]$ ll death-star-plans 
-rw-r----- 1 palpatine galactic-empire 0 Jan  8 21:41 death-star-plans

[genosians@CentOS ~]$ sudo chown princess-leia: death-star-plans 

[genosians@CentOS ~]$ ll death-star-plans 
-rw-r----- 1 princess-leia princess-leia 0 Jan  8 21:41 death-star-plans

[genosians@CentOS ~]$ sudo chown r2-d2 death-star-plans 

[genosians@CentOS ~]$ ll !$
-rw-r----- 1 r2-d2 princess-leia 0 Jan  8 21:41 death-star-plans

[genosians@CentOS ~]$ sudo chown :rebels death-star-plans 

[genosians@CentOS ~]$ ll !$
-rw-r----- 1 r2-d2 rebels 0 Jan  8 21:41 death-star-plans
```

---

> ## **newgrp [-] [GROUP]**
- Change the current real GID during a login session to GROUP

```
[root@CentOS ~]# id
uid=0(root) gid=0(root) groups=0(root)

[root@CentOS ~]# touch root-group-file

[root@CentOS ~]# ls -al root-group-file 
-rw-r--r-- 1 root root 0 Jan 21 02:33 root-group-file

[root@CentOS ~]# newgrp rebels

[root@CentOS ~]# id
uid=0(root) gid=600(rebels) groups=600(rebels),0(root)

[root@CentOS ~]# touch rebel-group-file

[root@CentOS ~]# ls -al rebel-group-file 
-rw-r--r-- 1 root rebels 0 Jan 21 02:32 rebel-group-file
```

---

> ## **SUID bit**
- Allows an executable to run with the permissions of the file owner

| `4` 2 1 | 4 2 1 | 4 2 1 | 4 2 1 |
|:-----:|:-----:|:-----:|:-----:|
|`SUID` \| SGID \| Sticky | r w x | r w x | r w x |
| Special | User | Group | Others |
```
[guru@CentOS ~]$ id
uid=500(guru) gid=500(guru) groups=500(guru)

[guru@CentOS ~]$ sudo -i

[root@CentOS ~]# ll /usr/bin/id
-rwxr-xr-x. 1 root root 27168 May 11  2016 /usr/bin/id

[root@CentOS ~]# chmod 4755 /usr/bin/id

[root@CentOS ~]# ll /usr/bin/id
-rwsr-xr-x. 1 root root 27168 May 11  2016 /usr/bin/id

[root@CentOS ~]# ^D

[guru@CentOS ~]$ id
uid=500(guru) gid=500(guru) euid=0(root) groups=500(guru)

[root@CentOS ~]# chmod u-x /usr/bin/id

[root@CentOS ~]# ll /usr/bin/id
-rwSr-xr-x. 1 root root 27168 May 11  2016 /usr/bin/id

[root@CentOS ~]# chmod 755 /usr/bin/id

[root@CentOS ~]# ll /usr/bin/id
-rwxr-xr-x. 1 root root 27168 May 11  2016 /usr/bin/id
```

---

> ## **SGID bit**

- Allows executable to run with the permissions of the group owner
- Folders with SGID keep group owner for all newly created subfolders/files, subfolders retain SGID bit

| 4 `2` 1 | 4 2 1 | 4 2 1 | 4 2 1 |
|:-----:|:-----:|:-----:|:-----:|
|SUID \| `SGID` \| Sticky | r w x | r w x | r w x |
| Special | User | Group | Others |

```
[guru@CentOS ~]$ id
uid=500(guru) gid=500(guru) groups=500(guru)

[root@CentOS ~]# chmod 2755 $(which id)

[root@CentOS ~]# ll /usr/bin/id
-rwxr-sr-x. 1 root root 27168 May 11  2016 /usr/bin/id

[root@CentOS ~]# ^D

[guru@CentOS tmp]$ id
uid=500(guru) gid=500(guru) egid=0(root) groups=0(root),500(guru)

[root@CentOS ~]# chmod g-s /usr/bin/id

[root@CentOS ~]# ll /usr/bin/id
-rwxr-xr-x. 1 root root 27168 May 11  2016 /usr/bin/id

[root@CentOS ~]# chmod 2745 /usr/bin/id

[root@CentOS ~]# ll /usr/bin/id
-rwxr-Sr-x. 1 root root 27168 May 11  2016 /usr/bin/id
```

---

> ## **Sticky bit**

### **Directories**
- Restricted Deletion Flag - prevents unprivileged users from removing or renaming a file in the directory unless they own the file or the directory

### **Files (varies by system)**
- Sticky bit - Saves the program’s text image on the swap device to facilitate faster load times

| 4 2 `1` | 4 2 1 | 4 2 1 | 4 2 1 |
|:-----:|:-----:|:-----:|:-----:|
|SUID \| SGID \| `Sticky` | r w x | r w x | r w x |
| Special | User | Group | Others |

```
[root@CentOS ~]# ll -d /tmp/
drwxrwxrwt. 6 root root 4096 Jan 13 14:42 /tmp/

[root@CentOS ~]# mkdir sticky

[root@CentOS ~]# ll -d sticky/
drwxr-xr-x 2 root root 4096 Jan 13 17:50 sticky/

[root@CentOS ~]# chmod o+t sticky/

[root@CentOS ~]# ll -d sticky/
drwxr-xr-t 2 root root 4096 Jan 13 17:50 sticky/

[root@CentOS ~]# chmod o-x sticky/

[root@CentOS ~]# ll -d sticky/
drwxr-xr-T 2 root root 4096 Jan 13 17:50 sticky/
```