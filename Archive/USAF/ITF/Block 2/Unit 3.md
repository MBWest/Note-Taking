# Unit 3 - Network Router

Objective 3A

## Routers

### What is a Router?

- **Definition** - A Router is a *Layer 3* networking device that uses IP addressing to forward packets between networks
- A router connects two or more lines from different networks

### How does a Router work?

1. When a packet comes into a route, the router reads the IP address to determine the destination network
2. The routers then uses the information in its routing table or routing policy to direct the packet to its next destination

### External Components

1. **Console Port** - This port allows you to configure the router locally by providing direct access to the router using a computer running terminal emulation software
    - Neither the port nor the router has to be configured in order to use the console port
    - This is where you would connect if you were initially configuring a “blank” router
2. **Auxiliary Port**- allows you to configure the router remotely using a modem
    - You can configure this port thru the console port or any
    of its network interfaces
    - This port should be disabled for security reasons
3. **Network Interfaces** - A router can be configured over any of its network interfaces
    - The router’s network interfaces are located on the motherboard or on separate interface modules
    - You configure Ethernet or Token Ring interfaces to allow connection to a LAN
    - The synchronous serial interfaces are configured to allow connection to WANs
    - Configuration information can be supplied using Trivial File Transfer Protocol (TFTP) servers, virtual terminals, Cisco’s Security Device Manager, or network management stations

### Internal Components

- **ROM** - **Read Only Memory -**This is where the diagnostic and boot up routines are stored
- **FLASH** - Manufacture memory that holds the Internetwork Operating Systems (IOS)
- **NVRAM** - **Non-volatile Random Access Memory -** is used to store the startup-configuration file
- **RAM** - **Random Access Memory -** is the working memory for the router. It contains the running configuration file, a copy of the IOS, the routing tables, and any associated data required by the routing process

### Router Start-up

1. First, the router runs the bootstrap program from the ROM and tests the hardware interfaces to verify they are operational
2. The Internetworking Operating System (IOS) is loaded from the
FLASH memory into the RAM
3. Next, the router copies the startup-configuration file from the
NVRAM into the RAM where it becomes the running-configuration. This is where the router stores the current configuration settings while powered on. 

<aside>
💡 Any changes to the running-configuration file are volatile. This means that if the router is turned off without copying the running-configuration file to the NVRAM, then all configuration changes will be lost.

</aside>

### Types of Gateways

Routers are also often distinguished on the basis of the network in which they operate. A router in a Local Area Network (LAN) is called an **interior** router. An **exterior** router directs packets between hosts in one LAN and hosts in another LAN. Routers connect a LAN with the Wide Area Network (WAN) they are called **border** routers or **gateways**.

### Gateways

- In today's terminology, the term gateway often refers specifically to a device that performs Application Layer protocol translation between devices, such as when a device transmits a packet with TCP/IP to a destination using the IPX/SPX stack
- **Definition** - a gateway refers to routers that perform routing protocol functions between machines or networks

### Autonomous System

- **Definition** - a collection of networks under a common administration that
share a common routing strategy
    - An example of an Autonomous System is the internal networks
    within an Air Force Base

### Interior Gateway

- **Definition** - Used for information exchange within Autonomous Systems and use a variety of Interior Gateway Protocols (IGPs) to accomplish this purpose
    - **Examples** -  Routing Information Protocol (RIP), Interior Gateway Routing Protocol (IGRP), Open Shortest Path First (OSPF) and Enhanced Interior Gateway Routing Protocol (EIGRP)

### Exterior Gateway

- **Definition** - move information between Autonomous Systems and use Exterior Gateway Protocols (EGPs)
    - **Examples** - Routing from one Air Force Base to another is an example of routing between Autonomous Systems. Border Gateway Protocol (BGP) is an example of an exterior gateway protocol

### Default Gateway

- **Definition** - Default gateway (Router) is defined as an IP address on a Layer 3 network device that serves as an access point to or from a network
- Also refers to a setting that is configured on hosts to provide them with a path to leave a LAN so they may transmit traffic to a remote network
- The default gateway address is the nearest router interface on a subnet
- A host or network device would utilize the IP address of the router interface associated with its own subnet as its default gateway

### Internetworking Challenges

- **Connectivity** - To support communication between very different technologies
- **Reliable Service** - Individual users and entire organizations depend on consistent, reliable access to network resources
- **Network Management** - How are we able to manage our networks
- **Flexibility** - Necessary for network expansion or contraction along with new applications and services

## Network Segmentation

### Broadcast Domains

- Routers break up **broadcast domains**
    - A broadcast domain is defined as a portion of a network, limited by its router connection to a specific group of host computers in a common LAN segment
    - Communications between devices on the broadcast domain are via *Data Link Layer* addresses (MAC)
    - All hosts in the broadcast domain also share a common logical *Network Layer* addressing scheme (directed broadcast), also called a **subnet**
    
    <aside>
    💡 **All Broadcasts stop at the router**
    
    </aside>
    

### Protocols

- Actual communication across an internetwork is made possible by using communication protocols
- **Definition** - a protocol is a formal set of rules and conventions that governs how computers and other network entities exchange information over a network medium

![Internet Protocols Span the Complete Range of the OSI Model Layers](Unit%203%20-%20N%2008a5a/Untitled.png)

Internet Protocols Span the Complete Range of the OSI Model Layers

## Addressing

### Physical Addressing

- The physical or MAC address is used to send information from one *Layer 2* interface to another *Layer 2* interface
- Hosts generally have only one physical network connection, and thus have only one MAC address
- Routers and other internetworking devices typically have multiple physical network connections and therefore also have multiple MAC addresses.

### Network Addressing

- Network or logical addresses are used to send information from one network to another network
- IPV4 and IPV6 are types of logical addresses
- Network addresses usually exist within a hierarchical address space and are sometimes called virtual or logical addresses
- logical address it is based on network characteristics such as a segment or VLAN

## Router Functions

### Path Determination

- **Definition** - When a router determines the optimal path (network) for a packet to travel
- They gather a list of possible routes to a destination only through communication with others routers
- Routers build and maintain their routing tables through the transmission of a variety of messages
    - A **broadcast** (routing update message) is a message that generally consists of sending a whole routing table to all directly connected neighbor routers
    - Broadcast messaging is used primarily by Distance Vector protocols for routing updates
- A **multicast** (Link-state advertisement), informs other routers of the state of the sender's link
    - Link information can be used to build a complete detailed picture of the networks topology to enable routers to determine the best routes to all network destinations
    - Multicast messaging is used by Link State protocols for routing updates

### Packet Switching

Once the path is determined, *Layer 3 function*, Packet Switching, *Layer 2 function*, is relatively simple

1. In most cases, a host determines that the packet it is sending is addressed to a host on a different network
2. The sending host then acquires a router’s IP address (usually via the designation of the router as the Default Gateway for the LAN) and sends an ARP request to determine the router interface MAC address
3. If the host already has the router interface MAC address in its ARP cache, there is no need for the ARP request
4. The host then sends a packet addressed specifically to the router port MAC address (contained in the *Layer 2* header) and the Network Layer protocol address of the destination host (contained in the in the *Layer 3* header)

![The Packet Switching Process](Unit%203%20-%20N%2008a5a/Untitled%201.png)

The Packet Switching Process