# Registry Management

| **Command** | **Description** |
|----------|-----------------|
| `Reg Add` | Add keys or values to the registry |
| `Reg Delete` | Delete keys or values to the registry |
| `Reg Query` | Queries the registry |
| `Regedit.exe` | View and edit the Windows Registry |
| `Reg Import` | Imports registry files |
| `Reg Save` | Saves Hive Files |
| `Reg Export` | Exports registry files |
| `Reg Restore` | Restores Hive Files |
| `Reg Unload` | Unloads a Hive file from the registry |
| `Reg Load `| Loads a Hive file to allow editing |
| **EXAMPLES** |
| `Reg Query HKLM /s `| Display HKLM recursively |
| `Reg Query HKLM /s /k /f SAM` | Searches HKLM recursively for the key SAM |
| `Reg Query HKLM /s /e /f Wallpaper` | Searches HKLM recursively for the exact keyword |
| `Reg Add HKLM\SOFTWARE\CWO` | Adds the CWO key to HKLM\SOFTWARE |
| `Reg Add HKLM\SOFTWARE\CWO\1b4` | Adds the 1b4 Key under the HKLM\SOFTWARE\CWO\1b4 |
| `Reg Add HKLM\SOFTWARE\CWO /v "String" /t reg sz /d "Stuff and Things"` | Adds the value with the name "string" type string and data "Stuff and Things"  to the CWO key |
| `Reg Add "RegistryLocation" -v "ValueName"` | Query the value |
