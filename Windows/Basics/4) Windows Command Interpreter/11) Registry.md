# PowerShell - Registry

## **req query**

- Queries the registry

```cmd
C:\>reg query hklm /s			        # Displays HKLM recursively
C:\>reg query hklm /s /k /f SAM		    # Searches HKLM recursively for the Key SAM
C:\>reg query hklm /s /e /f Wallpaper	# Searches HKLM recursively for the exact string Wallpaper 
```					