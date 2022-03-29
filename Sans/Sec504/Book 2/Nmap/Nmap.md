# Brief Intro

In this lab, you will evaluate several of the features of Nmap. You will conduct multiple scans against the local Linux VM and the Windows VM.
Requirements for This Lab

In this lab, you will use both your Slingshot Linux VM and the Windows 10 VM. Make sure both VMs are running before continuing with this lab exercise.

## Try It Yourself

Run scans against your local host with different permissions. Run scans from the Linux VM to the Windows VM. Experiment with different options to evaluate why a port is reported as open or closed, the differences between Nmap scanning as root and as a non-privileged user, performing OS identification, version scanning, and evaluating the standard listening port configuration on Windows.

## Walkthrough

### Overview

In this lab, you will use both your Linux and Windows VMs with Nmap. All scanning will be performed from your Linux system. Initially, you will keep the scanning local to the Linux VM, but later in the lab, you will also scan the Windows VM.

### Verify Connectivity

On the Linux VM, test connectivity to the Windows VM using the ping utility:

    sec504@slingshot:~$ ping -c 3 10.10.0.1
    PING 10.10.0.1 (10.10.0.1) 56(84) bytes of data.
    64 bytes from 10.10.0.1: icmp_seq=1 ttl=128 time=0.872 ms
    64 bytes from 10.10.0.1: icmp_seq=2 ttl=128 time=1.14 ms
    64 bytes from 10.10.0.1: icmp_seq=3 ttl=128 time=1.40 ms

    --- 10.10.0.1 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    rtt min/avg/max/mdev = 0.872/1.141/1.404/0.218 ms

Repeat this step, this time testing the connectivity from the Windows VM to the Linux VM:

    C:\Users\Sec504> ping 10.10.75.1

    Pinging 10.10.75.1 with 32 bytes of data:
    Reply from 10.10.75.1: bytes=32 time<1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time=1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time<1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time=1ms TTL=64

    Ping statistics for 10.10.75.1:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 0ms, Maximum = 1ms, Average = 0ms

If you are unable to get a response from the Windows VM or the Linux VM, take a look at the Testing Virtual Machine Connectivity module for troubleshooting steps.

### Open a Terminal

From the Slingshot Linux VM, open a terminal.

### Nmap as an Uprivileged User

Start a basic Nmap scan, as shown here.

    sec504@slingshot:~$ nmap 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:50 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00035s latency).
    Not shown: 998 closed ports
    PORT     STATE SERVICE
    9001/tcp open  tor-orport
    9002/tcp open  dynamid

    Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds

In this output, we see two TCP ports are open (your output may be slightly different than this example). Nmap indicates which port number is open and accepting connections, as well as a brief description of the service. The service description is based on common port-to-protocol descriptions (as defined in the /etc/services file).

Note that Nmap indicates 2 open ports and 998 closed ports. Instead of scanning all 65,535 possible ports, Nmap defaults to a list of the top 1,000 most common ports.

### Reason Information

By default, when running as a non-root account, Nmap does a full TCP connect scan, completing the TCP three-way handshake for each open TCP port on the target.

We are showing you how Nmap runs as a non-root user because it is important as an incident handler to understand that you do not need to be root to run nmap. Attackers who gain access to a system can still discover systems and ports even with limited privileges. 

Nmap can also tell you why it believes a port is open. For example, in UDP scans Nmap lists a port as Open|Filtered. This means it did not receive a response, so the UDP port in question is either open or filtered. Another example is if a firewall drops a packet, Nmap responds with Filtered as the status of a port.

Examine the Nmap reason output by rerunning the scan, this time with the nmap --reason command:

    sec504@slingshot:~$ nmap --reason 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:50 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up, received conn-refused (0.00030s latency).
    Not shown: 998 closed ports
    Reason: 998 conn-refused
    PORT     STATE SERVICE    REASON
    9001/tcp open  tor-orport syn-ack
    9002/tcp open  dynamid    syn-ack

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds

In this output, we see that Nmap discloses that it received a SYN/ACK for each of the open TCP ports.

### Nmap Root User Scan

