# The Linux Boot Process

| **Info**   | **Description** |
| --------------|--------------|
| `Basic Input/Output System (BIOS)` | Special firmware; Operating System independent |
| `Primary Purpose` | Perfroms the POST (Power-On Self Test); Knows about bootables devices; The boot device order can be changed |

## Boot loaders

Boot Loader start the operating system

| **Info**   | **Description** |
| --------------|--------------|
| **Boot Loaders** |
| `LILO` | Linux Loader |
| `GRUB` | Grand Unified Bootloader; Replaced LILO |

## Initial RAM Disk (initrd)

- Temporary filesystem that is loaded from dish and stored in memory
- Contains helpers and modules (drivers) required to load the permanent OS file system

## The /boot Directory

- Contains the files required to boot Linux
- initrd
- kernel
- Boot loader configuration

## Kernel Ring Buffer

- A **Ring Buffer** is a data structure that is always the same size
- Contains messages from the Linux Kernel
- **dmesg** - To see the contents of the ring buffer
- Stored in /var/log/dmesg

## Run Level

| **Run Level**   | **Description** |
| --------------|--------------|
| `0`  | Shuts down the system |
| `1, S, s`  | Single user mode; Used for maintenance |
| `2`  | Multi-user mode with graphical interface (Debian/Ubuntu) |
| `3`  | Multi-user text mode (RedHat/CentOS) |
| `4`  | Undefined |
| `5`  | Multi-user mode with graphical interface (RedHat/CentOS) |
| `6`  | Reboot |

## init

- **telinit RUNLEVEL** - Changes run level 
    - *Example* > telinit 5
        - Changes to the graphical interface

## Systemd

- Replacing init
- Uses targets instead of run levels
    - To see list of targets look in /lib/systemd/system
- **systemctl isolate TARGET**
    - *Example* > system isolate graphical.target
        - Changes to the graphical interface