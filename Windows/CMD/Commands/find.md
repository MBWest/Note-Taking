# find

- Searches for strings in files or the output of a command
- Does not use regular expression syntax

---

> ## **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `find "Window" C:\uberdirlisting.txt` | Search the file C:\uberdirlisting.txt for the string windows |
| `find "Windows" C:\uberdirlisting.txt` | Search the file C:\uberdirlisting.txt for the string Windows |
| `find /c "Windows" C:\uberdirlisting.txt` | Perform a line count on each of the 3 searches above, does it add up, why or why not? |
| `find file1.txt /i “hacker”` | Finds the string “hacker” with any case |
| `find file1.txt /c “hacker”` | Counts how many ‘lines’ have the string “hacker” |
| `find file1.txt /v “hacker”` | Finds everything EXCEPT “hacker” |
| `dir /? \| find /I “subfolder”` | Searches output of dir /? for the string “subfolder” |