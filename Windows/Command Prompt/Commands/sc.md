# sc

 Obtain Windows service information

 ## Examples

| **Command** | **Description** |
|-------------|-----------------|
| `sc query "winmgmt"` | Query the status of the winmgmt service |
| `sc queryex "winmgmt"` | Get the extended status of the winmgmt service |
| `sc qc winmgmt` | Get the configuration information for the winmgmt service |
| `sc quert state= all` | Query the status of all services |
| `sc query state= all \| find /i "installer"` | Find the OS's Installer service |
| `sc getkeyname "Windows Installer"` | What is the state and the start time of the OS's Installer service |
| `Sc query state= all \| find /i "Diagnostic Policy", sc stop DPS` | Find the Diagnostic Policy service and stop it |
| `sc config DPS start= demand, sc stop DPS` | Configure the Diagnostic Policy service to manual start then restart it |
| `sc query state= all \| find /i "Adobe Acorbat", sc config AdobeARMService start = disabled` | Findthe Adobe Acrobat service, make it so thats it is disabled |