# Linux File Structure - Accounts and Security Administration

> ## **sudo [OPTION]...[COMMAND]**
- Allows a permitted user to execute a COMMAND as the superuser or another user
- `-i` - simulate initial login (similar to su -l)
- `-l[l]` - list the allowed/forbidden commands for the user 
- `-u USER` - run the specified command as USER

```
[guru@CentOS ~]$ sudo -i 

[guru@CentOS ~]$ sudo -i -u chewie

[guru@CentOS tmp]$ ls ~chewie
ls: cannot open directory /home/chewie/: Permission denied

[guru@CentOS tmp]$ sudo -u chewie ls -Al ~chewie
total 24
-rw-------  1 chewie chewbacca  163 Jan  7 21:58 .bash_history
-rw-r--r--  1 chewie chewbacca   18 May 10  2016 .bash_logout
-rw-r--r--  1 chewie chewbacca  176 May 10  2016 .bash_profile
-rw-r--r--  1 chewie chewbacca  124 May 10  2016 .bashrc
-rw-r--r--  1 chewie chewbacca    0 Dec  8 16:23 .cloud-locale-test.skip

[guru@CentOS tmp]$ sudo cat /etc/shadow
root:$6$hwJt1KMO$EnOKUC0VfWapIUtjhSEZWCYw2TdHpXjTSHZuKfr7KHU/b48AMoc6FmP5zpn4lKjit3sz.Pgx/XwQoy23IgK74.:17164:0:14600:14:::
... LONG LIST OF USER PASSWORD INFO ...
```