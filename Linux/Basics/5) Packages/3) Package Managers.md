# Linux Packages - Package Managers

- Tool that downloads, installs, updates, and uninstalls packages
    - Downloads and updates are pulled from a repository
- Manages dependencies
    - Knows not to delete shared dependencies
- Package documentation location 
    - /usr/share/doc

---

> ## **YUM**

- Package manager based on RPM
- Query for information about available packages
- Fetch packages from repositories
- Install and uninstall packages
- Update an entire system to the latest available version
- provides secure package management by enabling GPG(GNU Privacy Guard)
- yum’s configuration file is /etc/yum.conf

> ## **yum [options] [command] [package ...]**
- `install` – Install the latest version of a package
- `update` – Updates currently installed packages
- `search` – Searches for a package with the given pattern
- `repolist` – Produces a list of configured repositories
- `info` – list information about available packages

```
[root@CentOS ~]# yum install httpd
```
---

> ## **Package Route**
```text
|-----------------|
|      User       |
|     System      |
|                 |
|-----------------|
        |
        |
|-----------------|
|    Package      |
|    Manager      |
|                 |
|-----------------|
        |
        |
|-----------------|   |-----------------|
|   Repository    |   |       Meta      |
|                 |---|       Data      |
|                 |   |                 |
|-----------------|   |-----------------|
        |              /
        |             /
|-----------------|  /
|    Packages     | /
|                 |/
|                 |
|-----------------|
        |
        |
|-----------------|
|    Package      |
|  Dependancies   |
|                 |
|-----------------|
```