# Process and Service Management

| **Command** | **Description** |
|----------|-----------------|
| `sc` | Communicating with the services control manager|
| `-query / -queryex` | List all active services by default |
| `schtasks` | Create, delete, query, change, run or end scheduled tasks |
| `shutdown` | Shutdown or restart the computer|
| `taskkill` | Terminate tasks by ID or image name |
| `tasklist` | Display a list of currently running processes |
| `Tasklist /fi ""WhatYourFiltering" "Operator" "Value""` | |
| `Tasklist` | |
| `Tasklist /m kernel32.dll` | |
| `Tasklist /svc /fi "service eq spooler"` | |
| `Tasklist /fi "imagename eq calculator.exe"` | |
| `schtasks /create /tn "NameofTask" /sc "time" /mo "How Many" /TR "exe"` | |
| `Taskkill /pid 1234` | |
| `Sc query` | |
| `Sc query state=all | find /i "servicename"` | |
| `sc getkeyname "Service"` | |
| `Sc query "NameoftheService"` | |
| `` | |
| `` | |


	Search Tasklist
	List all running processes
	List all processes using the kernel32.dll module
	Search for specific service and provide the service list
	Search for specific image name
	Create a new Task
	Terminate process with PID 1234
	List all active services
	Search services
	Get key name after searching for service name
	Query the keyname
Sc config DPS start=demand	Change DPS to ondemand start
Net start	List all Windows services that are started