Next, use sudo to run Nmap as root and repeat the scan again:

    sec504@slingshot:~$ sudo nmap --reason 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:52 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up, received localhost-response (0.000048s latency).
    Not shown: 998 closed ports
    Reason: 998 resets
    PORT     STATE SERVICE    REASON
    9001/tcp open  tor-orport syn-ack ttl 64
    9002/tcp open  dynamid    syn-ack ttl 64

    Nmap done: 1 IP address (1 host up) scanned in 1.69 seconds

When you run Nmap as a root user, the default scan type changes. As non-root, Nmap uses a TCP connect() to determine if a port is open or closed. As root, Nmap uses a half-open or TCP SYN scan (a TCP SYN is sent to start a connection, but the connection is never completed). The scan results are similar, but notice how the host discovery check indicates localhost-response, produced by Nmap's initial ping test that is only possible for the root user.

Nmap's half-open scan used by root accounts may generate fewer logs on a host system. However, it is also more suspicious on the network. To force Nmap to use the TCP connect scan as root, add the -sT argument. 

### Controlling the Port Specification

So far we've scanned using the Nmap default TCP ports. In some cases, it is desirable to scan a specified range of ports, such as all of the low-numbered ports from 1-1024.

Run the scan again, this time adding the -p argument to scan for ports in the range of 1 to 1024, as shown here:

    sec504@slingshot:~$ sudo nmap --reason -p 1-1024 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:53 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up, received localhost-response (0.000038s latency).
    All 1024 scanned ports on localhost (127.0.0.1) are closed because of 1024 resets

    Nmap done: 1 IP address (1 host up) scanned in 1.71 seconds

Here we see a complete scan with no ports open. This is not a surprise based on the earlier scan result, but we want to emphasize the functionality of the -p argument.

The -p argument is useful when you want to limit the range of ports to be tested, such as scanning for a web servers (-p 80,443,8000,8080), SMB servers (-p 135,139,445), or any range of ports needed to evaluate a target system.

To scan all TCP ports, you can specify -p 1-65535, or use the Nmap shorthand -p-. Scan all 65535 ports on the Slingshot Linux host, as shown here:

    sec504@slingshot:~$ sudo nmap --reason -p- 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:54 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up, received localhost-response (0.000034s latency).
    Not shown: 65531 closed ports
    Reason: 65531 resets
    PORT     STATE SERVICE    REASON
    5433/tcp open  pyrrho     syn-ack ttl 64
    5443/tcp open  spss       syn-ack ttl 64
    9001/tcp open  tor-orport syn-ack ttl 64
    9002/tcp open  dynamid    syn-ack ttl 64

    Nmap done: 1 IP address (1 host up) scanned in 10.51 seconds

Note that when we scan all TCP ports, we identify two additional services on TCP/5433 and TCP/5443 ports listening. These two services weren't identified in the earlier scans, since Nmap will only scan the top 1000 ports when no -p argument is specified.

### Getting More Information - Banners

In the last Nmap scan result, we saw four open ports:

    TCP/5433 is characterized as the pyrrho service
    TCP/5443 is characterized as the spss service
    TCP/9001 is characterized as the tor-orport service
    TCP/9002 is characterized as the dynamid service

The service information is collected from Nmap's own nmap-services file based on the port number. However, we know the port information can be arbitrary, and Nmap's service identification can be misleading.

