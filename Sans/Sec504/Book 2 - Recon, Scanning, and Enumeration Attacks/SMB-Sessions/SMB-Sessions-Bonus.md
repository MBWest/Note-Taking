# Unidentified Scan Target

Your Slingshot Linux VM is configured with an additional scan target that runs in a Docker container. To launch the target, open a terminal and run the gosmbtgt command, as shown here:

    sec504@slingshot:~$ gosmbtgt
    Starting Docker service ..... Done.
    smbd version 4.10.5 started.
    Copyright Andrew Tridgell and the Samba Team 1992-2019
    daemon_ready: daemon 'smbd' finished starting up and ready to serve connections
    nmbd version 4.10.5 started.
    Copyright Andrew Tridgell and the Samba Team 1992-2019
    daemon_ready: daemon 'nmbd' finished starting up and ready to serve connections

Open a new terminal prompt. Using the username erigby and the password weddingrice, identify and enumerate the SMB target system, answering the following questions:

1. What is the IP address of the SMB target server (in the range 172.30.0.2-254)?
2. What is the minimum SMB version permitted by the target server?
3. What other valid username exists on the server?
4. Does the server enforce complex passwords for the second valid username?
5. What is Eleanor Rigby's GoFundMe password?

## Click to see solution - Server IP Address

