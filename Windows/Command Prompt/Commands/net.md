# net

| **Command** | **Description** |
|-------------|-----------------|
| **accounts** |
| `net accounts` | Display the current password policy | 
| `net accounts minpwlen:0 /maxpwage:90 /uniquepw:10` | Change the password policy so users have to change their password every 90 days, the minimum length to 0 and remembers the last 10  passwords | 
| **users** |
| `net users /domain` | Display the domain accounts | 
| `net users engineer.dmn.adm 1qazxsw23QAZXSW@# /domain` | Change the engineer.dmn.adm account's password to 1qazxsw23!QAZXSW@# | 
| `net users` | Display the users on the local machine | 
| `net user first.last 1337N))Bie /add, net users` | Create a new local user named first.last with the password of 1337N))bie |
| **localgroup** |
| `net localgroup` | Display the groups on the local machine | 
| `net localgroup CWOStudents /add, net localgroup` | Create a new group CWOStudents. Make sure it was created | 
| `net localgroup CWOstudents first.last /add` | Add your new user to your new group | 
| `net localgroup CWOstudents` | Check the settings of your user and your new group to make sure it was added correctly | 
| **share** |
| `net share` | Display the current shares | 
| `net share admin$` | Display details of the Admin$ share | 
| `net share Exercise3a$=C"\Exercise3a /remark:"Exercises for Students" /Users:5` | Share out the Exercise3a folder limiting connections to 5 and the remark Exercises for Students and share name of Exercise3a$ | 
| `net share Exercise3a$` | Ensure you new share is properly configured | 
| **start** |
| `net start` | Display a list of running services using the Net suite of commands | 
| `net start "Print Spooler"` | Start the Print Spooler service | 
| **stop** |
| `net stop "Print Spooler"` | Stop the Print  Spooler service | 
| `net start "Print Spooler"` | Start the Print Spooler service | 