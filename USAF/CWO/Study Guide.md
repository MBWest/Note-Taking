# Study Guide

## **Kernel**

      Low level operations that are fast and simple

## **Processor**

      User Mode *-* Unprivileged/Restricted/Isolated/Private space 

Kernel Mode - Shares Space/Privileged/Unrestricted 

## **Drivers**

     Enable communication

## **Driver** Types

      User Mode - Interface Win32 app & kernel mode drivers

Kernel Mode - Interface with I/O, PnP memory, process

## **Driver Levels (Totem Pole)**

      Highest Level - LL Dependent [NTFS, FAT, CDFS]

Intermediate Level - LL Dependent [Function Drivers, Filter Drivers, Software Bus Drivers]

*Function Driver* - Handles R/Ws & Device Power Policy (A function driver is the main driver for a device)

*Filter Driver* - Optional Component providing additional function and communicates with other drivers 

Upper level filter drivers sit above the primary driver for the device (the function driver), while lower level filter drivers sit below the function driver and above the bus driver.

*Software Bus Driver* - Provides an interface for higher-level drivers to attach to a set of child devices

Lowest Level - Not LL Dependent, Control I/O bus at HW level [AGP/PCI HW bus Drivers]

## Driver Categories

     Software - Gain access to data accessible only to the kernel and is not associated with a hardware device (Runs in kernel mode)

Bus - Provides communication to the several devices sharing a bus, ex. PCI or USB bus (Runs in kernel mode)

Device - Drivers necessary for the OS to communicate with an attached device (Run in User OR Kernel mode)

## Boot Process

     BIOS Phase 

- UEFI (new BIOS) performs POST (**P**ower **O**n **S**elf **T**est aka Hardware Checks)
- Master Boot Record (MBR) is read in (Identifies where the system partition is, used to start the OS)
- Searches and runs the "Bootmgr" file

Boot Loader Phase

**Note**: The Boot Manager and Boot Loader work together to load the Kernel into memory

- Launches Window Boot Manager
    - Reads the BCD (Loaded into HKLM\BCD00000000)
- Launches Windows Boot Loader
    - Finds and starts the Winloader (Winload.exe)

Kernel Phase

- Loads registry and drivers marked as “BOOT_START”
- Launches the Session Manager (smss.exe)
    - User session processes launched
- Launch Services
    - Winlogon.exe (logon screen)
    - After login, session created for the user

## File System

      A file system is implemented by the OS designed to store and retrieve data when necessary.

## File Allocation Table (FAT)

- Does not support file compression or security features (i.e. encryption)
- FAT couldn’t support large amounts
    - **FAT16** – Support up to 16GB; handles max file size of 2GB
    - **FAT32** – Support up to 16TB; handles max file size of 4GB
    - **exFAT** – Intended for portable media storage allowing max storage size of 512TiB – 64ZiB; handles approximately 128 PiB

## New Technology File System (NTFS)

- Support hard drives up to just under 16EB with a max volume size of 256TB.
- Encrypting File System (EFS) – providing file/folder encryption.
- User and Group permissions on files/folders
- Uses a change log which logs system changes before the changes are made; therefore, allowing a revert to functioning condition.
- Volume Shadow Copy Service (VSS) – backs up files currently on the system.
- If sectors become corrupt, they are dynamically remapped so the system does not utilize them.

## NTFS Permissions

- Applied to every file and folder stored on an NTFS-formatted volume.
- Can be inherited from a root folder to the files and subfolders beneath.

Basic Permissions

- Read
- Read and Execute
- Write, Modify
- List Folder Contents
- Full Control
- Advanced Permissions: available for more granular control

Share Permissions

- Less granular than NTFS permissions
    - Full Control
    - Change
    - Read
- Only applies to files on a network share

## NTFS – Determining a user’s level of access to something

### **If a file is accessed locally**

      Only the NTFS permissions are used.

### If a file is accessed remotely

      NTFS and share permissions are both used. The most restrictive permission applies first.

### User permissions are cumulative with the group permissions that they are a member of.

      Inherited Permissions

     Inherited from a parent folder

Explicit Permissions

Assigned directly to a file/folder & Takes precedence over inherited permissions.

## Explicit Deny > Explicit Allow > Inherited Deny > Inherited Allow

## Copying within a NTFS partition

      Creates a new file which inherits permissions of target folder

### Moving across a NTFS partition

      Creates a new file and deletes the old one and Inherits the target folders permissions

### Moving within a NTFS partition

      Doesn't create a new file, updates location in directory and file keeps its original permissions

### Moving from NTFS partition to FAT partition

- Does not retain their attributes or security descriptors
- Does retain their long file names

## Registry

- A central hierarchical database that stores necessary configuration information for the system to run
- Contains information that Windows continually references during operation

## Registry Structure

      Root Keys

     **HKEY_LOCAL_MACHINE -** Configuration Information for the operating system

**HKEY_USERS -** User profile information

