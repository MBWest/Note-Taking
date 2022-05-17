# Objective 2a

**Identify relationships of basic facts and state general principles about components of the Windows Operating System.**

- **Components**
- **Boot Process**
- **File Structure**
- **Block Test:**
    - 15 Questions
    - Minimum passing score 70% (11/15)

---

## Windows Components

[Study Guide](Objective%20%20fa802/Study%20Guid%20902ce.md)

- Kernel
    
    ### Definition
    
    The heart of the operating system providing basic low-level operations (fast and simple) such as scheduling threads or routing hardware interrupts.
    
    ---
    
- Processor
    
    ## Runs in two modes
    
    ### **User Mode**
    
    - Unprivileged/Restricted
    - Has its own private virtual address space in memory
    - Isolates the app preventing alteration of:
        - Other application data
        - The OS itself
    
    ### **Kernel Mode**
    
    - Privileged/Unrestricted
    - Everything shares the same virtual address space
    - Possible to overwrite other programs and compromise the entire system (system crash)
    
    ---
    
- Drivers
    
    ## Definition
    
    Software component that enables communication between hardware and the OS
    
    - Can communicate directly with the hardware
    - Can communicate with lower-level drivers
    
    ## Driver Types
    
    **User Mode**
    
    Interface between a Win32 application and kernel-mode drivers or other OS components (not actual hardware).
    
    **Kernel Mode**
    
    Interface with I/O, Plug and play memory, process and thread management, security, etc..
    
    ## Driver Levels
    
    ### Highest-level
    
    - Always depend on lower level drivers for support
    - Examples include file system drivers for: NTFS, FAT, CDFS
    
    ## Intermediate-level
    
    - Always depend on lower level drivers for support
    - Divided into: Function, Filter, Software Bus Drivers
        
        ### **Function Drivers**
        
        - Handles reads/writes to the device
        - Manages device power policy
        
        ### Filter Drivers
        
        - Optional component, Provides additional functionality
        - Communicates with other filter drivers or function drivers
        
        ### Software Bus Drivers
        
        - Provides an interface for higher-level drivers to attach to a set of child devices
    
    ## Lowest-level
    
    - Control I/O bus in which the actual hardware device is connected
    - Does not depend on lower level drivers
    - Example:  AGP/PCI hardware bus drivers
    
    ## Driver Categories
    
    ### Software
    
    - Created to gain access to data accessible only to the kernel and is not associated with a hardware device
    - Always runs in kernel mode
    
    ### Bus
    
    - Provides communication to the several devices sharing a bus
    - Always runs in kernel mode
    - Example - peripheral component interconnect (PCI) bus, USB bus
    
    ### Device
    
    - Refers to drivers necessary for the OS to communicate with an attached device
    - Can run in User or Kernel mode
    
    ---
    
- Boot Process
    
    ## 1. BIOS Phase (Preboot)
    
    ### **The UEFI (Unified Extensible Firmware Interface) performs POST**
    
    - UEFI is essentially the new version of BIOS
    - POST (Power On Self Test) – Hardware checks
    
    ### **The Master Boot Record (MBR) is read in**
    
    - Identifies where the system partition is, this is used to start the OS
    
    ### **Searches and runs the “bootmgr” file**
    
    ## 2. Boot Loader Phase
    
    ### **Windows Boot Manager**
    
    - Launches Windows Boot Manager
    - Reads in the BCD
        - Is loaded into HKLM\BCD00000000
    
    ### Windows Boot Loader
    
    - Launches Windows Boot Loader
    - Finds and starts the Winloader (Winload.exe)
    
    **The Boot Manager and Boot Loader work together to load the Kernel into memory**
    
    ## 3. Kernel Phase
    
    - Loads registry and drivers marked as “BOOT_START”
    - Launches the Session Manager (smss.exe)
    - User session processes launched
    - Launch Services
    - Winlogon.exe (logon screen)
    - After login, session created for the user
