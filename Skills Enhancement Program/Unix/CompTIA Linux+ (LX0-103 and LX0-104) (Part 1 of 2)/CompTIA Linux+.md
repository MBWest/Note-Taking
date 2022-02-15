# CompTIA Linux+ (LX0-103 and LX0-104) 

## Processes

### Program vs. Process
- **Program** - Is an executable file on the disk
    - **Process** - Is an instance of that program

### User and System Processes
- They dont actuall run simultaneously
- The OS split time between each process and the CPU

## Process IDs

- **PID** (Process ID)
    - *Kernel* PID 0
- **PPID** (Parent Process ID)
    - init.d PID 1, PPID 0 
- **Process Tree**
    - Stars at PID 0

## Kernel Module
- Loaded on demand
    - Become part of the kernel once loaded

**Module commands**
- **insmod** - Insert a module into the kernel
- **rmmod** - Remove a module from the kernel
- **lsmod** - List the currently loaded modules
- **modinfo** - Display information about a module
- **modprobe** - Insert or remove a module from the kernel. Unlike insmod, modprobe automatically handles module dependencies. Dependent modules will be automatically loaded or unloaded with modprobe **-a**
    - *Example* > modpro [options] modulename params
    Option
    - **c** - Show configuration file
    - **l** - List modules
    - **r** - Remove modules

## File Sharing and Printing

### Network File System
- Remote access to file system
- Supported by Linux, UNIX, Windows
- Packages
- Name Resolution

### NFS Server Configuration
- **/etc/exports/** - Which file systems are exported, permissions and which host may mount them
- **/etc/host.allow** - Which hosts are permitted to mount exported file systems
- **/etc/host.deny** - Which host are explicity denied permissions to mount exported file systems

#### Mounting
Mount an NFS file system to access it
     - *Example* > mount -t nfs computer:fs /mount_point