# Nibbles

mkdir -p htb/Nibbles/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O -oA htb/Nibbles/nmap/initial 10.129.122.71

| **Flag** | **Description** |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port**   | **Description**   |
| --------------|-------------------|
| `22` | OpenSSH 7.2p2 |
| `80` | HTTP Apache/2.4.18 |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA htb/Nibbles/nmap/full 10.129.122.71

| **Option**   | **Description**   |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `-p-` |All Ports |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port**   | **Description**   |
| --------------|-------------------|
| `22` | OpenSSH 7.2p2 |
| `80` | HTTP Apache/2.4.18 |

## UDP Scan

Similarly, we run an nmap scan with the -sU flag enabled to run a UDP scan.

    sudo nmap -sU -O -p- --reason -oA htb/Nibbles/nmap/udp 10.129.122.71

| **Option**   | **Description**   |
| --------------|-------------------|
| `-sU` | Detect UDP |
| `-O` | Detect OS |
| `-p-` |All Ports |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

`I managed to root the box and write this all while this UDP scan still did not terminate.`

# Enumeration

Visit the site in the browser. 

![image](https://user-images.githubusercontent.com/87195021/162625741-0b1b316b-113b-4656-825b-0f46ba3dc1ba.png)

Nothing useful there. `Ctrl+u` for page source. We find a comment that gives us a new directory. 

![image](https://user-images.githubusercontent.com/87195021/162625837-857e812f-1666-4db7-ae58-8f7309e705ae.png)

This leads us to the following page. You can see at the bottom that it is powered by Nibbleblog. This is an indication that it an off the shelf software as apposed to custom software.

![image](https://user-images.githubusercontent.com/87195021/162625887-e36481bb-5d37-46a9-a10f-f8fef91f6c9e.png)

To confirm that, let’s google Nibbleblog.

![image](https://user-images.githubusercontent.com/87195021/162626038-2657d036-479e-429c-aaf9-9f64dbcdb5fd.png)

It’s an open-source engine for creating blogs using PHP. This is good news for us for two reasons: (1) you can download the software and play with it offline. This way you can poke at it as much as you want without having to worry about detection, and (2) since it is open-source and used by other people, it probably has reported vulnerabilities. If this was custom software, we would have had to find zero day vulnerabilities.

In order to see if this application is vulnerable, we need to find its version number. To do that, let’s run `Gobuster` to enumerate directories.

### Gobuster

    gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.122.71/nibbleblog

We get back the following results:

![image](https://user-images.githubusercontent.com/87195021/162626506-8231ed99-8370-457f-a438-a752a43933dd.png)

Navigate to the README page and there we find out that it is using version 4.0.3.

![image](https://user-images.githubusercontent.com/87195021/162626586-75defd3a-967a-4c8f-8465-b4920c1b7eba.png)

Google the name of the software and version to see if it has any exploits.

![image](https://user-images.githubusercontent.com/87195021/162626586-75defd3a-967a-4c8f-8465-b4920c1b7eba.png)

## Gaining an Initial Foothold

Navigate to the shell upload exploit [page](https://packetstormsecurity.com/files/133425/NibbleBlog-4.0.3-Shell-Upload.html).

    NibbleBlog 4.0.3: Code Execution

![image](https://user-images.githubusercontent.com/87195021/162627331-8e3e237c-35d9-43d8-be84-7e49628d93f0.png)

Several important pieces of information are mentioned in the page.

- It’s a code execution vulnerability.
- The vulnerability is in the “My image” plugin that allows the upload of PHP files. So it would allow us to upload a PHP reverse shell.
- It’s an authenticated vulnerability which means that we need admin credentials before we exploit this vulnerability.

**Alright, so the next steps would be:**

1. Navigate to the admin login page and figure out the admin credentials
2. Navigate to the My Image plugin page and upload a PHP reverse shell

As mentioned in the Proof of Concept, the admin page can be found here.

http://10.129.236.91/nibbleblog/admin.php

![image](https://user-images.githubusercontent.com/87195021/162627907-93f64f6e-4a39-4874-8653-dc4a61a7968c.png)

Now we need admin credentials. When I’m presented with an enter credentials page, the first thing I try is common credentials (admin/admin, admin/nibbles, nibbles/nibbles, nibbles/admin). If that doesn’t work out, I look for default credentials online that are specific to the technology. Last, I use a password cracker if all else fails.

In this case, the common credentials `admin/nibbles` worked! Step #1 is complete!

Next, we need to navigate to the My Image plugin. Click on Plugins > My image > Configure.

![image](https://user-images.githubusercontent.com/87195021/162628050-840166e4-b21c-4feb-a728-7ace1e286add.png)

Head over to [pentestmonkey](https://pentestmonkey.net/tools/web-shells/php-reverse-shell) and get the code for a PHP reverse shell. Change the IP address and port used by your attack machine. Then save it in a file called image.php and upload it on the site.

![image](https://user-images.githubusercontent.com/87195021/162628470-6d1a78b5-1d45-4a4c-93a6-28bce2ce2d11.png)

Start a listener on the above chosen port.

    nc -nlvp 4321

In the browser, navigate to the image we just uploaded to run the reverse shell script.

    http://10.129.122.71/nibbleblog/content/private/plugins/my_image/image.php


We have a low privileged shell!

![image](https://user-images.githubusercontent.com/87195021/162629058-28f60454-a6d5-4889-8a9b-85a3028a7408.png)

Let’s first upgrade to a better shell. Python is not installed but python 3 is.

    python3 -c 'import pty; pty.spawn("/bin/bash")'

This gives us a partially interactive bash shell. To get a fully interactive shell, background the session `(CTRL+ Z)` and run the following in your terminal which tells your terminal to pass keyboard shortcuts to the shell.

    stty raw -echo

Once that is done, run the command `fg` to bring netcat back to the foreground.

Grab the user flag.

![image](https://user-images.githubusercontent.com/87195021/162629282-92695a86-abc2-42ec-91ef-6da4b180124b.png)

Now we need to escalate privileges.

## Privilege Escalation

Find out what privileges you have.

    sudo -l


![image](https://user-images.githubusercontent.com/87195021/162629331-4574089e-f8a4-4d10-bceb-0b25e6215810.png)

We can run the script monitor.sh in the above specified directory as root without having to enter a root password. Why is that good news for us? If we call a shell in that script, we can run it as root!

First, let’s see what the script contains.

![image](https://user-images.githubusercontent.com/87195021/162629430-b59b7900-c0cc-41d2-abea-44a47cdcc7a5.png)

It does not exist! We’ll have to create one.

    mkdir -p home/nibbler/personal/stuff
    
    cd /home/nibbler/personal/stuff
    
    vi monitor.sh

n the monitor.sh script add the following code.

    #!/bin/sh
    bash

Give it execute privileges.

    chmod +x monitor.sh

Run the script with sudo.

    sudo ./monitor.sh

We are root!

![image](https://user-images.githubusercontent.com/87195021/162630220-c643f556-90b5-441f-ad8d-800ef98cfe28.png)

Grab the root flag!

de5e5d6619862a8aa5b9b212314e0cdd

![image](https://user-images.githubusercontent.com/87195021/162630257-19ab7869-fea0-46fe-a7aa-e5841b7b431c.png)