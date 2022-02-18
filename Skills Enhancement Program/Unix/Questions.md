#Questions

## Unix

### Unix Shells and Scripting

1. How would you view the manual page for SSH? **man ssh**

2. What is the standard shell that most other shell versions are based off of? **Bourne Shell**

3. What is root's default shell for FreeBSD? **tcsh**

4. In one line, write a find command that: Finds all files on the machine named "config" using case insensitive search and redirects STDERR to /dev/null. **find / -iname config 2>/dev/null**

5. What symbol is used to redirect STDOUT and STDERR to the same place? **>&**

6. Write a command that will count the number of lines in /etc/passwd and write the result to /tmp/lines. **wc -l /etc/passwd > /tmp/lines**

7. On one line write two commands that will assign the value /bin/bash to a variable called myshell and then print the value of myshell.

8. Write a command that will promote the variable myshell to an environment variable and reassign the value to /bin/sh.

9. What should be the first line in a bash script? **#!/bin/bash**

### Unix Filesystems

1. Which directory stores critical system and configuration files? **/etc**

2. Where is the file that contains the OS kernel usually located? **/boot**


3. Which directory contains on-line manual pages? **/usr/share/man**

4. Which of the following are stored as regular files?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Links

    B. Sockets

    C. Executables

    D. Configuration Files

    E. Device Files

    F. Text Files

    G. Libraries`

5. A link that has the same inode number as the original file is a:
Format: Multiple Choice, Letter only
**A. Hard Link**
B. Symbolic Link

6. (T/F) Hard links can be used across filesystems, while soft links cannot. **False**

7. Write a command that will create a symbolic link named /tmp/log to /var/log/secure. **ln -s /var/log/secure /tmp/log**

8. Which of the following correctly describes a partition?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. System that aggregates physical devices to form pools

    B. Determines where and how file contents are stored

    C. Is used to increase reliability by duplicating data across disks

    **D. Is a fixed-size subsection of a storage device**

    **E. Has its own device file**

9. (T/F) RAID can increase the amount of storage space available for a device. **False**


10. It can be beneficial to put which of the following directories on a secondary partition?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. /var/log

    **B. /tmp**

    C. /root

    **D. /var**

    E. /etc

11. Which partitioning scheme is preferred for newer devices? **GPT** (GUID Partition Table)

### Unix Users and Permissions 

1. What file defines groups in most Unix systems? **/etc/group**

    For assistance in completing this challenge refer to pages 244-252 in the UNIX and Linux System Administration Handbook 5th Edition.

2. On Linux, if you create a normal user, their UID will typically be higher than what number? **1000**

    For assistance in completing this challenge refer to pages 244-252 in the UNIX and Linux System Administration Handbook 5th Edition.

3. What would be the octal value equivalent of a file that has the following permissions (-rwx--x-w-): **712**

    For assistance in completing this challenge refer to pages 132-139 in the UNIX and Linux System Administration Handbook 5th Edition.

4. Using mnemonic syntax, provide the chmod command to add the following permissions to the file /myfile:
    Owner: rwx
    Group:rw
    Other:x

5. The parent of a currently running process dies. What is the new parent of this process? **init**
     
     For assistance in completing this challenge refer to pages 92-94 in the UNIX and Linux System Administration Handbook 5th Edition.

## Unix Networking and Name Resolution

1. In regards to **/etc/resolv.conf**, what keyword deteremines the domain(s) to be queried if the hostname is not fully qualified?

    For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition.



2.

3.

4.

5.

6.

7.

8.

9.

## Unix Firewalls 1

1. What is the default iptables table? **filter**

2. Which default iptables chain do packets pass through when they need to be forwarded to a different interface? **forward**

3. Which default iptables table can be used to circumvent kernel connection tracking? **raw**

4. An Ubuntu redirector has correct iptables rules configured to forward traffic to a target machine, however no packets are forwarded. Use the cat command to check the value of a kernel variable to see if ipv4 forwarding is enabled. **cat /proc/sys/net/ipv4/ip_forward**

5. An Ubuntu redirector has correct iptables rules configured to forward traffic to a target machine, however no packets are forwarded. We have discovered that it does not have routing enabled. Use the sysctl command to temporarily enable forwarding. **sysctl -w net.ipv4.ip_forward=1**

6. Write an iptables command that will set the default policy of the input chain to drop all packets. **iptables -P INPUT DROP**

7. Write an iptables command that will add a rule to log all packets received on eth0 that are destined for this machine. **iptables -A INPUT -i eth0 -j LOG**

    **Format**: iptables -option chain -option interface -option target

8. Write an iptables command that will add a rule to accept packets with any protocol that are destined for this device on eth1. **iptables -A INPUT -i eth1 -p ANY -j ACCEPT**

    **Format**: iptables -option chain -option interface -option proto -option target

9. Write an iptables command to add a rule that will allow any incoming TCP packets destined for the machine that are part of an ESTABLISHED or RELATED connection. **iptables -A INPUT -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT**

    **Format**: iptables -option chain -option proto -option match --state STATE,STATE -option target

10. Write a command to view the ipfilter active filtering rule set. **ipfstat -io**

11. Write a command to flush the existing ipfilter ruleset, and load a set of rules from /tmp/ipf/ipf.conf. **ipf -Fa -f /tmp/ipf/ipf.conf**

12. Based on the attached ipf.conf file, incoming packets from which of the following IP addresses would be blocked?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

   ** A. 10.1.254.12**

    B. 192.168.1.2

    **C. 210.18.28.10**

    **D. 192.168.1.12**

    E. 210.18.33.253

13. Based on the attached ipf.conf file, incoming TCP packets from 192.168.1.14 would be allowed to which of the following ports? Assume all packets are from a new connection.

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    **A. 22**

    B. 53

    **C. 80**

    **D. 111**

    **E. 443**

    F. 1337

    **G. 8080**

14. A router has made a decision to forward a packet. What is the next iptables table that will process the packet?

    Format: Multiple choice, single letter

    A. Forward

    B. Filter

    C. NAT

    D. Output

    **E. Mangle**

    F. Raw

## Unix Processes

1. What identification number determines the resources a process has access to at a given moment?

2. Which processes has the highest priority in CPU time?

    A. Process with a niceness of 0 

    **B. Process with a niceness of -10** 

    C. Process with a niceness of 10

3. Which of the following signals cannot be blocked and is processed at the kernel level?

    A. TERM 
    
    B. QUIT 
    
    C. INT 
    
    **D. KILL**

4. What command should be used to guarantee that the following process will die? **kill -9**

    USER PID COMMAND

    root 1023 nc -nlvp 1234 -e /bin/bash

5. Where in the /proc filesystem would you find the symbolic link to the file being executing for the following process? **/proc/1023/exe**

    PID USER COMMAND 1023 root nc -nlvp 5050 -e /bin/bash

    Enter absolute path

6. What command is used to follow the system calls made by a given process in Linux? **strace**

7. Write the crontab entry for running the command /usr/bin/nc -lp 1234 every Monday at 0800. **0 8 * * 1 /usr/bin/nc -lp 1234**

    FORMAT: Each field separated by a space

    e.g.,

    * * * * * echo $(date) >> ~/date.log

8. Based on the attached process list, write a pkill command that will send a TERM signal to the children of the script.sh process. Use the PID of the specified process. **pkill -15 -P 13635**

