# attrib

- View and modify file attributes

---

> ## **Examples**


| **Command** | **Description** |
|-------------|-----------------|
| `attrib /s "C:\Users\Student.dmn.adm\*"` | Display all attributes for files and files within sub-folders within the C:\Users\Student.dmn.adm folder |
| `attrib C:\This\is\*` | Using this information look at the .txt files we were not able to delete earlier. Can you use this information to delete them now? |
| `attrib +r C:\uberdirlisting.txt` | Change the attributes on C:\uberdirlisting.txt so that it is read only |
| `attrib` | Display attributes of all files in current directory |
| `attrib C:\CWO\*` | Display attributes of all files in CWO directory  |
| `attrib +h c:\temp\myfile.dll` |  Turns myfile.dll into a hidden file |
| `attrib -s c:\desktop.ini` | Removes system attribute |
| `attrib /s +r c:\windows\*.exe` | Adds read only to .exe files recursively |