# Example PowerShell Script

## Requirements

- Create a Powershellscript that does the following, only runs PowerShell code, Prompts the user for an absolute filepath.		
- After the value is provided the script checks to see if the file exists, if it does write "File Exists", if it does not ask the user if they want to make a file or folder.		
- If they want a file create a new file named after the users first response, if the user wants a folder create a new folder named after the users first response.		

```PowerShell
$APath = Read-Host -Prompt "Write an absolute path"		
If (Test-Path -LiteralPath  $APath) { 		
           Write-Host "Item Exist"		
}		
Else {		
$FileOrFolder = Read-Host -Prompt "Would you like a file or a folder to be created?"		
          If ($FileOrFolder -eq "Folder") { 		
          New-Item -LiteralPath  $APath -Type Directory		
          }		
Elseif { 		
          If ($FileOrFolder -eq "File") {		
          New-Item -LiteralPath $APath -Type File		
          } 		
}		
}		
Write-Host "Complete"		
```