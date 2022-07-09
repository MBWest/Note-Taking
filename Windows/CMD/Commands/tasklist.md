# tasklist

 - Look at how various services map to the processes they are launched from

---

> ## **Examples**


| **Command** | **Description** |
|-------------|-----------------|
| `tasklist` | Display all currently running processes |
| `tasklist /m` | Display all dll modules currently loaded into each process |
| `tasklist /svc /fi "services eq spoiler"` | What process has the spooler service loaded into it |
| `tasklist /m, tasklist /svc` | What is the caculator's PID? What DLLs does it have? Are there any services attached to this program? |
| `tasklist /fi "imagename eq calculator.exe", tasklist /m /fi "imagename eq calculator.exe", tasklist /svc /fi "imagename eq \| calculator.exe"` | Do the last step again but filter it so just the calculator.exe process is shown |
| `tasklist` | List all running processes |
| `tasklist /m kernel32.dll` | List all tasks using kernel32.dll module |
| `tasklist /svc` | Show services hosted in each process |
| `tasklist /v` | Show verbose information |
| `tasklist /fi "imagename eq cmd.exe"` | Show all cmd.exe processes |
| `tasklist /fi "imagename eq cmd.exe" /m` | How all modules used by cmd.exe process |
| `tasklist /fi "imagename eq cmd.exe" /svc` | Show all services hosted by cmd.exe |