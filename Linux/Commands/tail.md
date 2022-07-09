# tail


> ## **Syntax**

- tail [filename]

---

> ## **Example**

| **Command**   | **Description**   | 
| --------------|-------------------|
| `tail filename` | Prints a portion of a file starting at the end of the file (Default 10 lines) |
| `tail -n 21 filename`| 
| `--lines 21` | Equal to *-n 21* |
| `-21` | Equal to *--lines 21* or *-n 21* |
| `tail -c 8 filename` | Prints the last 8 bytes of the file | 
| `tail -f *filename` | Continue to output data from a file |

---
---

> ## **Options**

| **Option**   | **Description**   | 
| --------------|-------------------|
| `-f, --follow` | Continue to output data from a file |