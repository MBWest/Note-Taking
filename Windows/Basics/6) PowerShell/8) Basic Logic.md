# PowerShell - Basic Logic

> ## **If, elseif, else**

- Tests to see if a condition is True. If True, do a thing. If false, do something else
- The below example was ran 3 times, with a new value being provided via Read-Host each time

```PowerShell
$promptedVariable = Read-Host "Wat do you want to eat?"
if ($promptedVariable -eq "taco") {
    Write-Output "You want a taco."
} elseif ($promptedVariable -eq "burrito") {
    Write-Output "You want a burrito"
} else {
    Write-Output "You don't want a taco or burrito..."
}
```


---

> ## **While**

- Do things when a certain condition is True. Once the condition is false, stop doing the things. Will run forever if the condition does not change

```PowerShell
$cantstopwontstop = "yes"
while ($cantstopwontstop -eq "yes") {
    Write-Output "This will run forever"
}
```
- The below example shows a 2-minute timer.

```PowerShell
$startTime = Get-Date
while ($startTime.AddMinutes(2) -gt $(Get-Date)) {
    Write-Host "The current time is $(Get-Date)"
    Write-Host "The start time was $startTime"
    Write-Host "Sleeping for 30 secs"
    Start-Sleep - Seconds 30
} 
Write-Host "While loop is over, our timer is up."
```