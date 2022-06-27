# Example Batch Script

## Requirements

- Create a Batch script that meets the following requirements		
- The first argument is an absolute path of a folder		
- The second argument is a filename		
- When the script is ran, the following occurs:		
- Check to see if the folder exists, if it does not, create it		
- After checking/creating the folder, the file is created		
- After creating the file the following is sent to the file, a list of processes, a list of all TCP/IP Network Connections		
	
```cmd
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