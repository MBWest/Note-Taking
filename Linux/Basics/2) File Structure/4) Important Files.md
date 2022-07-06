# Linux File Structure - Important Files

> ## **/etc/passwd**

The /etc/passwd file is a text file that describes user login accounts for the system

### **New Logins**

If you create a new login, first put an asterisk (*) in the password field, then use passwd(1) to set it.

### **/etc/passwd Fields**

Each line of the file describes a single user, and contains seven colon-separated fields:

        name:password:UID:GID:GECOS:directory:shell

        root:x:0:0:root:/root:/bin/bash
        student:x:500:500:Stu Dent:/home/student:/bin/bash
        guru:x:501:501:guru:/home/guru:/bin/bash


**The fields are as follows:** 

| **Field** | **Description** | 
|-----------|-----------------|
| `name` | This is the user's login name. It should not contain capital letters |
| `password` | This is either the encrypted user password, an asterisk (*), or the letter aqxaq. (See pwconv(8) for an explanation of aqxaq.) |
| `UID` | The privileged root login account (superuser) has the user ID 0. Normal user accounts start with 1000 |
| `GID` | This is the numeric primary group ID for this user. (Additional groups for the user are defined in the system group file; see group(5)) |
| `GECOS` | This field (sometimes called the "comment field") is optional and used only for informational purposes. Usually, it contains the full username. Some programs (for example, finger(1)) display information from this field. **GECOS stands for "General Electric Comprehensive Operating System",** which was renamed to GCOS when GE's large systems division was sold to Honeywell. Dennis Ritchie has reported: "Sometimes we sent printer output or batch jobs to the GCOS machine. The gcos field in the password file was a place to stash the information for the $IDENTcard. Not elegant." |
| `directory` | This is the user's home directory: the initial directory where the user is placed after logging in. The value in this field is used to set the HOME environment variable |
| `shell` | This is the program to run at login (if empty, use /bin/sh). If set to a nonexistent executable, the user will be unable to login through login(1). The value in this field is used to set the SHELL environment variable |

---
---

> ## **/etc/group**

- User group file - stores supplementary group information

### /etc/group Fields

The /etc/group file is a text file that defines the groups on the system. There is one entry per line, with the following format:

    group_name:password:GID:user_list

**The fields are as follows:**

| **Field** | **Description** | 
|-----------|-----------------|
| `group_name` | The name of the group |
| `password` | The (encrypted) group password. If this field is empty, no password is needed |
| `GID` | The numeric group ID |
| `user_list` | A list of the usernames that are members of this group, separated by commas |

---
---

> ## **/etc/shadow**

- stores user account password information

### /etc/shadow Fields


```
root:$6$eTJc5PVwMRTUvMLP$IjWWxcsIYuUIsj30Duzkh6DVaXbIkKKC3Bh4PJ6ut3uejj36eTt1d5Zn3aWZwD1Wfg/lzQIhIF1olydTYhd8/0:15904:0:99999:7:::
```

**The fields are as follows:** 
| **Field** | **Description** | 
|-----------|-----------------|
| `Field 1` | User name |
| `Field 2` | Password field |
| `Subfield 1` | Encryption/Hash method ID (SHA-256, SHA-512, etc…) |
| `Subfield 2` | Password salt  |
| `Subfield 3` | Encrypted or Hashed password |
| `Field 3-8` | Password metadata (last password change, etc…)  |