# Questions

## Unix

### Unix Shells and Scripting

1. How would you view the manual page for SSH? **man ssh**

2. What is the standard shell that most other shell versions are based off of? **Bourne Shell**

3. What is root's default shell for FreeBSD? **tcsh**

4. In one line, write a find command that: Finds all files on the machine named "config" using case insensitive search and redirects STDERR to /dev/null. **find / -iname config 2>/dev/null**

5. What symbol is used to redirect STDOUT and STDERR to the same place? **>&**

6. Write a command that will count the number of lines in /etc/passwd and write the result to /tmp/lines. **wc -l /etc/passwd > /tmp/lines**

7. On one line write two commands that will assign the value /bin/bash to a variable called myshell and then print the value of myshell. **myshell=/bin/bash; echo $myshell**

8. Write a command that will promote the variable myshell to an environment variable and reassign the value to /bin/sh. **export myshell=/bin/sh**

9. What should be the first line in a bash script? **#!/bin/bash**

### Unix Filesystems

1. Which directory stores critical system and configuration files? **/etc**

2. Where is the file that contains the OS kernel usually located? **/boot**


3. Which directory contains on-line manual pages? **/usr/share/man**

4. Which of the following are stored as regular files?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Links

    B. Sockets

    **C. Executables**

    **D. Configuration Files**

    E. Device Files

    **F. Text Files**

    **G. Libraries**

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

4. Using mnemonic syntax, provide the chmod command to add the following permissions to the file /myfile: **chmod u+rwx,g+rw,o+x**

    Owner: rwx
    Group:rw
    Other:x

5. The parent of a currently running process dies. What is the new parent of this process? **init**
     
     For assistance in completing this challenge refer to pages 92-94 in the UNIX and Linux System Administration Handbook 5th Edition.

### Unix Networking and Name Resolution

1. In regards to **/etc/resolv.conf**, what keyword deteremines the domain(s) to be queried if the hostname is not fully qualified? **search**

    For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition.


2. For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition. **files**

    In regards to /etc/nsswitch.conf, what keyword refers to querying the /etc/hosts file for name resolution?

3. For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition.

    The following is an entry in /etc/nsswitch.conf

	hosts: dns [!UNAVAIL=return] files
    Assuming this the only entry in the file concerning name resolution, will /etc/hosts be referenced if DNS lookup fails? 

    Answer with either True or **False**

