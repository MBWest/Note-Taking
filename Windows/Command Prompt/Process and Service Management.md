# Process and Service Management

| **Command** | **Description** |
|----------|-----------------|
| `sc` | Communicating with the services control manager|
| `-query / -queryex` | List all active services by default |
| `schtasks` | Create, delete, query, change, run or end scheduled tasks |
| `shutdown` | Shutdown or restart the computer|
| `taskkill` | Terminate tasks by ID or image name |
| `tasklist` | Display a list of currently running processes |
| **Example** | 
| `Tasklist /fi ""WhatYourFiltering" "Operator" "Value""` | Search Task list |
| `Tasklist` | List all running processes |
| `Tasklist /m kernel32.dll` | List all processes using the kernel32.dll module |
| `Tasklist /svc /fi "service eq spooler"` | Search for specific service and provide the service list |
| `Tasklist /fi "imagename eq calculator.exe"` | Search for specific image name|
| `schtasks /create /tn "NameofTask" /sc "time" /mo "How Many" /TR "exe"` | Create a new Task |
| `Taskkill /pid 1234` | Terminate process with PID 1234 |
| `Sc query` | List all active services |
| `Sc query state=all | find /i "servicename"` | Search services|
| `sc getkeyname "Service"` | Get key name after searching for service name |
| `Sc query "NameoftheService"` |Query the key name|
| `Sc config DPS start=demand` | Change DPS to ondemand start |
| `Net start` | List all Windows services that are started |