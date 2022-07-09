# PowerShell vs CMD.exe

| **PowerShell** | **CMD** |
|--------------|-------|
| PowerShell 2.0 included with release of Windows 7 in 2009 |  Released with Windows NT Family in Dec 1987 |
| Continued support by Microsoft | Supported, but deprecated in 2008 by Microsoft |
| Built on top of .NET, allows far greater control over OS |  Capability limited to native binaries and internal functionality |
| Returns objects, allowing easy manipulation over the pipeline | Returns strings, limiting the use of data over the pipeline |
| Control over Enterprise services (Exchange, Active Directory, 365, Teams, SharePoint, etc…) | Enterprise support limited after the release of Server 2008 R2 (which included PowerShell 2.0) |

| **PowerShell** | **CMD** |
|--------------|-------|
| `Get-Process` | tasklist.exe |
| `Get-NetTCPConnection` | netstat.exe |
| `Get-Service` |  sc.exe| 
| `Get-ScheduledTask` | schtasks.exe |
| `Get-ChildItem` | dir (part of cmd.exe) | 
| `Write-Output` | echo |

---


> ## **Nuances with PowerShell**

**A not all-encompassing list of some nuances with PowerShell:**
- Escape character is the backtick character (`) shift + tilde
- Double quotes allow variable expansion, single quotes will not
- You can run native commands in a PowerShell window, but be aware that PowerShell metacharacters ($, &, %, ?, etc) may behave differently than they did in the Windows Command Intrepreter
- Check aliases…running dir in PowerShell runs Get-ChildItem…not dir
- PowerShell will NOT run scripts by default. To enable the execution of scripts in a training environment, perform the following
    - Set-ExecutionPolicy –ExecutionPolicy Bypass
- For additional information on what the execution policies are:
    - Get-Help about_Execution_Policies