4. What arguments for the netstat command will display the routing table without resolving host names, port numbers, and user names? **-rn**

    Refer to the manpage of netstat for assistance in answering this challenge. One place you can look is (https://linux.die.net/man/8/netstat) 

5. Refer to the manpage of netstat for assistance in answering this challenge. One place you can look is here (https://linux.die.net/man/8/netstat).  **-pantu**

    Provide the correct options for netstat that will perform the following:

    Show the PID of the program for each socket

    Show listening and non-listening ports

    Does not resolve hostnames,ports, or usernames

    Shows TCP connections

    Show UDP connections

    Provide you answer ordering options 1-5 from left to right. For example if the answer to 1 
    was -a and the answer to 2 was -b, etc, you answer will be -abcde

6. If the system you run netstat on attempted to initiate a connection but has not yet received a response, what state is the connection most likely listed as?  **SYN_SENT**

    To answer this challenge, you may refer to this page(https://www.supportsages.com/understanding-the-netstat-command/).

7.  This system is listening on tcp for what 3 network services? Separate each answer with commas, no spaces, and in alphabetical order. Use acronyms or abbreviated names of the services to get marked correct. **DNS,ipp,MySQL**

    To answer this challenge, refer to the attached netstat output and a listing of common UNIX ports such as this one.

8. What is the most popular implementation of DNS? **BIND**

    For assistance in completing this challenge refer to pages 498-500 in the UNIX and Linux System Administration Handbook 5th Edition.


9. Which version of NFS removed the need for the lockd and statd daemon? **4**

    For assistance in completing this challenge refer to pages 791-798 in the UNIX and Linux System Administration Handbook 5th Edition.


### Unix Firewalls 1

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

    **A. 10.1.254.12**

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

### Unix Processes

1. What identification number determines the resources a process has access to at a given moment? **EUID**

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

8. Which of the following methods can be used to investigate a suspicious process with a PID of 5435

    **A. ps -ef | grep 5435**

    **B. netstat -pant | grep 5435**

    **C. ls -l /proc/5435**

    **D. strace -p 5435**

9. Based on the attached process list, write a pkill command that will send a TERM signal to the children of the script.sh process. Use the PID of the specified process. **pkill -15 -P 13635**

### Unix Logging 1

1. What are the major subtasks of log management? 

    **A. Collecting logs from a variety of sources**

    **B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages**

    **C. Managing the retention and expiration of messages**

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

2. What role does Unix's syslog play in log management?

    **A. Collecting logs from a variety of sources**

    B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages

    C. Managing the retention and expiration of messages

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

3. What role does Linux's systemd journal play in log management?

    **A. Collecting logs from a variety of sources**

    **B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages**

    **C. Managing the retention and expiration of messages**

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

4. What is the usual default path in Unix for storing log files? **/var/log**

5. Where are private authorization messages logged, including authentication and ssh login attempts? **/var/log/secure**

6. What log file does the last command interact with to display the record of user login/logout and system reboot information? **/var/log/wtmp**

7. What log file does the lastlog command interact with to display the record of most recent logins of users? **/var/log/lastlog**

8. What is the command to view the last 5 entries of journal logs created by the cron service? **journalctl -u cron -n 5**

9. What is the command to view all journal entries from the date 2021-08-01 to 2021-08-07? **journalctl --since=2021-08-01 --until=2021-08-07**

    FORMAT: command --option=value --option=value

10. Where is the default configuration file for systemd journal stored? **/etc/systemd/journald.conf**

11. In what directory custom configuration files for systemd journal stored? **/etc/systemd/journal.conf.d**

12. Where is the default location for the rsyslog's configuration file? **/etc/rsyslog.conf**

13. (T/F) Unlike systemd journal, syslog acts as a message router by, (1) taking input from various plug-ins, (2) filtering them according to its rules, and (3) outputting them to their destinations. **T**

14. What is the correct syntax to log all sensitive/private authorization message to /var/log/secure? **authpriv.* /var/log/secure**

    FORMAT: [selector]space[action]

15. What is the correct syntax to log all crit severity level messages (excluding other severity levels) to /var/log/crit? ***.=crit /var/log/crit**

    FORMAT: [selector]space[action]

16. What is the correct syntax to forward mail-related messages at priorities notice, warning, and crit to IP address 192.168.10.10 on TCP port 514? **mail.=notice;mail.=warning;mail.=crit @@192.168.10.10**

    FORMAT: [selector]space[action]

### Unix Boot and Login 

1. What is the first step in the boot process after the machine is powered on?

    A. Load boot loader

    B. Load system kernel

    **C. Load BIOS/UEFI**

2. Match the following descriptions to the corresponding firmware: **U,U,B,B,U,U**

    FORMAT: comma separated list (e.g., B,U,U,B,B)

    B: BIOS U: UEFI

    More modern standard of PC firmware
    Uses a disk partitioning scheme known as GPT (GUID Partition Table)
    Assumes boot device starts with the MBR (Master Boot Record)
    Requires execution of second-stage boot loader
    Defines APIs for accessing system hardware
    Consults its partition table to identify the ESP

3. What sector of a storage device contains the code responsible for reading the partitioning information from the MBR and executing the second-stage boot loader?  **volume boot record**

4. What is the boot loader's main function?

    A. Consult the MBR for the location of the boot block 
    **B. Identity and load the OS kernel** 
    C. Start the initial process (init) D. Mount the root file system

5. What is the absolute path to the GRUB config file in Red Hat and CentOS? **/boot/grub2/grub.cfg**

6. What is the boot loader for FreeBSD known as? **loader**


7. From which file is the grub.cfg generated? **/etc/default/grub**

8. What is the kernel boot time option to use /dev/sda1 as the root file system? **root=/dev/sda1**

9. What is the name of the system management daemon with a process ID of 1, and is the parent process for all other processes? **init**

10. What are some of the core responsibilities of init?

    **A. Mount filesystems** 
    **B. Configure network interfaces**
    **C. Start up other daemons and services**
    D. Execute initial user log in scripts

    FORMAT: comma separated list (e.g., A,C,D)

11. What term associated with** systemd** is analogous to traditional init's runlevel , which defines the operational mode of the system? **target**

12. What is the command that is used to manage and check the status of the configurations of systemd units? **systemctl**

### Unix Kernel Basics

1. Which of the following are classified as UNIX operating systems? **B,C,E**

2. The kernel provides which of the following functions?

    **A. Communication with processes and threads**

    B. Runs user applications

    **C. Provides memory management**

    **D. Management of hardware devices**

    E. None of the above

3. (T/F) Many kernel parameters can accessed from user mode to change the behavior of the kernel. **T**

4. (T/F) User processes have access to all of a system's memory space. **F**

5. Which of the following statements correctly describe User Space?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    **A. It is a form of sandbox to prevent system damage.**

    B. Core OS functions usually run in user space.

    C. When a process malfunctions within user space it will often crash the entire system.

    D. User applications run in protection ring 1.

    **E. User space processes interact with the kernel through system calls.**

6. What directory contains file objects that can be used to tune kernel parameters during runtime?  **/proc/sys**

7. What file can be used with the sysctl command to permanently set parameter configurations?  /**etc/sysctl.conf**

8. Write an echo command that will temporarily set the "panic_on_oops" parameter to 3. **echo 3 > /proc/sys/kernel/panic_on_oops**

9. Write a sysctl command that will display all kernel parameter values. **sysctl -a**

10. Which of the following statements do not correctly describe Linux kernel modules?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Kernel modules allow a driver to be linked in while the kernel is running.

    B. Almost anything can be built as a loadable kernel module.

    **C. Loading a kernel module can never cause a kernel panic.**

    **D. The implementation of loadable modules is the same for every OS.**

11. Write a modprobe command to list the dependencies of the ip_tables module. Assume you are root. **modprobe -D ip_tables**

## Networking



