# Windows Command Interpreter - Manipulation/Navigation

## **Set**

- Without specifying any arguments, this command displays all environment variables that have been set

```
C:\>set z=44				Assigns 44 to z
C:\>echo %z%
44

C:\>set ans=C:\Excercise\answers.txt	# Assigns your answer file to ans.

C:\>echo %date%				# Predefined Variable (current Date)

C:\>echo %time%				# Predefined Variable (current Time)

C:\>echo %Random%			# Predefined Variable, produces random number
```

---
---
---
## **dir**
- Displays what is in a directory
- By Default it will not show:
    - Read only files/folders
    - Hidden files/folders
    - System files/folder

```
C:\>dir /ad		# ONLY display directories

C:\>dir /ah		# ONLY display hidden

C:\>dir /ar		# ONLY display read only attribute

C:\>dir /a		# Shows ALL files/folder regardless of attribute

C:\>dir /a-r C:\CWO		# Shows everything EXCEPT read only; starts at C:\CWO folder

C:\>dir /s		# Look in subfolder/subfiles (recursive)

C:\>dir /s *.exe		# Search for all .exe files; starts with current folder
```
---
---
---
## **cd or chdir**

- Changes to specified directory

```
C:\>cd “C:\Program Files”
```

---
---
---
## **md or mkdir**

- Makes new directories
- Can make multiple at one time

```
C:\>md CWO CWO2     # Make the CWO and CWO2 directory 

C:\CWO>md Testing\All\The\Things    # Make the Testing\All\The\Things directories
```

---
---
---

## **rd or rmdir**

- Removes the specified directory
- Will not remove directories that are not empty by default

```
C:\>rd CWO		# Removes the directory CWO – Unless NOT empty

C:\>rd CWO /s	# Removes all subfolders/files starting at CWO
```

---
---
---

## **more**

- Displays the output of a file (can be piped)
    - One screen at a time with “Space” 
    - One line at a time with “Enter

```
C:\>dir /s | more	# Displays the output of dir /s one page at a time

C:\>more Yum.txt	# Displays contents of Yum.txt one page at a time
```

---
---
---

## **copy and xcopy**
- Copy files from one location to another.
- xcopy has more advanced options
    - Can copy directories
    - Can copy file attributes
    - Can copy file ownership information

```
C:\>copy C:\Windows\*.exe C:\CWO    # Copies all .exe files from C:\Windows to C:\CWO

C:\>copy C:\file1.txt C:\CWO /y		# Copies file1.txt without prompting

C:\>xcopy C:\CWO\file1.txt C:\CWO\Exercise\ -k 	# Copies file1.txt keeping file attributes
```

---
---
---

## **move**

- Moves a file from one location to the other

```
C:\>move file1.txt C:\CWO		# Moves C:\file1.txt to C:\CWO folder
```

---
---
---

## **ren or rename**

- Renames a file.

```
C:\>ren file1.txt CWOFile.txt		# Renames file1.txt to CWOFile.txt
```

---
---
---

## **type**

- Displays contents of text files to the terminal

```
C:\>type Yum.txt		# Displays contents of Yum.txt to terminal
biscuits and gravy
breakfast
```

---
---
---

## **find**

- Searches for strings in files or the output of a command
- Does not use regular expression syntax

```
C:\>find file1.txt /i “hacker”	    # Finds the string “hacker” with any case

C:\>find file1.txt /c “hacker”	    # Counts how many ‘lines’ have the string “hacker”

C:\>find file1.txt /v “hacker”	    # Finds everything EXCEPT “hacker”

C:\>dir /? | find /I “subfolder”	# Searches output of dir /? for the string “subfolder”
```

---
---
---

## **findstr**
- Searches for strings in files or the output of a command
- Can use regular expressions

```
.			any character ONE time
*			zero or more occurrences of the previous character or class
^			beginning of line
$			end of line
[class]			Any ONE character in set
[^class]			Any ONE character not in set
[x-y]			Any ONE character in range 
\.			Escape: literal use of the character .
\<xyz			beginning of word
xyz\>			end of word
```

---
---
---

## **del**

- Deletes Files

```
C:\>del c:\Temp\MyStuff\passwds.txt		# Deletes passwds.txt

C:\>del /f c:\temp\MyStuff\*.txt 		# Forcefully delete read only text files

C:\>del /s c:\Temp 			# Delete files from c:/Temp and all sub folders

C:\>del /ar c:\Temp 		# Deletes only read only files

C:\>del /ah c:\Temp 		# Deletes only hidden files

C:\>del /a c:\Temp 			# Deletes all files – EXCEPT read only (use /f)

C:\>del /a-s c:\Temp		# Delete all files except system files and read
```

---
---
---

## **attrib**

- View and modify file attributes

```
C:\>attrib 			                  # Display attributes of all files in current directory

C:\>attrib C:\CWO\*	                  # Display attributes of all files in CWO directory 

C:\>attrib +h c:\temp\myfile.dll 	  # Turns myfile.dll into a hidden file

C:\>attrib -s c:\desktop.ini 	      # Removes system attribute

C:\>attrib /s +r c:\windows\*.exe	  # Adds read only to .exe files recursively
```

---
---
---
## **sort**

- Sorts from A-Z by default

```
C:\>sort file1.txt		# Sort file1.txt from A-Z

C:\>type file1.txt | sort /r	# Display file1.txt sort from Z-A
```