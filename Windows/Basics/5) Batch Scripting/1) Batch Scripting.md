# Batch Scripting

> ## Scripting with Batch Basics

| **Command** | **Description** |
|----------|-----------------|
| `.bat `| ensure file is saved as a .bat |
| `@echo off` | Command line won't be printed to screen |
| `%1,%2...` | Arguments used when user inputs information after the .bat script |
| `If /Else` | Run a statement list based on the results of one or more conditional tests |
| `Set` | Used to assign values to variables |
| `set local EnableDelayedExpansion` | Delay variable explosions until they are called upon |
| `@REM` | Turns echo off for the whole script |
| `goto:[label]` | Creates sections of codes and separate them with labels |


---

> ## **Scripting Uses**

- Automate tasks that are:
    - Repetitive
    - Need to be run on several computers
    - May take a while
- As easy as putting a group of commands together in a file


---

> ## **The @ Symbol**

- Generally an `@echo off` goes on the first line so that commands aren’t printed to the screen
- When done, only the output of a script (if any) goes to the screen


---

> ## **REM**

- For `comments` in your script
    - Used to explain what the script is for
    - Will not be executed

```
REM This is what a comment looks like
```


---

> ## **Script Creation**
- To make a batch script you should save a text file as .bat, echo a new file, or copy con a new file

```
C:\>echo your_text_here > filename.bat
C:\>copy con filename.bat
```


---

> ## **Running A Script**

- To execute your batch script, enter an absolute or relative path to your script.

```
C:\>C:\Users\Student.dmn.adm\HelloWorld.bat

Hello World
```


---

> ## **Batch Parameters**
- These are the arguments specified at the command-line
- There are ten variables available for use:
    - %0 - %9
    - %0 the name of the script 
    - %1 the first argument, %2 second argument, ect.

```batch
C:\>myscript.bat 44		# Running myscript.bat with an argument of 44
----myscript.bat-----
@echoOff						
Echo %1 %0			    # %0 is the name of script, %1 is first argument
---------------------
44 myscript.bat 
```

---

> ## **Variables**

- Variables are used to store a value
- Values are assigned to variables using the = character
    - There cannot be whitespace on the left side of the = 
- Values are accessed with the % characters 

```batch
C:\>start notepad Script.bat
@echo off
set cwoIsCool=1
set cwoIsActuallyLeet=1337
echo %cwoIsCool%, %cwoIsActuallyLeet%

C:\>Script.bat
1, 1337
```


---

> ## **setlocal and endlocal**
- Makes all variables local to the script
    - Place `setlocal` at the beginning of the script, just after the @echo off statement
    - Place `endlocal` at the end of the script
        - Ends localization of variables, it is `IMPLIED` by default
        - Good programming practice to always specify it


---

> ## **ENABLEDELAYEDEXPANSION**
- Necessary when using variables within loops or nested statements
- By wrapping your variable in “!”s it will wait until it’s line is read to be expanded

```batch
@echo off
setlocal enabledelayedexpansion
set VAR=before
if "%VAR%" == "before" (
	set VAR=after
	if "!VAR!" == "after" (
		echo If you see this, it worked
	)
)
```


---

> ## **Assignment Operator VS Comparison Operator**
- Assignment places a value into a variable
- Comparison evaluates to see if two things are the same
- When creating variables you must use the assignment operator

### **Assignment Operators**
- = (Put the value on the right in the variable on the left)

### **Increment Assignment Operator**
- += (Increase the variable on the left by the amount indicated on the right)

### **Decrement Assignment Operator**
- -= (Decrease the variable on the left by the amount indicated on the right)

### **Multiply Assignment Operator**
- *= (Multiply the variable on the left by the amount indicated on the right)

### **Divide Assignment Operator**
- \= (Divide the variable on the left by the amount indicated on the right)

```batch
@echo off		    @echo off		    @echo off
setlocal		    setlocal		    setlocal
set X=5		    	set Y=10		    set Z=4
set /a X+=2		    set /a Y/=5	        set /a Z-=1
echo %X% 		    echo %Y%		    echo %Z%

C:\>script.bat	    C:\>script.bat	    C:\>script.bat
7			        2			        3

- The /a switch specifies that the string to the right of the equal sign is a numerical expression that is evaluated.
```


---

