# Example Problems/Questions

`A comment was given after the last system reboot; Provide the text`

```PowerShell
Get-WinEvent -FilterHashtable @{logname = 'System'; id = 1074} | Format-List
```
------

`There are two Firewall Rules that have "Firefox" in the display name. Complete the following:`

- Change the Action in each rule to block
- Retrieves Firewall Rules	
- Allows searching by display name "*Firefox*"	
- Sets Firewall Rules	
- Changes the action property to "Block	

```Powershell
Get-NetFirewallRule -Displayname "*Firefox*" | Set-NetFirewallRule -Action Block
```

------

`Take a screenshot of the updated rules in Powershell` 

```PowerShell
Get-NetFirewallRule -Displayname "*Firefox*" | Format-List -Property DisplayName, Action
```

------

`Something is writing multiple text files to the system every minute. Find the location of these files.`

```PowerShell
Get-ChildItem -Force -Recurse 2> Errors.txt | Where -Property CreationTime -GT (Get-Date).addminutes(-3)
```

------

`There is .log file on the system with an Alternate Data Stream attached to it. Find the ADS.`

```PowerShell
Get-ChildItem -Force -Recurse *.log 2> error.txt | Get-Item -Stream * | Where -Property  PSPath -Notlike "*DATA*"
```

------

`A New service was created when you ran the script. Find the logs documents its creation!`

```PowerShell
Get-EventLog System -After "10 August 2021 12:25" -Before "15 August 2021 12:35" | Format-Table -Wrap
```

------

`A bunch of new firewall rules with the name "Backdoor" were created. How many were created? Provide a file with all the port numbers.`

```PowerShell
Get-NetFirewallRule -DisplayName Backdoor | Measure
Get-NetFirewallRule -DisplayName Backdoor | Get-NetFirewallPortFilter | Select LocalPort
```