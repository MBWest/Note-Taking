## Fawn Tasks

## TASK 1

What does the 3-letter acronym FTP stand for?

`file transfer protocol`

## TASK 2

What communication model does FTP use, architecturally speaking?

`client-server model`

## TASK 3

What is the name of one popular GUI FTP program?

`filezilla`

## TASK 4

Which port is the FTP service active on usually?

`21 TCP`

## TASK 5

What acronym is used for the secure version of FTP?

`SFTP`

## TASK 6

What is the command we can use to test our connection to the target?

`ping`

## TASK 7

From your scans, what version is FTP running on the target?

`vsftpd 3.0.3`

## TASK 8

From your scans, what OS type is running on the target?

`unix`

## SUBMIT FLAG

Submit root flag

![image](https://user-images.githubusercontent.com/87195021/164080298-f30ad499-cb58-4303-a1b2-e3abfa0c94a4.png)

# Fawn

## Ping Box 

ping [10.129.92.31]

## Make a new directory

mkdir -p htb/Fawn/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Fawn/nmap/initial 10.129.92.31

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
| `21` | FTP / vsftpd 3.0.3 |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Fawn/nmap/full 10.129.92.31

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
| `21` | FTP / vsftpd 3.0.3 |

**Anonymous FTP login is allowed.**

![image](https://user-images.githubusercontent.com/87195021/164079450-002d5097-5cd6-4fc1-9a12-38cfca7bfcd5.png)

## Login to FTP 

![image](https://user-images.githubusercontent.com/87195021/164080130-450451c2-a108-4ae7-83d0-75d0ebf77ee5.png)

## Box Solved

![image](https://user-images.githubusercontent.com/87195021/164080372-44f034a2-c38e-476b-9b3d-f7ac73c34443.png)