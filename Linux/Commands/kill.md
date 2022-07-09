# Kill

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
| `signal` | A system message sent from one process to another, not usually used to transfer data but instead of used to remotely command the partnered process. |
| `Default` | Process excecute the default action of the signal. |
|  `Default Example` | When process receives SIGTERM signal, process is terminated by default. |
| `Customized`  | Process executes customized processing on receiving the singal by executing the signal handler routine (Special function which is invoked when the process receives a signal. Executed at the highest priority). |
| `Customized Example` | When process receives the SIGTERM signa, process might want to print the Goodbye msg on the screen, or write its internal data structure in a file for offline debugging before it dies out. |
| `Ignore` | Process ignore the signal. |

---
---

> ## **Well Known Linux Signals**

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