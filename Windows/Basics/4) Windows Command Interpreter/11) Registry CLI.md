# Windows Command Interpreter - Registry CLI

## **reg**

> ### **query**

- Queries the registry

```cmd
C:\>reg query hklm /s			        # Displays HKLM recursively
C:\>reg query hklm /s /k /f SAM		    # Searches HKLM recursively for the Key SAM
C:\>reg query hklm /s /e /f Wallpaper	# Searches HKLM recursively for the exact string Wallpaper 
```					

> ### **add**

- Add keys or values to the registry

```cmd
C:\>reg add hklm\software\cwo		    # Adds the key cwo to hklm\software
C:\>reg add hklm\software\cwo\1b4		# Adds the key 1b4 under cwo
C:\>reg add hklm\software\cwo /v “string” /t reg_sz /d “stuff and things”       # Adds the value with the name string type string and data stuff and things

C:\>reg add hklm\software\cwo /v multi /t reg_multi_sz /d “Keesler AFB\0Nellis AFB”     # Adds the value with the name multi type multistring and data Keesler AFB on one line then Nellis AFB on the next line.

C:\>reg add hklm\software\cwo /v Expand /t reg_expand_sz /d ^%SystemDrive^%”\Program Files”     # Adds the value with the name expand type expandable and data %SystemDrive%\Program Files
 ```
 > ### **delete**

 - Deletes keys or values from the registry

 ```cmd
C:\>reg delete hklm\software\cwo\1b4	        # Deletes the key 1b4
C:\>reg delete hklm\software\cwo		        # Deletes the key cwo and any values under
C:\>reg delete hklm\software\cwo /v string	    # Deletes the value string under cwo
```

> ### **export**

- Export .reg backups

```cmd
C:\>reg export hklm\software C:\backup.reg		# Makes a registry file backup.reg
```

> ### **import**

- Imports .reg files and merges any changes

```cmd
C:\>reg import C:\backup.reg    # Imports backup.reg to hklm\software
```

> ### **save**

- Saves a backup hive file

```cmd
C:\>reg save hklm\software C:\backuphive        # Saves hive of hklm\software as backuphive
```

> ### **restore**

- Restores hive files permanently
- Overwrites all keys/values within hive

```cmd
C:\reg restore hklm\software C:\backuphive	    # Restores backuphive to hklm\software
```

> ### **load**

- Loads hive files to edit temporarily

```cmd
C:\>reg load hklm\temp C:\backuphive.hiv	# Loads a BLANK hive file to hklm\temp
C:\>reg load hklm\temp C:\backuphive	    # Loads the hive backuphive to hklm\temp
```

> ### **unload**

```cmd
C:\>reg unload hklm\temp		# Unloads hive file from hklm\temp and saves backuphive
```