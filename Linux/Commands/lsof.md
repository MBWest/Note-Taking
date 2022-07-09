# lsof

Identifies any open files on the system

---

> ## **Example**

| **Command**   | **Description**   |
| --------------|-------------------|
| `lsof +D /var/log` | Views all sub directories to see if anything is open |
| `lsof -u brandon` | View open files by the user Brandon |

---

> ## **Output of lsof**

| **Output**   | **Description**   |
| --------------|-------------------|
| `Command` | Name of the application ran  |
| `PID` | PID of the application |
| `USER` | Users context the application is running in |
| `FD` | File Drescriptor |
| `Cwd` | Shows the current working directory |
| `Txt` | Shows its a text file |
| `Mem` | Data Segment or Shared Object loaded into memory |
| `Number` | This will be a digit and will show the actual file discriptor number (#u) |
| `TYPE` | Tells us what type of file |
| `REG` | Regular file |
| `DIR` | Directory |
| `FIFO` | Named pipe, symbolic links, sockets, blocks |
| `UNKOWN` | Normally happens with kernel threads |
| `DEVICE` | The drive, EX: sda1 |
| `SIZE/OFF` | Size of the file |
| `NODE` | inode number |
| `NAME` | Name of the file |