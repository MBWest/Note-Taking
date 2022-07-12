# Networking - Basics - Network Models - Application Layer

>  ## **Application Layer**

- Provides services to the application software running on a computer
- Defines how host programs inferace with transport layer services to use the network
- Functions typically insclude identifying communication partners, determining resource availablity, and synchronyzing communication
- Example: HTTP defines how web browsers can pull the contents of a web page from  a web server 

```text
        ---TCP/IP---   ---Protocol Data Unit---
    |-------------------|-------------------|
  5 |    Application    |       Data        |  <-------------
    |-------------------|-------------------|
  4 |     Transport     | Segment, Datagram |
    |-------------------|-------------------|
  3 |      Network      |      Packet       |
    |-------------------|-------------------|
  2 |     Data Link     |      Frame        |
    |-------------------|-------------------|
  1 |      Physical     |       Bits        |
    |-------------------|-------------------|
```

---

>  ## **Application Layer Protocols**
- DNS
- DHCP
- HTTP
- HTTPS
- FTP 
- TFTP
- Telnet
- SSH
- NTP
- SNMP

>  ## **DNS**

- TCP/UDP - Port 53
- Hierarchical naming system
- Translates domain names into IP addresses
    - "Phone Book" for the internet
- Stores other types od information

>  ## **DHCP**

- UDP port 67 (Client to server, broadcast)
- UDP port 68 (Server to client, unicast)

- Server will asssign
    - IP Address
    - Lease
    - Subnet mask and default gateway
    - and possibly other options (i.e. DNS IP address, vendor specific information)
- Uses the "`DORA`" Process

>>  ## **DORA**

- `Discover` - Sent by the DHCP client to find a DHCP server (Broadcast)
- `Offer` - Sent by the DHCP serer to offer IP address and other parameters (Unicast) once a discover message is received
- `Request` - Reply from client to the server accepting offer. Message contins server ID option so all DHCP servers know an offer was accepted and if they can withdraw offer (Broadcast)
- `Acknowledgement` - Sent by the DHCP server to acknowledge final phase and deliver DHCP lease information. After the client receives this message, it can now use the IP address (unicast). Cient will ARP new IP to verify it does not overlap another and cause address conflicts

>  ## **HTTP**
- TCP 80 [8008, 8080]
- connumication protocol for the transfer of information on the internet
- Request/response standard between a cleint (end-user) and a server (website)
- In between the user agent and origin server may be several intermediaries, such as proxies, gateways and tunnels
- Utilizes TCP for reliability
- Identified using Uniform Resource Identifiers (URIs), or Uniform Resource Locators (URLs)

>  ## **HTTPS**
- TCP 443
    - Provies authentication and encrypted communication, and is widely used on the World Wife Web for security-sensitive communication
- URI/URL scheme used to indicate a secure HTTP connection
- URL indicates that HTTP is to be used, but with a different default TCP port (443) and an additional encryption/authentication layer between the HTTP and TCP
- Encrypts the sesson with a digital certificate
    - If NTP is not synchronized certificate signing can fail
- Self-signed certificates
    - Provides HTTPS confidentiality but does not confirm identity of the site

>  ## **FTP (File Transfer Protocol)**
- Default data - TCP 20
- Control - TCP 21
- Commonly used to transfer files over the internet
- Can be used through simple command line interface or with a commercial program that offers a graphical interface
 - Does not encrpy or protect data whilst in transit accross the network

>  ## **TFTP**
- UDP port 69
- Functionality of a very basic form of FTP
    - Easy to implement in a very small amount of memory
    - Can only read and write files (or mail) from/to a remote server
    - Cannot list directories
    - No provisions for user authentication
    - Typical usage is for the storage and retrieval of Cisco IOS and Catalyst switch configuration files


>  ## **TELNET**
- Used for remote terminal conection
- TCP port 23
- Non secure (sends username/password in plaintext)

>  ## **SSH**
- TCP port 22
- Used for remote terminal connections
- Encrypted remote access

>  ## **NTP**
- UDP port 123
- Synchronize computer clock times in a network
    - Down to a millisecond or fraction of a millisecond
- Uses differnt methods - radio and satellite system
