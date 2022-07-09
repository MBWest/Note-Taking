# PowerShell - The Pipeline

> ## **Piping Commands**

- Allows the stringing of powerful “one-liners” to do complex tasks
- When sending output over the pipeline, the receiving cmdlet/function must know how to work with it

```PowerShell
C:\Users\Matthew> $PSVersionTable | fl *


Name  : PSVersion
Key   : PSVersion
Value : 5.1.22000.653

Name  : PSEdition
Key   : PSEdition
Value : Desktop

Name  : PSCompatibleVersions
Key   : PSCompatibleVersions
Value : {1.0, 2.0, 3.0, 4.0...}

Name  : BuildVersion
Key   : BuildVersion
Value : 10.0.22000.653
```