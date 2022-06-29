# del

Deletes files

---

## Examples

| **Command** | **Description** |
|-------------|-----------------|
| `del C:\Excercise3a\USAF\MAJCOMs\renamed.txt` | Delete the file named renamed.txt |
| `del /s C:\Exercise\This\is\a\test` | Delete all of the files in this\is\a\test folder including all of its sub-files |
| `del C:\Exercise\This\is\a\*.exe` | Delete all the .exe  files in this\is\a directory |
| `del C:\Exercise3a\This\is\*.txt` | Delete all the .txt  files in this\is directory |
| `del c:\Temp\MyStuff\passwds.txt` | deletes passwds.txt |
| `del /f c:\temp\MyStuff\*.txt ` | Forcefully delete read only text files |
| `del /s c:\Temp 	` | Delete files from c:/Temp and all sub folders |
| `del /ar c:\Temp ` | Deletes only read only files |
| `del /ah c:\Temp ` | Deletes only hidden files |
| `del /a c:\Temp 	` | Deletes all files – EXCEPT read only (use /f) |
| `del /a-s c:\Temp` | Delete all files except system files and read |