# Linux - Process and Service Management

> ## **ps [OPTIONS]**
- Report a snapshot of the current processes
- By default, ps selects all processes with the same effective user ID (EUID) as the current user and associated with the same terminal as the invoker
- `-A` or `-e` - select all processes
- `-f` - full format listing
- `-u userlist` - select processes by EUID or user name
- `-p pidlist` or `--pid` - select process by PID
- `--ppid` - select process by PPID

```
[guru@CentOS ~]$ ps 
  PID TTY          TIME CMD
20392 pts/0    00:00:00 ps
28822 pts/0    00:00:00 bash

[guru@CentOS ~]$ ps -e | head -n 4 
  PID TTY          TIME CMD
    1 ?        00:00:04 init
    2 ?        00:00:00 kthreadd
    3 ?        00:00:00 migration/0

[guru@CentOS ~]$ ps -ef | head -n 4 
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0  2016 ?        00:00:04 /sbin/init
root         2     0  0  2016 ?        00:00:00 [kthreadd]
root         3     2  0  2016 ?        00:00:00 [migration/0]
```

---

> ## **kill [-s signal|-p] [--] pid... || kill -l [signal]**
- Sends the specified signal to the specified process
- `-s` - specify the signal to send
- `-l` - display list of signal names

```
[guru@CentOS ~]$ kill -l
 1) SIGHUP	2) SIGINT	3) SIGQUIT	4) SIGILL   5) SIGTRAP
 6) SIGABRT	7) SIGBUS	8) SIGFPE	9) SIGKILL  10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM 15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP 20) SIGTSTP

[guru@CentOS ~]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
guru     26386 29630  0 00:40 pts/1    00:00:00 find /
guru     29630 29629  0 Jan01 pts/1    00:00:00 -bash
guru     26391 29630  0 00:42 pts/1    00:00:00 ps -f

[guru@CentOS ~]$ kill 26386
[guru@CentOS ~]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
guru     26386 29630  0 00:40 pts/1    00:00:00 find /
guru     26391 29630  0 00:42 pts/1    00:00:00 ps -f
guru     29630 29629  0 Jan01 pts/1    00:00:00 -bash

[guru@CentOS ~]$ kill -s 9 26386
[guru@CentOS ~]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
guru     26391 29630  0 00:42 pts/1    00:00:00 ps -f
guru     29630 29629  0 Jan01 pts/1    00:00:00 -bash
```

---

> ## **killall [OPTIONS] name... **
- Sends a signal to all processes running any of the specified commands.  

```
[guru@CentOS ~]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
guru     26689 28822  0 02:44 pts/0    00:00:00 python -m SimpleHTTPServer
guru     26691 28822  1 02:44 pts/0    00:00:00 python -m SimpleHTTPServer 
guru     26693 28822  0 02:44 pts/0    00:00:00 ps -f
guru     28822 28821  0 Jan01 pts/0    00:00:00 -bash

[guru@CentOS ~]$ killall python

[guru@CentOS ~]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
guru     26697 28822  0 02:45 pts/0    00:00:00 ps -f
guru     28822 28821  0 Jan01 pts/0    00:00:00 -bash
```

---

> ## **^Z**
- Ctrl + Z; Suspend a process by sending a SIGSTOP signal 
- Control is returned to the terminal after suspending the process

```
[guru@CentOS ~]$ python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
^Z
[1]+  Stopped                 python -m SimpleHTTPServer
[guru@CentOS ~]$ pwd
/home/guru
```

---

> ## **jobs [-lnprs] [jobspec]...**
- Lists the active jobs
- `-l` - display PID also 
- `-p` - display PIDs only

```
[guru@CentOS ~]$ jobs
[1]+  Stopped                 	python -m SimpleHTTPServer

[guru@CentOS ~]$ jobs -l
[1]+ 26704 Stopped                python -m SimpleHTTPServer

[guru@CentOS ~]$ jobs -p
26704
```

---

> ## **fg [jobspec]**
- Place the job jobspec in the foreground, making it the current job
- Control of the terminal is given to the process that is brought to the foreground

```
[guru@CentOS ~]$ jobs
[1]+  Stopped                 python -m SimpleHTTPServer
[guru@CentOS ~]$ fg 1
python -m SimpleHTTPServer
```

---

> ## **bg [jobspec]...**
- Place the jobs identified by each jobspec in the background, as if they had been started with a '&'
- Control of the terminal does not change

```
[guru@CentOS ~]$ jobs
[1]+  Stopped                 python -m SimpleHTTPServer

[guru@CentOS ~]$ bg 1
[1]+ python -m SimpleHTTPServer &
```

---

> ## **COMMAND &**
- Run command in the background
- Control of the terminal does not change

```
[guru@CentOS ~]$ jobs
[1]+  Running                 python -m SimpleHTTPServer &

[guru@CentOS ~]$ python -m SimpleHTTPServer 1025 & 
[2] 26790

[guru@CentOS ~]$ Serving HTTP on 0.0.0.0 port 1025 ...

[guru@CentOS ~]$ jobs
[1]-  Running                 python -m SimpleHTTPServer &
[2]+  Running                 python -m SimpleHTTPServer 1025 &
```

---

> ## **shutdown [OPTION]... TIME [MESSAGE]**
- Bring the system down in a safe way
- Notifies users of pending shutdown
- Prevents new logins if within 5 minutes of shutdown


```
[guru@CentOS ~]$ shutdown -r now
```
