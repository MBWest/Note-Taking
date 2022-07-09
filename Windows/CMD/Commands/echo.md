# Echo

> ## **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `echo I am a CLImaster` | Display the message I am a CLImaster to the cmd window |
| `echo I am a CLImaster > C:\CLI.txt` | Using echo and >, send the same message to the file C:\CLI.txt |
| `type C:\CLI.txt` | Display the contents of C:\CLI.txt using the type command |
| `echo I am a CLImaster > C:\CLI.txt` | Using echo and >, send  the message again to the file C:\CLI.txt |
| `echo ^<^(^^^-^^^)^> >  C:\CLI.txt` | Using echo  send the text <(^-^)>  to the file C:\CLI.txt |
| `echo %MyVar% is My very own variable` | Using echo display the following text %MyVar% is My very own variable |
| `echo cat >> file1.txt, echo dog >> file1.txt, Echo bird >> file1.txt; echo cat >> file2.txt, echo dog >> file2.txt, echo bird >> file2.txt; echo car >> file3.txt, echo bear >> file3.txt, echo bird >> file3.txt` | Create 3 files in the folder Student.dmn.adm\Desktop:file1.txt, file2.txt, and file3.txt. Put the following text in each one with each word on a new line (File1: Cat, Dog, Bird) (File2: Cat, Dog, Bird) (File3: Cat, Bear, Bird) |
| `echo new > NewFileOnMyDesktop.txt; icacls NewFileOnMyDesktop.txt /inheritance:d; icacls NewFileOnMyDesktop.txt /remove student.dmn.adm` | Make a new file on your desktop. Remove only your own permissions while keeping all other effective permissions |
| `echo %date%` | Predefined Variable (current Date) |
| `echo %time%` | Predefined Variable (current Time) |
| `echo %Random%` |	Predefined Variable, produces random number|