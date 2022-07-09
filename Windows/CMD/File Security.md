# File Security

---

> ## **Examples**

| **Command** | **Description** |
|----------|-----------------|
| `attrib` | Displays or changes file attributes | 
| `icacls` | Displays or modifies access control lists for files | 
| `takeown` | Take ownership change on file and directories  | 
| **Examples** | 
| `icacls C:\File /setowner "username"` | Set owner to someone other than yourself | 
| `icacls C:\File\* /grant "useraccount":[Permission Arguemnt]` | To give permission to a folder and all the files beneath it | 
| `icacls C:\Folder /inheritance:e /t` | Implement inheritance recursively| 
| `dir /q` | Show ownership of a file | 
| `attrib C:\Directory` | Display the attributes of all files in a current directory | 
| `attrib C:\CWO\*` | Display attributes of all files in CWO directory| 
| `attrib +h C:\MyFile.dll` | Turns myfile.dll into a hidden file | 
| `attrib -s C:\desktop.ini` | Removes system attributes | 
| `attrib /s +r C:\Windows\*.exe` | Adds read only to .exe files recursively | 

