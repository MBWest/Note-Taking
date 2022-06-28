# Windows Registry

## Registry Definition
> **Definition:** a central hierarchical database that stores necessary configuration information for the system to run
- Contains information that Windows continually references during operation

---
---
---
## Registry Structure

> **2 Root Keys**
- HKEY_LOCAL_MACHINE
    - Configuration Information for the operating system
- HKEY_USERS
    - User profile information

> **3 Linked Keys**
- HKEY_CLASSES_ROOT
    - Shortcut to: `HKLM\SOFTWARE\Classes`
- HKEY_CURRENT_USER
    - Shortcut to: `HKU\SID`
- HKEY_CURRENT_CONFIG
    - Shortcut to: `HKLM\SYSTEM\CurrentControlSet\HardwareProfiles\Current`