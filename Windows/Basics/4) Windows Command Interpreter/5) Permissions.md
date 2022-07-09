# Windows Command Interpreter - Permissions

> ## **icacls**

- Displays or modifies access control list (ACL) of files or folders
- Allows editing of inheritance of permissions
- Allows changing of ownership
- Allows saving of ACLs for later use

```
C:\>icacls c:\temp\config.dll 			        # Display ACL for this file

C:\>icacls c:\temp\config.dll /grant Users:R 	# Add Read to Users group ACL

C:\>icacls c:\temp\config.dll /grant:r Users:W 	# Replace Users permissions with write

C:\>icacls c:\projects\admin /remove:g guest 	# Revoke guest account permissions

C:\>icacls c:\windows /t /deny guest:f		    # Deny guest account recursively

C:\>icacls c:\windows\* /save temp /T	 	    # Saves ACLs for all files under windows to temp

C:\>icacls c:\temp /inheritance:r		        # Removes and disables inheritance permissions

C:\>icacls C:\Exercise /inheritance:d		    # Disabled inheritance while keeping the current ACLs
```

---

> ## **takeown**

- Forces ownership change on files/folders
- Used by administrators to regain access to files/folder locations

```
C:\>takeown /f lostfile			        # Current user takes ownership of lostfile

C:\>takeown /f c:\windows\*.txt /d		# Take ownership of .txt and ignore prompts

C:\>takeown /f c:\windows /r /d		    # Recursively take ownership of windows dir
```

