# Redirection

*Standard Input* -> **Command** -> *Standard Output* or -> *Standard Error*

The **>** operator default to 1 as the file descriptor number which is why we dont need to specify **1>** to redirect standard output. 
The **<** operator uses a default file descriptor number of 0, so we dont ned to specify **0<** to redirect to standard input, although you can. 

## Standard Input

Standard input is where a program or command get its input from. By default, the shell directs standard input from the keyboard
- The input information could come from a keyboard, a file, or even from another command. 

## Standard Output

Standard output is a place to which a program or command can send information.
- The information could go to a screen to be displayed, to a file, or even to a printer or other device

## Standard Error

Commands and programs also have a destination to send error messages: Standard Error
- By default, the shell directs standard error information to the screen for the user to read, but this destination can be changed if needed. 
- If you have standard output and standard error in the same command you must redirect standard output first and then standard error. 

## Redirecting Output (>)

The redirect output symbol (**>**) tells the shell to redirect the output of a command to a specific file instead of the screen. 
- By default, the **date** command will print the current date to the screen. If we instead run **date > output.txt** the output will be redirected to a file called output.txt

The append output symbol (**>>**) tells the shell to redirect the output SSof a command to a specific file instead of the screen.
- To instead keep the existing contents in the file and add new content to the end of the file, use (**>>**) when redirecting. 

## Redirecting Standard Input (<)

To pass contents of a file to standard input use the (**<**) symbol followed by the filename. 
- *Example* > cat < filename.txt

## Redirecting Standard Input and Output at the Same Time

- *Example* > cat **<** original.txt *>* output.txt

## Redirecting Standard Error (2>)

By default, error messages are output top the screen. The standard error redirection operator is **2>**
- *Example* > ls notrealfolder 2> errorlog.txt
	- Redirects the error text to the errorlog.txt file

## Redirecting Standard Output and Error at the Same Time (&>)

Newer versions of bash allow for (&>) to redirect both standard output and standard error to the same file