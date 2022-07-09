# touch

Change file timestamps and create files

---

> ## **Syntax**

- touch [options] [file or directory name]

---

> ## **Examples**

| **Command**   | **Description**   |
| --------------|-------------------|
| `touch filename filename...` | Create multiple files at once; If you wish to have a space in the file name you must wrap the name in "quotation marks" |
|`touch ../filename` | Creates a file in the parent directory |
| `touch file.txt` | Updates file.txt last modified time to the second you ran the command |
| `touch -t <timestamp> <filename>` | Set a specific timestamp for an existing file |
| `[[CC]YY]MMDDhhmm[.ss]`  | Timestamp format|
| | **Example** `touch -t 199901010000 test` |
|| `CC` - the first two digits for a year |
|| `YY` - the last two digits for a year |
|| `MM` - the month |
|| `DD` - the day |
|| `hh` - the hour |
|| `mm` - the minutes |
|| `ss` - the seconds |


---
---

> ## **Options**

| **Options**   | **Description**   |
| --------------|-------------------|
| `-a` | Changes the access time. |
| `-c` `--no-create` | Avoids creating a new file. |
| `-d=<string>` `--date=<string>` | Changes a timestamp using a date string. |
| `-f` | No effect. In older BSD's the option forces changes. |
| `-h` `--no-dereference` |	Changes a symbolic link's timestamp. |
| `-m` | Changes the modification time. |
| `-r=<file>` `--reference=<file>` | Changes a timestamp to the referenced file's timestamp. |
| `-t <stamp>` | Modifies a timestamp, where the stamp is the date/time format. |
| `--help` | Opens the help menu. |
| `-v` `--version` | Prints the program version. |

---
---

> ## **References**

https://phoenixnap.com/kb/touch-command-in-linux