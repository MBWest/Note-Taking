# Apt

- Copy files and set attributes
- Search for and install software packages (Debian/Ubuntu).
- apt is a subset of the most commonly used apt-get and apt-cache(8) commands, use apt-get for more the low-level package management options.

---

> ## **Syntax** 

- install [OPTION]... [-T] SOURCE DEST
- install [OPTION]... SOURCE... DIRECTORY
- install [OPTION]... -t DIRECTORY SOURCE...
- install [OPTION]... -d DIRECTORY...

---

> ## **Options** 


| **Apt Option**  | **Description**  | **Apt-Get Equivalent**  |
--------------|-------------------|--------------|
| `list` | list is used to display a list of packages. It supports shell pattern for matching package names and the following options: --installed, --upgradable, --all-versions are supported. |  |
|`search` |Search for the given term(s) and display matching packages. | `apt‑cache search` |
|`show` |Show the package information for the given package(s). |`apt-cache show` |
|`install` |  install is followed by one or more package names desired for installation or upgrading. A specific version of a package can be selected for installation by following the package name with an equals and the version of the package to select. This will cause that version to be located and selected for install. Alternatively a specific distribution can be selected by following the package name with a slash and the version of the distribution or the Archive name (stable, testing, unstable). | `apt-get install` |
|`remove` | remove is identical to install except that packages are removed instead of installed. Note that removing a package leaves its configuration files on the system. If a plus sign is appended to the package name (with no intervening space), the identified package will be installed instead of removed. | `apt-get remove` |
|`edit‑sources` | Edit the sources. list file and provides basic sanity checks. | |
|`update` | Resynchronize the package index files from their sources. | `apt-get update`  |
|`upgrade` | Install the newest versions of all packages currently installed on the system from the sources enumerated in etc/apt/sources.list. New packages will be installed, but existing packages will never be removed. | `apt-get upgrade` |
|`full‑upgrade` | Perform the function of upgrade but may also remove installed packages if that is required in order to resolve a package conflict. | `apt‑get dist‑upgrade` |

---
---

> ## **Example** 

| **Command**   | **Description**   |
| --------------|-------------------|
| `apt update` | Ensures the sysetm has the most up to date information. Should be ran with `sudo`. |
| `apt upgrade` | Installs new dependecies and programs. |
| `apt install pdftk` | Installs the PDF viewer tool (pdftk).  |
| `apt search pdftk` | Searches the repositories for the pdftk tool. |
| `apt show pdftk` | Check information about a packet before installing it. |
| `apt remove pdftk` | Removes the pdftk application, leaving the dependecies that were installed alongside it. |
| `apt purge pdftk` | Removes configuration files that were instealled alongside the tool. |
| `apt autoremove` | Removes dependencies that tools and applications left behind after uninstalling.  |

