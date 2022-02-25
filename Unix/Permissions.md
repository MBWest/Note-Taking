# Permissions

## Groups

On Unix systems, a single user may be the owner of files and directories, meaning that they have control over their access. 
Additionally, users can belong to groups which are given access to particular files and folders by their owners. 
- **whoami** - Shows current terminal user

## User and Group IDs

When a new user account is made, it is assigned a user ID. The user is also assigned a group ID. 
These user IDs are stored in /etc/passwd, and the group IDs are stored in /etc/group.
- **id** - View Users and Group IDs

## File Attributes

### File Type
- **-** - Regular File
- **d** - Directory
- **c** - Special File or Device
- **l** - Symbolic Link
- **b** - Block Device
- **s** - Socket
- **p** - Named Pipe

|Owner|Group|World|
|---|---|---|
|rwx|rwx|rwx|

| Character | Effect On Files | Effect On Directories |
|--|--|--|
| r | file can be read | directory's contents can be listed |
| w | file can be modified | directory's contents can be modified (create new files, rename files/folders) but only if the executable attribute is also set |
| x | file can be treated as a program to be executed |  allows a directory to be entered or "cd"ed into |
| - | file cannot be read, modified, or executed depending on the location of the - character  | directory contents cannot be shown, modified, or cd'ed into depending on the location of the - character |

### Examples

|Owner|Group|World|
|---|---|---|
|rw-|- - -|- - -|

- In the above example, we see that the file's owner has read and write permissions but NOT execute permissions. No one else has any access.

|Owner|Group|World|
|---|---|---|
|rwx|- - -|- - -|

- In the above example, we see that the file's owner has read, write, AND execute permissions. No one else has any access.

|Owner|Group|World|
|---|---|---|
|rw-|r- -|r- -|

- In the above example, we see that the file's owner has read, and write BUT NOT execute permissions. Members of the file's owner group can only read the file. Everyone else can read the file too.

|Owner|Group|World|
|---|---|---|
|rwx|rwx|- - -|

- In the above example, we see that the directory's owner AND member's of the owner group can enter the directory, rename, and remove files from within the directory. 


|Owner|Group|World|
|---|---|---|
|rwx|- -x|- - -|

- In the above example, we see that the directory's owner can enter the directory, rename, and remove files from within the directory. Members of the owner group can enter the directory but
cannot create, delete, or rename files.

## The Sticky Bit 
The sticky bit is to tell the OS to run the executable as its owner. Indicated by the ‘s’ instead of ‘x’
- **-rwsrwx---** - This is very important to configure correctly. If you have a root based executable with the sticky bit set for everyone then anyone can run it as root!