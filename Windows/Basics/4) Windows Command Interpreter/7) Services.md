# Windows Command Interpreter - Services

## **sc**

> **sc query / queryex**

- Lists all active services by default

```
C:\>sc query 				    # Lists all active services

C:\>sc query state= inactive    # Lists all inactive services

C:\>sc query state= all			# Lists all services

C:\>sc query state= all | find /I “firewall”        # Will find string “firewall”
```

> **sc qc**

- Queries the configuration of a service
- Must have the service name to use

```
C:\>sc qc sharedaccess				# Displays config for SharedAccess 
[SC] GetServiceConfig Success

SERVICE NAME: SHAREDACCESS
	TYPE:		: 20  Win32_Share_Process
	START_TYPE:	: 2   Auto_Start
---------------------------------------------
```

> **sc config**

- Change configuration settings for services
- Takes the service key name as an argument
- Requires at least one other option to be specified

```
C:\>sc config sharedaccess start= demand		# Changes start to demand (manual)
```


> **sc getdisplayname**

- Helpful if you need to know the display name for a service when you only know the service key name

```
C:\>sc getdisplayname DHCP
[SC] GetServiceDisplayName Success Name = “DHCP Client”
```

> **sc getkeyname**
- Helpful if you need to know the service key name for a service when you only know the display name

```
C:\>sc getkeyname “DHCP Client”
[SC] GetServiceKeyName Success Name = DHPC
```

> **sc start**

- Starts a service (Must use Service Name)

```
C:\>sc start dhcp       # Starts dhcp serivce.
```

> **sc stop**

- Stops a service (Must use Service Name)

```
C:\>sc stop dhcp		# Stops dhcp service.
```

---
---
---
## **net**

> **start**

- Starts specified service using either the display name or key name
- Without arguments, lists display names of all running services

```
C:\>net help start 		    # Display detailed help information

C:\>net start 			    # Lists running services by their display name

C:\>net start "net logon" 	# Starts the Net Logon service
```

> **stop**

- Stops running services

```
C:\>net stop “net logon”	# Stops the Net Logon service
```