> ## **Comparison Operators**
- Performs an operation depending on the operators definition (Returns T/F)

### **String Comparison**

- `==` (Are the two strings equal)

### **Integer Comparison**

- `EQU` (Are the two equal)
- `NEQ` (Are the two different)
- `LSS` (Is x less than y)
- `LEQ` (Is x less than or equal to y)
- `GTR` (Is x greater than y)
- `GEQ` (Is x greater than or equal to y)

```batch
@echo off				    @echo off
Setlocal				    setlocal
set X=Wooden			    set Y=5
if %X%==Wooden (		    if %Y% LSS 10 (
	echo it works!		    echo Y is less than 10
)						    )

C:\>script.bat			    C:\>script.bat
it works!				    Y is less than 10
```


---

> ## **IF Statement**
- If the expression in the if statement is true, then perform a given set of actions.  If the same expression is false, do not perform those actions.

```batch
@echo off
setlocal
set size=womprat
if %size%==womprat (
	C:\scripts\proton-torpedos.bat
)
```


---

> ## **Sequential IF Statement**
- With sequential if statements, multiple possible outcomes may be defined

```batch
@echo off
setlocal
set host=mailserver
if %host%==gateway (
	ping 192.168.1.1
)
if %host%==mailserver (
	ping 192.168.1.25
)
```
---

> ## **ELSE Statement**
- Perform a set of actions in the event that is no other expression evaluates to true

```batch
@echo off
Setlocal

Set BackupDir=C:\backups

if EXIST %BackupDir% (
	copy C:\users\student.dmn.adm\somefile %BackupDir%
) ELSE (
	md %BackupDir%
	copy C:\users\student.dmn.adm\somefile %BackupDir%
)
```


---

> ## **IF, ELSE Statement**

```batch
@echo Off
Setlocal
Set var=4

If %var%==4 ( 
	echo “It sure was four.”
) Else ( 
	echo “must have not been 4.”
)
```


---

> ## **Nested IF Statements**

> ### **Example 1**
```batch
@echo Off
Setlocal
Set var1=4
Set var2=stuff
If %var1%==4 (
	echo “It sure was four.”
	if %var2%==stuff (
		echo “must have been four and stuff”
	)
) Else ( 
	echo “must have not been 4.”
)
```
> ### **Example 2**
```batch
@echo Off
Setlocal
Set var1=4
Set var2=stuff
If %var1%==4 ( 
	echo “It sure was four.” >> ans.txt
   	if %var2%==stuff (
		echo “must have been four and stuff” >> ans.txt
	)
) Else ( 
	echo “must have not been 4.”
)
```
> ### **Example 3**
```batch
@echo Off
Setlocal
Set var1=4
Set var2=stuff
If %var1%==4 (
	echo “It sure was four.” >> ans.txt
   	if %var2%==stuff (
		echo “must have been four and stuff” >> ans.txt
	)
) Else ( 
	echo “must have not been 4.”
)
Echo “jk” > ans.txt
```

---

> ## **Input Validation**
- Ensures information collected from the user will not cause any unexpected errors
- Examples:
    - If your script will only execute with one argument then make sure the user provided a single argument
    - If you are asking for a Y or N response and you get something else, make sure your script knows what to do with those other responses
    - If you are asking for a year in the past and you get a year in the future, make sure your script knows how to handle a future date


---

> ## **Example Batch Script Usage**

> ### **Requirements**

- Create a Batch script that meets the following requirements		
- The first argument is an absolute path of a folder		
- The second argument is a filename		
- When the script is ran, the following occurs:		
- Check to see if the folder exists, if it does not, create it		
- After checking/creating the folder, the file is created		
- After creating the file the following is sent to the file, a list of processes, a list of all TCP/IP Network Connections		
	
```batch
@Echo Off		
Set Path_of_a_Folder=%1		
Set File_Name=%2		
If exist %Path_of_a_Folder% (		
echo File Exists		
) Else (		
     mkdir %Path_of_a_Folder%		
     echo Tasklist command > %Path_of_a_Folder%"\"%File_Name%		
     tasklist >> %Path_of_a_Folder%"\"%File_Name%		
     echo netstat -A command >> %Path_of_a_Folder%"\"%File_Name%		
     netstat -A >> %Path_of_a_Folder%"\"%File_Name%		
) 		
```