# Windows Command Interpreter - Processes

> ## **tasklist**

- Allows you to view running processes

```
C:\>tasklist 				    # List all running processes

C:\>tasklist /m kernel32.dll 	# List all tasks using kernel32.dll module

C:\>tasklist /svc 				# Show services hosted in each process

C:\>tasklist /v 				# Show verbose information

C:\>tasklist /fi "imagename eq cmd.exe" 	    # Show all cmd.exe processes

C:\>tasklist /fi "imagename eq cmd.exe" /m	    # Show all modules used by cmd.exe process

C:\>tasklist /fi "imagename eq cmd.exe" /svc  	# Show all services hosted by cmd.exe
```

---

> ## **taskill**

- Terminates processes based on PID or IMAGENAME

```
C:\>taskkill /pid 1234 			# Terminate process with process ID 1234

C:\>taskkill /im iexplore.exe 	# Terminate all iexplore.exe processes

C:\>taskkill /t /pid 1234 		# Terminate PID 1234 & all child processes 

C:\>taskkill /f /pid 1234 		# Forcefully terminate process 1234

C:\>taskkill /fi “imagename eq cmd.exe”	    # Terminate cmd.exe
```

---

> ## **schtasks**

- Create, delete, query, change, run and end scheduled tasks on a local or remote system. 

```
C:\>schtasks /create /?     # Show a help page for creating a task (this applies for delete, query, etc.)

C:\>schtasks /create /TN games /TR “C:\game.exe” /SC minute /MO 2       # Create a task Named “games” that will run “game.exe” scheduled for 2min intervals

C:\>schtasks /query /TN games                   # Query the pre-existing task name “games”

C:\>schtasks /run /TN rubber-duck               # Run the scheduled task “rubber-duck”

C:\>schtasks /change /disable /TN “games”       # Disabling the pre-existing task named “games”

C:\>schtasks /delete /TN games                  # Deleting the task using the task name “games”
```