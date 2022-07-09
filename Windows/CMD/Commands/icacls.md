# icacls

- Displays or modifies access control list (ACL) of files or folders
- Allows editing of inheritance of permissions
- Allows changing of ownership
- Allows saving of ACLs for later use

---

> ## **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `icacls "C:\Users\Student.dmn.adm\Desktop\*"` | What are the permissions for each of these files? |
| `icacls /t "C:\Users\Student.dmn.adm\desktop"` | In one command, display the desktop folders permissions and all 3 of the newly created file permissions |
| `icacls file1.txt /grant NoGuest:(R)` | Make it so that the NoGuest user has read  access to file1  without modifying any other persmissions |
| `icacls file2.txt /gran "Power Users":m` | Change Power Users  access to modify on file2 without modifying any other permissions |
| `icacls "C:\Users\Student.dmn.adm\desktop\*" /grant engineer.lcl.adm:R` | Give the user engineer.lcl.adm read permissions to all 3 files in one command without modifying any other permissions |
| `icacls file3.txt /inheritance:r /remove engineer.lcl.adm /grant:r NoGuest:r student.dmn.adm:f /deny "power users":w` | Now man file3 have the following permissions replacing all of the current permissions to: NoGuest: read; Student.dmn.adm: Full Control; and deny Power users: Write |
| `icacls c:\temp\config.dll` | Display ACL for this file |
| `icacls c:\temp\config.dll /grant Users:R` |`Add Read to Users group ACL |
| `icacls c:\temp\config.dll /grant:r Users:W` |Replace Users permissions with write |
| `icacls c:\projects\admin /remove:g guest` |Revoke guest account permissions |
| `icacls c:\windows /t /deny guest:f` | Deny guest account recursively |
| `icacls c:\windows\* /save temp /T`| Saves ACLs for all files under windows to temp |
| `icacls c:\temp /inheritance:r` | Removes and disables inheritance permissions |
| `icacls C:\Exercise /inheritance:d` | Disabled inheritance while keeping the current ACLs |