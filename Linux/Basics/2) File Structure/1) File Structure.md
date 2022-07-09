# Linux File Structure

## **Directory Hierarchy**

> ## **Root Directory**
- / is the top of the directory structure
- User root has total control of the system (superuser)
- /root is the root user's home directory

---

> ## **Current Directory**
- Commonly called current working directory or cwd
- Parent/Child Directories

---

> ## **Parent directory is one level above the child directory**
- Child directory is one level below the parent directory
---

> ## **Directories**


| **Paths**   | **Description**   |
| --------------|-------------------|
| **Relative Path/Absolute Path** |
| `Relative Path` | Paths that specify a directory/file relative to the current directory |
| `Absolute Path` | Paths that specify a directory/files full path so it works in any directory |
| **Root Directory** |
| `/` | Starting point of the entire Directory, called the root directory (Top Level Directory); Not the actual folder with the name "root" |
| **Home Directory** |
| `/home` | Contains a home folder for each user on the system |
| `/home/west` | My home folder |
| `cd ~` | The home directory can be accessed using the 'tilde ~' key |

---
---

> ## **Home Directory**
- Each user has a unique home directory
- Default starting point for users
    - Can be referenced from the CLI with a tilde `~`
- Located in /home
    - Each folder in /home corresponds to a username
        - ex.  /home/student is the user student's home folder