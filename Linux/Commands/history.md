# History

GNU History Library

---

> ## **Syntax**

- history

---

> ## **Example**

| **Command**   | **Description**   |
| --------------|-------------------|
| `history` | View previous run commands |
| `history \| less` | Easier way to manage a long history |
| `![number]` | Rerun a command using its line number from the history |
| `!!` | Refer to the previous command.  This is a synonym for '!-1' |
| `!cat` | Reruns the last commands that started with 'cat' |
| `Ctrl-r` | Search through your history |

---

> ## **Arrow Keys**

| **Key**   | **Description**   |
| --------------|-------------------|
| `Left/Right` | Move the cursor along the command |
| `Up` | Cycle through previous commands |
| `Down` | Cycle through recent commands |

---

> ## **Files and Configurations**

| **File**   | **Description**   |
| --------------|-------------------|
| `~/.history` | Default filename for reading and writing saved history |
| `.bash_history` | Where the history is saved |
| `$HISTFILESIZE` | Number of items stored in history (Stored in ~/.bashrc)  |
| `$HISTSIZE` | The number of item which will be shown to the user when running *history* (Stored in ~/.bashrc) |


