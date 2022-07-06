# Linux File Structure - Inodes

- A file is stored in two different parts
    - Data blocks contain the contents of the file
    - Inodes contain the metadata about the file
        - Permissions
        - Owner/Group ID
        - File size
        - Number of links to the file 
        - Timestamps 
        - Pointers to data blocks storing the file’s contents 
- Always unique on their respective partitions
- Directories are files that contain the table that links filenames to inodes 