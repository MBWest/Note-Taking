# Windows Command Interpreter – Fundamentals

## Case Sensitivity
> **Case Sensitivity**
- Object creation retains case (files, folders, registry items)
- Most commands ignore case
- Very few commands with case sensitive switches

---
---
---

## Command-Line Syntax

| **DESCRIPTION** | **NOTATION** |
|-----------------|:------------:|
| `Items you must type as shown` | Text without brackets or braces |
| `Placeholder for which you must supply a value` | < Text inside angle brackets > |
| `Optional items` | [ Text inside square brackets ] |
| `Set of required items; choose one` | { Text inside braces } |
| `Separator for mutually exclusive items; choose one` | Vertical bar ( \| )
| `Items that can be repeated` | Ellipsis ( … ) |

---
---
---

## Paths

> **Absolute path**
- The entire path, starting with the root partition letter

```
    C:\Windows\System32\cmd.exe
    C:\>cd “C:\Program Files”
    C:\Program Files> cd “Internet Explorer”
```

> **Relative path**
- The path relative to the current directory

```
    C:\Program Files\Internet Explorer>cd ..\
    C:\Program Files>cd .\Internet Explorer
```