# DNS Interrogation

## Brief Intro

In this lab, you will use several tools to interrogate a DNS server, collecting information like an attacker would as part of a reconnaissance assessment for the Falsimentis organization. Following the DNS server interrogation, you will review DNS logging information to gain insight into the evidence left behind after this attack.

## Requirements for This Lab

In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Launch the Falsimentis DNS server target by running gonameserver. Use dig to interrogate the server at 172.30.0.254, identifying different servers. Use the Nmap dns-brute script to collect more information, customizing the host list to identify even more systems. Review the DNS server logging information after the attack in ~/labs/dnslog.
## Walkthrough

## Overview

In this lab you will interrogate the Falsimentis DNS server as part of an authorized assessment of their infrastructure.

### Open a Terminal

From the Slingshot Linux VM, open a terminal.

### Start the Lab Target Server

From the terminal, start the DNS server that will be the target for the assessment by running gonameserver, as shown here.

    sec504@slingshot:~$ gonameserver
    Starting Docker service ..... Done.
    Starting DNS server target
    bdc91ba5f5948bf028c3751134975943dd1914a7f590a2dd8fcc3b315cd0e040
    Continue with the lab exercise steps.

Minimize this terminal window. Leave this script running for the duration of the lab exercise.

### Identifying the Authoritative DNS Server

When interrogating DNS, we generally want to query the authoritative DNS server for the domain. You can find the authoritative DNS server for a domain using a WHOIS query. We've reproduced the results of a WHOIS query for the falsimentis.com domain here.

    Note: You don't have to run this command in the lab; it is presented here for illustration purposes. 

In this output we see that Falsimentis uses three authoritative DNS servers; the first being ns1.falsimentis.com. We can interrogate this server by name, or we can look up the IP address using the Linux host utility as shown in the screenshot.

In this lab you will interrogate the authoritative DNS server for falsimentis.com at 172.30.0.254.

### Open a New Terminal

From the Slingshot Linux VM, open a new terminal.

### DNS Interrogation with Dig

Dig is popular command-line tool for querying DNS servers from the Internet Software Consortium (ISC). Let's examine the command-line parameters for a simple DNS query; run the dig command example shown here to query the Falsimentis DNS server for the name www.falsimentis.com.

    sec504@slingshot:~$ dig @172.30.0.254 A www.falsimentis.com

    ; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> @172.30.0.254 A www.falsimentis.com
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24987
    ;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
    ;; WARNING: recursion requested but not available

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 1232
    ; COOKIE: 294c2a918145914c0100000060e1a0fd8281ac884ce6ab9f (good)
    ;; QUESTION SECTION:
    ;www.falsimentis.com.       IN  A

    ;; ANSWER SECTION:
    www.falsimentis.com.    86400   IN  A   45.76.171.86

    ;; Query time: 0 msec
    ;; SERVER: 172.30.0.254#53(172.30.0.254)
    ;; WHEN: Sun Jul 04 11:52:29 UTC 2021
    ;; MSG SIZE  rcvd: 92

The arguments for this command break down as follows:

    @172.30.0.254: The @ sign indicates that the query should be sent the server identified by a host name or IP address; here the DNS request is sent to 172.30.0.254
    A: The DNS record type to interrogate; an A record is an address record, returning an IPv4 address
    www.falsimentis.com: The value to interrogate; here we are asking the DNS server to return the IP address for www.falsimentis.com

In this output we see verbose DNS processing information (lines beginning with ;), and an answer where www.falsimentis.com returns an IP address of 45.76.171.86.

    In the answer section, the number 86400 is the Time To Live (TTL), or the amount of time the resolver (e.g., the client performing the lookup) should cache the DNS answer, in seconds. IN stands for an internet record. 

Dig also supports query modifiers specified as command line arguments with a leading plus sign. One useful query modifier is +short which will make the DNS server response less verbose. Run the query again, this time adding the +short query modifier, as shown here.

    sec504@slingshot:~$ dig +short @172.30.0.254 A www.falsimentis.com
    45.76.171.86

In some cases you may want the greater detail provided by default, but for most dig uses the +short modifier makes the output easier to read and understand.

### Zone Transfer Request

In the book materials associated with this lab, we learned about the DNS zone transfer, a feature where a DNS server will disclose all DNS records. We can request a zone transfer with dig, using the DNS record type AXFR and the target domain name (e.g., falsimentis.com). Modify the previous dig command to request a zone transfer from the Falsimentis DNS server, as shown here.

    sec504@slingshot:~$ dig +short @172.30.0.254 AXFR falsimentis.com
    ; Transfer failed.

