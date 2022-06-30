# PwoerShell - Object Oriented vs Text

> ### **PowerShell**
## **Objects contain a lot of data...**
- Get-Process gets process objects, Where-Object provides filtering
- Additional information for the cmd process exists but is not shown – formatting limits what we see

## Objects allow easy manipulation over the pipeline
- Get a Process with Get-Process to see if it exists
- Get the same process, but pass the object to Stop-Process by using the pipeline
- Once stopped, we verify that the process is no longer running

> ### **CMD.exe**
## **Text is just text...**

- tasklist.exe generates output, we search that output for the string “cmd.exe”
- Nothing else is available in the shell after find…only the string of text remains