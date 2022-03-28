
# SANS SEC 504 Lab Wiki

## Lab 1.2: Network Investigation

### Brief Intro

In this lab you will analyze network evidence from a simulated compromise.

The scenario used in this lab is continued in the two labs that follow (Lab 1.3: Memory Investigation, and Lab 1.4: Malware Investigation). In these labs you will examine additional evidence (memory images and malware) from the same compromise. So, make sure to keep your notes from this exercise, and add to them in later labs.
Requirements for This Lab

In this lab you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.
Try It Yourself

Read the scenario at the start of the Walkthrough section. Once you've familiarized yourself with the scenario, analyze the following files in the /home/sec504/labs/falsimentis directory:

    access.log
    falsimentis.pcap

As you analyze these files, try to answer the following questions:

    What systems are likely compromised in the organization?
    When did the threat actors begin their attack?
    What host(s) are the threat actors using for command and control (C2)?

### Walkthrough

The Scenario

The victim is Falsimentis, a small (fictitious) corporation based in Los Angeles, California, that produces artificial intelligence hardware and software. On Thursday the CEO decided to take the employees out to lunch. The CEO recalls locking their screen and leaving for lunch around 11:50 AM. Returning from lunch around 1:05 PM, the CEO noticed their computer had rebooted. After logging on, the CEO saw the following:

Ransom note

The message is a ransom note from a group of threat actors calling themselves the Midnite Meerkats. The note states that the Midnite Meerkats have control of the victim's systems, and unless the victim pays the ransom within 24 hours, the victim's files will be deleted. The URL that contains the ransom note is https://midnitemeerkats.com/note/.

The CEO contacted the system administrator, who collected various pieces of evidence. The system administrator was able to collect a packet capture of the internal network traffic that Falsimentis was recording for an upcoming audit by one of their large customers. The system administrator was also able to collect logs from a Squid proxy.

Here is a diagram of the Falsimentis network:

Falsimentis Network Diagram

The systems on the internal Falsimentis network are listed below.
IP 	Hostname 	Description
172.16.42.2 	FM-SRV-DC01.falsimentis.com 	Domain controller
172.16.42.3 	FM-SRV-FS01.falsimentis.com 	Corporate file server
172.16.42.10 	FM-NET-FW01.falsimentis.com 	Network firewall and Squid server
172.16.42.20 	FM-WEBDEV.falsimentis.com 	Internal web development server
172.16.42.103 	FM-TETRIS.falsimentis.com 	System administrator's workstation
172.16.42.105 	FM-ELECTRONICA.falsimentis.com 	Web developer's workstation
172.16.42.107 	FM-CEO.falsimentis.com 	CEO's workstation
172.16.42.108 	FM-ALGORITHM.falsimentis.com 	V.P. of Operations' workstation
172.16.42.109 	FM-GOLF.falsimentis.com 	An engineer's workstation

The publicly accessible Falsimentis systems are as follows:
IP 	Hostname 	Description
52.219.120.171 	www.falsimentis.com 	Public website
52.219.120.171 	email.falsimentis.com 	Webmail client (on same server as www)
10.5.96.4 	n/a 	Private IP address of the server hosting the public website
144.202.115.64 	fm-ext.falsimentis.com 	Firewall and VPN server
10.5.96.3 	n/a 	The private IP address of the firewall and VPN server

#### Getting Started

    Note: The approach taken here is not the only way to proceed through this exercise. Different analysts may take different approaches. 

Taking notes is vital to effective incident response, so let's record some key facts from the scenario (feel free to write these down yourself in your own notes):

    The CEO locked their workstation and left for lunch at around 11:50 AM.
    The CEO returned from lunch and logged on to their workstation at around 1:05 PM.
    The ransom note popped up after the CEO logged on.
    The ransom note is hosted at https://midnitemeerkats.com/note/
    The note states the victim has 24 hours to pay, or their files will be deleted.
    Compromised systems
    172.16.42.107 (FM-CEO)

The first three facts can be used as an anchor to start a timeline. The fact that the pop-up occurred implies there must have been threat actor activity prior to this point in time, since they would need to install whatever caused the pop-up. The fourth fact (the location of the ransom note) can be used as a pivot when searching through evidence. The 24-hour deadline (fifth fact) might be used by the business decision makers when deciding how to proceed. The fact about a compromised system is useful as a starting point for determining the scope, or how widespread the incident is.

Before proceeding, you will need to verify that an incident actually occurred. In the Falsimentis scenario, verification is relatively straight forward—the CEO had a ransom note pop-up on their screen. Even if the threat to delete the files is fake, the fact the message appeared right after logging on is enough to consider this an incident.

In any environment there will be a lot of data, often too much to go through by hand. To deal with this you will need to employ several different data reduction strategies, including filtering and pivoting.

#### Correlating Network Traffic

