# Linux - Logs - Manipulating/Viewing Audit Rules

> ## **auditctl [options]**

- Used to configure kernel options related to auditing, view status of the configuration, and load audit rules
- `-l` - list all rules
- `-a list,action` - append rule to the end of list with action
    - List names include:  task, exit, user, exclude
    - Action names include:  never, always
    - exit - this list is used upon exit from a syscall to determine if an audit event should be created
- `-F field=value` - build a rule field
    - Some fields include:  path, perm, key, dir
    - ex. path=/some/file/to/audit

- **Adding and viewing a rule**

```
[root@CentOS ~]# auditctl -a exit,always -F path=/root/passwords -F perm=rwxa -F key=secret

[root@CentOS ~]# auditctl -l
-w /root/passwords -p rwxa -k secret
```
```
[root@CentOS ~]# tail -f /var/log/audit/audit.log
... ADDITIONAL ENTRIES ... 
type=CONFIG_CHANGE msg=audit(1485030851.087:215110): auid=0 ses=567 op="add rule" key="secret" list=4 res=1
... ADDITIONAL ENTRIES ... 
```
---
- **Listing an audited file**

```
[root@CentOS ~]# ls passwords 
passwords
```

```
[root@CentOS ~]# tail -f /var/log/audit/audit.log
... ADDITIONAL ENTRIES ... 
type=PROCTILE msg=audit(1485031370.900:215119): proctile=76496883965829C39658292769
type=SYSCALL msg=audit(1485031370.900:215119): arch=40000003 syscall=229 success=no exit=-61 a0=bfd5d801 a1=b5fafc a2=bfd5b5bc a3=14 items=1 ppid=6152 pid=6528 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=567 comm="ls" exe="/bin/ls" key="secret"

type=CWD msg=audit(1485031370.900:215119):  cwd="/root"

type=PATH msg=audit(1485031370.900:215119): item=0 name="passwords" inode=136126 dev=fc:01 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL
```

---

- **Viewing an audited file’s contents**

```
[root@CentOS ~]# cat passwords 
luggage=12345
WOPR=joshua
```

```
[root@CentOS ~]# tail -f /var/log/audit/audit.log
... ADDITIONAL ENTRIES ... 
type=PROCTILE msg=audit(1485031977.737:215147): proctile=76457727758472C2894D2 9486992CD5817746425882FD7375465437F674767D65847747F4728C487274D37
type=SYSCALL msg=audit(1485031977.737:215147): arch=40000003 syscall=5 success=yes exit=3 a0=bfb2f7ff a1=8000 a2=0 a3=1 items=1 ppid=6152 pid=6538 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=567 comm="cat" exe="/bin/cat" key="secret"

type=CWD msg=audit(1485031977.737:215147):  cwd="/root"

type=PATH msg=audit(1485031977.737:215147): item=0 name="passwords" inode=136127 dev=fc:01 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL
```
---

- **Deleting a rule**

```
[root@CentOS ~]# auditctl -d exit,always -F path=/root/passwords -F perm=rwxa -F key=secret

[root@CentOS ~]# auditctl -l
No rules

[root@CentOS ~]# 
```

```
[root@CentOS ~]# tail -f /var/log/audit/audit.log
... ADDITIONAL ENTRIES ... 
type=CONFIG_CHANGE msg=audit(1485030870.053:215111): auid=0 ses=567 op="remove rule" key="secret" list=4 res=1
... ADDITIONAL ENTRIES ... 
```

---

- **Stores rules that will be loaded by using the `auditctl` command whenever `auditd` is started.**

```
[root@CentOS ~]# cat /etc/audit/audit.rules 
# This file contains the auditctl rules that are loaded
# whenever the audit daemon is started via the initscripts.
# The rules are simply the parameters that would be passed to auditctl 

# First rule - delete all
-D

# Increase the buffers to survive stress events.
# Make this bigger for busy systems
-b 320

# Feel free to add below this line. See auditctl man page

[root@CentOS ~]# 
```
---
> ## **ausearch [options]**
- Queries auditd logs for events based on different criteria
- `-k KEY`  - search for an event based on KEY
- `--start START` - search for events with timestamps equal to or after the given START
    - Valid STARTs include recent, today, yesterday, 18:00:00, etc 
- `--end END` - search for events with timestamps equal to or before the given END
    - Valid ENDs are the same as those for --start 
- `-i` - interpret numeric entities into text

- **Searches only entries in the audit log**
    - /var/log/audit/audit.log

```
[root@CentOS ~]# ausearch -k secret 
----
time->Sat Jan 21 20:34:11 2017
type=CONFIG_CHANGE msg=audit(1485030851.087:215110): auid=0 ses=567 op="add rule" key="secret" list=4 res=1

[root@CentOS ~]# ausearch -i -k secret
----
type=CONFIG_CHANGE msg=audit(01/21/2017 20:34:11.087:215110) : auid=root ses=567 op="add rule" key=secret list=exit res=yes 
```

- Each entry in the log file has a unique ID along with a timestamp
    - When dealing with filesystem auditing, each triggered event will contain 3 entries in the log file, all with the same unique ID
        - PATH, CWD, SYSCALL

```
[root@CentOS ~]# ausearch -k secret
----
time->Sat Jan 28 00:42:33 2017
type=PATH msg=audit(1485564153.840:216093): item=0 name="passwords" inode=136127 dev=fc:01 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL
type=CWD msg=audit(1485564153.840:216093):  cwd="/root"
type=SYSCALL msg=audit(1485564153.840:216093): arch=40000003 syscall=5 success=yes exit=3 a0=bfe66814 a1=8000 a2=0 a3=1 items=1 ppid=6318 pid=9517 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts1 ses=571 comm="cat" exe="/bin/cat" key="secret"
```