To get additional information from the listening service to better characterize what is actually listening, we can conduct a version detection scan. Nmap will connect to each service and interact with the server, attempting to obtain service information from a series of connection probes. Repeat the prior scan, this time adding the -sV argument to conduct a version detection scan against the target, as shown here:

    sec504@slingshot:~$ sudo nmap -sV --reason -p 5433,5443,9001,9002 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-08 23:59 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up, received localhost-response (0.00011s latency).

    PORT     STATE SERVICE    REASON         VERSION
    5433/tcp open  postgresql syn-ack ttl 64 PostgreSQL DB 9.6.0 or later
    5443/tcp open  ssl/http   syn-ack ttl 64 Thin httpd
    9001/tcp open  http       syn-ack ttl 64 nginx 1.14.0 (Ubuntu)
    9002/tcp open  http       syn-ack ttl 64 nginx 1.14.0 (Ubuntu)
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
    SF-Port5433-TCP:V=7.60%I=7%D=7/8%Time=60E79171%P=x86_64-pc-linux-gnu%r(Ker
    SF:beros,8C,"E\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x20frontend\x
    SF:20protocol\x2027265\.28208:\x20server\x20supports\x201\.0\x20to\x203\.0
    SF:\0Fpostmaster\.c\0L2030\0RProcessStartupPacket\0\0")%r(SMBProgNeg,8C,"E
    SF:\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x20frontend\x20protocol\
    SF:x2065363\.19778:\x20server\x20supports\x201\.0\x20to\x203\.0\0Fpostmast
    SF:er\.c\0L2030\0RProcessStartupPacket\0\0");
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 18.29 seconds

Note the use of -p in this example; since we know there are 4 ports listening, we specify them explicitly on the command line. No need to scan all 65,535 ports again just to add version scan output! 

By adding the version detection scan output, Nmap returns a different characterization of the open port service identifiers:

    TCP/5433 is characterizes as a PostgreSQL database server version 9.6.0
    TCP/5443 is characterized as a SSL/HTTP service running Thin httpd (a lightweight web server)
    TCP/9001 is characterized as an nginx web server version 1.14.0 running on Ubuntu
    TCP/9002 is also characterized as an nginx web server version 1.14.0 running on Ubuntu

The output of the version detection scan is much more useful to us, since we can properly characterize the TCP/5443, TCP/9001, and TCP/9002 services as web servers. Knowing this, we can also ask Nmap to further interrogate the web servers using web enumeration scripts.

Note that Nmap reports an unrecognized service for TCP/5433, even though it is characterized as PostgreSQL. Nmap has observed unexpected output, and always welcomes additional information to improve identification capabilities. 

### Getting More Information - Scripts

In addition to version detection scan, Nmap can also use one or more scripts to collect detailed information from a target platform. Nmap includes over 600 different scripts for vulnerability assessment, password attacks, sensitive data disclosure collection, and much more as part of Nmap Scripting Engine (NSE) library.

You can see a list of all of the Nmap scripts on the Nmap website at https://nmap.org/nsedoc/. From the Linux command line, you can obtain help information for a specific category of scripts using the --script-help command line argument. Run the Nmap command shown below to obtain a list of all of the Nmap scripts beginning with http in the script name:

    sec504@slingshot:~$ nmap --script-help "http-*"

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:05 UTC

    http-adobe-coldfusion-apsa1301
    Categories: exploit vuln
    https://nmap.org/nsedoc/scripts/http-adobe-coldfusion-apsa1301.html
    Attempts to exploit an authentication bypass vulnerability in Adobe Coldfusion
    servers to retrieve a valid administrator's session cookie.

    Reference:
    * APSA13-01: http://www.adobe.com/support/security/advisories/apsa13-01.html

    http-affiliate-id
    Categories: safe discovery
    https://nmap.org/nsedoc/scripts/http-affiliate-id.html
    ... omitted for space

    This is a long list of scripts, with more detail than what you may want to look through. Limit the output using grep, as shown here:

    sec504@slingshot:~$ nmap --script-help "http*" | grep "^http-"
    http-adobe-coldfusion-apsa1301
    http-affiliate-id
    http-apache-negotiation
    http-apache-server-status
    http-aspnet-debug
    http-auth-finder
    http-auth
    http-avaya-ipoffice-users
    http-awstatstotals-exec
    http-axis2-dir-traversal
    ... omitted for space

The grep command argument syntax uses a regular expression to filter the output. The leading ^ indicates that grep should only display lines that begin with the string http-. 

For any given script name, we can obtain the help information using --script-help followed by the script name. Obtain the script help for the Nmap http-git script, as shown here:

    sec504@slingshot:~$ nmap --script-help http-git

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:06 UTC

    http-git
    Categories: default safe vuln
    https://nmap.org/nsedoc/scripts/http-git.html
    Checks for a Git repository found in a website's document root
    /.git/) and retrieves as much repo information as
    possible, including language/framework, remotes, last commit
    message, and repository description.

The Nmap http-git script checks for Git repository information on a web server, which can often reveal detailed information about the web application, potentially including old passwords or other sensitive information. Run the http-git script on the Slingshot Linux Nginx web servers using the Nmap --script argument, as shown here, omitting the -sV argument:

    sec504@slingshot:~$ sudo nmap --script http-git 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:07 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.000046s latency).
    Not shown: 998 closed ports
    PORT     STATE SERVICE
    9001/tcp open  tor-orport
    9002/tcp open  dynamid

    Nmap done: 1 IP address (1 host up) scanned in 1.83 seconds
    sec504@slingshot:~$

