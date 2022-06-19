# Dancing Tasks

## TASK 1

What does the 3-letter acronym SMB stand for?

`Server Message Block`

## TASK 2

What port does SMB use to operate at?

`445`

## TASK 3

What network communication model does SMB use, architecturally speaking?

`client-server model`

## TASK 4

What is the service name for port 445 that came up in our nmap scan?

`microsoft-ds` 

## TASK 5

What is the tool we use to connect to SMB shares from our Linux distribution?

`smbclient`

## TASK 6

What is the `flag` or `switch` we can use with the SMB tool to `list` the contents of the share?

`-L`

## TASK 7

What is the name of the share we are able to access in the end?

`workshares`

![image](https://user-images.githubusercontent.com/87195021/164082990-fa8c6f3a-38b4-4328-8442-60a321f79b14.png)

## TASK 8

What is the command we can use within the SMB shell to download the files we find?

`get`

## SUBMIT FLAG

Submit root flag

![image](https://user-images.githubusercontent.com/87195021/164084494-f9258eba-fbab-4d41-a2fa-f822f6d23f0f.png)

# Dancing

## Ping Box 

ping 10.129.1.12

## Make a new directory

mkdir -p htb/Dancing/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Dancing/nmap/initial 10.129.1.12

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
| `445` | microsoft-ds? |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Dancing/nmap/full 10.129.1.12

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
| `445` | microsoft-ds? |
| `5985` | http / Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP) |
| `49664-49669` | Microsoft Windows RPC |

## Listing SMB Shares

`smbclient -L 10.129.1.12`

![image](https://user-images.githubusercontent.com/87195021/164082990-fa8c6f3a-38b4-4328-8442-60a321f79b14.png)

## Accessing SMB Shares

`smbclient //10.129.1.12/Workshares`

## Retrieve Flag

`cd James.P`

`ls`

`get flag.txt`

![image](https://user-images.githubusercontent.com/87195021/164084218-075e94c5-1047-4b13-b80b-52a764e01843.png)

## Box Solved

![image](https://user-images.githubusercontent.com/87195021/164084673-e692cac2-5cf0-4487-9f9b-30e4de38c72c.png)
