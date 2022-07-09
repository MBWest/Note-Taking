# Linux - Logs - Log Rotation

- Logs may be rotated, compressed, removed, or shipped off to another system based on different criteria
- /etc/logrotate.conf is the configuration file that handles the log rotation policy

```
[root@CentOS ~]# ls -altr /var/log
total 12368
-rw-------   1 root utmp 12225408 Jan 21 02:32 btmp-20170201
-rw-------   1 root root     5794 Jan 21 15:24 secure-20170122
-rw-------   1 root utmp        0 Feb  1 03:09 btmp
-rw-------   1 root root      228 Feb  5 23:14 secure
-rw-rw-r--.  1 root utmp    20352 Feb  5 23:14 wtmp
-rw-r--r--.  1 root root   148044 Feb  5 23:14 lastlog
drwxr-x---.  2 root root     4096 Feb  5 23:31 audit
[root@CentOS ~]# 
```

---

> ## **Viewing rotated logs**
- `Ascii` - can perform normal operations on the file 
- Binary 
-   `last -f /var/log/wtmp`
-   `lastb -f /var/log/btmp`

```
[root@CentOS ~]# ls -altr /var/log
total 12368
-rw-------   1 root utmp 12225408 Jan 21 02:32 btmp-20170201
-rw-------   1 root root     5794 Jan 21 15:24 secure-20170122
... ADDITIONAL ENTRIES ... 

[root@CentOS ~]# cat /var/log/secure-20170122
... LOG ENTRIES ... 

[root@CentOS ~]# lastb -f /var/log/btmp-20170201
... LOG ENTRIES ... 
```