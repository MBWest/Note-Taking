# Security - SysInternals

## **Basic Information**

- **Free suite of more than 70 Windows applications**
    - Developed in 1996 by Mark Russinovich and Bryce Cogswell
    - Purchased by Microsoft in 2006 after it identified XCP rootkit in Sony CDs
- **Used to monitor, manage, and troubleshoot Windows OS**
    - Most tools require Administrator access
- **Portable**
    - Can be put on USB
    - Can be run without downloading/installing from SysInternals Live
    - Available in the following location on your machines:
        - C:\SysInternalsSuite

---
---
---

## **Autoruns**

- Identifies auto startup, registry keys, scheduled tasks, and other auto executed components on PC boot.
- Hides everything that is built into Windows and set to auto start
    - Can enable, not recommended
- Should be run as Administrator for full functionality

### **Autorun Tabs**

- `Logon Tab` – Checks “normal” startup locations (Run, RunOnce, Start Menu, etc.)
- `Explorer Tab` – Add-on components that load themselves into Windows Explorer
- `Internet Explorer Tab` – List browser extensions, toolbars, browser helper objects
- `Scheduled Tasks Tab` – Shows scheduled tasks
- `Services Tab` – Shows services
- `Drivers Tab` – Shows device drivers
- `Codecs Tab` – Libraries of code for media playback/audio
- `Boot Execute Tab` – Items that start up during system boot
- `Image Hijack Tab` – Items that are not being executed under the image they are supposed to
- `AppInit` – Displays custom DLLs to be loaded into address space of interactive applications
- `KnownDLLs` – Displays verified Windows DLL files
- `Winlogon, Winsock Providers, Print Monitors, LSA Providers, Network Providers Tabs` – Contain add-ons that extend various aspects of Windows
- `Sidebar Gadgets` – Shows gadgets for Vista/Windows 7

---
---
---

## **Process Explorer**

- Task manager and system monitor application
    - Only supported by Windows XP and up
- Hierarchical tree view of processes
    - Displayed in Parent/Child relationship
- View complete data about any process, including threads, memory usage, handles, objects
- Kill an entire process tree, recursively
- Suspend a process, freezing all threads

---
---
---

## **TCP View**

- Graphical User Interface to see what applications are connecting to what services over the network
- Similar to netstat with additional functionality