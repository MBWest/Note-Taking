# smbclient

## Example

`smbclient -L \\\\[ip]\\[Sharename]`

`-L` Lists Files

## HTB Examples

Shares
SMB allows users and administrators to share folders and make them accessible remotely by other users. Often these shares have files in them that contain sensitive information such as passwords. A tool that can enumerate and interact with SMB shares is smbclient. The `-L` flag specifies that we want to retrieve a list of available shares on the remote host, while `-N` suppresses the password prompt.

### Shares
    MBWest@htb[/htb]$ smbclient -N -L \\\\10.129.42.253

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        users           Disk      
        IPC$            IPC       IPC Service (gs-svcscan server (Samba, Ubuntu))
    SMB1 disabled -- no workgroup available

This reveals the non-default share users. Let us attempt to connect as the guest user.

    MBWest@htb[/htb]$ smbclient \\\\10.129.42.253\\users

    Enter WORKGROUP\users's password: 
    Try "help" to get a list of possible commands.

    smb: \> ls
    NT_STATUS_ACCESS_DENIED listing \*

    smb: \> exit

The `ls` command resulted in an access denied message, indicating that guest access is not permitted. Let us try again using credentials for the user bob (`bob:Welcome1`).

    MBWest@htb[/htb]$ smbclient -U bob \\\\10.129.42.253\\users

    Enter WORKGROUP\bob's password: 
    Try "help" to get a list of possible commands.

    smb: \> ls
    .                                   D        0  Thu Feb 25 16:42:23 2021
    ..                                  D        0  Thu Feb 25 15:05:31 2021
    bob                                 D        0  Thu Feb 25 16:42:23 2021

            4062912 blocks of size 1024. 1332480 blocks available
            
    smb: \> cd bob

    smb: \bob\> ls
    .                                   D        0  Thu Feb 25 16:42:23 2021
    ..                                  D        0  Thu Feb 25 16:42:23 2021
    passwords.txt                       N      156  Thu Feb 25 16:42:23 2021

            4062912 blocks of size 1024. 1332480 blocks available
            
    smb: \bob\> get passwords.txt 
    getting file \bob\passwords.txt of size 156 as passwords.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)