# ln

- Make links between files
- See 'File System.md' for more information on links

---

> ## **Syntax**

- ln [OPTION]... TARGET


> ## **Hard Links**

| **Command**   | **Description**   |
| --------------|-------------------|
| `ln hello.txt hello-hard-link.txt` | Makes a hard link (hello-hard-link.txt) to the original file (hello.txt) |

---

> ## **Soft Link (Symbolic System)**

| **Command**   | **Description**   |
| --------------|-------------------|
| `ln -s ./hello.txt hello-soft-link.txt` | Makes a soft link (hello-soft-link.txt) to the original file (hello.txt) |