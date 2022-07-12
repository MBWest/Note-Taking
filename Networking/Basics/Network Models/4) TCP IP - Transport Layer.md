# Networking - Basics - Network Models - Transport Layer

>  ## **Transport Layer**
- Provides services to higher layer protocol and communication session management between hosts
- Defines the level of service and status of the connection when transporting data
- Transmission Control Protocol (TCP)
    - Connection-Oriented
    - Guaranteed Delivery
- User Datagram Protocol (UDP)
    -Conntectionless
    - Fire and forget 


```text
        ---TCP/IP---   ---Protocol Data Unit---
    |-------------------|-------------------|
  5 |    Application    |       Data        |  
    |-------------------|-------------------|
  4 |     Transport     | Segment, Datagram |   <-------------
    |-------------------|-------------------|
  3 |      Network      |      Packet       |
    |-------------------|-------------------|
  2 |     Data Link     |      Frame        |
    |-------------------|-------------------|
  1 |      Physical     |       Bits        |
    |-------------------|-------------------|
```
---

>  ## **Transmission Control Protocol (TCP)**
- Enables two hosts to establish a connection and exchange streams of data
    - Guarantees delivery of data
    - Guarantees packets will be delivered in the same order in which they were sent
- Reassembles individual segments and ensures they are correctly ordered

>  ## **Transmission Control Protocol (TCP) Functions**
- Breaks messages into segment
- Resends anything that is not received
- Reassembles messages from the segments
- TCP supplis a virtual circuit between end-user applications
    - A virtual circuit (VC) is a means of transporting data over a packet switched computer network in such a way that it appears as though there is a dedicated physical layer link between the source and destination end systems of this data.
    - Virtual circuit communication resembles circuit switching, since both are connection oriented, meaning that in both cases data is delivered in correct order, and signaling overhead is required during a connection establishment phase

>  ## **Transmission Control Protocol (TCP) Header**
>> ### **TCP header contains certain fields**
- `Source port` - (16 bits) identifies the sending port.
- `Destination port` - (16 bits) identifies the receiving port.
- `Sequence Numbers` - (32 bits) has a dual role: If the SYN flag is set (1), then this is the initial sequence number. The sequence number of the actual first data byte and the acknowledged number in the corresponding ACK are then this sequence number plus 1.
- `Acknowledgement Numbers` - (32 bits) if the ACK flag is set then the value of this field is the next sequence number that the sender of the ACK is expecting. This acknowledges receipt of all prior bytes (if any). The first ACK sent by each end acknowledges the other end’s initial sequence number itself, but no data.
- `Data offset` - (4 bits) Specifies the size of the TCP header in 32-bit words. The minimum size header is 5 words and the maximum is 15 words thus giving the minimum size of 20 bytes and maximum of 60 bytes, allowing for up to 40 bytes of options in the header. This field gets its name from the fact that it is also the offset from the start of the TCP segment to the actual data.
- `Reserved` - (3 bits) for future use and should be set to zero.
- `Flags/Control bits (e.g. SYN, ACK, FIN, PSH, RST, etc)` - (9 bits) (aka Control bits) Contains 9.1-bit flags.
- `Window size` -  (16 bits) the size of the receive window, which specifies the number of window size units (by default, bytes) (beyond the segment identified by the sequence number in the acknowledgment field) that the sender of this segment is currently willing to receive (see Flow control and Window Scaling).
- `Checksum` - (16 bits) The 16-bit checksum field is used for error-checking of the header, the Payload and a Pseudo- Header. The Pseudo-Header consists of the Source IP Address, the Destination IP Address, the protocol number for the TCP-Protocol (0x0006) and the length of the TCP-Headers including Payload (in Bytes).
- `Urgent pointer` - (16 bits) if the URG flag is set, then this 16-bit field is an offset from the sequence number indicating the last urgent data byte.