Identify the server using and Nmap host discovery scan, as shown here:

    sec504@slingshot:~$ nmap -sP 172.30.0.1-254

    Starting Nmap 7.60 ( https://nmap.org ) at 2020-01-18 22:13 UTC
    Nmap scan report for slingshot (172.30.0.1)
    Host is up (0.00016s latency).
    Nmap scan report for 172.30.0.22
    Host is up (0.00044s latency).
    Nmap done: 254 IP addresses (2 hosts up) scanned in 3.22 seconds

In this output, 172.30.0.1 is the Slingshot Linux system (for the container network interface). The 172.30.0.22 server is the target SMB server.

## Click to see solution - Minimum SMB Version

Identify the minimum SMB version on the server using the Nmap -A argument, as shown here:

    sec504@slingshot:~$ nmap -A 172.30.0.22

    Starting Nmap 7.60 ( https://nmap.org ) at 2020-01-18 22:14 UTC
    Nmap scan report for 172.30.0.22
    Host is up (0.00013s latency).
    Not shown: 998 closed ports
    PORT    STATE SERVICE       VERSION
    139/tcp open  netbios-ssn?
    | fingerprint-strings:
    |   SMBProgNeg:
    |_    SMBr
    445/tcp open  microsoft-ds?
    | fingerprint-strings:
    |   SMBProgNeg:
    |_    SMBr
    2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
    ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
    SF-Port139-TCP:V=7.60%I=7%D=1/18%Time=5E23835B%P=x86_64-pc-linux-gnu%r(SMB
    SF:ProgNeg,29,"\0\0\0%\xffSMBr\0\0\0\0\x88\x03@\0\0\0\0\0\0\0\0\0\0\0\0\0\
    SF:0@\x06\0\0\x01\0\x01\xff\xff\0\0");
    ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
    SF-Port445-TCP:V=7.60%I=7%D=1/18%Time=5E238356%P=x86_64-pc-linux-gnu%r(SMB
    SF:ProgNeg,29,"\0\0\0%\xffSMBr\0\0\0\0\x88\x03@\0\0\0\0\0\0\0\0\0\0\0\0\0\
    SF:0@\x06\0\0\x01\0\x01\xff\xff\0\0");

    Host script results:
    |_nbstat: NetBIOS name: SAMBASERV, NetBIOS user: , NetBIOS MAC:  (unknown)
    | smb2-security-mode:
    |   2.10:
    |_    Message signing enabled but not required
    |_smb2-time: Protocol negotiation failed (SMB2)

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 122.83 seconds

Note that this scan will take a few minutes to complete. 

In this output, we see that Nmap has trouble recognizing the server response data, though the subsequent Nmap Script Engine (NSE) results indicate it as a Samba server that supports the SMBv2 protocol.

Optionally, you can enumerate the SMB version using the smbclient tool as an authenticated user with the -m argument, as shown here:

    sec504@slingshot:~$ smbclient -U erigby -L 172.30.0.22 -m SMB3
    WARNING: The "syslog" option is deprecated
    Enter erigby's password: weddingrice
    Domain=[SAMBASERV] OS=[] Server=[]

        Sharename       Type      Comment
        ---------       ----      -------
        data            Disk      Data
        IPC$            IPC       IPC Service (Samba 4.11.4)
    ...
    sec504@slingshot:~$ smbclient -U erigby -L 172.30.0.22 -m SMB2
    WARNING: The "syslog" option is deprecated
    Enter erigby's password: weddingrice
    Domain=[SAMBASERV] OS=[] Server=[]

        Sharename       Type      Comment
        ---------       ----      -------
        data            Disk      Data
        IPC$            IPC       IPC Service (Samba 4.11.4)
    ...
    sec504@slingshot:~$ smbclient -U erigby -L 172.30.0.22 -m NT1
    WARNING: The "syslog" option is deprecated
    protocol negotiation failed: NT_STATUS_INVALID_NETWORK_RESPONSE

In this output, we see that the SMB target server supports SMBv3 and SMBv2, but does not support the NTv1 SMB version (smbclient's notation for SMBv1).

###  Click to see solution - Other Valid Username

To enumerate the valid users on the target server, use the erigby/weddingrice username and password with the rpcclient utility, as shown here:

    sec504@slingshot:~$ rpcclient 172.30.0.22 -U erigby
    Enter erigby's password: weddingrice
    rpcclient $> enumdomusers
    user:[erigby] rid:[0x3e8]
    user:[fmackenzie] rid:[0x3e9]

Here the rpcclient enumdomusers command enumerates local Samba/Linux users, including a previously unidentified user fmackenzie.
Click to see solution - Password Complexity Policy

To enumerate information about password policies on the server, use the rpcclient getdompwinfo utility, as shown here:

    rpcclient $> getdompwinfo
    min_password_length: 5
    password_properties: 0x00000000
    rpcclient $> getusrdompwinfo 1000
    min_password_length: 5
        &info.password_properties: 0xb7d1c734 (3083978548)
            0: DOMAIN_PASSWORD_COMPLEX
            0: DOMAIN_PASSWORD_NO_ANON_CHANGE
            1: DOMAIN_PASSWORD_NO_CLEAR_CHANGE
            0: DOMAIN_PASSWORD_LOCKOUT_ADMINS
            1: DOMAIN_PASSWORD_STORE_CLEARTEXT
            1: DOMAIN_REFUSE_PASSWORD_CHANGE

In this output, we see that getdompwinfo reveals the minimum password length of 5 (the default for Samba servers). Further, running getusrdompwinfo followed by a user RID (the first user in a Samba server is 1000, which can be determined with queryuser) indicates a collection of password settings, including that the server does not enforce a password complexity policy (DOMAIN_PASSWORD_COMPLEX is 0).

Before moving on to the next section, close rpcclient by issuing a CTRL+C at the rpcclient $> prompt.

## Click to see solution - Eleanor Rigby's GoFundMe Password

To examine the contents of the share, use the smbclient tool, followed by the server IP address and share name, as shown here:

    sec504@slingshot:~$ smbclient -U erigby //172.30.0.22/data -m SMB2
    WARNING: The "syslog" option is deprecated
    Enter erigby's password: weddingrice
    Try "help" to get a list of possible commands.
    smb: \>

From the smb :\> prompt, you can use common FTP-like commands to list files (ls), change directories (cd), download files (get filename), and upload files (put filename).

Explore the contents of the files on the share to retrieve Eleanor Rigby's password, as shown here:

    smb: \> ls
    .                                   D        0  Mon Jul 15 17:27:29 2019
    ..                                  D        0  Mon Jul 15 17:27:43 2019
    lyrics.txt                          N      963  Mon Jul 15 16:59:38 2019
    StPetersChurchWoolton-Liverpool.jpg      N   158146  Mon Jul 15 16:59:38 2019
    1Password                           D        0  Mon Jul 15 17:27:29 2019

            23671960 blocks of size 1024. 8607472 blocks available
    smb: \> cd 1Password
    smb: \1Password\> ls
    .                                   D        0  Mon Jul 15 17:27:29 2019
    ..                                  D        0  Mon Jul 15 17:27:29 2019
    1Password.1pif                      D        0  Mon Jul 15 17:27:29 2019

            23671960 blocks of size 1024. 8607472 blocks available
    smb: \1Password\> cd 1Password.1pif
    smb: \1Password\1Password.1pif\> ls
    .                                   D        0  Mon Jul 15 17:27:29 2019
    ..                                  D        0  Mon Jul 15 17:27:29 2019
    data.1pif                           N      684  Mon Jul 15 16:59:38 2019

            23671960 blocks of size 1024. 8607472 blocks available
    smb: \1Password\1Password.1pif\> get data.1pif
    getting file \1Password\1Password.1pif\data.1pif of size 684 as data.1pif (334.0 KiloBytes/sec) (average 334.0 KiloBytes/sec)
    smb: \1Password\1Password.1pif\> exit

    The data.1pif file is a JSON-formatted ASCII file. Display the contents of the file with the cat utility, as shown here:

    sec504@slingshot:~$ cat data.1pif
    {"uuid":"gm3xduxanfcsriizik2hvzdkca","updatedAt":1563194790,"locationKey":"gofund
    me.com","securityLevel":"SL5","openContents":{"tags":["eleanor rigby","the beatle
    s"]},"contentsHash":"67587a25","title":"GoFundMe","location":"https:\/\/ww.gofund
    me.com","secureContents":{"fields":[{"value":"erigby","name":"username","type":"T
    ","designation":"username"},{"value":"classic*1","name":"password","type":"P","de
    signation":"password"}],"notesPlain":"Church Sexton Fundraiser","sections":[{"tit
    le":"Related Items","name":"linked items"}],"URLs":[{"label":"","url":"https:\/\/
    ww.gofundme.com"}]},"createdAt":1563194790,"typeName":"webforms.WebForm"}
    ***5642bee8-a5ff-11dc-8314-0800200c9a66***

**Terminate the Container**

At the end of the exercise, return to the terminal window where you ran gosmbtgt and press CTRL+C to terminal the container instance.

## Additional Resources

This lab was designed to look at local workstation passwords. However, doing this on a domain is also straightforward. Beau Bullock of Black Hills Information Security has created a password guessing script that can be used on a domain. It can be found on his GitHub page.

This script is powerful for identifying weak passwords in an environment. Before trying to use it in your own environment, know that it can easily trigger account lockout. Always get permission before applying attack scripts to evaluate your organization's security, and be aware of the potential for account lockout as a negative consequence of testing.