Notice that, although we've told Nmap to interrogate the server using the http-git script, we don't get any script output from the target. This is because Nmap does not recognize the web servers on non-standard ports, and does not attempt to run the http-git script.

Note: It is essential for Nmap to properly characterize the target service to apply the correct scripts. 

Repeat the scan again, this time adding the -sV argument:

    sec504@slingshot:~$ sudo nmap -sV --script http-git 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:08 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.000031s latency).
    Not shown: 998 closed ports
    PORT     STATE SERVICE VERSION
    9001/tcp open  http    nginx 1.14.0 (Ubuntu)
    | http-git:
    |   127.0.0.1:9001/.git/
    |     Git repository found!
    |     Repository description: Unnamed repository; edit this file 'description' to name the...
    |     Remotes:
    |_      ssh://git@github.com-wiki/joswr1ght/SANS-504-Student-Wiki
    |_http-server-header: nginx/1.14.0 (Ubuntu)
    9002/tcp open  http    nginx 1.14.0 (Ubuntu)
    |_http-server-header: nginx/1.14.0 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 12.99 seconds

In this output we see the output of the http-git script, identifying the Nginx server listening on TCP/9001 as having a Git repository pointing to the URL ssh://git@github.com-wiki/joswr1ght/SANS-504-Student-Wiki.

TIP: You can use the Nmap --script argument to specify multiple scripts. For example, to run all of the Nmap HTTP scripts, specify the --script http* argument. 

### Getting More Information - Aggressive Scanning

Nmap includes a powerful option with the -A argument. This option enables OS detection, version detection, script scanning, and traceroute output. It gives you far more information than a SYN or TCP connect scan. Let's run it now:

    sec504@slingshot:~$ sudo nmap -A -p 5433,5443,9001,9002 127.0.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:10 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.000062s latency).

    PORT     STATE SERVICE    VERSION
    5433/tcp open  postgresql PostgreSQL DB 9.6.0 or later
    | fingerprint-strings:
    |   Kerberos:
    |     SFATAL
    |     VFATAL
    |     C0A000
    |     Munsupported frontend protocol 27265.28208: server supports 1.0 to 3.0
    |     Fpostmaster.c
    |     L2030
    |     RProcessStartupPacket
    |   SMBProgNeg:
    |     SFATAL
    |     VFATAL
    |     C0A000
    |     Munsupported frontend protocol 65363.19778: server supports 1.0 to 3.0
    |     Fpostmaster.c
    |     L2030
    |_    RProcessStartupPacket
    5443/tcp open  ssl/http   Thin httpd
    ...omitted for space

    Nmap done: 1 IP address (1 host up) scanned in 116.98 seconds

    This scan takes approximately 90-120 seconds to complete. 

Nmap provides us with not only the port information but also the service version (such as Nginx 1.14.0). It also queries the services to identify which commands it supports (for example, SMTP commands), and other useful information available (such as the HTTP page title).

### Standard Windows Ports

Next, examine the results from scanning the Windows server at 10.10.0.1, as shown here:

    sec504@slingshot:~$ sudo nmap -A 10.10.0.1

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:16 UTC
    Nmap scan report for 10.10.0.1
    Host is up (0.00032s latency).
    Not shown: 997 closed ports
    PORT    STATE SERVICE      VERSION
    135/tcp open  msrpc        Microsoft Windows RPC
    139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
    445/tcp open  microsoft-ds Windows 10 Enterprise 17134 microsoft-ds (workgroup: SEC504)
    MAC Address: 00:0C:29:57:40:85 (VMware)
    No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
    ...

    This scan takes approximately 60-90 seconds to complete. 

The big thing to take from this is to see which ports are available to most un-firewalled systems. The standard RPC/SMB ports (135, 139, and 445) are an Achilles heel for many Windows systems. It is over these ports that many exploits access Windows systems remotely or allow an attacker to remotely authenticate and access the system via valid credentials.

## Why This Lab Is Important

We've given a brief intro into the ways in which Nmap allows one to see what ports are open and available. By using Nmap, or tools like it, attackers and defenders can learn how a network is actually configured and running.