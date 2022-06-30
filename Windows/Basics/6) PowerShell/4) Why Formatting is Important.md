# PowerShell - Why Formatting is Important

## **Formating**

- PowerShell returns objects, each with their own properties
- The number of properties displayed can change depending on formatting
    - Under the hood, if you do not define how to format output, PowerShell will send everything to `Out-Default`
        - For reference, the following files define what this formatting will look like – we will not be covering them
            - C:\windows\systems32\windowspowershell\v1.0\DotNetTypes.format.ps1xml
            - C:\windows\systems32\windowspowershell\v1.0\Types.ps1xml
- If you want to see all properties in your output, provide formatting at the very end of your command

> ### **No Specified Formatting**

- Process objects default to a table, and 8 properties are shown

```PowerShell
C:\Users\Matthew> Get-Process cmd

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
     70       6     5192       5128       0.02  19252   7 cmd
```

> ### **Format as a List**

- Process objects display 5 properties

```PowerShell
C:\Users\Matthew> Get-Process cmd | Format-List


Id      : 19252
Handles : 70
CPU     : 0.015625
SI      : 7
Name    : cmd
```

- If you want to see all properties, use `Format-List -Property *`
    - Can be shortened to `Format-List *`, or use the alias `fl *`
    - Generally, `Format-List *` is a quick way to see everything in an object
- If multiple objects are returned, all properties for each will be shown, which can quickly clutter your output

```PowerShell
PS C:\Users\Matthew> Get-Process cmd | fl *


Name                       : cmd
Id                         : 19252
PriorityClass              : Normal
FileVersion                : 10.0.22000.1 (WinBuild.160101.0800)
HandleCount                : 70
WorkingSet                 : 5234688
PagedMemorySize            : 3215360
PrivateMemorySize          : 3215360
VirtualMemorySize          : 61833216
TotalProcessorTime         : 00:00:00.0156250
SI                         : 7
Handles                    : 70
VM                         : 2203380056064
WS                         : 5234688
PM                         : 3215360
NPM                        : 6288
Path                       : C:\WINDOWS\system32\cmd.exe
Company                    : Microsoft Corporation
CPU                        : 0.015625
ProductVersion             : 10.0.22000.1
Description                : Windows Command Processor
Product                    : Microsoft® Windows® Operating System
__NounName                 : Process
BasePriority               : 8
ExitCode                   :
HasExited                  : False
ExitTime                   :
Handle                     : 3008
SafeHandle                 : Microsoft.Win32.SafeHandles.SafeProcessHandle
MachineName                : .
MainWindowHandle           : 0
MainWindowTitle            :
MainModule                 : System.Diagnostics.ProcessModule (cmd.exe)
MaxWorkingSet              : 1413120
MinWorkingSet              : 204800
Modules                    : {System.Diagnostics.ProcessModule (cmd.exe), System.Diagnostics.ProcessModule
                             (ntdll.dll), System.Diagnostics.ProcessModule (KERNEL32.DLL),
                             System.Diagnostics.ProcessModule (KERNELBASE.dll)...}
NonpagedSystemMemorySize   : 6288
NonpagedSystemMemorySize64 : 6288
PagedMemorySize64          : 3215360
PagedSystemMemorySize      : 46856
PagedSystemMemorySize64    : 46856
PeakPagedMemorySize        : 5316608
PeakPagedMemorySize64      : 5316608
PeakWorkingSet             : 5251072
PeakWorkingSet64           : 5251072
PeakVirtualMemorySize      : 63930368
PeakVirtualMemorySize64    : 2203382153216
PriorityBoostEnabled       : True
PrivateMemorySize64        : 3215360
PrivilegedProcessorTime    : 00:00:00
ProcessName                : cmd
ProcessorAffinity          : 255
Responding                 : True
SessionId                  : 7
StartInfo                  : System.Diagnostics.ProcessStartInfo
StartTime                  : 6/29/2022 3:48:30 PM
SynchronizingObject        :
Threads                    : {824, 12928}
UserProcessorTime          : 00:00:00.0156250
VirtualMemorySize64        : 2203380056064
EnableRaisingEvents        : False
StandardInput              :
StandardOutput             :
StandardError              :
WorkingSet64               : 5234688
Site                       :
Container                  :
```

> ### **Final note on formatting...**

- Always format last – do not try to filter or manipulate objects after they’ve been formatted
- Formatting is for viewing and presenting the data, so take advantage of it
- Get used to using Format-List * to see all the properties of an object when first using PowerShell – it helps you learn what properties exist and what their values look like