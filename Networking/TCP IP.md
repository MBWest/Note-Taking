# TCP/IP

- **TCP** - Transmission Control Protocol
    - Controls data exchange
- **IP** - Internet Protocol
    - Sends data from one device to another
- **Hosts** - Devices on a network that have an IP address
    - **hostname** - Human-readable name for an IP address
        - *Example* > webprod01 = 10.109.155.174 

---

> ## **IP Address**

- *Example* > 199.83.131.186
    - octet.octet.octet.octet
        - Each octet is *8 bits* and range from 0-255
- Each address must be unique for proper routing

---

> ### **Reserved Private Address Space (RFC 1918)**

| Class | Range | Private Address Space |
|:-:|:-:|:-:|
| A | 1.0.0.0 - 127.255.255.255  | 10.0.0.0 - 10.255.255.255 |
| B | 128.0.0.0 - 191.255.255.255 | 172.16.0.0 - 172.31.255.255  |
| C | 192.0.0.0 - 233.255.255.255 | 192.168.0.0 - 192.168.255.255 |

---

> ## **Subnet Mask**

- *Example* > 255.255.255.0

- The octects with 255 are the network portion and the octects with 0s are the host portion

| Class | Subnet Mask |
|:-:|:-:|
| A | 255.0.0.0  |
| B | 255.255.0.0 |
| C | 255.255.255.0  |

---

> ## **Broadcast Address**

- Special Logical address used to send data to all hosts on a given network
    - *Example* > 199.83.131.255

| Class | Network  | Subnet Mask  | Broadcast |
| :-:|:-:|:-:|:-:|
| A | 17.0.0.0 | 255.0.0.0  | 17.255.255.255  |
| B | 183.194.0.0 | 255.255.0.0  | 183.194.255.255 |
| C | 199.83.131.0 | 255.255.255.0  | 199.83.131.255 |

---

> ## **Address Classes**

| Class |Network  | Hosts Allowed |
|:-:|-|:-:|
| A | 1.0 -> 127.0 Example: 17.24.88.9  | 16,777,216 |
| B | 128.0 -> 191.255 Example: 183.194.46.31 | 65,536 |
| C | 192.0.0 -> 233.255.255 Example: 199.83.131.186 | 255 |

---

> ## **Classless Inter-Domain Routing (CIDR)**

- Allows networks to be subdivided regardless of their traditional class

---

> ## **Examples**
- **CIDR Network** - 121.67.198.0
- **CIDR Subnet** - 255.255.255.0
- **CIDR Broadcast** - 121.67.198.255