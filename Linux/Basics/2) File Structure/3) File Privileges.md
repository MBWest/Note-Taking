# Linux File Structure - File Privileges

> ### **User Privileges**
- Users can affect any file/folder to which they have appropriate permissions

> ### **Root User Privileges**
- Has all privileges
- Can use su command and switch to any user without knowledge of their password

## **Terminal**

- If you are logged into the system as a normal user the command prompt will end in a **dollar sign ($)**
- If you are logged into the system as a normal user the command prompt will end in a **pound sign (#)**
---

## **Groups**

On Unix systems, a single user may be the User of files and directories, meaning that they have control over their access. 
Additionally, users can belong to groups which are given access to particular files and folders by their owners. 

```
whoami
```
- Shows current terminal user

---

## **User and Group IDs**

When a new user account is made, it is assigned a user ID. The user is also assigned a group ID. 
These user IDs are stored in /etc/passwd, and the group IDs are stored in /etc/group.

```
id
```
- View Users and Group IDs

---

## **File Attributes**

| **Letter** | **Description**   |
| --------------|-------------------|
| **File Type** |
| `-` | Regular File |
| `d` | Directory  |
| `c` | Special File or Device |
| `l` | Symbolic Link |
| `b` | Block Device |
| `s` | Socket |
| `p` | Named Pipe |

|**User**|**Group**|**World**|
|---|---|---|
|rwx|rwx|rwx|

| **Character** | **Effect On Files**| **Effect On Directories** |
|--|--|--|
| `r` | file can be read | directory's contents can be listed |
| `w` | file can be modified | directory's contents can be modified (create new files, rename files/folders) but only if the executable attribute is also set |
| `x` | file can be treated as a program to be executed |  allows a directory to be entered or "cd"ed into |
| `-` | file cannot be read, modified, or executed depending on the location of the - character  | directory contents cannot be shown, modified, or cd'ed into depending on the location of the - character |

---

## The Sticky Bit 
The sticky bit is to tell the OS to run the executable as its User. Indicated by the ‘s’ instead of ‘x’
- **-rwsrwx---** - This is very important to configure correctly. If you have a root based executable with the sticky bit set for everyone then anyone can run it as root!

***Example**
```
-rw-r--r--.  1 student student   	 531 Jul 16 18:13 .bashrc
-rwsrwx---.  2 student cadre	    4096 Sep 25 07:00 Assignments
drwx------.  2 student student  	4096 Sep 25 07:00 .ssh
```

---

## **Examples**

|**User**|**Group**|**World**|
|---|---|---|
|rw-|- - -|- - -|

- In the above example, we see that the file's User has read and write permissions but NOT execute permissions. No one else has any access.

|**User**|**Group**|**World**|
|---|---|---|
|rwx|- - -|- - -|

- In the above example, we see that the file's User has read, write, AND execute permissions. No one else has any access.

|**User**|**Group**|**World**|
|---|---|---|
|rw-|r- -|r- -|

- In the above example, we see that the file's User has read, and write BUT NOT execute permissions. Members of the file's User group can only read the file. Everyone else can read the file too.

|**User**|**Group**|**World**|
|---|---|---|
|rwx|rwx|- - -|

- In the above example, we see that the directory's User AND member's of the User group can enter the directory, rename, and remove files from within the directory. 


|**User**|**Group**|**World**|
|---|---|---|
|rwx|- -x|- - -|

- In the above example, we see that the directory's User can enter the directory, rename, and remove files from within the directory. Members of the User group can enter the directory but
cannot create, delete, or rename files.

---