- File Structure
    
    ## File System Definition
    
    - A file system is implemented by the OS designed to store and retrieve data when necessary.
    - Typically starting from a root drive and expanding out into a tree-like structure.
    
    ## File Allocation Table (FAT)
    
    - Initially developed for Windows systems
    - Still in use today with a variety of devices and older OS’s.
    - Does not support file compression or security features (i.e. encryption).
    - FAT couldn’t support large amounts
        - **FAT16** – Support up to 16GB; handles max file size of 2GB
        - **FAT32** – Support up to 16TB; handles max file size of 4GB
        - **exFAT** – Intended for portable media storage allowing max storage size of 512TiB – 64ZiB; handles approximately 128 PiB
    
    ## New Technology File System (NTFS)
    
    - Can support hard drives up to just under 16EB with a max volume size of 256TB.
    - Encrypting File System (EFS) – providing file/folder encryption.
    - User and Group permissions on files/folders
    - Uses a change log which logs system changes before the changes are made; therefore, allowing a revert to functioning condition.
    - Volume Shadow Copy Service (VSS) – backs up files currently on the system.
    - If sectors become corrupt, they are dynamically remapped so the system does not utilize them.
    
    ## NTFS Permissions
    
    - Applied to every file and folder stored on an NTFS-formatted volume.
    - Can be inherited from a root folder to the files and subfolders beneath.
    
    ### **Basic Permissions:**
    
    - Read
    - Read and Execute
    - Write, Modify
    - List Folder Contents
    - Full Control
    - Advanced Permissions: available for more granular control
    
    ### Share Permissions
    
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
    
    - Inherited Permissions: inherited from a parent folder
    - Explicit Permissions: assigned directly to a file/folder.
        - Takes precedence over inherited permissions.
    
    ### Explicit Deny > Explicit Allow > Inherited Deny > Inherited Allow
    
    ## Copy, Move, & Inheritance
    
    ### Copying within a NTFS partition
    
    - Creates a new file which inherits permissions of target folder
    
    ### Moving across a NTFS partition
    
    - Creates a new file and deletes the old one and Inherits the target folders permissions
    
    ### Moving within a NTFS partition
    
    - Does not create a new file, updates location in directory and file keeps its original permissions
    
    ### Moving from NTFS partition to FAT partition
    
    - Do not retain their attributes or security descriptors
    - Do retain their long file names
    
    ---
    
- Registry
    
    ## Definition
    
    - A central hierarchical database that stores necessary configuration information for the system to run
    - Contains information that Windows continually references during operation
    
    # Structure
    
    ## 2 Root Keys
    
    ### **HKEY_LOCAL_MACHINE**
    
    - Configuration Information for the operating system
    
    ### **HKEY_USERS**
    
    - User profile information
    
    ## 3 Linked Keys
    
    ### **HKEY_CLASSES_ROOT**
    
    - Shortcut to: HKLM\SOFTWARE\Classes
    
    ### **HKEY_CURRENT_USER**
    
    - Shortcut to: HKU\SID
    
    ### **HKEY_CURRENT_CONFIG**
    
    Shortcut to: HKLM\SYSTEM\CurrentControlSet\HardwareProfiles\Current
    
    ## Structure of the Registry
    
    - **Keys** - Comparable to Folders in the File System
    - **Values** - Comparable to Files in the File System
    
    ### 6 different “Types,” similar to file extensions in the file system
    
    **Binary: REG_BINARY**
    
    - binary data
    
    **String: REG_SZ**
    
    - null-terminated string
    
    **Multi String: REG_MULTI_SZ**
    
    - sequence of null-terminated strings
    
    **Expandable String: REG_EXPAND_SZ**
    
    - can use environment variables
    
    **Double Word: REG_DWORD**
    
    - 32 Bit Number
    
    **Quadruple Word: REG_QWORD**
    
    - 64 Bit Number
    
    **Data** – Content determined by the value’s type (*see above*)
    
    # Common items
    
    ## SID
    
    - Unique value of variable length that is used to identify a security principal
        
        ### **Domain Identifier**
        
        - Unique to the Domain the SID was created in. No other domain in the enterprise has this value.
        
        ![Objective%20%20fa802/Untitled.png](Objective%20%20fa802/Untitled.png)
        
        ### **Relative ID (RID)**
        
        - Unique to the user, group, or computer account the SID was generated for. No other account or group in the domain has a SID with the same RID.
    - SIDs that identify generic users or groups (*ie: Administrators*) are called “well known SIDs” – their values are static
    
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
    
    ### **Use case**
    
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