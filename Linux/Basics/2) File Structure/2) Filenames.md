# Linux File Structure - Filenames

- Letters, numbers, and certain punctuation allowed
- Avoid special characters
    - ``? , ( ) | { } [ ] ~ `` etc… 
    - These characters have special meaning to the shell
- Keep filenames simple 
- If special characters and spaces are used, they must be accounted for
    - Escape them with a backslash (\)
    - Use quotes 

---

> ## **File System**

### **Spaces in Paths and Filenames**

- Spaces in filenames and Paths can cause problems when trying to open files or folders. Use a `\` in front of the space to have the system treat the space as part of the arguement. 
- **cat file\ name.txt** Opens the 'file name.txt' file
    - The alternative is to place the entire name in quotes ("file name.txt")

**Official Filesystem Hierarchy Standard:** https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html

### **Soft Links (see ln.md)**

- Can cross the file systems
- Allows you to link between directories
- Has different inodes number and file permissions than original file
- Permissions will not be updated

### **Hard Links (see ln.md)**

- Cant cross the file system
- Cant link directories
- Has the same inodes number and permissiosn of original file
- Permissions will be updated if we change the permissions of source file

### **Descriptions**

| **Directory**   | **Description**   |
| --------------|-------------------|
| `man hier` | Description of the filsystem hierarchy |
| `/boot` | Holds important files during boot-up process, including Linux Kernel  |
| `/root` | This is the home directory of root user and should never be confused with ‘/‘ |
| `/dev` | Contains device files for all the hardware devices on the machine e.g., cdrom, cpu, etc |
| `/etc` | Contains Application’s configuration files, startup, shutdown, start, stop script for every individual program |
| `/bin -> /usr/bin` | All the executable binary programs (file) required during booting, repairing, files required to run into single-user-mode, and other important, basic commands viz., cat, du, df, tar, rpm, wc, history, etc  |
| `/sbin -> /user/sbin` | Contains binary executable programs, required by System Administrator, for Maintenance. Viz., iptables, fdisk, ifconfig, swapon, reboot, etc. |
| `/opt` | Optional is abbreviated as opt. Contains third party application software. Viz., Java, etc. |
| `/proc` | A virtual and pseudo file-system which contains information about running process with a particular Process-id aka pid |
| `/lib -> /usr/lib` | The Lib directory contains kernel modules and shared library images required to boot the system and run commands in root file system |
| `/tmp` | System’s Temporary Directory, Accessible by users and root. Stores temporary files for user and system, till next boot |
| `/home` | Home directory of the users. Every time a new user is created, a directory in the name of user is created within home directory which contains other directories like Desktop, Downloads, Documents, etc. |
| `/var` | Stands for variable. The contents of this file is expected to grow. This directory contains log, lock, spool, mail and temp files |
| `/run` | System daemons that start very early to store temporary runtime files like PID files |
| `/mnt` | Temporary mount directory for mounting file system |
| `/media` | Temporary mount directory is created for removable devices viz., media/cdrom. |
| `/lost+found` | This Directory is installed during installation of Linux, useful for recovering files which may be broken due to unexpected shut-down |
| `/run` | This directory is the only clean solution for early-runtime-dir problem |
| `/srv` | Service is abbreviated as ‘srv‘. This directory contains server specific and service related files |
| `/sys` | Modern Linux distributions include a /sys directory as a virtual filesystem, which stores and allows modification of the devices connected to the system |
| `/usr` | Contains executable binaries, documentation, source code, libraries for second level program  |

**Linux is a complex system which requires a more complex and efficient way to start, stop, maintain and reboot a system unlike Windows. There is a well defined configuration files, binaries, man pages, info files, etc. for every process in Linux.** (https://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/)


| **Directory**   | **Description**   |
| --------------|-------------------|
| `/boot/vmlinuz` | The Linux Kernel file |
| `/dev/hda` | Device file for the first IDE HDD (Hard Disk Drive) |
| `/dev/hdc` | Device file for the IDE Cdrom, commonly |
| `/dev/null` | A pseudo device, that don’t exist. Sometime garbage output is redirected to /dev/null, so that it gets lost, forever |
| `/etc/bashrc` | Contains system defaults and aliases used by bash shell |
| `/etc/crontab` | A shell script to run specified commands on a predefined time Interval |
| `/etc/exports` | Information of the file system available on network |
| `/etc/fstab` | Information of Disk Drive and their mount point |
| `/etc/group` | Information of Security Group |
| `/etc/grub.conf` | grub bootloader configuration file |
| `/etc/init.d` | Service startup Script |
| `/etc/lilo.conf` | lilo bootloader configuration file |
| `/etc/hosts` | Information of Ip addresses and corresponding host names |
| `/etc/hosts.allow` | List of hosts allowed to access services on the local machine |
| `/etc/host.deny` | List of hosts denied to access services on the local machine |
| `/etc/inittab` | INIT process and their interaction at various run level |
| `/etc/issue` | Allows to edit the pre-login message |
| `/etc/modules.conf` | Configuration files for system modules |
| `/etc/motd` | motd stands for Message Of The Day, The Message users gets upon login |
| `/etc/mtab` | Currently mounted blocks information |
| `/etc/passwd` | Contains password of system users in a shadow file, a security implementation |
| `/etc/printcap` | Printer Information |
| `/etc/profile` | Bash shell defaults |
| `/etc/profile.d` | Application script, executed after login |
| `/etc/rc.d` | Information about run level specific script |
| `/etc/rc.d/init.d` | Run Level Initialisation Script |
| `/etc/resolv.conf` | Domain Name Servers (DNS) being used by System |
| `/etc/securetty` | Terminal List, where root login is possible |
| `/etc/skel` | Script that populates new user home directory |
| `/etc/termcap` | An ASCII file that defines the behaviour of Terminal, console and printers |
| `/etc/X11` | Configuration files of X-window System |
| `/usr/bin` | Normal user executable commands |
| `/usr/bin/X11` | Binaries of X windows System |
| `/usr/include` | Contains include files used by ‘c‘ program |
| `/usr/share` | Shared directories of man files, info files, etc |
| `/usr/lib` | Library files which are required during program compilation |
| `/usr/sbin` | Commands for Super User, for System Administration |
| `/proc/cpuinfo` | CPU Information |
| `/proc/filesystems` | File-system Information being used currently |
| `/proc/interrupts` | Information about the current interrupts being utilised currently |
| `/proc/ioports` | Contains all the Input/Output addresses used by devices on the server |
| `/proc/meminfo` | Memory Usages Information |
| `/proc/modules` | Currently using kernel module |
| `/proc/mount` | Mounted File-system Information |
| `/proc/stat` | Detailed Statistics of the current System |
| `/proc/swaps` | Swap File Information |
| `/version` | Linux Version Information |
| `/var/log/lastlog` | log of last boot process |
| `/var/log/messages` | log of messages produced by syslog daemon at boot |
| `/var/log/wtmp` | list login time and duration of each user on the system currently |


