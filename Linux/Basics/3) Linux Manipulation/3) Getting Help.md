# Linux Manipulation - Getting Help

> ##  **Explain Shell**

- [ExplainShell.com](https://ExplainShell.com) is a useful website that explains sections of a command in a helpful fashion

> ## **What are Man Pages?**
Built-in form of documentation available on nearly all UNIX-like operating systems

---

> ## **help [-dms] [pattern ...]**
- Displays information about shell builtin commands
- If pattern is specified, gives detailed help on all commands matching pattern, otherwise the list of help topics is printed
```
-h, --help
```
- When available as an option, prints a short help statement about the command
- Useful when the command is already familiar to the user

---

> ## **man [section] page...**
- man is the system's manual pager
- Each page argument given to man is normally the name of a program, utility, or function.  - Pages are displayed using less.

| **Command** | **Meaning** |
|-------------|-------------|
| `h` | Get help on operating the pager |
| `jk` or `Arrrow Keys` | Move the cursor left, down, up, and right |
| `q` | Exit the pager | 
| `/pattern` | Search for a pattern in the file |
| `n` or `N` | Search for next (n) or previous (N) match of pattern |

---
---

> ## **Manual Sections**

### **Different sections of Man Pages**
- Using the corresponding number below you can look at certain section of man pages
- This will look at the *System Calls* section of the printf command
```
man 2 printf
```

1. User Commands
2. System Calls
3. C Library Functions
4. Special Files
5. File Forms
6. Games
7. Miscellaneous
8. System Admin Commands

---

> ## **Info Pages**

### **What are Info Pages**

Intended to be a replacement for man pages

### **info [OPTION]... [MENU-ITEM...]**

- Read Info documents
- Similar to man, but material is presented differently
- **info *command*** - Opens the info page for a command

