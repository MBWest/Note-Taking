# Linux - Logs - Searching System Logs

> ## **Searching /var/log using the grep command**
```
[root@CentOS ~]# useradd yoda

[root@CentOS ~]# egrep -R yoda /var/log 
/var/log/audit/audit.log:type=ADD_GROUP msg=audit(1485004075.461:215000): user pid=6262 uid=0 auid=0 ses=567 msg='op=add-group acct="yoda" exe="/usr/sbin/useradd" hostname=? addr=? terminal=pts/0 res=success'
/var/log/secure:Jan 21 13:07:55 CentOS useradd[6262]: new group: name=yoda, GID=506
/var/log/secure:Jan 21 13:07:55 CentOS useradd[6262]: new user: name=yoda, UID=506, GID=506, home=/home/yoda, shell=/bin/bash

[root@CentOS ~]# date -d @1485004075.461
Sat Jan 21 13:07:55 UTC 2017
```