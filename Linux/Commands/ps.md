# ps

List processes and their attributes

---

> ## **Example**

| **Command**   | **Description**   | 
|:-------------:|-------------------|
| **Standard Syntax Examples** |
| `ps -aux` or `-ax` | See every process on the system |
| `ps -U root -u root u` | See every process owned by root |
| **BSD Syntax Examples** |
| `ps -e` or `-ef` or `-eF` or `-ely` | See every process on the system |
| **Process Tree Examples** |
| `ps -ejH` or `axjf` or `eh` | Print a process tree |
|**Thread Information Examples** |
| `ps -eLf` or `-axms` | Get information about threads |
| **Display the process for the cron command** |
| `ps -C cron` | Get information about the cron process |
| **Sort processes by the 3rd column** |
| `ps -A \| sort -k 3` | Sorts all shown processes by the third column |

---

> ## **PS Command Attributes**

| **Attribute** | **Description** |
|--------------:|-----------------|
| `F:` | Flags associated with the process (different meaning depending on the UNIX variant |
| `S:` | State of the process (varies depending on the UNIX variant) |
| `UID:` | The effective user ID of the process or the associated username if the -f option is used |
| `PID:` | The process ID of the process |
| `PPID:` | The parent process ID |
| `PRI:` | The priority of the process |
| `NI:` | The nice value (used for priority computation) |
| `ADDR:` | The memory address of the process |
| `SZ:` | The total size of the process in virtual memory including all mapped files and devices |
| `WCHAN:` | The address of an event for which the process is sleeping (this will be blank for running processes) |
| `STIME:` | The starting time of the process given in hours minutes and seconds |
| `TTY:` | The terminal assigned to the process |
| `TIME:` | The cumulative execution time for the process given in minutes and seconds |
| `CMD:` | The command name. If the -f option is used the full command name and its arguments are printed up to an 80-characters limit. |