# Unit 2 - Active Directory (AD)

Objective 2a

## Windows Server Operating System

Windows Server 2008R2 is the version of Microsoft Operating System currently used by the Air Force

### Windows Server Features

- Centralized administration
- Centralized management of resources
- Security
- Scalability and compatability
- Reliabilty
- Fault tolerance and recovery

## Windows Domain

- A network where all user accounts, computers, and printers are registered in a central database located on one or most specialized servers known as **Domain Controllers.**
- Domains give network administrators a way to manage a large number of PC's and to also control them from one location.

## Active Directory (AD) Purpose

Active Directory is a powerful tool allowing multiple sites, domains, and even the Internet to fully integrate together

### Directory

- **Definition** - A list of organizing resources and associates characteristics; similar to a telephone directory

### Active Directory

- Is a directory service that stores information about all network resources such as servers, printers, individual user accounts, groups of user accounts, security policy, and other information across a domain
- Used for managing permissions and user/group access to network resources
- Has a tree like structure
    - Consists of forests, trees, domains, organizational units, objects and sites

# Active Directory (AD Structure

Provides both *logical* and *physical* structures for grouping network components with the largest and most comprehensive being the physical structure.

## Active Directory Logical Structure

Grouping resources logically enables finding a resource by its name rather than its physical location

### Partition

- **Definition** - Where the AD information is segregated and logically stored
- Every domain controller contains *three* directory partitions
    - **Configuration** - Contains the Configuration container, which stores configuration objects for the entire forest
    - **Schema** -Contains the Schema container, which stores class and attribute definitions for all existing and possible AD objects
    - **Domain** - Contains a [Domain] container, for example the [Resket.com](http://resket.com) container, which stores users, computers, groups, and other objects for a specific windows 2000 domain

### *Schema*