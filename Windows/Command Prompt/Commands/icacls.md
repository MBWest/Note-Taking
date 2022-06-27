# icacls

| **Command** | **Description** |
|-------------|-----------------|
| `icacls "C:\Users\Student.dmn.adm\Desktop\*"` | What are the permissions for each of these files? |
| `icacls /t "C:\Users\Student.dmn.adm\desktop"` | In one command, display the desktop folders permissions and all 3 of the newly created file permissions |
| `icacls file1.txt /grant NoGuest:(R)` | Make it so that the NoGuest user has read  access to file1  without modifying any other persmissions |
| `icacls file2.txt /gran "Power Users":m` | Change Power Users  access to modify on file2 without modifying any other permissions |
| `icacls "C:\Users\Student.dmn.adm\desktop\*" /grant engineer.lcl.adm:R` | Give the user engineer.lcl.adm read permissions to all 3 files in one command without modifying any other permissions |
| `icacls file3.txt /inheritance:r /remove engineer.lcl.adm /grant:r NoGuest:r student.dmn.adm:f /deny "power users":w` | Now man file3 have the following permissions replacing all of the current permissions to: NoGuest: read; Student.dmn.adm: Full Control; and deny Power users: Write |