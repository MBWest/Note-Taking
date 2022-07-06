# Processes

## Program vs Process

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


