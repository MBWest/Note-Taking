# Kernel

- The Linux Kernel is a result of collaborative development efforts from developers accross the globe.
- Small incremental changes, also known as patches add:
    - New features
    - Make enhancements
    - Fix bugs
- A new release of Linux kernel happens every 2 to 3 months. 
    - Realeases are time based rather than feature based

# Kernel Module
- Loaded on demand
    - Become part of the kernel once loaded

| **Command**   | **Description**   |
| --------------|-------------------|
| **Module Commands** |
| `insmod` | Insert a module into the kernel |
| `rmmod` | Remove a module from the kernel |
| `lsmod` | List the currently loaded modules |
| `modinfo` | Display information about a module |
| `modprobe` |  Insert or remove a module from the kernel. Unlike insmod, modprobe automatically handles module dependencies. |
| **Options** ||
| `-c` | Show configuration file |
| `-l` | List modules |
| `-r` | Remove modules |
| `-a` | Dependent modules will be automatically loaded or unloaded with modprobe  |