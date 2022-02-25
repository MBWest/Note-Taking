# Network File Sharing (NFS)

## Network File System (NFS) 
- Default Port 2049
- Remote access to file system
- Supported by Linux, UNIX, Windows
- Packages
- Name Resolution

## NFS Server Configuration
- **/etc/exports/** - Which file systems are exported, permissions and which host may mount them
- **/etc/host.allow** - Which hosts are permitted to mount exported file systems
- **/etc/host.deny** - Which host are explicity denied permissions to mount exported file systems

## Mounting
Mount an NFS file system to access it
     - *Example* > mount -t nfs computer:fs /mount_point