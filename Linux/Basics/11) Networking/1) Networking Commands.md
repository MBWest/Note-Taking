# Linux Networking - Commands

> ## **ifconfig [interface] || ifconfig interface [aftype] options | address**
- Used to configure network interfaces (deprecated)
- `interface` - name of the interface (eth0, eth1, ...)
- `aftype` - supported address family (inet, inet6)

```
[guru@CentOS ~]$ ifconfig ens32
ens32      Link encap:Ethernet  HWaddr 6E:37:88:D2:6F:D7  
          inet addr:104.236.58.12  Bcast:104.236.63.255  Mask:255.255.192.0
          inet6 addr: fe80::6c37:88ff:fed2:6fd7/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:460744 errors:0 dropped:0 overruns:0 frame:0
          TX packets:506895 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:94777063 (90.3 MiB)  TX bytes:99987778 (95.3 MiB)

[guru@CentOS ~]$ sudo ifconfig ens32 192.168.1.200/24

[guru@CentOS ~]$ ifconfig ens32
ens32      Link encap:Ethernet  HWaddr 6E:37:88:D2:6F:D7  
          inet addr:192.168.1.200 Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::6c37:88ff:fed2:6fd7/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:460744 errors:0 dropped:0 overruns:0 frame:0
          TX packets:506895 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:94777063 (90.3 MiB)  TX bytes:99987778 (95.3 MiB)
```

---

> ## **route [add|del] target [netmask nm] [gw gw]**
- Manipulates the kernel’s IP routing tables (deprecated)

```
[guru@CentOS ~]$ route add default gw 104.236.0.1 dev ens32

[guru@CentOS ~]$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
104.236.0.0     0.0.0.0         255.255.192.0   U     0      0        0 eth0
10.17.0.0       0.0.0.0         255.255.0.0     U     0      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1002   0        0 eth0
0.0.0.0         104.236.0.1     0.0.0.0         UG    0      0        0 eth0
```

---

> ## **ping [OPTIONS] destination**
- Uses the ICMP protocol’s ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway
- `-b` - allow pinging a broadcast address
- `-c COUNT`    - stop after sending COUNT packets
- `-i INTERVAL` - wait INTERVAL seconds between each packet

```
[guru@CentOS ~]$ sudo ping -c 2 -i 0.1 amazon.com
[sudo] password for guru: 
PING amazon.com (54.239.25.200) 56(84) bytes of data.
64 bytes from 54.239.25.200: icmp_seq=1 ttl=236 time=8.35 ms
64 bytes from 54.239.25.200: icmp_seq=2 ttl=236 time=8.14 ms
--- amazon.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 108ms
rtt min/avg/max/mdev = 8.141/8.248/8.355/0.107 ms
```

---

> ## **/etc/sysconfig/network-scripts**
- Contains configuration files named after their interfaces
    - ifcfg-ens32, ifcfg-ens33 ...
- Also contains IP, netmask, and gateway settings
- Permanent IP setting changes can be made using these files

---

> ## **/etc/resolv.conf**
- Resolver configuration file
- Make permanent changes to DNS server settings

```
[guru@CentOS ~]$ cat /etc/resolv.conf 
nameserver 8.8.8.8
nameserver 8.8.4.4
```

---

> ## **ssh [options] [user@]hostname [command]**
- A program for logging into a remote machine
- `-l login_name` – user to login as on the remote machine
- `-p port` – port to connect to on the remote machine
- `-v` – increase verbosity
- `-X` – enables X11 forwarding 

```
[student.lcl.adm@CentOS ~]$ ssh 10.0.0.227
student.lcl.adm@10.0.0.227’s password: 
Last login: Mon Oct 30 16:39:51 2017
```

---

> ## **netstat [OPTIONS]...**
- Print network connections
- `-a` – show both listening and non-listening sockets
- `-n` – numerical addresses instead of resolving host, port, or user names
- `-p` – show PID and name of the program to which each socket belongs
- `-t` – show only tcp protocol

```
# netstat –anpt
tcp	0      0 *:22	*:*	LISTEN	456/sshd
tcp	0      0 *:80	*:*	LISTEN	9056/httpd
tcp	0      0 10.0.1.3:80   	10.0.12.227:57642 		TIME_WAIT   -
tcp	0      0 10.0.1.3:80 	10.0.12.227:57783 		TIME_WAIT   -
tcp	0      0 10.0.1.3:80 	10.0.12.227:57769	 	TIME_WAIT   -
tcp	0      0 10.0.1.3:80 	10.0.12.227:35270		TIME_WAIT   -
tcp	0      0 10.0.1.3:80 	10.0.12.227:41614 		TIME_WAIT   -
tcp	0      0 10.0.1.3:22	10.0.12.227:31765		ESTABLISHED
```

