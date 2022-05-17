# Unit 1 - LAN Technologies

Objective 1A

---

# What is a Switch?

- Hardware based
- Utilizes Application Specific Integrated Circuits (ASIC's) to build and maintain MAC address tables
- Used for workgroup connectivity and network segmentation
- Connects Local Area Networks (LAN's), such as computers and printers together
- They move 'Frames' of information at the Data Link Layer (DLL) - Layer 2
- Multilayer switches perform functions across multiple layers of the OSI model

> Switching is always a Layer 2 function, and routing is always a layer 3 function
> 

## **Media Access Control (MAC) address**

- Each network device connected to a switch can be identified using a 48 bit unique identifier

![Ethernet Frame With Optional VLAN TAG](Unit%201%20-%20L%2090b7d/Untitled.png)

Ethernet Frame With Optional VLAN TAG

- Switches are more secure/intelligent than a network hub because hubs have to transmit all data sent to every port of the hub
- Switches break up the network into **collision domains**

### **Switch Performance**

- **Hardware-based bridging (MAC)** - by using ASICs, switches learn and form multiple internal connections to pass or filter traffic
- **Wire speed** - Can be configured to the media (cable) speed
- **Low latency** - Indicates that the switch can receive, process, and apply an update in minimum time thereby resuming traffic flow quickly.
- **Low cost** - Switches are relatively inexpensive when compared to the number of ports a single switch can have aka 'Low cost high port density'
- **Broadcast control** - Switches can segment a network into smaller broadcast domains if used with VLANs.
    - Without VLANs, broadcasts are not filtered until they get to a Layer 3 device
- **Analyze** - Switches analyze incoming frames to determine if the incoming data needs to be transmitted 
to another segment (a port) of the network or flooded (broadcast) out all ports except the 
original incoming port

## External Components

### Console Port

- Allows direct local access to configure a switch using a "dumb terminal" or a computer running terminal emulation software for initial configuring of a 'blank switch'
- Found on all networking devices
- Connected by a Console/Rollover cable
- DoD policy states console ports must be password protected

### Network Interfaces

- Where devices are connected
- Can be used to test connectivity (Ping), which is useful for troubleshooting
- Provided the administrator assigned an IP (logical) address to the switch as a whole, switches can accept an incoming Telnet connection over any of its network interfaces. This connection is used for remote management of a switch (configuration changes)

<aside>
💡 Remember, switches use MAC addresses to make Forward/Filter decisions with Layer 2 Frames.

</aside>

## Internal Components

### Flash Memory

- Where the Operating System is saved

### ROM

- Contains the diagnostic and boot up routines
- this is the burned in memory that cannot be accessed or changed

### RAM

- The running memory that the switch uses for all of its operations
- When configuration changes are made on the switch it is stored here in a file called '*running-configuration*'

### NVRAM

- What is accessed to save startup-configurations, along with other information that need long term storage
- The 'startup-configuration' file is loaded to the RAM upon boot up, and becomes the 'running-configuration'

---

Objective 1B

## Layer 2 Switch Functions

### Essential Functions

- Address Learning
- Forward/Filter decisions
- Loop Avoidance

### Address Learning

- The MAC address table (Content Addressable Memory) is stored in the switches RAM
    1. When the switch is first put into service the table is empty
    2. When any attached device transmits a *frame*, the switch takes the **source address** and places it in the MAC address table along with the interface ID on which the device is connected to 
    3. Because the **destination hardware address** is not listed in the switches MAC address table, the frame is **flooded (Broadcast)** out to all active interfaces (ports), except the port which the frame was received
    4. When the device answers the flood, the switch adds that devices information (MAC address, and interface ID) to the MAC address table

### Forward/Filter Decision

- The layer 2 switch uses the MAC address table to both forward and filter frames
- If the destination hardware address is listed in the MAC address table, the frame is only **forwarded** out the interface identified with the host
- The frame is not sent out any other interface
    - This process is the **frame filtering**

### Loop Avoidance

- **Definition** - A loop is simply having more than one path to a destination device
- To overcome a single point of failure, it is a good idea to use multiple links (paths) between switches or use multiple switches
- Instability problems
    - Broadcast storms
    - Multiple frame copies
    - Multiple loops
- The standardized solution for Loop Avoidance is called **Spanning 
Tree Protocol (STP)**
    - In 2001, IEEE introduced 802.1w (Rapid Spanning Tree Protocol)

### Broadcast Storms

- Also known as a network storm
- Occurs when a network system is overwhelmed by the continuous multicast of broadcast traffic
- Reasons a broadcast storm occurs
    1. Poor technology
    2. Low port rate switches
    3. improper network configurations
- If loop avoidance schemes are not in place, the switches will flood (broadcast) endlessly throughout the internetwork

![Broadcast Storm](Unit%201%20-%20L%2090b7d/Untitled%201.png)

Broadcast Storm

### Multiple Frame Copies

- **Definition** - Multiple Copies of the same frame
- The result of this is the MAC address filter table becomes confused as to where a device (Server/host X) is located because the switch can receive the frame from more than one link

### Multiple Loops

- **Definition** - Loops occurring within other loops
- Switches can be configured to avoid loops
- IEEE standardized a solution (IEEE 802.1D) to prevent bridging loops in data networks and provide 
loop-free topologies

## Switching Methods

### Store-and-Forward Switching

- Store the entire frame in internal memory and check the frame for errors before forwarding the frame to its destination
- Error checking is done through a cyclical redundancy check (CRC), which is a mathematical calculation based on the number of (1s) in the frame
- If an error is found the frame is discarded and an error message is sent the the sender MAC address
- Store-and-Forward ensures a high level or error-free traffic because bad frames are discarded

### Cut-Through Switching

- Copies only the destination MAC address into memory
- The switch looks up the address in its switching table and places the frame on the outgoing interface
- Cut-Through switching reduces latency; however, bad frames are forwarded and the destination will ultimately have to request the source send the frame again

### Fragment-Free Switching

- Hybrid of Store-and-Forward and Cut-Through Switching
- Stores the first 64 bytes before forwarding
    - This is where frame fragmentation is most likely to happen
- If there is fragmentation then the frame is discarded and an error message sent back to the sender MAC address

## Collisions

- When two system transmissions occur at the same time, on shared bandwidth, the result is a collision
- Collisions are a part of Ethernet communications and do not imply any error condition

### Late Collission

- A late collision is similar to an Ethernet collision, except that it occurs after all hosts on the network should have been able to notice that a host (computer) was already transmitting
- A late collision indicates that another system attempted to transmit after a host has transmitted at least the first 64bytes of its frame
- Late collisions are often caused by an Ethernet LAN being too large and
therefore the LAN needs to be segmented
- Late collisions can also be caused by faulty network devices on the segment and duplex mismatches (for example, half-duplex/full-duplex) between connected devices

### Final Notes

- Cut-Through works best at the core layer where there are fewer errors and speed is important
- Some switches use adaptive switching to select the best method base on traffic conditions

---