To begin, let's start by identifying network traffic that correlates with the CEO's statement about the ransom note appearing at around 1:05 PM. This is a good idea because human memory is less than perfect. It would not be uncommon if the CEO recalled the ransom note appearing up at 1:30 PM, even if it actually appeared up at 1:05 PM.

To do this start by looking at the Squid access.log file. Recall that Squid uses this file to record information about HTTP and HTTPS requests. Since threat actors commonly use these protocols for command and control (C2) communication, the Squid logs may contain useful clues.

During an investigation it is always important to keep in mind the limitations of the evidence you are analyzing, and the tools you are using. Squid proxy logs usually capture traffic only on the standard ports for HTTP and HTTPS (TCP ports 80 and 443 respectively). If the threat actors used HTTP and/or HTTPS on non-standard ports, then the Squid logs likely will not have records of the requests.

To start, open a terminal in Slingshot Linux. Next, change to the /home/sec504/labs/falsimentis directory and search through the access.log file for midnitemeerkats, the site where the ransom note was hosted. You can search with the grep command as shown here:

    sec504@slingshot:~$ cd /home/sec504/labs/falsimentis
    sec504@slingshot:~/labs/falsimentis$ grep midnitemeerkats access.log
    1584648356.572    175 172.16.42.107 TCP_MISS/301 671 GET http://www.midnitemeerkats.com/note - ORIGINAL_DST/69.163.156.144 text/html
    1584648359.613   2018 172.16.42.107 TCP_MISS/301 461 GET https://www.midnitemeerkats.com/note - ORIGINAL_DST/69.163.156.144 text/html
    1584648360.761    569 172.16.42.107 TCP_MISS/200 4404 GET https://midnitemeerkats.com/note/ - ORIGINAL_DST/69.163.156.144 text/html
    1584648360.983     51 172.16.42.107 TCP_MISS/200 1873 GET https://midnitemeerkats.com/wp-content/plugins/memberpress/css/ui/theme.css? - ORIGINAL_DST/69.163.156.144 text/css

The output shows Squid's native logging format. Each line contains multiple fields, most of which are separated by one or more spaces. Let's focus on just a few relevant fields: the time of the request, the requesting client, and the requested URL. These are the first, third, and seventh fields, respectively. To extract just these fields, use the awk command as shown here:

    sec504@slingshot:~/labs/falsimentis$ awk '/midnitemeerkats/ {print $1, $3, $7}' access.log
    1584648356.572 172.16.42.107 http://www.midnitemeerkats.com/note
    1584648359.613 172.16.42.107 https://www.midnitemeerkats.com/note
    1584648360.761 172.16.42.107 https://midnitemeerkats.com/note/
    1584648360.983 172.16.42.107 https://midnitemeerkats.com/wp-content/plugins/memberpress/css/ui/theme.css?

The awk command breaks down as follows:

    /midnitemeerkats/ - only process lines that contain the string midnitemeerkats
    print - print the following fields
    $1 - first field (timestamp)
    $3 - third field (requesting client)
    $7 - seventh field (requested URL)
    access.log - The file to process

The reduced output is easier to read than the original log contents. However, the timestamp field is in POSIX time format (also known as Epoch time), the number of seconds since January 1st 1970 00:00:00 UTC. With Squid logs, the timestamp also includes a millisecond resolution (the part to the right of the decimal point). To display POSIX time in a human-friendly format, you can use the strftime function with awk as shown here:

    sec504@slingshot:~/labs/falsimentis$ TZ=America/Los_Angeles awk '/midnitemeerkats/ {print strftime("%T", $1), $3, $7}' access.log
    13:05:56 172.16.42.107 http://www.midnitemeerkats.com/note
    13:05:59 172.16.42.107 https://www.midnitemeerkats.com/note
    13:06:00 172.16.42.107 https://midnitemeerkats.com/note/
    13:06:00 172.16.42.107 https://midnitemeerkats.com/wp-content/plugins/memberpress/css/ui/theme.css?

Let's break down the differences from this command line, and the previous awk command line:

    TZ=America/Los_Angeles - Temporarily sets the local timezone to America/Los_Angeles. This is needed because the timestamps are stored in the UTC timezone, and the strftime function can only display timestamps according to either UTC, or the local system timezone.
    strftime("%T", $1) - print the timestamp in HH:MM:SS format.

Based on the output, you can see network traffic correlates with the CEO's statement about the ransom note appearing around 1:05 PM.

#### Looking for Beacons in access.log

Now let's see if there are any footprints revealing network beacons. This (usually) means that you will see many requests to the same URL, at fairly consistent time intervals. Rather than attempting to use awk, try using a tool called findbeacons.py, which does as the name suggests: it finds beacons.

