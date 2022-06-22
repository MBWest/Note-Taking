# nmap

## Base Syntax

    nmap [ScanType] [Options] {targets}

------

## Flags

| **Flag** | **Description** |
|----------|-----------------|
| `-sn` | Probe only (host discovery, not port scan) |
| `-sS` | SYN Scan |
| `-sT` | TCP Connect Scan |
| `-sU` | UDP Scan |
| `-sV` | Version Scan |
| `-O` | OS Detection |
| `-A` | Use several features, including OS Detection, Version Detection, Script Scanning (default), and traceroute |
| `-n` | Disable reverse IP address lookups |
| `--reason` | Display reason Nmap thinks port is open, closed, or filtered |
| `-Pn` | Don't probe (assume all hosts are up) |

## dns-zone-transfer 

`Attempts to pull a zone file (AXFR) from a DNS server:`

    $ nmap --script dns-zone- transfer.nse --script-args dns-zone- transfer.domain=<domain> -p53 <hosts>

------

## Robots.txt

`Harvests robots.txt files from discovered web servers:`

    $ nmap --script http-robots.txt <hosts>

------ 

## SMB-Brute

`smb-brute: Attempts to determine valid username and password combinations via automated guessing:`

    $ nmap --script smb-brute.nse -p445 <hosts>

------

## SMB-psexec

`Attempts to run a series of programs on the target machine, using credentials provided as scriptargs:`

    $ nmap --script smb-psexec.nse – script-args=smbuser=<username>, smbpass=<password>[,config=<config>] -p445 <hosts> 

-------

## Scripting Engine

`Run default scripts`

    -sC

`Run individual or groups of scripts`

    --script=<ScriptName>|<ScriptCategory>|<ScriptDir>...
    
`Use the list of script arguments`

    --script-args=<Name1=Value1,...>
    
`Update script database`

    --script-updatedb

### Scripting Categories

Nmap's script categories include, but are not limited to, the following:

| **Category** | **Description** |
|--------------|-----------------|
| `auth` | Utilize credentials or bypass authentication on target hosts. |
| `broadcast` | Discover hosts not included on command line by broadcasting on local network. |
| `brute` | Attempt to guess passwords on target systems, for a variety of protocols, including http, SNMP, IAX, MySQL, VNC, etc. |
| `default` | Scripts run automatically when -sC or -A are used. |
| `discovery` | Try to learn more information about target hosts through public sources of information, SNMP, directory services, and more. |
| `dos` | May cause denial of service conditions in target hosts. |
| `exploit` | Attempt to exploit target systems. |
| `external` | Interact with third-party systems not included in target list. |
| `fuzzer` | Send unexpected input in network protocol fields. |
| `intrusive` | May crash target, consume excessive resources, or otherwise impact target machines in a malicious fashion. |
| `malware` | Look for signs of malware infection on the target hosts. |
| `safe` | Designed not to impact target in a negative fashion. |
| `version` | Measure the version of software or protocol spoken by target hosts. |
| `vul` | Measure whether target systems have a known vulnerability. |

------

## Target Ports

No port range specified scans 1,000 most popular
ports 

| **Option** | **Description** |
|------------|-----------------|
| `-F` | Scan 100 most popular ports |
| `-p<port1>-<port2>` | Port range |
| `-p<port1>,<port2>,...` | Port List |
| `-pU:53,U:110,T:20-445` | Mix TCP and UDP |
| `-r` | Scan linearly (do not randomize ports) |
| `--top-ports <n>` | Scan n most popular ports |
| `-p-65535` | Leaving off initial port in range makes Nmap scan start at port 1 |
| `-p0-` | Leaving off end port in range makes Nmap scan through port 65535 |
| `-p-` | Scan ports 1-65535 |

## Automated DNS Guessing Example

Note: Collection of lists that are useful for security assessments, including a longer list of host names than nmap default - https://github.com/danielmiessler/SecLists

| **Command**   | **Description**   |
| --------------|-------------------|
| **Automated DNS Guessing Using nmap** |
| `sudo nmap --dns-servers 172.30.0.254 --script dns-brute --script-args dns-brute.domain=falsimentis.com` | Automated DNS Guessing | 
| **Breakdown** |
| `sudo nmap` | Run Nmap with root privileges using sudo |
| `--dns-servers 172.30.0.254` |Specify the DNS server to use for name resolution; this can be a local DNS server, the target organization's DNS server, or another DNS resolver (such as Google's public DNS resolver at 8.8.8.8) |
| `--script dns-brute` | Tell Nmap to run the dns-brute script |
| `--script-args dns-brute.domain=falsimentis.com` | Specify the falsimentis.com domain as an argument for the dns-brute.domain parameter |

## Top ports

Shows the top 1000 ports that nmap uses

`nmap -vv -oG -`