# Explosion Tasks

## TASK 1

What does the 3-letter acronym RDP stand for?

`Remote Desktop Protocol`

## TASK 2

What is a 3-letter acronym that refers to interaction with the host through a command line interface?

`CLI`

## TASK 3

What about graphical user interface interactions?

`GUI`

## TASK 4

What is the name of an old remote access tool that came without encryption by default?

`telnet`

## TASK 5

What is the concept used to verify the identity of the remote host with SSH connections?

`Public-key Cryptography`

## TASK 6

What is the name of the tool that we can use to initiate a desktop projection to our host using the terminal?

`xfreerdp`

## TASK 7

What is the name of the service running on port 3389 TCP?

`ms-wbt-server`

## TASK 8

What is the switch used to specify the target host's IP address when using xfreerdp?

`/v:`

## SUBMIT FLAG

Submit root flag

![image](https://user-images.githubusercontent.com/87195021/164129959-62c647c3-4177-4e29-99f9-b62a36c36300.png)

# Explosion

## Ping Box 

ping 10.129.92.121

## Make a new directory

mkdir -p htb/Explosion/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Explosion/nmap/initial 10.129.92.121

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
| `445` | microsoft-ds? / |
| `3389` | ms-wbt-server / Microsoft Terminal Services |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Explosion/nmap/full 10.129.92.121

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
| `445` | microsoft-ds? / |
| `3389` | ms-wbt-server / Microsoft Terminal Services |
| `5895` | http / Microsoft HTTPAPI httpd 2.0  |
| `47001` | http / Microsoft HTTPAPI httpd 2.0  |
| `47664-47671` | msrpc / Microsoft Windows RPC |

## Connecting to RPD with xfreerdp

`xfreerdp /v:10.129.92.121 /cert:ignore /u:Administrator`

    /cert:ignore : Specifies to the scrips that all security certificate usage should be
    ignored.
    /u:Administrator : Specifies the login username to be "Administrator".
    /v:{target_IP} : Specifies the target IP of the host we would like to connect to.

![image](https://user-images.githubusercontent.com/87195021/164129842-29660040-c945-4116-9efe-491aebed3f2b.png)

## Box Solved

![image](https://user-images.githubusercontent.com/87195021/164130017-d96e050a-aacb-4110-bfd0-95caa5b892ea.png)