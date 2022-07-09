# Boot Process

## **BIOS Phase (Preboot)**

> ### **1) The UEFI (Unified Extensible Firmware Interface) performs POST**
- UEFI is essentially the new version of BIOS
- `POST (Power On Self Test)` – Hardware checks

> ### **2) The Master Boot Record (MBR) is read in**
- Identifies where the system partition is, this is used to start the OS

> ### **3) Searches and runs the “bootmgr” file**

---

## **Boot Loader Phase**

> ### **1) Windows Boot Manager**
- Launches Windows Boot Manager
- Reads in the BCD
- Is loaded into HKLM\BCD00000000

> ### **2) Windows Boot Loader**
- Launches Windows Boot Loader
- Finds and starts the Winloader (Winload.exe)

> ### **3) The Boot Manager and Boot Loader work together to load the Kernel into memory**

---

## **Kernel Phase (Windows NT OS Kernel)**

- Loads registry and drivers marked as “BOOT_START”
- Launches the Session Manager (smss.exe)
- User session processes launched
- Launch Services
- Winlogon.exe (logon screen)
- After login, session created for the user



