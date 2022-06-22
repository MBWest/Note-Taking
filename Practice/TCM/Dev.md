# Dev

## IP Address Dev

`10.0.2.6`

## IP Address Kali

`10.0.2.4`

## Nmap

    ┌──(root💀kali)-[~]
    └─# nmap -A -T4 10.0.2.6 
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-21 10:21 EDT
    Nmap scan report for 10.0.2.6
    Host is up (0.00047s latency).
    Not shown: 995 closed tcp ports (reset)
    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
    | ssh-hostkey: 
    |   2048 bd:96:ec:08:2f:b1:ea:06:ca:fc:46:8a:7e:8a:e3:55 (RSA)
    |   256 56:32:3b:9f:48:2d:e0:7e:1b:df:20:f8:03:60:56:5e (ECDSA)
    |_  256 95:dd:20:ee:6f:01:b6:e1:43:2e:3c:f4:38:03:5b:36 (ED25519)
    80/tcp   open  http    Apache httpd 2.4.38 ((Debian))
    |_http-server-header: Apache/2.4.38 (Debian)
    |_http-title: Bolt - Installation error
    111/tcp  open  rpcbind 2-4 (RPC #100000)
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100003  3           2049/udp   nfs
    |   100003  3           2049/udp6  nfs
    |   100003  3,4         2049/tcp   nfs
    |   100003  3,4         2049/tcp6  nfs
    |   100005  1,2,3      37463/udp   mountd
    |   100005  1,2,3      43355/tcp6  mountd
    |   100005  1,2,3      48548/udp6  mountd
    |   100005  1,2,3      50433/tcp   mountd
    |   100021  1,3,4      35130/udp   nlockmgr
    |   100021  1,3,4      38566/udp6  nlockmgr
    |   100021  1,3,4      45721/tcp   nlockmgr
    |   100021  1,3,4      45879/tcp6  nlockmgr
    |   100227  3           2049/tcp   nfs_acl
    |   100227  3           2049/tcp6  nfs_acl
    |   100227  3           2049/udp   nfs_acl
    |_  100227  3           2049/udp6  nfs_acl
    2049/tcp open  nfs_acl 3 (RPC #100227)
    8080/tcp open  http    Apache httpd 2.4.38 ((Debian))
    |_http-server-header: Apache/2.4.38 (Debian)
    | http-open-proxy: Potentially OPEN proxy.
    |_Methods supported:CONNECTION
    |_http-title: PHP 7.3.27-1~deb10u1 - phpinfo()
    MAC Address: 08:00:27:19:93:7E (Oracle VirtualBox virtual NIC)
    Device type: general purpose
    Running: Linux 4.X|5.X
    OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
    OS details: Linux 4.15 - 5.6
    Network Distance: 1 hop
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    TRACEROUTE
    HOP RTT     ADDRESS
    1   0.47 ms 10.0.2.6

                              