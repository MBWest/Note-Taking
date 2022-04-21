# Autoruns

Identifies auto startup, registry keys, scheduled tasks, and other autorun components. 

## Entries

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Runonce
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunonceEx

## Registry Query CLI

- reg query HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\run
- reg query HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\runonce
- reg query HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\runonceex