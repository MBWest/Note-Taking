# Unit 1 - Appliances

Objective 1a

# Network Models

When two or more computers are linked together it is considered a network. 

### Peer To Peer Architecture (Non-Dedicated)

- Popularized by the file sharing system Napster in 1999
- By default, no computer on a peer-to-peer network has more authority than another
- Each computer can be configured to share only some of its resources and keep other resources inaccessible to the network.
    - With this model, management of network resources is **decentralized**
    - Allows all the devices on a network to function as either a server or client on an as-needed basis

### Client Server Architecture (Dedicated)

- **Definition** - Client-server architecture is a network where each computer is configured either as a client or a server
- By connecting to a server, they also have the option of using shared applications, data and devices
    - Clients send a request or query to the server and the server responds accordingly
    - Please note the client on a client/server network does not share their resources directly with each other but rather use the server as an intermediary
- A client-server network is designed for end-users, called *clients*, to access resources such as files, songs, video collections, or some other service from a central computer called a server
    
    <aside>
    💡 A server's sole purpose is to do what its name implies - serve its clients!
    
    </aside>
    

## Components

- **Server**
A computer on the network managing shared resources for other systems on the network. Servers usually have more processing power, memory and hard disk space than clients. They run network operating software to manage not only data, but also users, groups, security and applications on the network.
- **Client**
A client is a computing device that initiates contact with a server in order to make use of a shareable resource. In some cases, a client could also act as a server.
- **Thin Client**
A desktop terminal that has no hard drive. All features typically found on the desktop PC, such as applications and memory, are stored on the server back at the data center. Along with being easy to install, thin clients also offer a lower total cost of ownership over thick clients.
- **Thick Client**
    
    Also known as *fat client or rich client.* It is a workstation computer in a client server configuration functioning independent of the server. Many applications are installed locally on the client hard drive. A thick client pulls some data from the central server yet only needs to be 
    occasionally connected to that server; it can run on its own without having to always be connected.
    
- **Workstations** 
A personal computer (such as a desktop or laptop) that may or may not be connected to a network. Most clients are workstation computers.

## Advantages and Disadvantages

Comparing client servers to peer to peer network

**Advantages**

- **Central management of the server -** Only one server is used to host the resources that all the clients request and use.
- **Security** - Defining rules for security and access rights as requests are monitored and logged. This will prevent any illegal or unauthorized data access.
- **Organization and management of resources** - including data updates and editing along with creating backups based on a centralized data source for efficient recovery of data

**Disadvantages**

- **More expensive** - in setup and maintenance due to specialized server equipment and software.
- **Adding more clients increases the workload** - of the server resulting in potential reduction in network speed.
- The **bandwidth** consumption also increases.
- **Not very robust**. Should the server fail, the network could collapse. The clients are not able to function until the server is restored.
- **If the server crashes** and it’s the only location where the data is stored, all the data could be lost if there’s no backup.

# Network Control

## Workgroups

Workgroups are commonly known as peer-to-peer networks

- There is no centralized control and computers act as a standalone systems
- There is no formal membership as in a domain nor is there 
network authentication
- There may still be a server, but it will only control access to its own 
resources
- Every computer is treated as an equal in network control and they look out for themselves
- In workgroups, computers quite often share files with other computers
    - While they are doing the sharing, they act as a server and control the access to their shared files
    - When requesting data from another computer, it acts as a client and the other computer is now the server

## Domains

Domains are commonly known as client/server networks where the network is controlled from a single or centralized point. A server controls everyone’s access to the network resources. The central point is the server and its role is to control access of other computers/clients through 
network authentication. Good management is essential for all modern networks. 

## SERVER TYPES

There are many requests a client may require so resources placed on the servers must be able to accomplish the task at hand. With that in mind, the server platform (the hardware or software for the system) must be designed to service those requests. In a small network, many services can be handled by one server. In a medium to large network, there can be many servers with each performing different tasks. With the increased use of the Internet, servers in the client-server environment have become ever more specialized to accommodate the expanding needs of the users. 
There are many different types of servers configured to perform different tasks and requests from users such as: 

### Application Server

Sometimes referred to as a type of middleware. Middleware is computer software that provides services to software applications beyond those available from the operating system. They occupy a large chunk of computing territory between database servers and the end user, and they often connect the two. They are designed for or dedicated to run specific applications, such as word processing, spreadsheets, and desktop publishing programs, etc. 

### Audio/Video Server

Provides multimedia capabilities to websites by assisting the user to broadcast streaming multimedia contents. 1-5

### Dynamic Host Configuration Protocol (DHCP) Server

Designed to reduce configuration time by automatically assigning each computer an Internet Protocol (IP) address from a list of available addresses. It also logs and tracks Internet and network connections.

## Domain Name System (DNS) Server

Provides a translation or resolution of domain names to IP addresses. In other words a computer does not understand where the human readable WWW.CNN.COM is. The DNS finds the machine readable IP address for WWW.CNN.COM. 

### File Transfer Protocol (FTP) Server

One of the oldest of the Internet services, making it possible to move one or more files securely between computers while providing file security and organization as well as transfer control.

### Mail Server

Transfers and stores mail over corporate networks through Local Area Networks (LANs), Wide Area Networks (WANs), and across the Internet.

### Proxy Server

Acts as a mediator (proxy) between a client and an external server filtering requests in order to improve performance as well as share previous connections with other clients on the network. Can also be used to hide the addresses of all devices on the network from the internet as well as prohibit network users from gaining access to unauthorized sites, download files, etc. 

### Telnet Server

Telnet is the method that allows connecting to a remote computer over Internet and using programs and data as if they were on your local machine. Enables the users to remotely log on to a host computer and execute tasks. 

### Virtual Servers

Server at another location shared by multiple web site owners. It allows each owner to use and administer the system’s services as if they have complete control of the server. When using a virtual server, the device may not realize there is another virtual machine running on the virtual 
server.

### Web Server

The main purpose of a web server is to store, process and transfer web site data upon the request of a visitor’s browser. Provides static content to a web browser by loading a file from a disk and transferring it across the network to the user’s web browser. The communication between client 
and server takes place using the Hypertext Transfer Protocol (HTTP).1-6

### Terminal Server

A popular method for gaining remote access to Local Area Networks (LANs). In terminal services, multiple remote computers can connect to a terminal server on the LAN. The terminal server is a computer running specialized software allowing it to act as a host (a computer enabling resource sharing by other computers on the same network) and supply applications and resource sharing to remote clients. There are several functionalities and capabilities of terminal services: 

- A terminal server allows multiple simultaneous connections. 

- A terminal server is optimized for fast processing and application handling offering a similar performance to remote users as if on a LAN connected workstation. Implementing terminal services requires more sophisticated software and significant configuration. 

- A terminal server may be configured on the network to where connections must pass through a firewall, switch or router offering greater flexibility and security than using remote control. 

- A workstation using terminal services to access a LAN is often called a thin client because very little hard disk space or processing power is required of the workstation