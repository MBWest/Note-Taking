# Windows Command Interpreter - Networking

## **ipconfig**

- Displays network adapter information

```
C:\>ipconfig /all		    # Displays detailed information for each network adapter

C:\>ipconfig /release	    # Releases current DHCP address

C:\>ipconfig /renew	        # Renews DHCP address
```

---
---
---

## **ping**

- Sends four ICMP requests and waits for a response to see if the specified system is up (is there connectivity to the device?)

```
C:\>ping www.google.com 		# Pings www.google.com 4 times

C:\>ping –n 2 10.10.0.3			# Pings 10.10.0.3 2 times

C:\>ping –t 10.10.0.3			# Pings 10.10.0.3 until it’s stopped
```

---
---
---

## **tracert**

- Traces each hop (next router interface) between the source and destination IPs

```
C:\>tracert www.google.com	        # Traces the number of hops to www.google.com

C:\>tracert –d 192.168.0.11	        # Traces hops to 192.169.0.100, won’t resolve hostnames

C:\>tracert –w 50 www.google.com	# Traces hops to www.google.com – only waits 50 ms
```

---
---
---

## **netstat**

- Displays protocol and Ethernet statistics, and current TCP/IP connections

```
C:\>netstat			    # Displays active connections

C:\>netstat –a			# Displays all connections (listening ports)

C:\>netstat –b			# Displays executables associated with ports

C:\>netstat –p			# Displays only TCP connections

C:\>netstat –r			# Displays routing table

C:\>netstat –e			# Displays Ethernet statistics
```