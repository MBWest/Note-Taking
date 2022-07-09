# dir

- Displays what is in a directory
- By Default it will not show:
    - Read only files/folders
    - Hidden files/folders
    - System files/folder

---

> ## **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `dir` | List the contents of your current directory | |
| `dir /ad` | ONLY display directories |
| `dir /ah` | ONLY display hidden |
| `dir /ar` | ONLY display read only attribute |
| `dir /a` | Shows ALL files/folder regardless of attribute |
| `dir /a-r C:\CWO` | Shows everything EXCEPT read only; starts at C:\CWO folder |
| `dir /s` | Look in subfolder/subfiles (recursive) |
| `dir /s *.exe` | Search for all .exe files; starts with current folder
| `dir C:\Windows` | List the contents of the C:\Windows directory |
| `dir /as C:\Windows` | List only the system files in the C:\Windows directory |
| `dir /ah C:\Windows` | List only the hidden files in the C:\Windows directory |
| `dir /ahs C:\Windows` | Display just those overlappoing files in C:\Windows |
| `dir /ah-s C:\Windows` | Display hidden files that are not system files in C:\Windows |
| `dir /s C:\Windows > C:\uberdirlisting.txt` | Display all files and subdirectories under C:\Windows, sending this output to a file called C:\Uberdirlisting.txt  |
| `dir /s /a C:\WinMail.exe or dir /s /a /b C:\ \| find "WinMail.exe"` | Find all instances of WinMail.exe on the entire C drive |
| `dir /s \| more` | Use the dir command, do a recursive directory search from C:\ and make it to where it displays the output a page at a time |