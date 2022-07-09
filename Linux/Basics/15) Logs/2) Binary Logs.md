# Linux - Logs - Binary Logs


> ## **/var/log/lastlog**
- Contains information about the `last login` of each user
- Viewed by using the `lastlog` command
---
> ## **/var/log/btmp**
- Contains information about `failed login` attempts
- Viewed by using the `lastb` command

> ### **lastb [OPTION]...**
- Same as the last command, except that by default it shows the contents of /var/log/btmp
- `-f FILE` - use a specific file instead of wtmp
- `-n NUM` - show NUM lines instead of the whole file

```
[root@CentOS ~]# lastb
root     ssh:notty    108-234-171-194. Fri Feb 10 02:24 - 02:24  (00:00)    
root     ssh:notty    108-234-171-194. Fri Feb 10 02:24 - 02:24  (00:00)    
... ADDITIONAL ENTRIES ...

[root@CentOS ~]# ls -al /usr/bin/last*
-rwxr-xr-x. 1 root root 14100 Jul 23  2015 last
lrwxrwxrwx. 1 root root     4 Dec  8 16:14 lastb -> last
-rwxr-xr-x. 1 root root 13680 May 10  2016 lastlog
```
---
> ## **/var/run/utmp**
- Contains information about who is `currently logged in`
- Viewed by using the `who` or `w` commands
---
> ## **/var/log/wtmp**
- Contains information about all logins/logouts (`historical utmp`)
- Viewed by using the `last` command


> ### **last [OPTION]...**
- Searches back through `/var/log/wtmp` and displays a list of all users logged in (and out) since that file was created
- `-f FILE` - use a specific file instead of wtmp
- `-n NUM` - show NUM lines instead of the whole file

```
[root@CentOS ~]# last
root     pts/2        108-234-171-194. Sun Feb 12 00:35 - 16:06 (3+15:30)   
root     pts/0        108-234-171-194. Fri Feb 10 17:28   still logged in   
... ADDITIONAL ENTRIES ...

[root@CentOS ~]# last -f /var/log/btmp-20170201
root     ssh:notty    155a133b40c230.g Sun Jan  1 04:17 - 04:17  (00:00)    
admin    ssh:notty    155a133b40c230.g Sun Jan  1 04:17 - 04:17  (00:00)    
... ADDITIONAL ENTRIES ...
```