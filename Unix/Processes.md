# Processes

## Program vs. Process
- **Program** - Is an executable file on the disk
    - **Process** - Is an instance of that program or is a program or application that is in execution

## Types of Processes

### Foreground Process

Also known as an interactive process. Terminal for example or web browser. 

### Background Process

Also known as a non-interactive process. These are not normally connected to any foreground process and don't expect any user input. 

## User and System Processes
- They dont actuall run simultaneously
- The OS split time between each process and the CPU

## Process IDs

- **PID** (Process ID) When a program is started it is assigned a PID
    - *Kernel* PID 0
- **PPID** (Parent Process ID)
    - init.d PID 1, PPID 0 
- **Process Tree**
    - Starts at PID 0

## States of a Process

- **Running** - Either actively running or waiting for a CPU core to be assigned to it
- **Waiting** - In this state the process is waiting for 1 of 2 things
    - Event to happen such as user input, etc
    - Systems resources to become available
    - ***Two Types of Waiting***
        - **Interrupted** - Some hardware based conditions would cause this
        - **Uninterruptible** - This process cannot be stopped by any event or signal
- **Stopped** - The process has been stopped by some means
    - This can be a signal to stop from the user or system
    - Can also be in this state during the time a debugger is attached to it
- **Zombie/Orphan** - The process is no longer alive or AKA dea
    - The reason it is still showing as a 'Zombie' or 'z' is due to still being on the process entry table in the kernel

## Signals

A system message sent from one process to another, not usually used to transfer data but instead of used to remotely command the partnered process.

When a process receives a Signal, either of the **three** things can happen:
- **Default** - Process excecute the default action of the signal.
    - *Example* > When process receives SIGTERM signal, process is terminated by default
- **Customized** -  Process executes customized processing on receiving the singal by executing the *signal handler routine* (Special function which is invoked when the process receives a signal. Executed at the highest priority)
    - *Example* > When process receives the SIGTERM signa, process might want to print the Goodbye msg on the screen, or write its internal data structure in a file for offline debugging before it dies out
- **Ignore** - Process ignore the signal

### Well Known Linux Signals

- **SIGINT** - Interrupt (i.e., Ctrl-C)
- **SIGUSR1 and SIGUSR2** - User defined signals
- **SIGKILL** - Sent to the process from kernel when kill -9 is invoked on a PID. 
    - This signal cannot be caught by the process.
- **SIGABRT** - Raised by abort() by the process itself. Cannot be blocked. The process is terminated. 
- **SIGTERM** - Raised when *kill* is invoked. Can be caught by the process to execute user defined actions.  
- **SIGSEGV** - Segmentation fault, raised by the kernel to the process when illegal memory is referenced.
- **SIGCHILD** - Whenever a child terminates, this is the signal sent to the parent. 