To tell findbeacons.py what time interval to look for use the -i argument. To specify a minimum number of beacon requests (to reduce false positives) use the -c argument. This is shown below:

    sec504@slingshot:~/labs/falsimentis$ ./findbeacons.py  -i 5 -c 10 172.16.42.107 access.log
    Sites that had at least 10 5-second intervals
    193 - https://push.services.mozilla.com/
    11 - 172.217.11.162:443
    43 - https://px.moatads.com/pixel.gif?
    12 - 216.58.217.194:443
    20 - 172.217.5.194:443
    11 - https://t.wayfair.com/b.php?
    11 - https://att-app.quantummetric.com/?
    10 - https://a.espncdn.com/combiner/i?
    3268 - http://www1-google-analytics.com/collect
    28 - https://start.specless.tech/report/1
    11 - https://apx.moatads.com/pixel.gif?

The findbeacons.py command breaks down as follows:

    -i 5 - look for beacons that are at 5-second intervals
    -c 10 - look for a minimum of 10 beacons
    172.16.42.107 - look for beacon traffic from host 172.16.42.107
    access.log - search through the file access.log

The output of findbeacons.py shows one URL that has several thousand packets at 5-second intervals, http://www1-google-analytics.com/collect. This URL is suspicious not only because of the large number of regularly-spaced requests, but also because it appears similar to www.google-analytics.com, which is a legitimate site.

#### Finding More Compromised Hosts

To find additional hosts in the network that are compromised, pivot on the domain www1-google-analytics.com by searching for it in the access.log file as shown.

sec504@slingshot:~/labs/falsimentis$ awk '/www1-google-analytics.com/ {print $3}' access.log | sort -u
172.16.42.103
172.16.42.105
172.16.42.107
172.16.42.109

This command line breaks down into the following components:

    awk '/www1-google-analytics.com/ {print $3};' access.log - print the third field (the requesting IP address) for lines that contain www1-google-analytics.com in the file access.log
    sort -u - sort the list of IP addresses, returning unique values

The output shows three additional systems communicating with www1-google-analytics.com: 172.16.42.103, 172.16.42.105, and 172.16.42.109. It would be a good idea to add theses to the list of compromised systems.

#### Finding Even More Compromised Hosts

Up to this point we've been searching through the access.log file, which only reflects HTTP and HTTPS traffic recorded by the proxy. Any HTTP and HTTPS traffic on non-standard ports would not be visible. So, let's pivot again on this host, but this time by searching through the packet capture file.

To do this we need to first determine the IP address of www1-google-analytics.com. This information can be found in the access.log file as shown here:

    sec504@slingshot:~/labs/falsimentis$ grep www1-google-analytics.com access.log | head -n 1
    1584638136.869    179 172.16.42.107 TCP_MISS/200 62808 POST http://www1-google-analytics.com/collect - ORIGINAL_DST/167.172.201.123 text/html

The command line can be broken down into the following components:

    grep www1-google-analytics.com access.log - extract lines that contain the string www1-google-analytics.com.
    head -n 1 - only show the first line of output

Here we can see the IP address of www1-google-analytics.com is 167.172.201.123. Now we can search through the packet capture file falismentis.pcap for traffic destined to this IP as shown here:

    sec504@slingshot:~/labs/falsimentis$ tcpdump -nr falsimentis.pcap dst host 167.172.201.123 | cut -d ' ' -f 3 | cut -d '.' -f 1-4 | sort -u
    172.16.42.103
    172.16.42.105
    172.16.42.107
    172.16.42.108
    172.16.42.109
    172.16.42.2
    172.16.42.3

Broken into pieces, this command line is as follows:

    tcpdump -nr falsimentis.pcap dst host 167.172.201.123 - print packets from the file falsimentis.pcap that are destined for host 167.172.201.123
    cut -d ' ' -f 3 - return the third space-delimited field from the tcpdump output (the IP address and port number).
    cut -d '.' -f 1-4 - cut the IP address and port number combination into pieces at the . character, and then select the first four fields (the IP address).
    Sort the IP addresses with sort, displaying only unique lines (-u).

