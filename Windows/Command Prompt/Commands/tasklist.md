# tasklist

 Look at how various services map to the processes they are launched from

| **Command** | **Description** |
|-------------|-----------------|
| `tasklist` | Display all currently running processes |
| `tasklist /m` | Display all dll modules currently loaded into each process |
| `tasklist /svc /fi "services eq spoiler"` | What process has the spooler service loaded into it |
| `tasklist /m, tasklist /svc` | What is the caculator's PID? What DLLs does it have? Are there any services attached to this program? |
| `tasklist /fi "imagename eq calculator.exe", tasklist /m /fi "imagename eq calculator.exe", tasklist /svc /fi "imagename eq \| calculator.exe"` | Do the last step again but filter it so just the calculator.exe process is shown |