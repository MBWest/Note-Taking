# Windows Command Interpreter – Fundamentals

## **Case Sensitivity**

> **Case Sensitivity**
- Object creation retains case (files, folders, registry items)
- Most commands ignore case
- Very few commands with case sensitive switches

---
---
---

## **Command-Line Syntax**

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

## **Paths**

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
---
---
---

## **Command Arguments**

- **Definition:** Predefined value, specified during the command's programming, which causes the command to work differently than it would without the specified argument
- Always follow the command name and is separated by a space

```
C:\>Time
The current time is: 13:40:07:52
Enter the new Time:  14:40

C:\>Time /t
02:40 PM
```

> **Help Argument**
- Specified as an argument to the command
- May be specified by typing "help" or "/?“ after the command

```
C:\>shutdown /?
C:\>shutdown help
C:\>net help
C:\>net /?
```

> **Double Quote and Escape**
- Necessary to use metacharacters for their literal meaning
- The caret "^" is the escape character

```
C:\>echo “hello ^^||”
“hello ^^||”

C:\>echo hello |
The syntax of this command is incorrect

C:\>echo hello ^|
hello |

C:\>echo hello ^^
hello ^
```

> **Wildcard (\*)**
- Any Character
- Examples:
    - *.exe (All files with an “exe” extension)
    - Win* (All files beginning with “Win”)
    - *.* (All files)

```
C:\>mkdir C:\exefiles && mkdir C:\winstuff
C:\>copy C:\Windows\System32\*.exe C:\exefiles
C:\>copy C:\Windows\System32\win* C:\winstuff
```

---
---
---

## **Three Defined Handlers**
> **Standard IN (STDIN) - 0**
- Input from Keyboard (Default)

> **Standard OUT (STDOUT) - 1**
- Sends output to the Terminal 

> **Standard ERROR (STDERR) - 2**
- Sends errors to the Terminal

---
---
---
## **Redireection**

> **Input redirection (<)**
- Can get information from a file instead of the keyboard

```
C:\>tasklist 1> cwo.txt		# Writes running tasks to cwo.txt (creates file)
```

> **Output redirection (>, >>)**
- `>` is used to overwrite information in the destination
- `>>` is used to append information in the destination

```
C:\>echo A new line >> cwo.txt	# Appends A new line cwo.txt (can create file)
```

> **Error redirection (2>, 2>>)**

```
C:\>dir C:\ 2> cwo.txt		# Overwrites cwo.txt with the error message
```

---
---
---
## **Streams and Pipes**

> **Streams**
- Input / Output stream (can be redirected)

```
C:\>dir /? | find /I “hidden” 	# Sends the STDOUT from dir /? to find “hidden”
```

> **Pipes**
- Redirects STDOUT to piped command

```
C:\>dir /s | find /I “readme”	# Sends the STDOUT from dir /s to find “readme”
```

---
---
---

## **Echo**

- Displays messages to the terminal
- Using the output redirection operators (>,>>) you can create new files with the specified text

```
C:\>echo biscuits and gravy		# Displays biscuits and gravy to terminal biscuits and gravy

C:\>echo biscuits and gravy > Yum.txt  	# Redirects biscuits and gravy to Yum.txt

C:\>echo breakfast >> Yum.txt		# Redirects(appends) breakfast to Yum.txt
```
