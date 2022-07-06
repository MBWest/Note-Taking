# Linux File Structure - Links

> ## **Hard Link**

- Points to another file/directory
- Share the same inode 
- Changes to target file appear in link
- Cannot span multiple filesystems

> ## **Soft Link (symbolic link)**

- Points to the path of target file, instead of its inode
- A moved/renamed file will break the link 
- Can span multiple filesystems

```text
            Hard-Link
            |
|---|       |
|HDD|-----INODE
|---|       |           
            |
            Original File
            |
            |
            Soft-Link
```