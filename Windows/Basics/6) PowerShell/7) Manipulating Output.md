# PowerShell - Manipulating Output

## **Select-Object**
- The `Select-Object` cmdlet selects specified properties of an object or set of objects. It can also select unique objects, a specified number of objects, or objects in a specified position in an array

```PowerShell
C:\Users\Matthew> Get-Process cmd | Select-Object -Property name,threads,StartTime

Name Threads StartTime
---- ------- ---------
cmd  {824}   6/29/2022 3:48:30 PM
```

---
---
---

## **Where-Object**

- The `Where-Object` cmdlet selects objects that have particular property values from the collection of objects that are passed to it
- Sometimes cmdlets can filter by themselves, but this can be limited. Where-Object is the solution in those cases

```PowerShell
PS C:\Users\Matthew> Get-Command -Type Cmdlet | Where-Object -Property Verb -EQ Get

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Get-Acl                                            3.0.0.0    Microsoft.PowerShell.Security
Cmdlet          Get-Alias                                          3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-AppProvisionedSharedPackageContainer           3.0        Dism
...Output truncated due to length...
```

### **Where-Object Help**

- Comparison Operators
- Used to compare values – is x equal to y, is date1 older than date2, etc
- Additional documentation available through help

```PowerShell
Get-Help about_Comparison_Operators
```

- Comparison operators let you compare values or finding values that match
specified patterns. PowerShell includes the following comparison operators: 

| **Type** | **Operators** | **Description** |
|----------|---------------|-----------------|
|  `Equality` |     -eq           | equals |
|           |     -ne           | not equals |
|           |     -gt           | greater than |
|           |     -ge           | greater than or equal |
|           |     -lt           | less than |
|           |     -le           | less than or equal |
|  `Matching` |     -like         | string matches wildcard pattern |
|           |     -notlike      | string does not match wildcard pattern |
|           |     -match        | string matches regex pattern |
|           |     -notmatch     | string does not match regex pattern |
|  `Replacement`|   -replace      | replaces strings matching a regex pattern |
|  `Containment`|   -contains     | collection contains a value |
|             |   -notcontains  | collection does not contain a value |
|             |   -in           | value is in a collection |
|             |   -notin        | value is not in a collection |
|  `Type`       |   -is           | both objects are the same type |
|             |   -isnot        | the objects are not the same type |