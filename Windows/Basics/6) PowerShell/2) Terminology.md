# PowerShell - Terminology

## **Terms**

> **Module**
- Package that contains PowerShell commands, such as cmdlets, providers, functions, workflows, variables, and aliases

> **Cmdlet**
- Compiled code written in a .NET language such as C#

> **Function**
- A list of PowerShell statements that has an assigned, callable name

> **Script**
- Plain text file ending in a .ps1 file extension that contains one or more PowerShell commands

---
---
---

## **Verb-Noun Syntax**

- All PowerShell `functions/cmdlets` are written in a verb-noun syntax
    - Finding and using new cmdlets is far easier in PowerShell
        - Want to find commands with “tcp” in the name? `Get-Command “*tcp*”`
        - Want to find commands for Services? `Get-Command –Noun Service`
        - Want to find commands that “Get” information? `Get-Command –Verb Get`
    - Want to find Services? `Get-Service`
    - Want to stop Services? `Stop-Service`
    - Want to modify Services? `Set-Service`
    - Want to remove Services? `Remove-Service` (available in PowerShell 7.0+)
- Verb/Noun syntax is a standard, not a language specific requirement. You can name your own custom functions however you want

---
---
---

## **Objects**

- Exist in all object-oriented programming languages
- A collection of data that represents an item
- Every action you take in PowerShell occurs within the context of objects
- To view the type of an object, run the Get-Member cmdlet

```Powershell
C:\Windows\System32> Get-Process notepad++ | Get-Member

    TypeName: System.Diagnostics.Process
                                    ^
    The type of object is shown here^
```

### For more info run the following command

```PowerShell
Get-Help about_objects
```

---
---
---

## **Properties**

- Data that is associated with an object
- Different types of objects have different properties
    - `Process` objects have a `PID` property, `Service` objects do not
- Only a few properties are shown by default after running a cmdlet
- All Property `names` and `types` can be viewed by using `Get-Member`
- All Property `names` and `values` can be viewed by using `Format-List *`

```PowerShell
C:\Users\Matthew> Get-Process -Name cmd

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
     70       6     5180       5124       0.02   5288   7 cmd
```

---
---
---

## **Parameters**

- Options provided by users to modify how a function, cmdlet, or script will operate
- A Parameter name is preceded by a `hyphen`, not a forward slash
- Some Parameters do not require/accept a parameter value, while others will require one
- Requirements for parameters vary depending on the cmdlet being used
- Default Parameters
    - Some Parameters have a default value if one isn’t provided by the user
    - Example: a `-ComputerName parameter` will commonly default to the local hostname if it isn’t specified

### For more info run the following command

```PowerShell
Get-Help about_objects
```

---
---
---

## **Variables**

> **User Created Variables**
    - Variables defined by the user to store data

```PowerShell
C:\Users\Matthew> $my_custom_var = Get-Process -Name cmd
C:\Users\Matthew> $my_custom_var

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
     70       6     3128       5104       0.02   5288   7 cmd
```

### For more info run the following command

```PowerShell
Get-Help about_objects
```

> **Automatic Variables**

- Variables defined and used by PowerShell that cannot be changed
- The below variable holds the current version information for PowerShell

```PowerShell
C:\Users\Matthew> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.22000.653
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.22000.653
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1


C:\Users\Matthew> $PSVersionTable = "nothing"
Cannot overwrite variable PSVersionTable because it is read-only or constant.
At line:1 char:1
+ $PSVersionTable = "nothing"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (PSVersionTable:String) [], SessionStateUnauthorizedAccessException
    + FullyQualifiedErrorId : VariableNotWritable
```

> **Preference Variables**

- Variables defined and used by PowerShell that modify user preferences – can be modified by the user
- The below example demonstrates changing $MaximumHistoryCount

```PowerShell
C:\Users\Matthew> history

Id CommandLine
-- -----------
1 $my_custom_var = Get-Process -Name cmd
2 $my_custom_var
3 $PSVersionTable
4 $PSVersionTable = "nothing"
5 clear


C:\Users\Matthew> $MaximumHistoryCount = 1
C:\Users\Matthew> history

Id CommandLine
-- -----------
7 $MaximumHistoryCount = 1


C:\Users\Matthew>
```
---
---
---

## **Aliases**

- Like most shell environments, PowerShell supports aliases for commonly used cmdlets and functions

```PowerShell
C:\Users\Matthew> Get-Command -noun Alias

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Export-Alias                                       3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-Alias                                          3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Import-Alias                                       3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          New-Alias                                          3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Set-Alias                                          3.1.0.0    Microsoft.PowerShell.Utility
```

