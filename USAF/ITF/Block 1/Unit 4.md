# Unit 4 - OSI Model

**Unit 4 OSI Model**

**Layered Architecture**

- Developed by the International Organization for Standardization (ISO)
- Defines a networking framework to implement protocols in the seven layes
- Layers 1-4

◇ Lower Layers - Concerned with moving data around

- Layers 5-7

◇ Upper Layers - Contains application-level data

- Networks operate on one basic principle

◇ “Pass it on”

**Model Layer Relationships**

- Control passed from one layer to the next
- Starts at application layer (Layer 7) in one station and proceeds to physical layer (Layer 1)
- Over the channel (Media) to next station
- Back through the layer from the physical layer (Layer 1) to application layer (Layer 7)

**Seven Layers of the OSI Model**

- 

**Layer 7 - Application Layer (DATA)**

◇ Closet to the end user

◇ Whatever you see on your screen

◇ Where the user inputs data and data is output to the user

◇ Relates to services that directly support user applications

◇ Communication partners are identified

◇ High Level API's

◇ Quality of service is identified

◇ User authentication and privacy are considered

◇ Any constraints on data syntax are identified

◇ Everything at this level is application specific

▪ Web Browsers

- FTP

- DHCP

- HTTP

- SMTP

- SNMP

- Telnet

- 

**Layer 6 - Presentation Layer (DATA)**

◇ Translation of data between a network service and an application

◇ Where the operating system lies

◇ Data compression and encryption/decryption

◇ Provides freedom from compatibility problems in data representation by translating from application to network format and vice versa

◇ Ensures information sent is reformatted back into the same format as original

◇ Renders underlying code into words, pictures, video, or audio supported by the application layer

◇ Application/protocols include

▪ ASCII

▪ TIFF

▪ GIF

▪ JPEG

▪ MPEG

▪ MIDI

- Layer 5 - Session Layer (DATA)

◇ Managing communication sessions

◇ Establishes, manages and terminates connections between applications

◇ Continuous exchange of information in the form of multiple back and forth transmissions between two nodes

◇ Deals with session and connection coordination

◇ Examples

▪ NetBios name

▪ SQL

- Layer 4 - Transport Layer (SEGMENT, DATAGRAM)

◇ Deals with the coordination of data transfer between end systems and hosts

◇ Determines how much data is sent and at what rate

◇ Either

▪

**TCP**

**(Transmission Control Protocol)**

- Requires 3 way handshake

- Syn, Syn/Ack, ack

▪

**UDP**

**(User Datagram Protocol)**

- Just sends data

- No verification

◇ Ensures complete data transfer

- Layer 3 - Network Layer (PACKET)

◇ Responsible for the address packets and translating logicial addresses (IP) and names in physical addresses (MAC)

◇ Concerned with the path data taes to reach the receiving device

◇ Includes logical addressing so packets can be routed to the correct destination

◇ Enables switching and routing technologies to create logical paths, known as virtual circuits

◇ Function are

▪ Routing

▪ Forwarding

▪ Addressing

▪ Internetworking

▪ Error Handling

▪ Congestion Control

▪ Packet Sequencing

◇ Routers operate at this later

◇ Protocol Examples

▪ ARP

▪ IPsec

▪ IPV4

▪ IPV6

▪ RIP

◇ Routers connect networks such as connecting a private network or users to the internet

◇ Routers act as a dispatcher, choosing the best path for the information to travel

- Layer 2 - Data Link Layer (DLL) (FRAME)

◇ Switches operate at this layer

▪ Switches connect computers, printers, servers and other devices to the private network

▪ Works as a controller enabling devices on the network to communicate with each other

◇ Deals with MAC Addresses

◇ Responsible for node to node delivery of message

◇ Main function is to make sure data transfers is error-free from one node to another, over the physical later

◇ When a packet arrives in a network, DLL transmits it to Host using MAC address

◇ Data packets are encoded and decoded into bits

◇ Furnishes transmission protocol knowledge and management and handles errors in the physical layer, flow control and fram synchronization

◇

**Divided into two sub layers**

▪ Media Access Control (MAC) Layer - Controls how a computer on the network gains access to the data and permission to transmit it

▪ Logical Link Control Layer (LLC) - Layer controls fram synchronization, flow control and error checking

◇ Protocol Examples

▪ 802.11 (WIFI)

▪ MAC

▪ VLAN

▪ FDDI

▪ NDP

- Layer 1 - Physical Layer (SYMBOL)

◇ Conveys the bit stream

▪ Electrical impulse, light or radio signal through the network at the electrical and mechanical level

◇ Provides hardware means of sending and receiving data on a carrier, including defining cables, cards and physical aspects

◇ When networking problems occur, many networking pros go right to physical layer to check cables are properly connected and the power plug hasnt been pulled from router, switch or computer

◇ Examples

▪ Physical topologies

▪ Digital subscriber line DSL

▪ Ethernet Physical layer

▪ RJ45 and RS-232

**Acronymns**

- Top Down

◇ All People Seem To Need Data Processing

**• Bottom UP**

◇ Please Do Not Throw Sausage Pizza Away

**Data Packets**

- Each layer addes (or encapsulates) some form of header

◇ Layer 2, the Data Link layer, is responsible for adding a trailer which encapsulates the packet

◇ Each layer removes  the applicable layer all the way up to the application layer