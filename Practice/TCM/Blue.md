# Blue

## IP

`10.0.2.15`

## Nmap

    Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-20 21:07 EDT

    PORT      STATE SERVICE      VERSION
    135/tcp   open  msrpc        Microsoft Windows RPC
    139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
    445/tcp   open  microsoft-ds Windows 7 Ultimate 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
    49152/tcp open  msrpc        Microsoft Windows RPC
    49153/tcp open  msrpc        Microsoft Windows RPC
    49154/tcp open  msrpc        Microsoft Windows RPC
    49155/tcp open  msrpc        Microsoft Windows RPC
    49156/tcp open  msrpc        Microsoft Windows RPC
    49158/tcp open  msrpc        Microsoft Windows RPC
    
    MAC Address: 08:00:27:2A:95:91 (Oracle VirtualBox virtual NIC)

    Device type: general purpose
    Running: Microsoft Windows 7|2008|8.1
    OS CPE: cpe:/o:microsoft:windows_7::- cpe:/o:microsoft:windows_7::sp1 cpe:/o:microsoft:windows_server_2008::sp1 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_8.1
    OS details: Microsoft Windows 7 SP0 - SP1, Windows Server 2008 SP1, Windows Server 2008 R2, Windows 8, or Windows 8.1 Update 1
    Network Distance: 1 hop
    Service Info: Host: WIN-845Q99OO4PP; OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    |_clock-skew: mean: 1h20m01s, deviation: 2h18m33s, median: 1s
    | smb-os-discovery: 
    |   OS: Windows 7 Ultimate 7601 Service Pack 1 (Windows 7 Ultimate 6.1)
    |   OS CPE: cpe:/o:microsoft:windows_7::sp1
    |   Computer name: WIN-845Q99OO4PP
    |   NetBIOS computer name: WIN-845Q99OO4PP\x00
    |   Workgroup: WORKGROUP\x00
    |_  System time: 2022-06-20T21:08:14-04:00
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode: 
    |   2.1: 
    |_    Message signing enabled but not required
    |_nbstat: NetBIOS name: WIN-845Q99OO4PP, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:2a:95:91 (Oracle VirtualBox virtual NIC)
    | smb2-time: 
    |   date: 2022-06-21T01:08:14
    |_  start_date: 2022-06-21T01:04:30

    TRACEROUTE
    HOP RTT     ADDRESS
    1   0.72 ms 10.0.2.15

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 69.69 seconds
