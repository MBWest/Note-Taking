# Backdoor

## Ping Box 

ping 10.129.131.242

## Make a new directory

mkdir -p htb/Backdoor/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Backdoor/nmap/initial 10.129.131.242

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
| `22` | ssh / OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 |
| `80` | http / Apache/2.4.41 / WordPress 5.8.1 / http-title: Backdoor &#8211; Real-Life |

    Nmap scan report for 10.129.131.242
    Host is up, received echo-reply ttl 63 (0.019s latency).
    PORT   STATE SERVICE REASON         VERSION
    22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 b4:de:43:38:46:57:db:4c:21:3b:69:f3:db:3c:62:88 (RSA)
    |   256 aa:c9:fc:21:0f:3e:f4:ec:6b:35:70:26:22:53:ef:66 (ECDSA)
    |_  256 d2:8b:e4:ec:07:61:aa:ca:f8:ec:1c:f8:8c:c1:f6:e1 (ED25519)
    80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    |_http-generator: WordPress 5.8.1
    |_http-title: Backdoor &#8211; Real-Life

    Network Distance: 2 hops
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Backdoor/nmap/full 10.129.131.242

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
| `22` | ssh / OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 |
| `80` | http / Apache/2.4.41 / WordPress 5.8.1 / http-title: Backdoor &#8211; Real-Life |
| `1337` | waste? |

    Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-20 12:10 BST
    Host is up, received echo-reply ttl 63 (0.0046s latency).
    PORT     STATE SERVICE REASON         VERSION
    22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 b4:de:43:38:46:57:db:4c:21:3b:69:f3:db:3c:62:88 (RSA)
    |   256 aa:c9:fc:21:0f:3e:f4:ec:6b:35:70:26:22:53:ef:66 (ECDSA)
    |_  256 d2:8b:e4:ec:07:61:aa:ca:f8:ec:1c:f8:8c:c1:f6:e1 (ED25519)
    80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: Backdoor &#8211; Real-Life
    |_http-generator: WordPress 5.8.1
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    1337/tcp open  waste?  syn-ack ttl 63

## UDP Scan

Similarly, we run an nmap scan with the -sU flag enabled to run a UDP scan.

    sudo nmap -sU -O -p- --reason -oA htb/Backdoor/nmap/udp 10.129.131.242

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

## Enumeration

To do that, let’s run `Gobuster` to enumerate directories.

### Gobuster

gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.131.242/

We get back the following results:

    /wp-content           (Status: 301) [Size: 321] [--> http://10.129.131.242/wp-content/]
    /wp-includes          (Status: 301) [Size: 322] [--> http://10.129.131.242/wp-includes/]
    /wp-admin             (Status: 301) [Size: 319] [--> http://10.129.131.242/wp-admin/] 
    /server-status        (Status: 403) [Size: 279]

## Gaining an Initial Foothold

Now we need to escalate privileges.

## Privilege Escalation

Find out what privileges you have.

    sudo -l

