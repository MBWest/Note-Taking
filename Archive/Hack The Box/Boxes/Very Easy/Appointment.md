# Appointment Tasks

## TASK 1

What does the acronym SQL stand for?

`Structured Query Language`

## TASK 2

What is one of the most common type of SQL vulnerabilities?

## TASK 3

What does PII stand for?

## TASK 4

What does the OWASP Top 10 list name the classification for this vulnerability?

## TASK 5

What service and version are running on port 80 of the target?

## TASK 6

What is the standard port used for the HTTPS protocol?

## TASK 7

What is one luck-based method of exploiting login pages?

## TASK 8

What is a folder called in web-application terminology?

## TASK 9

What response code is given for "Not Found" errors?

## TASK 10

What switch do we use with Gobuster to specify we're looking to discover directories, and not subdomains?

## TASK 11

What symbol do we use to comment out parts of the code?

## SUBMIT FLAG

Submit root flag

# Appointment

## Ping Box 

ping 10.129.92.228

## Make a new directory

mkdir -p htb/Appointment/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Appointment/nmap/initial 10.129.92.228

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

    sudo nmap -sC -sV -O -p- --reason -oA htb/Appointment/nmap/full 10.129.92.228

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

    sudo nmap -sU -O -p- --reason -oA htb/Appointment/nmap/udp 10.129.92.228

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