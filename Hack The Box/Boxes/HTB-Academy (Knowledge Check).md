# knowledgecheck

mkdir -p htb/knowledgecheck/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA htb/knowledgecheck/nmap/initial 10.129.242.186

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
| `22` | SSH / OpenSSH 8.2p1  |
| `80` | HTTP / Apache httpd 2.4.41 |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/knowledgecheck/nmap/full 10.129.242.186

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
| `22` | SSH / OpenSSH 8.2p1  |
| `80` | HTTP / Apache httpd 2.4.41 |

## UDP Scan

Similarly, we run an nmap scan with the -sU flag enabled to run a UDP scan.

    sudo nmap -sU -O -p- --reason -oA htb/knowledgecheck/nmap/udp 10.129.242.186

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

Visit the site in the browser. 

![image](https://user-images.githubusercontent.com/87195021/162631722-1605301a-b761-459e-83d0-ce0008531499.png)

Nothing useful there. `Ctrl+u` for page source.

Nothing Useful there. 

In order to see if this application is vulnerable, we need to find its version number. To do that, let’s run `Gobuster` to enumerate directories.

### Gobuster

gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.242.186

We get back the following results:

![image](https://user-images.githubusercontent.com/87195021/162631839-702102b4-863e-4e6f-8d4c-475dbf98cea4.png)

Lookthing through the results, in the /data/cache folder there is a file that reads:

    {"status":"0","latest":"3.3.16","your_version":"3.3.15","message":"You have an old version - please upgrade"}

Use searchsploit to look for known exploits:

![image](https://user-images.githubusercontent.com/87195021/162633504-f1e0e863-c579-4575-a01e-683399288f2c.png)

## Gaining an Initial Foothold

Load up metasploit and search for `getsimplecms`, you will see two options. We will be using the following:

    multi/http/getsimplecms_unauth_code_exec

Change all the necessary options (RHOSTS, LHOST, etc...) and type `exploit`

We have access!

![image](https://user-images.githubusercontent.com/87195021/162633671-af03e833-933d-4c7c-ac98-a8384a7fd5c6.png)

Find the user flag in the /home/mrb3n/user.txt file

![image](https://user-images.githubusercontent.com/87195021/162633764-9c0f039a-93ca-42af-945b-d1581ac852db.png)

Now we need to escalate privileges.

## Privilege Escalation

Let’s first upgrade to a better shell. Python is not installed but python 3 is.

    python3 -c 'import pty; pty.spawn("/bin/bash")'

Find out what privileges you have.

    sudo -l

![image](https://user-images.githubusercontent.com/87195021/162634809-24dde606-907a-4638-9a70-5ddf1a994570.png)

We see that we can run the `php` command as sudo. 

Using that information we can navigate to [GTFObin](https://gtfobins.github.io/gtfobins/php/) to look up a way to take advantage of our sudo rights.

![image](https://user-images.githubusercontent.com/87195021/162634875-13a729e3-c903-49b8-8c4a-1d3e3598f1bd.png)

We can run the above command to gain Root access. 

![image](https://user-images.githubusercontent.com/87195021/162634922-54cbb01d-3e35-4e8a-9397-2765dae538cc.png)

Navigate to the /root folder for the final flag. 

![image](https://user-images.githubusercontent.com/87195021/162634965-5657ec83-134d-47cc-81c9-9bd1ad72054a.png)

Cat the root.txt

![image](https://user-images.githubusercontent.com/87195021/162634988-7530c1a9-f8a6-486e-9aff-9c54bdc7a4ad.png)

Submit the final flag and we are done. 