Here we see the zone transfer request failed. This is to be expected; it is uncommon for DNS servers to allow for zone transfer requests, particularly for internet-facing DNS systems. However, it does not prevent us from interrogating the DNS server directly for specific names and DNS record types.

### Mail Exchange Record Request

Most DNS requests require that the resolver specify a record type and a host name (such as the A record request for www.falsimentis.com). However, the Mail Exchange (MX) record type will reveal host name information for the mail systems associated with a domain. Modify the previous dig command to request the MX records from the Falsimentis DNS server for the falsimentis.com domain, as shown here.

    sec504@slingshot:~$ dig +short @172.30.0.254 MX falsimentis.com
    20 mail-falsimentis-com.mail.protection.outlook.com.
    10 falsimentis-com.mail.protection.outlook.com.
    30 mail.falsimentis.com.

Here the DNS server returns three records; the 10 record is the smallest number and the highest-priority mail server, indicating that email for user@falsimentis.com should be delivered to falsimentis-com.mail.protection.outlook.com (the Microsoft Office 365 server). The 20 record is the first backup server, sending mail to mail-falsimentis-com.mail.protection.outlook.com. The 30 record is the second backup, sending mail to mail.falsimentis.com.

In this output we learn that Falsimentis uses O365 for email – a valuable piece of reconnaissance information. We also learn about the presence of the mail.falsimentis.com server; identify the IP address for that server by requesting the A record as shown here.

    sec504@slingshot:~$ dig +short @172.30.0.254 A mail.falsimentis.com
    104.47.73.10

    Tip: A motivated attacker will take notes as they gather reconnaissance information for the target network. You can do so as well, writing the results in a notebook or copy and paste the commands and results to a text file for later reference, if desired. 

### Manual DNS Interrogation

We've seen so far that we can use dig to manually interrogate the server. An attacker can ask the DNS server to resolve any name, allowing them to guess common names that may provide insight into additional target hosts.

Use dig to request several common DNS names: admin, login, backup, ns, share, and support, as shown here.

    sec504@slingshot:~$ dig +short @172.30.0.254 A admin.falsimentis.com
    sec504@slingshot:~$ dig +short @172.30.0.254 A login.falsimentis.com
    23.21.211.161
    sec504@slingshot:~$ dig +short @172.30.0.254 A backup.falsimentis.com
    sec504@slingshot:~$ dig +short @172.30.0.254 A ns.falsimentis.com
    sec504@slingshot:~$ dig +short @172.30.0.254 A share.falsimentis.com
    sec504@slingshot:~$ dig +short @172.30.0.254 A support.falsimentis.com
    172.17.0.211

In this output we learn that when dig is unable to resolve the DNS record, it returns no output (when used with the +short modifier). Several of the common names we evaluated don't return any information, but we did learn about two new entities: login.falsimentis.com and support.falsimentis.com. Notice also how the IP addresses are different in format; this could indicate a misconfigured DNS server, revealing both public IP addresses (23.21.211.161) and private IP addresses (172.17.0.211) to an attacker.

Manually guessing DNS names is ineffective however. As an alternative, an attacker can use an automated DNS name guessing tool, such as the Nmap dns-brute module.

### Automated DNS Guessing

Nmap is a multi-functional tool for host and network discovery, port scanning, and target enumeration. We'll look at the many uses of Nmap later on in class, but for now we'll focus on Nmap's automated DNS guessing feature: dns-brute.

The Nmap dns-brute script uses the list of host names (without the domain suffix) from /usr/share/nmap/nselib/data/vhosts-default.lst to automate the process of DNS name guessing against a specified name server. Examine the first few lines from the vhosts-default.lst file using head, then count the number of lines using the wc utility, as shown here.

    sec504@slingshot:~$ head /usr/share/nmap/nselib/data/vhosts-default.lst
    admin
    administration
    ads
    adserver
    alerts
    alpha
    ap
    apache
    app
    apps
    sec504@slingshot:~$ wc -l /usr/share/nmap/nselib/data/vhosts-default.lst
    127 /usr/share/nmap/nselib/data/vhosts-default.lst

