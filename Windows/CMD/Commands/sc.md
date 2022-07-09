# sc

- Obtain Windows service information

> ## **query**

- Lists all active services by default

> ### **Examples**


| **Command** | **Description** |
|-------------|-----------------|
| `sc query` | Lists all active services |
| `sc query state= inactive` | Lists all inactive services |
| `sc query state= all` | Lists all services |
| `sc query state= all \| find /I “firewall”` | Will find string “firewall” |
| `sc query "winmgmt"` | Query the status of the winmgmt service |
| `sc queryex "winmgmt"` | Get the extended status of the winmgmt service |
| `sc query state= all` | Query the status of all services |
| `sc query state= all \| find /i "installer"` | Find the OS's Installer service |
| `sc query state= all \| find /i "Adobe Acorbat", sc config AdobeARMService start = disabled` | Findthe Adobe Acrobat service, make it so thats it is disabled |
| `Sc query state= all \| find /i "Diagnostic Policy", sc stop DPS` | Find the Diagnostic Policy service and stop it |


---

> ## **qc**

- Queries the configuration of a service 

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc qc sharedaccess` | Displays config for SharedAccess |
| `sc qc winmgmt` | Get the configuration information for the winmgmt service |

---

> ## **config**

- Change configuration settings for services

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc config sharedaccess start= demand` | Changes start to demand (manual) |\

---

> ## **getdisplayname**

- Helpful if you need to know the display name for a service when you only know the service key name 

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc getdisplayname DHCP` |  Displays display name for DHCP | 


---

> ## **getkeyname**

- Helpful if you need to know the service key name for a service when you only know the display name

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc getkeyname “DHCP Client”` | Displays the service key name for DHCP Client |
| `sc getkeyname "Windows Installer"` | What is the state and the start time of the OS's Installer service |


---

> ## **start**

- Starts a service (Must use Service Name)

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc start dhcp` | Starts dhcp service |


---

> ## **stop**

- Starts a service (Must use Service Name)

> ### **Examples**

| **Command** | **Description** |
|-------------|-----------------|
| `sc stop dhcp` | Stops dhcp service |