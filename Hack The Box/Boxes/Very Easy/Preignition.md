# Preignition Tasks

## TASK 1

What is considered to be one of the most essential skills to possess as a Penetration Tester?

`dir busting`

## TASK 2

What switch do we use for nmap's scan to specify that we want to perform version detection

`-sV`

## TASK 3

What service type is identified as running on port 80/tcp in our nmap scan?

`http`

## TASK 4

What service name and version of service is running on port 80/tcp in our nmap scan?

`nginx 1.14.2`

## TASK 5

What is a popular directory busting tool we can use to explore hidden web directories and resources?

`gobuster`

## TASK 6

What switch do we use to specify to gobuster we want to perform dir busting specifically?

`dir`

## TASK 7

What page is found during our dir busting activities?

`admin.php`

## TASK 8

What is the status code reported by gobuster upon finding a successful page?

`200`

## SUBMIT FLAG

Submit root flag

![image](https://user-images.githubusercontent.com/87195021/164132912-53043b22-1df2-4ea8-a8a5-d548b03e38c0.png)

# Preignition

## Ping Box 

ping 10.129.92.131

## Make a new directory

mkdir -p htb/Preignition/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/Preignition/nmap/initial 10.129.92.131

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
| `80` | http / nginx 1.14.2  |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Preignition/nmap/full 10.129.92.131

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
| `80` | http / nginx 1.14.2  |

### Gobuster

Use gobuster to find any directories we are unaware about. 

gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.92.131/

We get back the following results:

`admin.php`

## Exploring admin.php

http://10.129.92.131/admin.php

![image](https://user-images.githubusercontent.com/87195021/164132690-480a5d83-4569-4568-95f1-15d8643d6ba9.png)

Now we need admin credentials. When I’m presented with an enter credentials page, the first thing I try is common credentials (admin/admin, admin/password). If that doesn’t work out, I look for default credentials online that are specific to the technology. Last, I use a password cracker if all else fails.

`admin/admin` got us in!

## Box Sovled

![image](https://user-images.githubusercontent.com/87195021/164132950-37fb1e67-bfa3-48fc-8369-e1e288a8e872.png)