This file is a simple list of 127 names, one per line. Let's use this list to interrogate the Falsimentis DNS server again with Nmap, as shown here.

    sec504@slingshot:~$ sudo nmap --dns-servers 172.30.0.254 --script dns-brute --script-args dns-brute.domain=falsimentis.com

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-12-09 12:43 UTC
    Pre-scan script results:
    | dns-brute:
    |   DNS Brute-force hostnames:
    |     news.falsimentis.com - 172.17.0.183
    |     ns1.falsimentis.com - 172.30.0.254
    |     ns2.falsimentis.com - 10.200.81.238
    |     mail.falsimentis.com - 104.47.73.10
    |_    www.falsimentis.com - 45.76.171.86
    WARNING: No targets were specified, so 0 hosts scanned.
    Nmap done: 0 IP addresses (0 hosts up) scanned in 0.25 seconds

This command breaks down as follows:

    sudo nmap: Run Nmap with root privileges using sudo
    --dns-servers 172.30.0.254: Specify the DNS server to use for name resolution; this can be a local DNS server, the target organization's DNS server, or another DNS resolver (such as Google's public DNS resolver at 8.8.8.8)
    --script dns-brute: Tell Nmap to run the dns-brute script
    --script-args dns-brute.domain=falsimentis.com: Specify the falsimentis.com domain as an argument for the dns-brute.domain parameter

In this output we see that Nmap identified 5 hosts with the dns-brute script; most of these we had already discovered but we also learn about the news.falsimentis.com server as an additional target.

### Automated DNS Guessing - Expanded List

The vhosts-default.lst list that Nmap distributes for DNS brute-force guessing is fairly short, and will only identify the most common DNS names. We can augment the dns-brute capabilities by using a more detailed list.

Daniel Miessler maintains a collection of lists that are useful for security assessments, including a longer list of host names. Examine the first few lines of this list using head, then count the number of lines using wc, as shown here.

    sec504@slingshot:~$ head labs/dns/namelist.txt
    0
    01
    02
    03
    1
    10
    11
    12
    13
    14
    sec504@slingshot:~$ wc -l labs/dns/namelist.txt
    2326 labs/dns/namelist.txt

This list of host names is considerably longer. Repeat the dns-brute scan, this time adding the dns-brute.hostlist argument to specify this custom list, as shown here.

    sec504@slingshot:~$ sudo nmap --dns-servers 172.30.0.254 --script dns-brute --script-args dns-brute.domain=falsimentis.com,dns-brute.hostlist=/home/sec504/labs/dns/namelist.txt

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-12-09 12:56 UTC
    Pre-scan script results:
    | dns-brute:
    |   DNS Brute-force hostnames:
    |     support.falsimentis.com - 172.17.0.211
    |     downloads.falsimentis.com - 10.200.74.2
    |     login.falsimentis.com - 23.21.211.161
    |     email.falsimentis.com - 45.76.171.86
    |     mail.falsimentis.com - 104.47.73.10
    |     news.falsimentis.com - 172.17.0.183
    |     www.falsimentis.com - 45.76.171.86
    |     ns1.falsimentis.com - 172.30.0.254
    |_    ns2.falsimentis.com - 10.200.81.238
    WARNING: No targets were specified, so 0 hosts scanned.
    Nmap done: 0 IP addresses (0 hosts up) scanned in 1.30 seconds

This command is very similar to the previous Nmap command, except that we've added a second parameter to the dns-brute script arguments to specify the dns-brute.hostlist. When specifying multiple arguments to an Nmap script, we separate each argument by a comma.

The Nmap output here reveals an additional host that we had not identified previously: downloads.falsimentis.com.

### Automated DNS Guessing - Custom List

An attacker will not solely rely on publicly-available lists of names to interrogate DNS, opting to expand the number of identified hosts using custom lists based on previously-gathered intelligence.

Recall in our Network Analysis lab, we learned about the Falsimentis host fm-tetris. Falsimentis, like many organizations, uses a prefix for some of their hostnames of fm. Knowing this, an attacker may create a custom wordlist, using the names of common hosts with the Falsimentis-specific prefix of fm.

From the terminal, create a new list of host names, using the Daniel Miessler list with a prefix of fm-. We can do this with awk, as shown here.

    sec504@slingshot:~$ awk '{ print "fm-"$1 }' labs/dns/namelist.txt  | head
    fm-0
    fm-01
    fm-02
    fm-03
    fm-1
    fm-10
    fm-11
    fm-12
    fm-13
    fm-14
    sec504@slingshot:~$ awk '{ print "fm-"$1 }' labs/dns/namelist.txt  > falsimentis-namelist.txt

