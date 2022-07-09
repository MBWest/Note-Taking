# wmic

> ## **Process List Brief Example**

- **wmic process list brief**
    - **HandleCount**: A count of handles or open files and pipe resources
    - **Name**: The process name, often the executable name
    - **Priority**: The CPU scheduling priority of a process from 0 (least priority) to 31 (highest priority)
    - **ProcessId**: The unique identifier for a process so that the system can reference it by the numeric value, also known as a PID
    - **ThreadCount**: The number of threads or basic units of activity that consume processor time and system resources
    - **WorkingSetSize**: The amount of memory allocated to a process in bytes

---

> ## **Process List Full Example**

- **wmic process where name="nssm.exe" list full** - Shows all the information for every process
- **wmic process where processid=2984 list full** - Shows all the information for the process with the id of 2984
- **wmic process where processid=2984 get name,commandline,processid,parentprocessid** - Shows the requested information for the process with id 2984
- **wmic process where parentprocessid=620 get name,commandline,processid,parentprocessid** - Shows the requested information for the parent process with id 620

---

> ## **Startup**

- **wmic startup**