The output from tcpdump reveals three additional hosts sending traffic to www1-google-analytics.com, 172.16.42.2 (the domain controller), 172.16.42.3 (the file server), and 172.16.42.108 (the VP of Operation's workstation). As before, it would be a good idea to add these systems to the list of compromised systems.

#### Finding the First Packet

To get an estimate when the malicious traffic started, we can examine the first packet that was sent from each compromised host to www1-google-analytics.com (167.172.201.123). This can be done with a for loop as shown here:

    sec504@slingshot:~/labs/falsimentis$ for octet in 2 3 103 105 107 108 109; do TZ=PST7PDT tcpdump -tttt -n -r falsimentis.pcap -c 1 "src host 172.16.42.$octet and dst host 167.172.201.123" 2>/dev/null; done
    2020-03-19 09:10:48.693390 IP 172.16.42.2.53699 > 167.172.201.123.8090: Flags [SEW], seq 141186417, win 8192, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:38:15.622304 IP 172.16.42.3.52449 > 167.172.201.123.8090: Flags [SEW], seq 966832680, win 8192, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:46:11.679708 IP 172.16.42.103.51838 > 167.172.201.123.8090: Flags [S], seq 945749049, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:48:39.181576 IP 172.16.42.105.58343 > 167.172.201.123.8090: Flags [S], seq 2308409837, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:50:23.886662 IP 172.16.42.107.57932 > 167.172.201.123.8090: Flags [S], seq 1940514557, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:55:19.306997 IP 172.16.42.108.61412 > 167.172.201.123.8090: Flags [S], seq 4172553415, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 09:57:04.359504 IP 172.16.42.109.64231 > 167.172.201.123.8090: Flags [S], seq 3275538513, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0

Note: The underlines have been added to make the timestamps and port numbers easier to see in the workbook. You won't see them when you run the command at the terminal. 

There is a lot going on with this for loop; it breaks down as follows:

    for octet in 2 3 103 105 107 108 109; - Defines the loop variable, octet, and a list of numbers to iterate across. This list contains the last octet of each compromised system.
    do - Denotes the start of the commands that are executed in each iteration of the loop.
    TZ=PST7PDT - Set the timezone used to display timestamps. Unlike the awk command, tcpdump needs the daylight savings time information included in the timezone specification.
    tcpdump -tttt -n -r falsimentis.pcap -c 1 - Show timestamps in HH:MM:SS.(fractions of a second) format, don't resolve hosts or port numbers, read packets from the file falsimentis.pcap, and stop after finding the first packet that matches the filter.
    "src host 172.16.42.$octet and dst host 167.172.201.123" - Search for traffic originating from one of the systems believed to be compromised, going to 167.172.201.123.
    2>/dev/null - Discard some of the irrelevant tcpdump output.
    done - Denotes the end of the commands that are executed in each iteration of the loop.

Notice that the timestamps for these packets varies from 9:10 AM to 9:57 AM. However, these timestamps are for packets destined for port 8090, not port 80.

To find the first timestamp for port 80 traffic, modify the previous for loop as shown here:

    sec504@slingshot:~/labs/falsimentis$ for octet in 2 3 103 105 107 108 109; do TZ=PST7PDT tcpdump -tttt -n -r falsimentis.pcap -c 1 "src host 172.16.42.$octet and dst host 167.172.201.123 and dst port 80" 2>/dev/null; done
    2020-03-19 10:34:16.505799 IP 172.16.42.103.52458 > 167.172.201.123.80: Flags [S], seq 1388216751, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 10:38:00.315836 IP 172.16.42.105.61182 > 167.172.201.123.80: Flags [S], seq 979163751, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 10:15:36.693484 IP 172.16.42.107.60227 > 167.172.201.123.80: Flags [S], seq 2927374010, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
    2020-03-19 10:48:35.338023 IP 172.16.42.109.51040 > 167.172.201.123.80: Flags [S], seq 493181052, win 64240, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0

Notice the end of the filter now contains and dst port 80, focusing on just HTTP traffic. 

The underlines have been added to the workbook to make the timestamps easier to read. They will not appear in your terminal. 

### Summary and Timeline of Events

At this point there has been a fair amount of information uncovered, including a new C2 server www1-google-analytics.com, and the scope of the incident has expanded from the CEO's workstation to almost every machine in the Falsimentis network. There are also specific timestamps gathered representing beaconing and other network activity.

One way to represent this information in a succinct manner is to create an SE3R Diagram as shown below.

### Timeline of Events

The horizontal line, called the event line, shows what events occurred at which points in time. The boxes near the bottom are called knowledge bins and are an efficient way to group related information together. The information in knowledge bins can add and enhance the information on the event line.
Why This Lab is Important

When first responding to an incident you need to quickly verify that an incident actually occurred and gain an initial scope. As you found in this exercise what was initially reported as the compromise of a single system, turned out to be much bigger incident.

Building a timeline of events transforms a series of independent facts into a visual representation and can help understand the big picture by showing how different events relate to each other.

Lastly, successful investigations involve more than just technical skills. Being able to identify, extract, and organize relevant data, and identify gaps are also important skills. This is not to say that technical skills are not important, they certainly are. However, they are just one of the many things used to conduct a successful investigation.
Video Walkthrough

### Watch the accompanying video instructions for additional information.

Video Walkthrough Screen Shot
Additional Resources
SANS Classes

    SEC503: Intrusion Detection In-Depth
    FOR572: Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response

Other Related Resources

    Network Forensics: Tracking Hackers through Cyberspace
    SE3R: Capture and Analyze Fine-Grain Detail