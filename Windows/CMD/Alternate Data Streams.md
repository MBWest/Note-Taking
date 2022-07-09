# Alternate Data Stream

> ## **Examples**

| **Description** | **Command** |
|----------|-----------------|
| `Add Content` | Echo "ThisText" >> C:\User\Desktop\file.txt:NameofAS | 
| `Display Content` | More < C:\AbsoluteFilePath | 
| `Find ADS Files` | Dir /a /r \| findstr "$DATA" [or] dir /a /r /s \| findstr /i "\$DATA" [or] dir /a /r (Filepath) | 
