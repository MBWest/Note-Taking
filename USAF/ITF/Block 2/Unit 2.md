# Unit 2 - VLAN Fundamentals

Objective 2A

# VLANS

### What is a VLAN?

- **Definition** - A 'Logical' grouping of network devices into a single broadcast domain or flat network
    - Flat networks have a ***single*** broadcast domain, meaning that every connected device sees every broadcast packet that is transmitted
- VLAN's limit broadcasts by keeping the broadcast from one VLAN from going to another VLAN
    - This segmentation means that communication between VLAN's must go through a *Layer 3* device

### VLAN Benefits

- **Increased Security** - Security is increased because only those devices part of the same VLAN will receive the frame
- **Flexibility and Scalability** - By limiting or adding only the devices you want in the broadcast domain regardless of its physical location
- **No Geographical Barrier** - A VLAN can span multiple physical LAN segments but have the same Broadcast Domain (Logical)

### Creating VLANS

- VLANs can exist on a single switch or span multiple switches such as Access Switches (ASWs) and Distribution Switches (DSWs)
- After your additional VLANs are created, you will assign selected switch ports to each VLAN
    - VLANS are identified by the use of a number (VLAN 1, VLAN 20)
    - If you create VLAN 30 on one switch and also create VLAN 30 on a connected switch, they will both treat all VLAN 30 traffic as a single local network
- **JUNOS** - Using JUNOS, a VLAN is created with a name, and then assigned a number

### VLAN Switchport Memberships

- **CISCO Switches** - Initially, on Cisco switches, all switch ports are assigned to default VLAN 1 until changed by the administrator
    - You have the ability to view this in your switches using the "**show vlan**" command while in privileged EXEC mode
- **Security** - Any port that is not used should be shut down and assigned to an inactive VLAN

### VLAN Trunking

- **Definition** - A trunk is a connection between network devices that carry more than one VLAN
- Frame tagging (frame identification or encapsulation), uniquely assigns a user-defined trunking ID to each frame
    - The trunking ID will match the VLAN to the traffic belonging to that VLAN
    - When the frame is placed on an access port (traffic to and from one VLAN), this tag is removed
- When an Ethernet frame crosses a trunk a **VLAN tag** is applied
    - This is used to keep track of frames traversing a switch-fabric

<aside>
💡 The Layer 2 switch will only pass traffic within a VLAN, it has no method to move a frame from one VLAN to another. For that, a Layer 3 device must be used.

</aside>

### Common Trunking Methods

- **Inter-Switch Link (ISL)** – Cisco proprietary standard for trunks (deprecated)
    - ISL tags the frame but instead of using the frame as it is, ISL adds a new header and trailer to the existing frame
- **IEEE 802.1q** – defined open standard for trunks
    - A way of encapsulating a VLAN frame that utilizes a space in the standard frame header

<aside>
💡 ISL only works with Cisco devices, where IEEE 802.1q works with all major manufacture’s models

</aside>

### Management VLANs

- **Definition** - Management VLAN is used for purposes such as telnet (logging on to a computer), SNMP (manage and monitor network devices), and syslog (network devices sending messages to a logging server)
- It is a security best practice to ensure that the management VLAN does not have any user traffic on it
    - This can be done by assigning unused ports to a dead VLAN that is not used for any network function
    - It is also a security best practice to make the management VLAN something besides VLAN 1
    
    ![Unit%202%20-%20V%20b96fe/Untitled.png](Unit%202%20-%20V%20b96fe/Untitled.png)