# [BOXNAME]

## Ping Box 

ping [IP]

## Make a new directory

mkdir -p htb/[BOXNAME]/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/[BOXNAME]/nmap/initial [IP]

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
| `` |  |
| `` |  |
| `` |  |
| `` |  |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/[BOXNAME]/nmap/full [IP]

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
| `` |  |
| `` |  |
| `` |  |
| `` |  |

## UDP Scan

Similarly, we run an nmap scan with the -sU flag enabled to run a UDP scan.

    sudo nmap -sU -O -p- --reason -oA htb/[BOXNAME]/nmap/udp [IP]

| **Flag** | **Description** |
| --------------|-------------------|
| `-sU` | Detect UDP |
| `-O` | Detect OS |
| `-p-` |All Ports |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port** | **Description** |
| --------------|-------------------|
| `` |  |
| `` |  |
| `` |  |
| `` |  |

