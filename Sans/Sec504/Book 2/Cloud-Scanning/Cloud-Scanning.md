# Cloud Scanning

## Brief Intro

In this lab, you will scan a large range of IP addresses simulating a cloud environment to identify a previously unknown Falsimentis server using Masscan, TLS-Scan, JQ, and EyeWitness.

## Requirements for This Lab

In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Run gomasscannet to setup the target environment. Scan the 10.200.0.0/16 network using Masscan for servers listening on TCP/443, then use TLS-Scan to enumerate the listening servers. Use JQ to extract server identity information from the TLS-Scan output. Use EyeWitness to build a report of the active host websites, identifying the Falsimentis cloud server.

## Walkthrough

### Overview

In this lab, you will use your Slingshot Linux VM to scan a simulated cloud environment using Masscan. After identifying several unique hosts in the target environment, you will enumerate the TLS servers using TLS-Scan, and attribute the system ownership using certificate data. Finally you will perform an EyeWitness scan to generate a report of the hosts, then identify the Falsimentis cloud VM target using the results of the scans.

### Open a Terminal

From the Slingshot Linux VM, open a terminal.

### Start the Simulated Cloud Environment

From the Slingshot Linux terminal, run gomasscannet to launch the simulated cloud environment, as shown here. Note that some of the values shown in the example below will be different for your system.

    sec504@slingshot:~$ gomasscannet
    Starting Docker service ..... Done.
    3656882e60630e29fc873c496b7e3503fb5b0df17b54c617b68e8e9d5f87a77a
    3ecfd495fb81e317f370aa52bb728942e24c272c569f9c7dfc4867decd80a9a6
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         192.168.171.1   0.0.0.0         UG    0      0        0 eth0
    10.200.0.0      192.168.200.10  255.255.0.0     UG    0      0        0 br-49bbe3a7dc68
    172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
    192.168.171.0   0.0.0.0         255.255.255.0   U     0      0        0 eth0
    192.168.200.0   0.0.0.0         255.255.255.0   U     0      0        0 br-49bbe3a7dc68

In this output we see the remote network representing the cloud environment (10.200.0.0/16) is accessible through the router (gateway) at 192.168.200.10.

## Examine Masscan Usage

Run masscan with no arguments to launch the tool and to display basic usage information, as shown here.

    sec504@slingshot:~$ masscan
    usage:
    masscan -p80,8000-8100 10.0.0.0/8 --rate=10000
    scan some web ports on 10.x.x.x at 10kpps
    masscan --nmap
    list those options that are compatible with nmap
    masscan -p80 10.0.0.0/8 --banners -oB 
    save results of scan in binary format to 
    masscan --open --banners --readscan  -oX 
    read binary scan results in  and save them as xml in 

Masscan accepts arguments that are similar to Nmap, including -p (designate ports to scan), -iL iplist.txt (obtain a list of target IP addresses from a file), or a range of IP addresses using CIDR or hyphenated ranges. One important additional argument for Masscan is --rate, where the attacker specifies the number of packets per second that Masscan will transmit.

For Masscan to be effective, the rate specified must not exceed host or network capacity, either local to the attacker or in any hop between the attacker and the target network environment. To improve performance, an attacker will use a cloud system that matches the environment of the target to best leverage single-cloud performance. 

## Enumerate Cloud Targets

