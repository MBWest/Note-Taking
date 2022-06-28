# Linux - Initial Enumeration

`We have landed on a box, what are we working with?`

**Host information**

    hostname
    uname -a
    cat /proc/version
    cat /etc/issue
    lscpu

**Service Information**

    ps aux

 **User Enumeration**

    whoami
    id
    sudo -l
    cat /etc/passwd | cut -d : -f 1
    groups
    cat /etc/groups
    history
    w

**Netowrk Enumeration**

    ipconfig
    ip a
    route
    ip route
    arp -a
    arp -a
    ip neigh3) Passwords and File Permissions
    netstat -ano

**Password Hunting**

    grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2> /dev/null
    locate password | more
    find / -name authorized_keys 2> /dev/null
    find / -name id_rsa 2> /dev/null

# Resources

`Basic Linux Privilege Escalation`

https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/

`Linux Privilege Escalation`

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md

`Checklist - Linux Privilege Escalation`

https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist

`Sushant 747's Guide (Country dependant - may need VPN)`

https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_-_linux.html

`Course Repo`

https://github.com/TCM-Course-Resources/Linux-Privilege-Escalation-Resources

`LinuxPrivSec TryHackMe`

https://tryhackme.com/room/linuxprivescarena

`GTFOBins`

https://gtfobins.github.io/gtfobins/less/#sudo

`Payload All the Things`

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md