Linked Keys

**HKEY_CLASSES_ROOT -** Shortcut to: HKLM\SOFTWARE\Classes

**HKEY_CURRENT_USER -** Shortcut to: HKU\SID

**HKEY_CURRENT_CONFIG -** Shortcut to: HKLM\SYSTEM\CurrentControlSet\HardwareProfiles\Current

## Structure of the Registry

      **Keys**

      Comparable to Folders in the File System

**Values**

Comparable to Files in the File System

### 6 different “Types,” similar to file extensions in the file system

**Note**: **The Data** – Content determined by the value’s type

      **Binary**

     **REG_BINARY -** binary data (Think Binary for Binary)

**String**

**REG_SZ -** null-terminated string (Think String that endZ for SZ)

**Multi String**

**REG_MULTI_SZ -** sequence of null-terminated strings (Think Multiple Strings that endZ for Multi SZ)

**Expandable String**

**REG_EXPAND_SZ -** can use environment variables (Think Expandable StringZ for Expand SZ)

**Double Word**

**REG_DWORD -** 32 Bit Number (Think D for Double Word)

**Quadruple Word**

**REG_QWORD -** 64 Bit Number (Think Q for Quadruple Word)

## SID

- Unique value of variable length that is used to identify a security principal
- SIDs that identify generic users or groups (*ie: Administrators*) are called “well known SIDs” – their values are static
    
    ### **Domain Identifier**
    
    - Unique to the Domain the SID was created in. No other domain in the enterprise has this value.
    
    ### **Relative ID (RID)**
    
    - Unique to the user, group, or computer account the SID was generated for. No other account or group in the domain has a SID with the same RID.

## GUID

- 128 bit number used to identify information in computer systems
- Commonly used to identify hardware and software versions
- Example - installed software, listed by GUID:
    - HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
- Software GUIDs can be evaluated to determine if specific software versions are installed

## Hex

- Uses 16 characters (*0-9, A-F*)
- Used in many languages and operating systems for data storage

# Practical Examples

## Run Software when a user logs in

- **HKLM\Software\Microsoft\Windows\CurrentVersion\Run**
    - System location – any user logging in will run
- **HKU\Software\Microsoft\Windows\CurrentVersion\Run**
    - Only the specific user will run
- Values can be named anything, data is an absolute file-path
    - If the file-path exists and is executable, the program will be executed with the permissions of the user
- Used legitimately by commercial software
- Commonly used by malware for persistence
    - Use the Autoruns utility from SysInternals to find software that is set to start from this location

## 1. Make the Windows Command Interpreter autorun a command when you start cmd.exe

- HKLM\Software\Microsoft\Command Processor
    - Value: AutoRun
    - Data: command *(that exists in the PATH variable)* or filepath to a program
- Use case
    - You have a command(s) you want to run whenever you launch cmd.exe
        - Create the REG_SZ value AutoRun with the data “wmic qfe list”
            - When you launch cmd.exe – you’ll be presented with a list of installed hotfixes
    - You want to create a denial of service
        - Create the REG_SZ value AutoRun with the data exit
            - When you launch cmd.exe – it immediately closes
        - Create the REG_SZ value AutoRun with the data cmd
            - When you launch cmd.exe – it will launch cmd.exe, which will launch cmd.exe, which will launch cmd.exe…

## 2. Remote Desktop Configuration

- Remote Desktop Protocol (RDP) normally enabled in Enterprise Environments for remote management purposes
- HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server
    - Value: fDenyTSConnections
        - Data:
            - 0 = RDP Enabled
            - 1 = RDP Disabled

### **Use case:**

- You’re a member of a security team, and want to enable/disable RDP for a legitimate reason
- You’re a malicious person and want to create a Denial of Service, so you turn off RDP on machines

## 3. Modify Services through the registry

- Registry location for all installed services:
    - HKLM\SYSTEM\CurrentControlSet\Services
- Browse to the location and modify/create your own service
- Caveat…the binary must know how to communicate with the services controller, otherwise it will be terminated shortly after execution

## 4. Pending File Rename Operations

- Long name meaning “Delete or move files on reboot”
- HKLM\SYSTEM\CurrentControlSet\Control\Session Manager
    - Value: PendingFileRenameOperations
    - Data: Absolute File Paths for the moving/deleting of certain files
- The registry value is cleared after reboot as well

### Use Case:

- You want to delete a file that can’t be removed while the system is running
- You want to delete system files on reboot to brick your system
- You want malware to reboot a system and remove itself to cover your tracks

The SysInternals tools movefile and pendmoves simplify this process

## 5. Exclusion location for Windows Defender

- HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths
    - Value: Absolute Filepath to a folder
    - Data: REG_DWORD 0x0

### Use Case

- Create a folder that you want to store malicious software in
- Add the folder as a value name in the above key
- Windows Defender will no longer perform any actions on directory contents
- Multiple Antivirus solutions offer similar solutions