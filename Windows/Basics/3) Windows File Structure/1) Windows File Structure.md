# Windows File Structure

> ### **What is a file system?**
- A file system is implemented by the OS designed to store and retrieve data when necessary.
- Typically starting from a root drive and expanding out into a tree-like structure.

---
---
---

## **File Systems - FAT**

> ### **File Allocation Table (FAT)**
- File System initially developed for Windows systems starting from MS-DOS up to Windows ME.
- Still in use today due to compatibility w/ a variety of devices and older OS’s. 
- Does not support file compression or security features (i.e. encryption).
- FAT couldn’t support large amounts of data and had several advancements over time:
    - `FAT16` – Formatted drives can support up to 16GB; handles max file size of 2GB
    - `FAT32` – Formatted drives can support up to 16TB; handles max file size of 4GB
    - `exFAT` – Intended for portable media storage allowing max storage size of 512TiB – 64ZiB; handles MUCH larger files sizes than 4GB! (approximately 128 PiB)

---
---
---

## **File Systems - NTFS**

> ### **New Technology File System (NTFS)**
- The primary file system introduced in Windows NT and currently in use on Windows 10. 
- Features:
    - Can support hard drives up to just under 16EB with a max volume size of 256TB.
    - Encrypting File System (EFS) – providing file/folder encryption.
    - User and Group permissions on files/folders 
    - Uses a change log which logs system changes before the changes are made; therefore, allowing a revert to functioning condition.
    - Volume Shadow Copy Service (VSS) – backs up files currently on the system.
    - If sectors become corrupt, they are dynamically remapped so the system does not utilize them.