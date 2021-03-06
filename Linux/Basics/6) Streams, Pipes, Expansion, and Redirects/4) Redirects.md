# Streams, Pipes, Expansion, and Redirects - Redirects

> ## **File descriptors**
- A non-negative integer that represents an opened file
    - In-use file descriptors are managed and tracked by the kernel
    - Each process maintains a record of its own file descriptors
- Each process created has 3 file descriptors by default:
    - STDIN→0
    - STDOUT→1
    - STDERR →2

---

> ## **Redirection**

### **Redirect output**
- `[n]>word`
    - Causes the file word to be opened for writing on file descriptor n, or STDOUT (fd 1) if n is no specified
    - If the file does not exist, it is created; if it does exist, it is truncated to zero size
- `[n]>>word`
    - Causes the file word to be opened for appending on file descriptor n, or STDOUT (fd 1) if n is not    specified
    - If the file does not exist, it is created

### **Redirect output and error**
- `&>word`
- `>&word`
- `> word 2>&1`
    - All 3 versions allow both STDOUT (fd 1) and STDERR (fd 2) to be redirected to the file word
    - Can be done in append (>>) mode as well 

--- 

*Standard Input* -> **Command** -> *Standard Output* or -> *Standard Error*

The **>** operator default to 1 as the file descriptor number which is why we dont need to specify **1>** to redirect standard output. 
The **<** operator uses a default file descriptor number of 0, so we dont ned to specify **0<** to redirect to standard input, although you can. 

| **Information** |
| --------------|
| **Standard Input** |
| Standard input is where a program or command get its input from. By default, the shell directs standard input from the keyboard. The input information could come from a keyboard, a file, or even from another command.  |
| **Standard Output** |
| Standard output is a place to which a program or command can send information. The information could go to a screen to be displayed, to a file, or even to a printer or other device. |
| **Standard Error** |
| Commands and programs also have a destination to send error messages: Standard Error. By default, the shell directs standard error information to the screen for the user to read, but this destination can be changed if needed. If you have standard output and standard error in the same command you must redirect standard output first and then standard error. |
| **Redirecting Output (>)** |
| The redirect output symbol (**>**) tells the shell to redirect the output of a command to a specific file instead of the screen. By default, the **date** command will print the current date to the screen. If we instead run **date > output.txt** the output will be redirected to a file called output.txt. |
| **Append Output (>>)** |
|The append output symbol (**>>**) tells the shell to redirect the output SSof a command to a specific file instead of the screen.To instead keep the existing contents in the file and add new content to the end of the file, use (**>>**) when redirecting. |
| **Redirecting Standard Input (<)** | 
| To pass contents of a file to standard input use the (**<**) symbol followed by the filename. `cat < filename.txt` |
| **Redirecting Standard Input and Output at the Same Time** |
| `> cat < original.txt > output.txt` | 
| **Redirecting Standard Error (2>)** |
| By default, error messages are output top the screen. The standard error redirection operator is **2>**. `ls notrealfolder 2> errorlog.txt` (Redirects the error text to the errorlog.txt file) |
| **2> /dev/null** |
| In linux the /dev/null is like a blackhole. Send errors here if you dont wish to view them at a later date. `find / -name 'sample.txt' 2> /dev/null` |
| **Redirecting Standard Output and Standard Error at the Same Time (&>)** |
| Newer versions of bash allow for (&>) to redirect both standard output and standard error to the same file. `find / -name 'sample.txt' &> all.txt` |