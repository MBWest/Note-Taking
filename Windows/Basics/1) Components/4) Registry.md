# Windows Registry

## **Registry Definition**
> ### **Definition:** a central hierarchical database that stores necessary configuration information for the system to run
- Contains information that Windows continually references during operation

---
---
---

## **Registry Structure**

> ### **2 Root Keys**
- HKEY_LOCAL_MACHINE
    - Configuration Information for the operating system
- HKEY_USERS
    - User profile information

> ### **3 Linked Keys**
- HKEY_CLASSES_ROOT
    - Shortcut to: `HKLM\SOFTWARE\Classes`
- HKEY_CURRENT_USER
    - Shortcut to: `HKU\SID`
- HKEY_CURRENT_CONFIG
    - Shortcut to: `HKLM\SYSTEM\CurrentControlSet\HardwareProfiles\Current`

> ### **Structure of the Registry**
- `Keys` - Comparable to Folders in the File System
- `Values` - Comparable to Files in the File System
    - **6 different “Types,” similar to file extensions in the file system**
        - Binary: `REG_BINARY `
            - binary data
        - String: `REG_SZ `
            - null-terminated string
        - Multi String: `REG_MULTI_SZ `
            - sequence of null-terminated strings
        - Expandable String: `REG_EXPAND_SZ `
            - can use environment variables
        - Double Word: `REG_DWORD`
            - 32 Bit Number
        - Quadruple Word: `REG_QWORD`
            - 64 Bit Number

---
---
---

## **SID**

> ### **SID**
- `Unique` value of variable length that is used to identify a security principal 
- SIDs that identify generic users or groups (ie: `Administrators`) are called “well known SIDs” – their values are static
- `Example:` HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileListGUID 
    - This location shows user accounts with active profiles

> ### **SID Domain Identifier**
- Unique to the Domain the SID was created in. No other domain in the enterprise has this value.

> ### **SID Relative ID**
- Unique to the user, group, or computer account the SID was generated for. No other account or group in the domain has a SID with the same RID.

```Text
S-1-5-21-0123456789-0123456789-0123456789-500
  | | |                                 |  |
  | | |---------Domain ID---------------|  |
  | |                                      |
  | ID Authority                       Relative ID
  |
Version
```

---
---
---

## **GUID**

> ### **GUID**
- 128 bit number used to identify information in computer systems
- Commonly used to identify `hardware` and `software` versions
- Example - installed software, listed by GUID:
    - HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

---
---
---

## **Practical Examples**

> ### **Run Software when a user logs in:**
- `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
    - System location – any user logging in will run
- `HKU\Software\Microsoft\Windows\CurrentVersion\Run`
    - Only the specific user will run
- Values can be named anything, data is an absolute file-path
    - If the file-path exists and is executable, the program will be executed - with the permissions of the user
- Used legitimately by commercial software
- Commonly used by malware for persistence
    - Use the `Autoruns` utility from `SysInternals` to find software that is set to start from this location

> ### **Make the Windows Command Interpreter autorun a command when you start cmd.exe:**
- `HKLM\Software\Microsoft\Command Processor`
    - **Value:** AutoRun
    - **Data:** command (that exists in the PATH variable) or filepath to a program
- `Use cases:`
    - You have a command(s) you want to run whenever you launch cmd.exe
        - Create the REG_SZ value AutoRun with the data “wmic qfe list”
            - When you launch cmd.exe – you’ll be presented with a list of installed - hotfixes
    - You want to create a denial of service
        - Create the REG_SZ value AutoRun with the data exit
            - When you launch cmd.exe – it immediately closes
        - Create the REG_SZ value AutoRun with the data cmd
            - When you launch cmd.exe – it will launch cmd.exe, which will launch cmd.exe, which will launch cmd.exe…

> ### **Remote Desktop Configuration**
- Remote Desktop Protocol (RDP) normally enabled in Enterprise Environments for remote management purposes
- `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server`
    - **Value:** fDenyTSConnections
    - **Data:**
        - 0 = RDP Enabled
        - 1 = RDP Disabled
- `Use case`
    - You’re a member of a security team, and want to enable/disable RDP for a legitimate reason
    - You’re a malicious person and want to create a Denial of Service, so you turn off RDP on machines

> ### **Modify Services through the registry**
- Registry location for all installed services:
    - `HKLM\SYSTEM\CurrentControlSet\Services`
- Browse to the location and modify/create your own service
- Caveat…the binary must know how to communicate with the services controller, otherwise it will be terminated shortly after execution

> ### **Exclusion location for Windows Defender**
- `HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths`
    - **Value:** Absolute Filepath to a folder
    - **Data:** REG_DWORD 0x0
- `Use Case`
    - Create a folder that you want to store malicious software in
    - Add the folder as a value name in the above key
    - Windows Defender will no longer perform any actions on directory contents
    - Multiple Antivirus solutions offer similar solutions


---
---
---
## **Hex**
- Uses 16 characters `(0-9, A-F)`
- Used in many languages and operating systems for data storage