Run Masscan to enumerate the cloud targets, identifying any hosts listening on TCP/443 (HTTPS), as shown here.

    sec504@slingshot:~$ masscan -p 443 --rate 10000 -oL simcloud.txt 10.200.0.0/16
    Starting masscan 1.3.2 (http://bit.ly/14GZzcT) at 2021-05-11 10:20:28 GMT
    Initiating SYN Stealth Scan
    Scanning 65536 hosts [1 port/host]
    ...

**The command line can be broken down into the following components:**

- **-p 443** - Identify systems listening on TCP/443 using a half/open (SYN) scan technique
- **--rate 10000** - Send 10,000 packets per second
- **-oL simcloud.txt** - Save the results in list format (one entry per line) in the specified file name
- **10.200.0.0/16** -  Scan the specified list of IP addresses (65535 hosts) using CIDR notation

NOTE: At the end of the scan, Masscan should report the discovery of 14 hosts. This is not always predictable, since Masscan may send packets faster than your host system can accommodate, even in the simulated cloud environment. If your scan reports fewer than 14 identified hosts, re-run the scan. You can also experiment with different rates, either increasing or decreasing the rate to experiment with Masscan performance. 

## Examine Scan Results

Display the contents of the scan result file using cat, as shown below.

    sec504@slingshot:~$ cat simcloud.txt
    #masscan
    open tcp 443 10.200.227.71 1620729347
    open tcp 443 10.200.0.3 1620729349
    open tcp 443 10.200.84.164 1620729350
    open tcp 443 10.200.23.203 1620729350
    open tcp 443 10.200.11.125 1620729350
    open tcp 443 10.200.89.164 1620729351
    open tcp 443 10.200.13.31 1620729351
    open tcp 443 10.200.30.42 1620729351
    open tcp 443 10.200.125.68 1620729352
    open tcp 443 10.200.74.2 1620729352
    open tcp 443 10.200.140.181 1620729352
    open tcp 443 10.200.248.218 1620729353
    open tcp 443 10.200.137.13 1620729354
    open tcp 443 10.200.1.10 1620729355
    # end

The Masscan results in list format (-oL) are mostly self-explanatory except for the last column. The last column represents the epoch timestamp when Masscan identified the open port. The epoch timestamp can be converted to a human-friendly timestamp using the date utility (date -d '@1620729347') if desired.

With this information we can represent the new targets visually, as shown here.

Masscan Expanded View of Attacker and Targets by IP Address

## Build a Target IP List

The Masscan results identify the systems listening on TCP/443, but for compatibility with other tools we need to create a file that includes only the listening IP addresses, one per line. Use the following Awk example to extract this list from the Masscan results.

    sec504@slingshot:~$ awk '/open/ {print $4}' simcloud.txt > simcloud-targets.txt
    sec504@slingshot:~$ cat simcloud-targets.txt
    10.200.227.71
    10.200.0.3
    10.200.84.164
    10.200.23.203
    10.200.11.125
    10.200.89.164
    10.200.13.31
    10.200.30.42
    10.200.125.68
    10.200.74.2
    10.200.140.181
    10.200.248.218
    10.200.137.13
    10.200.1.10

**The Awk command line can be broken down into the following components:**

- **awk '** - Run awk and start a new program within single quotes
- **/open/** -  Only process lines that include the string open (similar to grep)
- {: Start the action portion of the Awk program
- **print $4** - Print the 4th tokenized column (the Masscan-reported IP address)
- **}** - End the action portion of the Awk program
- **'** - End the Awk program with the closing single quote
- **> simcloud-targets.txt** - Redirect the output of the Awk program to the specified file name

Once you have a list of IP addresses, we can use other tools to interrogate these hosts to perform attribution assessment of the targets.

## Collect TLS Information

Next we'll use TLS-Scan to conduct target attribution against the identified list of hosts. Run the tls-scan command as shown below.

    sec504@slingshot:~$ tls-scan --port=443 --cacert=/opt/tls-scan/ca-bundle.crt -o simcloud-tlsinfo.json < simcloud-targets.txt
    elapsed-time: 0 secs | status: 1/1 | tls-handshake: 1 | target: 10.200.227.71
    elapsed-time: 0 secs | status: 2/2 | tls-handshake: 2 | target: 10.200.0.3
    elapsed-time: 0 secs | status: 3/3 | tls-handshake: 3 | target: 10.200.84.164
    elapsed-time: 0 secs | status: 4/4 | tls-handshake: 4 | target: 10.200.23.203
    elapsed-time: 0 secs | status: 5/5 | tls-handshake: 5 | target: 10.200.11.125
    elapsed-time: 0 secs | status: 6/6 | tls-handshake: 6 | target: 10.200.89.164
    elapsed-time: 0 secs | status: 7/7 | tls-handshake: 7 | target: 10.200.13.31
    elapsed-time: 0 secs | status: 8/8 | tls-handshake: 8 | target: 10.200.30.42
    elapsed-time: 0 secs | status: 9/9 | tls-handshake: 9 | target: 10.200.125.68
    elapsed-time: 0 secs | status: 10/10 | tls-handshake: 10 | target: 10.200.74.2
    elapsed-time: 0 secs | status: 11/11 | tls-handshake: 11 | target: 10.200.140.18
    elapsed-time: 0 secs | status: 12/12 | tls-handshake: 12 | target: 10.200.248.21
    elapsed-time: 0 secs | status: 13/13 | tls-handshake: 13 | target: 10.200.137.13
    elapsed-time: 0 secs | status: 14/14 | tls-handshake: 14 | target: 10.200.1.10
            pid: 19946 | ciphers: (0) |host-count: 14 |network-error: 0 |dns-errcount: 0 |remote-close-error: 0 |unknown-error: 0 |connect-error: 0 |timeout-error: 0 |tls-handshake: 14 |gross-tls-handshake: 14 |
    elapsed-time: 0.95191 secs

    Due to a bug in TLS-Scan, you may not see the detailed output with elapsed-time messages. TLS-Scan will still generate the output file we need for the scan results. 

**The TLS-Scan command line can be broken down into the following components:**

- **--port=443** - Collect TLS information using TCP port 443
- **--cacert=/opt/tls-scan/ca-bundle.crt** -  Specifies the path to the root CA certificate bundle used to verify certificates
- **-o simcloud-tlsinfo.json** - Save the scan results to the specified output file name
- **< simcloud-targets.txt** - Get the list of target IP addresses to assess using shell redirection (read the contents of the simcloud-targets.txt file)

TLS-Scan will quickly connect to each of the 14 target hosts and collect certificate information, saving the collected information in the specified JSON file. The collected certificate information will often reveal the cloud system owner, allowing an attacker to perform attribution analysis on the target.

## Conduct Target Attribution

The TLS-Scan JSON file includes several pieces of information that can be used for attribution: certificate subject, common name, subject alt name, and others. We can use JQ to process the JSON file to extract this information. Run the JQ command shown below to extract IP address and subject common name information from the certificate chain for each identified TLS server, as shown below.

    sec504@slingshot:~$ jq '.ip + " " + .certificateChain[].subjectCN' < simcloud-tlsinfo.json
    "10.200.227.71 *.genusight.com"
    "10.200.0.3 *.sunsetisp.com"
    "10.200.84.164 *.genusight.com"
    ...

**The JQ command line can be broken down into the following components:**

- **'.ip + " " + .certificateChain[].subjectCN'** - The JQ program, selecting the .ip and .certificateChain[].subjectCN fields for each record in the JSON file, concatenated with spaces
- **< simcloud-tlsinfo.json** - Get the JSON data using shell redirection

### Question: What is the IP address and host name of the Falsimentis system?

The output of the JQ command will reveal IP address and certificate subject common name information for several hosts. You can inspect the results manually, or use `grep` to identify any string returned that identifies the falsimentis.com domain, as shown here.

    sec504@slingshot:~$ jq '.ip + " " + .certificateChain[].subjectCN' < simcloud-tlsinfo.json | grep falsimentis
    "10.200.74.2 downloads.falsimentis.com"

**Answer**: The IP address and host name of the Falsimentis system are 10.200.74.2 and downloads.falsimentis.com.

## Create an EyeWitness Report

Although not required for cloud scanning, EyeWitness is a useful tool to create a visual report of several target systems. Unlike Masscan and Nmap, EyeWitness focused on visually representing the target system by taking a screenshot of the website or other graphical interfaces (RDP, VNC), creating an HTML report of the scan results.

From the Slingshot Linux command line, create an EyeWitness report for all of the cloud systems identified in the Masscan results, as shown here.

    sec504@slingshot:~$ /opt/eyewitness/Python/EyeWitness.py --web -f simcloud-targets.txt --prepend-https

    ################################################################################
    #                                  EyeWitness                                  #
    ################################################################################
    #           FortyNorth Security - https://www.fortynorthsecurity.com           #
    ################################################################################

    Starting Web Requests (28 Hosts)
    Attempting to screenshot http://10.200.227.71
    Attempting to screenshot https://10.200.227.71
    Attempting to screenshot http://10.200.0.3
    Attempting to screenshot https://10.200.0.3
    ...
    Finished in 44.29612350463867 seconds

    [*] Done! Report written in the /home/sec504/05112021_165523 folder!
    Would you like to open the report now? [Y/n]
    y

After opening the EyeWitness report in Firefox, scroll to find the Falsimentis target system, as shown here. Note that the server may not be on the first page of scan results since the servers are enumerated in the Masscan target list file order.

EyeWitness Report Showing downloads.falsimentis.com

### Cleanup

Terminate the simulated cloud network by running stopmasscannet, as shown here.

    sec504@slingshot:~$ stopmasscannet
    Stopping Docker containers for masscan lab
    masscantarget
    dockerrouter
    Done

## Why This Lab Is Important

To many, cloud assets can seem anonymous: just another server deployed in the cloud. Especially when the systems are not actively in use (perhaps for staging or development purposes), or have not been allowed public DNS entries, a cloud server can be lost in a sea of other systems.

In this lab, we see how an attacker can scan large numbers of entities using Masscan. While we scanned only 65,535 hosts in this exercise, Masscan can quickly scan millions of systems to identify a list of targets listening on designated ports. While these scan results don't provide any ownership attribution for the identified targets, TLS-Scan can quickly extract certificate information which can reveal the target server owner quickly.

Attackers can use these techniques to scan and enumerate assets hosted by various cloud providers, disclosing servers that belong to a target organization. After identifying the systems, the attackers can attempt to exploit them directly, often bypassing other security controls including Web Application Firewalls (WAFs). We'll return to these additional attacks including WAF bypass later in the course.