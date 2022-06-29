# Example CMD Problems/Questions

`Find the file which contains the string "NotMalware"`

```cmd
cd \ & dir /a /b /s *NotMalware*
```
------

`Find the schedule task that:`
- Starts with 2 uppercase letters	
- Then has one lowercase letter	
- Then has 3 numbers	
- Then has a # sign	
- Then has a lowercase letter	
- Then has an uppercase letter	
- Then has the number 7	

```cmd
schtasks | findstr [A-Z][A-Z][a-z][0-9][0-9][0-9][#][a-z][A-Z][7]
```
------ 

`Provide a screenshot with the verbose task information in list format`

```cmd
schtasks /query /v /FO List /tn TPs478#aG7
```

`Permission have been removed for the student.dmn.adm account under following locations: C:\Users\student.dmn.adm\documents`

- Fix the permissions so that inheritance is enabled	

```cmd
cacls C:\Users\student.dmn.adm\documents /inheritance:e		
```

- Change the owner to student.dmn.adm

```cmd
Takeown C:\Users\student.dmn.adm\documents
```

- Create a file called "proof.txt"

```cmd
echo . > C:\Users\student.dmn.adm\documents\proof.txt
```

- Provide a screenshot that displays permissions of the documents folder (Screenshot) cacls C:\Users\student.dmn.adm\documents

```cmd
dir /q C:\Users\student.dmn.adm\documents
```

------

`Find the Alternate Data Stream somewhere within C:\Windows`

```cmd
dir /r C:\Windows | findstr /i ":$Data"
```