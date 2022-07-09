# Linux - Identifying and Managing Command Shells

> ## **Change your shell temporarily**
- Type the shell you want to start
    - sh
    - ksh
    - bash
    - csh

```
[guru@CentOS ~]$ sh
sh-4.1$ bash

[guru@CentOS ~]$ dash
$ csh

[guru@CentOS ~]$ sh
sh-4.1$
```

---

> ## **Shells**

### **$SHELL**
- Contains your default login shell

### **$shell**	
- When available, contains currently logged in shell

> ## **ps –f**
- Displays PID and PPID
- Can be used to trace PPIDs back to the PID of the calling shell

```
sh-4.1$ ps -f
UID	PID	PPID	C	STIME	TTY	TIME		CMD
guru	24718	24716	0	02:46	pts/1	00:00:00		-bash
guru	24809	24718	0	02:46	pts/1	00:00:00		sh
guru	24810	24809	0	02:46	pts/1	00:00:00		ps -f
```

> ## **ps -p $$**
- `$$` is a special parameter that expands out to the PID of the current shell

```
sh-4.1$ ps -p $$
PID	TTY	TIME		CMD
25736	pts/0	00:00:00		sh
```
---

> ## **chsh [-s shell] [-l] [-u] [-v] [username]**
- Change shell permanently
    - Change your login shell
- Edit /etc/passwd by hand

```
[guru@CentOS ~]$ grep guru /etc/passwd
guru:x:500:500::/home/guru:/bin/bash

[guru@CentOS ~]$ chsh -s /bin/sh
Changing shell for guru.
Password: 
Shell changed.

[guru@CentOS ~]$ grep guru /etc/passwd
guru:x:500:500::/home/guru:/bin/sh
```

---


> ## **Resources**

| **Resource**   | **Description**   |
| --------------|-------------------|
| **Bash Resource** |
| `Bash manual` | https://www.gnu.org/software/bash/manual/bash.html |