This awk command breaks down as follows:

    '{ : Begin an awk program; a space after { isn't necessary but it makes the Awk program easier to read
    print "fm-"$1: The awk program itself; print to the screen the string "fm-" followed by the first column in the processed file; for this example, the program will prepend "fm-" to each word in the name list
    }': End the awk program; the space isn't necessary here either, but improves readability
    labs/dns/namelist.txt: Process each line in the labs/dns/namelist.txt file
    > falsimentis-namelist.txt: Redirect the output (the print output from the awk program) to the named file

Next, repeat the dns-brute scan, using the falsimentis-namelist.txt file, as shown here.

    sec504@slingshot:~$ sudo nmap --dns-servers 172.30.0.254 --script dns-brute --script-args dns-brute.domain=falsimentis.com,dns-brute.hostlist=falsimentis-namelist.txt

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-04 14:49 UTC
    Pre-scan script results:
    | dns-brute:
    |   DNS Brute-force hostnames:
    |     fm-ceo.falsimentis.com - 172.16.42.107
    |     fm-fs01.falsimentis.com - 172.16.42.3
    |     fm-webdev.falsimentis.com - 172.16.42.20
    |     fm-fw01.falsimentis.com - 172.16.42.10
    |_    fm-golf.falsimentis.com - 172.16.42.109
    WARNING: No targets were specified, so 0 hosts scanned.
    Nmap done: 0 IP addresses (0 hosts up) scanned in 1.55 seconds

By creating a custom wordlist, using our knowledge of Falsimentis' convention of prepending fm- to names, we learn about several additional systems from the DNS server.
Incident Response - DNS Log Analysis

We'll finish this lab with a look at what we can see as incident responders following a DNS interrogation attack. For this lab, the DNS server has been configured using the ISC recommendations for logging, which are not the default settings. See the Additional Resources section below for more information on configuring logging for DNS servers.

From your terminal, change to the ~/labs/dnslogs directory, then list the files in the directory in long form, as shown here.

    sec504@slingshot:~$ cd ~/labs/dnslog/
    sec504@slingshot:~/labs/dnslog$ ls -l
    total 1524
    -rw-r--r-- 1 root root    2891 Jul  4 15:40 auth_servers
    -rw-r--r-- 1 root root     148 Jul  4 15:45 client_security
    -rw-r--r-- 1 root root       0 Jul  4 15:40 ddns
    -rw-r--r-- 1 root root     276 Jul  4 15:40 default
    -rw-r--r-- 1 root root     103 Jul  4 15:40 dnssec
    -rw-r--r-- 1 root root       0 Jul  4 15:40 dnstap
    -rw-r--r-- 1 root root 1544020 Jul  4 15:51 queries
    -rw-r--r-- 1 root root       0 Jul  4 15:40 query-errors
    -rw-r--r-- 1 root root       0 Jul  4 15:40 rate_limiting
    -rw-r--r-- 1 root root       0 Jul  4 15:40 rpz
    -rw-r--r-- 1 root root       0 Jul  4 15:40 zone_transfers

These logs were generated by your attacks during the lab exercise (the file sizes may be different on your system). One point to notice is that the zone_transfers file is empty, indicating that there are no logs of successful zone transfers. However, examine the contents of the client_security log file with cat, as shown here.

    sec504@slingshot:~/labs/dnslog$ cat client_security
    04-Jul-2021 15:45:04.517 security: error: client @0x55a7ff06d160 172.30.0.1#50167 (falsimentis.com): zone transfer 'falsimentis.com/AXFR/IN' denied

Here we see that the server recorded a failed zone transfer attempt from the host at 172.30.0.1 (the Slingshot Linux host, as observed by the DNS container). The presence of a failed zone transfer is valuable, if only to use the offending source IP address on a watchlist to look for other malicious activity.

    In some rare cases, the client_security file may be empty. If this happens, you can still see the zone transfer activity by running grep AXFR queries. 

