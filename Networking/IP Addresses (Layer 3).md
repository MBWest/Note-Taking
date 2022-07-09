# Ip Addresses are Layer 3 Protocols (Networking)

---

> ## **Command**
**ifconfig** - Your *inet* is your IPv4 address (dotted decimal),  *inet6* is your IPv6 address (hexadecimal). 

---

> ## **IPv4 Theory**

- IPv4 is 32 bits ( 4 bytes) in total, with each section being 8 bits
	-  **Example** - 11111111.11110111.11110011.10001101
		- Each 1 and 0 aligns to one of the following numbers, 128, 64, 32, 16, 8, 4, 2, 1
- 2 ^ 32 power is the number of different IP addresses possible with IPv4 (Roughly 4.3 billion)

---

> ## **IPv6 Theory**

- IPv6 is 128 bits
- 2 ^ 128 power is the number of different IP addresses possible with IPv6

---

> ## **Network Address Translation**

- Assigns multiple private IP addresses to one 
	- Example - 192.168.0.0
	- All the network traffic goes out the one IP

---

> ## **Network Classes (Big 3)**

> ### **Class A**

- Starts with 10.0.0.0
- Network Mask - 255.0.0.0
- Number of Networks - 126
- Number of Hosts - 16,646,144

---

> ### **Class B**

- Starts with 172.16.0.0 through 172.31.0.0 
- Network Mask - 255.255.0.0
- Number of Networks - 16,383
- Number of Hosts - 65,024

---

> ### **Class C**

- Number of Networks - 2,097,151
- Number of Host - 254
- Network Mask - 255.255.255.0
- Most common household and small business use
- Starts with 192.168.0.0 through 192.168.255.255

---

> ### **LOOPBACK (Localhost)**

- 127.0.0.0 through 127.0.0.7
