# Windows Command Interpreter - Account Management

## **net**

> **user**

- Allows creating or modifying user accounts

```
C:\>net user 			            # Displays all user accounts

C:\>net user John 			        # Displays details about the John user account

C:\>net user TestUser /add		    # Adds a new user “TestUser” with blank password

C:\>net user TestUser pw /add	    # Adds a new user “TestUser” with “pw” as password

C:\>net user TestUser * /add        # Adds a new user “TestUser” prompted for password

C:\>net user TestUser /delete 	    # Removes the TestUser account

C:\>net user TestUser /active:no 	# Disables the account

C:\>net user student.dmn.adm Tr@!n3d2D3f3nd /domain         # Changes the domain account “Student.dmn.adm” password to Tr@!n3d2D3f3nd
```

> **localgroup**

- Allows managing local group accounts

```
C:\>net localgroup			                # Lists the local groups

C:\>net localgroup testgroup /add		    # Adds localgroup “testgroup”

C:\>net localgroup testgroup		        # Displays information about testgroup

C:\>net localgroup testgroup testuser /add	# Adds “testuser” to the group “testgroup”
```

> **group**

- Allows managing domain group accounts

```
C:\>net group /domain			                    # Lists the domain groups

C:\>net group testgroup /add /domain	            # Adds domain group “testgroup”

C:\>net group testgroup /domain          	        # Displays information about testgroup

C:\>net group testgroup testuser /add /domain       # Adds “testuser” to the group “testgroup”
```
