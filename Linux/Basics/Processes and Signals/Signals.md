# Signals

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

## Well Known Linux Signals

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