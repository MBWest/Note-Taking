# taskkill

- Terminates processes based on PID or IMAGENAME

---

> ## **Examples**


| **Command** | **Description** |
|-------------|-----------------|
| `taskkill /fi "imagename eq calculator.exe"` | Close the calculator.exe process using the Command Prompt |
| `taskkill /f "PID eq ****"` | Reopen calculator.exe and kill it by the pid |
| `taskkill /pid 1234` | Terminate process with process ID 1234 |
| `taskkill /im iexplore.exe` | Terminate all iexplore.exe processes |
| `taskkill /t /pid 1234` | Terminate PID 1234 & all child processes  |
| `taskkill /f /pid 1234` | Forcefully terminate process 1234 |
| `taskkill /fi “imagename eq cmd.exe”` | Terminate cmd.exe |

