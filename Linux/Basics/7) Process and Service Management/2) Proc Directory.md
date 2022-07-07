# Linux Process and Service Management - Proc Directory

- Pseudo-filesystem
- Contains information about all currently running processes
- Provides an interface to kernel data structures
- Most of it is read-only, but some files allow kernel variables to be changed
- Created every time a system is booted and disappears every time a system is shutdown

## **/proc Structure**
- /proc/PID (Process ID or PID can be any running process)
- Files/folders that provide information about the process
    - `cmdline` - command and arguments used to invoke the process
    - `environ` - environment variables 
    - `cwd` - link to current working directory of the process
    - `exe` - link to the executable of the process
    - `stat` - status information about the process
    - `fd` - folder containing one entry for each file which the process has open, named by its file descriptor, which is a link to the actual file
- `/proc/cpuinfo` - CPU and system architecture items
- `/proc/meminfo` - memory and swap usage
- `/proc/cmdline` - options used to start the kernel
- `/proc/filesystems` - filesystems supported by the kernel
- `/proc/modules` - active kernel modules
- `/proc/mounts` - mounted devices
- `/proc/uptime` - system uptime (up:idle)
- `/proc/net` - network information
- `/proc/version` - kernel and linux version information

