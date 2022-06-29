# net

## **accounts**

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net accounts` | Display the current password policy | 
| `net accounts minpwlen:0 /maxpwage:90 /uniquepw:10` | Change the password policy so users have to change their password every 90 days, the minimum length to 0 and remembers the last 10  passwords | 

---
---
## **user**

- Allows creating or modifying user accounts

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net user /domain` | Display the domain accounts | 
| `net user engineer.dmn.adm 1qazxsw23QAZXSW@# /domain` | Change the engineer.dmn.adm account's password to 1qazxsw23!QAZXSW@# | 
| `net user` | Display the users on the local machine | 
| `net user first.last 1337N))Bie /add, net users` | Create a new local user named first.last with the password of 1337N))bie |
| `net user` | Displays all user accounts |
| `net user John` | Displays details about the John user account |
| `net user TestUser /add` | Adds a new user “TestUser” with blank password |
| `net user TestUser pw /add`| Adds a new user “TestUser” with “pw” as password |
| `net user TestUser * /add` | Adds a new user “TestUser” prompted for password |
| `net user TestUser /delete` | Removes the TestUser account |
| `net user TestUser /active:no` | Disables the account |
| `net user student.dmn.adm Tr@!n3d2D3f3nd /domain` | Changes the domain account “Student.dmn.adm” password to Tr@!n3d2D3f3nd |

---
---

## **localgroup**

- Allows managing local group accounts

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net localgroup` | Display the groups on the local machine | 
| `net localgroup CWOStudents /add, net localgroup` | Create a new group CWOStudents. Make sure it was created | 
| `net localgroup CWOstudents first.last /add` | Add your new user to your new group | 
| `net localgroup CWOstudents` | Check the settings of your user and your new group to make sure it was added correctly | 
| `net localgroup testgroup /add` | Adds localgroup “testgroup” |
| `net localgroup testgroup` | Displays information about testgroup |
| `net localgroup testgroup testuser /add` | Adds “testuser” to the group “testgroup” |

---
---
## **group**

- Allows managing domain group accounts

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net group /domain` | Lists the domain groups |
| `net group testgroup /add /domain` | Adds domain group “testgroup” |
| `net group testgroup /domain` | Displays information about testgroup |
| `net group testgroup testuser /add /domain` | Adds “testuser” to the group “testgroup” |

---
---

## **share**

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net share` | Display the current shares | 
| `net share admin$` | Display details of the Admin$ share | 
| `net share Exercise3a$=C"\Exercise3a /remark:"Exercises for Students" /Users:5` | Share out the Exercise3a folder limiting connections to 5 and the remark Exercises for Students and share name of Exercise3a$ | 
| `net share Exercise3a$` | Ensure you new share is properly configured | 

---
---

## **start**

- Starts specified service using either the display name or key name
- Without arguments, lists display names of all running services

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net start` | Display a list of running services using the Net suite of commands | 
| `net start "Print Spooler"` | Start the Print Spooler service | 

---
---

## **stop**

- Stops running services

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net stop "Print Spooler"` | Stop the Print  Spooler service | 
| `net start "Print Spooler"` | Start the Print Spooler service | 

---
---

## **use**

- Connects a computer to a shared resource or disconnects a computer from a shared resource. When used without options, it lists the computer’s connections.

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net use` | Display all shared folders |
| `net use X: \\DC01\C$` | Mounts DC01’s C$ share to the X drive |
| `net use X: /delete` | Stops using this resource |

---
---

## **share **

- Manage local resources to share with other users.

### Examples

| **Command** | **Description** |
|-------------|-----------------|
| `net share` | Display all shared folders |
| `net share c$ /users:2` | Only two users can simultaneously use this share |
| `net share IPC$ /unlimited` | An unlimited amount of users can use this share |
| `net share c$ /delete` | Stops sharing this resource |