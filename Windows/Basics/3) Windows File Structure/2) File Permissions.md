# File Systems – NTFS Permissions

> ### **NTFS Permissions**
- Basic Permissions: Read, Read and Execute, Write, Modify, List Folder Contents, and Full Control
- Advanced Permissions: available for more granular control
- Applied to every file and folder stored on an NTFS-formatted volume
- Can be inherited from a root folder to the files and subfolders beneath

## **NTFS – Determining a user’s level of access to something**
- If a file is accessed locally, only the NTFS permissions are used
- If a file is accessed remotely, NTFS and share permissions are both used. The most restrictive permission applies first.
- User permissions are cumulative with the group permissions that they are a member of.
- Inherited Permissions: inherited from a parent folder
- Explicit Permissions: assigned directly to a file/folder. Takes precedence over inherited permissions.

```
Explicit Deny > Explicit Allow > Inherited Deny > Inherited Allow
```
> ### **NTFS File/Folder Permissions**

| **Permissions** | **Basic Full Control** | **Basic Modify** | **Basic Read & Execute** | **Basic List Folder Contents** | **Basic Read** | **Basic Write** |
|-----------------|:----------------------:|:----------------:|:------------------------:|:------------------------------:|:--------------:|:---------------:|
|**Travers Folder/Execute File**|`X`|`X`|`X`|`X`|||
|**List Folder/Read Data**|`X`|`X`|`X`|`X`|`X`||
|**Read Attributes**|`X`|`X`|`X`|`X`|`X`||
|**Read Extended Attributes**|`X`|`X`|`X`|`X`|`X`||
|**Create Files/Write Data**|`X`|`X`||||`X`|
|**Create Folder/Append Data**|`X`|`X`||||`X`|
|**Write Attributes**|`X`|`X`||||`X`|
|**Write Extend Attributes**|`X`|`X`||||`X`|
|**Delete Subfolders and Files**|`X`||||||
|**Delete**|`X`|`X`|||||
|**Read Permissions**|`X`|`X`|`X`|`X`|`X`|`X`|
|**Change Permissions**|`X`||||||
|**Take Ownership**|`X`||||||
|**Synchronize**|`X`|`X`|`X`|`X`|`X`|`X`|

---

## **NTFS Permissions - Copy, Move, & Inheritance**

> ### **Copying within a NTFS partition**
- Creates a new file which inherits permissions of target folder

> ### **Moving across a NTFS partition**
- Creates a new file and deletes the old one and Inherits the target folders permissions

> ### **Moving within a NTFS partition**
- Does not create a new file, updates location in directory and file keeps its original permissions

> ### **Moving from NTFS partition to FAT partition**
- Do not retain their attributes or security descriptors
- Do retain their long file names


---
---
---
## **Share Permissions**
- Less granular than NTFS permissions
- Full Control, Change, Read
- Only applies to files on a network share
