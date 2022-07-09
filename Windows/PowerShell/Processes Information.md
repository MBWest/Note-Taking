# Processes

> ## **Examples**

| **Command** | **Usage** |
|-------------|-----------|
| `Get-Process` | List all processes |
| `Get-Process "ProcessName"` | List specific process |
| `Get-Process "ProcessName" -FileServerInfo` | Get File path for process |
| `Get-Process "ProcessName"` | Another way to get file path for process |
| `Get-Process \| Where-Object -Property Path -like C:\* \| Select-Object -Property Name, Path \| Sort-Object -Unique -Property Path` | Get process with a path in C: and list their Names and Path; sort by unique path |