Next, examine the first few lines from the queries file, as shown here.

    sec504@slingshot:~/labs/dnslog$ head queries
    04-Jul-2021 15:43:56.498 queries: info: client @0x55a7ff0641c0 172.30.0.1#44693 (www.falsimentis.com): query: www.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:44:04.506 queries: info: client @0x55a7ff0641c0 172.30.0.1#41517 (www.falsimentis.com): query: www.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:45:04.517 queries: info: client @0x55a7ff06d160 172.30.0.1#50167 (falsimentis.com): query: falsimentis.com IN AXFR -E(0)TK (172.30.0.254)
    04-Jul-2021 15:45:24.524 queries: info: client @0x55a7ff0641c0 172.30.0.1#51919 (falsimentis.com): query: falsimentis.com IN MX +E(0)K (172.30.0.254)
    04-Jul-2021 15:45:44.532 queries: info: client @0x55a7ff0641c0 172.30.0.1#38070 (mail.falsimentis.com): query: mail.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:46:04.548 queries: info: client @0x55a7ff06fec0 172.30.0.1#58239 (admin.falsimentis.com): query: admin.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:46:14.556 queries: info: client @0x55a7ff0641c0 172.30.0.1#43501 (login.falsimentis.com): query: login.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:46:25.563 queries: info: client @0x55a7ff06fec0 172.30.0.1#37581 (backup.falsimentis.com): query: backup.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:46:40.575 queries: info: client @0x55a7ff06fec0 172.30.0.1#41578 (ns.falsimentis.com): query: ns.falsimentis.com IN A +E(0)K (172.30.0.254)
    04-Jul-2021 15:46:51.583 queries: info: client @0x55a7ff0641c0 172.30.0.1#44267 (share.falsimentis.com): query: share.falsimentis.com IN A +E(0)K (172.30.0.254)

Here we see a log of all DNS queries sent to the server. For a busy DNS server this is going to create a lot of logging information, so we would need to be careful about rolling the logs over and saving old logging data. Still, it provides a lot of useful information for the defender, including:

    Source IP address of the resolving client
    Host name attempted to resolve
    Date and time for the DNS request
    The record type (A, AXFR, MX, etc.)
    DNS request flags; +E(0)K indicates recursion request (+), enhanced DNS request (E(0)), and if the client requested a DNS cookie (K)

Evaluating the data in the queries log file is best done in a Security Information Event Management (SIEM) platform, but we can do some basic analysis at the command line. For example, we can use cut, and uniq to perform some basic analysis of the number of events over time, as shown here.

    sec504@slingshot:~/labs/dnslog$ awk '/172.30.0.1/ { print $2 }' queries | cut -d: -f1-2 | uniq -c
        1 15:43
        1 15:44
        3 15:45
        6 15:46
        256 15:48
    4654 15:50
    4654 15:51

    Note that your output will be different than what is shown here, reflecting the time changes when you complete this lab, and possibly the addition of additional DNS requests. 

This command breaks down as follows. It is helpful to visualize a log entry when reviewing the command parameters, included here:

    04-Jul-2021 15:04:14.685 queries: info: client @0x5598bf4e6f20 172.30.0.1#35907 (fm-iis.falsimentis.com): query: fm-iis.falsimentis.com IN AAAA + (172.30.0.254)

- awk '/172.30.0.1/ { print $2 }' queries |: Use awk to focus on log entries containing the attacker IP address with a program that prints the 2nd column of information (the time field) from the queries file
- cut -d: -f1-2 |: Using a colon delimiter, retrieve the first and second fields from the time; that is, the hour and minute (eliminating the seconds field)
- uniq -c: Count the number of unique instances of the log output (e.g., how many events happened each minute)

This script presents some time analysis results for Events Per Minute (EPM). In the first few minutes we see only one or a small number of requests from the attacker, until we get to 15:48 where there were 256 requests in one minutes or less. This indicates a transition from manual interrogation to an automated tool. A few minutes later we see two significantly larger EPM values, both for 4654 requests from the attacker.

    Note: Nmap's dns-brute script makes requests for an A record, and a AAAA (quad-A; IPv6) record. This produces two requests for each line in the name list file. 

This analysis is useful, but must be taken into careful consideration with non-malicious events on the server. Some DNS servers may normally handle millions of request per minute, with many originating from the same source IP address (when considering NAT-based networks). Always take into consideration the baseline analysis for your network when deciding if the observed activity is anomalous.
Cleanup

Return to the terminal where you launched the gonameserver script. Press CTRL+C to terminate the script.

## Why This Lab Is Important

In this lab we looked at the reconnaissance steps an attacker could apply to collect information from a DNS server. Since many organizations have public-facing DNS servers, this is a common tactic for attackers as part of their pre-attack reconnaissance analysis. By practicing these techniques, and evaluating the logging evidence left behind on the DNS server, we are better informed to recognize and understand the implications of these attacks.