# Linux - Process and Service Management


> ## **Program vs Process**

| **Topic**   | **Description**   |
| --------------|-------------------|
| **Program vs Process** |
| `program` | Is an executable file on the disk |
| `Process` | Is an instance of that program or is a program or application that is in execution |
| **Types of Processes** |
| `Foreground Process` | Also known as an interactive process. Terminal for example or web browser. |
| `Background Process` | Also known as a non-interactive process. These are not normally connected to any foreground process and don't expect any user input. |
| **User and System Processes** |
| | They dont actuall run simultaneously |
| | The OS split time between each process and the CPU |
| **Process IDs** |
| `PID` | (Process ID) When a program is started it is assigned a PID `Kernel` PID 0 |
| `PPID` | (Parent Process ID) `init.d PID 1, PPID 0` |
| **Process Tree** |
| | Starts at PID 0 |
| **States of a Process** |
| `Running`| Either actively running or waiting for a CPU core to be assigned to it. |
| `Stopped` | The process has been stopped by some means; This can be a signal to stop from the user or system; Can also be in this state during the time a debugger is attached to it. |
| `Zombie/Orphan` | The process is no longer alive or AKA dead; The reason it is still showing as a 'Zombie' or 'z' is due to still being on the process entry table in the kernel. |
| `Waiting` | In this state the process is waiting for 1 of 2 things; Event to happen such as user input, etc; Systems resources to become available. |
| **Two Types of Waiting**| 
| `Interrupted` | Some hardware based conditions would cause this. |
| `Uninterruptible` | This process cannot be stopped by any event or signal. |

---
---


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

> ## **Signals**

| **Topic**   | **Description**   |
| --------------|-------------------|
| **Signals** |
| `signal` | A system message sent from one process to another, not usually used to transfer data but instead of used to remotely command the partnered process. |
| **(When a process receives a Signal, either of the **three** things can happen)** |
| `Default` | Process excecute the default action of the signal. |
|  `Default Example` | When process receives SIGTERM signal, process is terminated by default. |
| `Customized`  | Process executes customized processing on receiving the singal by executing the signal handler routine (Special function which is invoked when the process receives a signal. Executed at the highest priority). |
| `Customized Example` | When process receives the SIGTERM signa, process might want to print the Goodbye msg on the screen, or write its internal data structure in a file for offline debugging before it dies out. |
| `Ignore` | Process ignore the signal. |

### **Well Known Linux Signals**

| **Signal** | **Description** | **Default Action** |
|------------|-----------------|--------------------|
| `SIGHUP` | Hangup. Usually means that the controlling terminal has been disconnected. This signal is generated when a user presses Ctrl+D at the shell command line. | Terminate process. | 
| `SIGINT` | Interrupt from keyboard. This signal is generated when a user presses Ctrl+C at the shell command line. | Terminate process. | 
| `SIGQUIT` | Quit from keyboard. This signal is generated when a user presses Crtl+\ at the command line. | Terminate process and create a core dump. | 
| `SIGKILL` | Kill signal. This is a sure kill because it cannot be trapped (caught) or ignored (masked). | Terminate the process. | 
| `SIGTERM` | Termination signal. A gentle kill that gives processes a chance to clean up. | Terminate the process. | 
| `SIGCHLD` | Child status changed (stopped or terminated). | Ignore the signal.| 
| `SIGSTOP` | Stop signal. Pauses a process. This signal cannot be caught or ignored. | Stop process.| 
| `SIGCONT` | Resume signal. Can be caught/trapped but cannot be ignored/masked. | Continue the process if it is currently stopped.Otherwise, ignore. | 
| `SIGTSTP` | Stop signal. Pauses a process. Can be caught or ignored. | Stop process.| 
| `SIGTTIN` | Terminal Input from background process. | Stop process.| 
| `SIGTTOU` | Terminal output from background process. | Stop process. | 
| `SIGFPE` | Arithmetic exception. Informs a process of a floating-point error. | Terminate process and create a core dump.| 
| `SIGSEGV` | Segmentation Fault (or Invalid Memory Access). | Terminate process and create a core dump.| 
| `SIGSYS` | Bad system call. | Terminate process and create a core dump.| 
| `SIGILL` | Illegal instruction. | Terminate process and create a core dump.| 
| `SIGPIPE` | Broken pipe. Write to pipe with no reader. | Terminate process.| 
| `SIGALRM` | Timer signal from an Alarm Clock. | Terminate process.| 
| `SIGUSR1` | User-defined signal 1. | Terminate process.| 
| `SIGUSR2` | User-defined signal 2. | Terminate process.| 
| `SIGPWR` | Power failure or system restart. | Terminate process.| 

---
---

> ## **killall [OPTIONS] name...**
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
