## **copy and xcopy**

- Copy files from one location to another.
- xcopy has more advanced options
    - Can copy directories
    - Can copy file attributes
    - Can copy file ownership information

---

> ## **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `copy C:\Windows\*.exe C:\CWO` | Copies all .exe files from C:\Windows to C:\CWO |
| `copy C:\file1.txt C:\CWO /y` | Copies file1.txt without prompting |
| `xcopy C:\CWO\file1.txt C:\CWO\Exercise\ -k` | Copies file1.txt keeping file attributes |
| `copy con file.txt` | Copy from the console (accept user input)  |
| `copy nul EmptyFile.txt` | Create an empty file |