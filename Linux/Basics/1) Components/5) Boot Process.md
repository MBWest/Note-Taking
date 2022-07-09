# Linux Components - Boot Process

> ## **BIOS Tasks**
- Power-On Self-Test (POST)
- Initial hardware setup and configuration
- Appropriate boot device is selected and the boot loader is executed

> ## **Grand Unified Bootloader (GRUB) Stage 1**
- Small machine code located on the Master Boot Record (MBR)
- Sole purpose is to locate and load the second stage of the boot loader into memory

> ## **GRUB Stage 2**
- Kernel selection menu is presented
- Loads initial RAM disk into memory
    - Known as `initrd`
    - Mounted as the root filesystem until the real root filesystem is available
    - Used by the kernel to load drivers required to complete boot
- Loads kernel from the disk into memory

> ## **Linux Kernel**
- Initializes and configures memory and hardware
- Mounts initrd and uses it to load necessary drivers and kernel modules
- Mounts root filesystem
- Executes `/sbin/init `
```
BIOS→GRUB¹→GRUB²→Kernel
```
---
> ## **Startup Files**

| **File**   | **Description**   |
| --------------|-------------------|
| **Login Sessions** |
| `/etc/profile` | Global config for all users. |
| `~/.bash_profile` | user's personal config file. |
| `~/.bash_login` | read if bash_profile isn't found. |
| `~/.profile` | used if previous two aren't found. |
| **Non-login Session (ypical session when you launch the terminal via the GUI)** |
| `etc/bash.bashrc` | Global config for all users. |
| `~/.bashrc` | Specific settings for each user. This is where you can define your own settings and configurations. |

---
---

> ## **Resources**
`Bash manual chapter on startup files` -  https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html 

