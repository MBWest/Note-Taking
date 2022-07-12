# Networking - Basics - Network Models - OSI and TCP/IP Models

> ## **OSI Reference Model**
- Comprised of 7 layers
- Benifits of using a layered approach:
    - Easier troublshooting
    - Standardizes networking architecture
    - Allows vendor interoperability
    - Each layer only communicates with peer layer

```text
         ---OSI---
    |-------------------|
  7 |    Application    |
    |-------------------|
  6 |    Presentation   |
    |-------------------|
  5 |      Session      |
    |-------------------|
  4 |     Transport     |
    |-------------------|
  3 |      Network      |
    |-------------------|
  2 |     Data Link     |
    |-------------------|
  1 |      Physical     |
    |-------------------|
```


> ## **OSI Model Mnemonics**
- All People Seem To Need Data Processing (Layers 70 to 1)
- Please Do Not Throw Sausage Pizzas Away (Layers 1 to 7)

---

> ## **Transmission Control Protocol/Internet Protocol (TCP/IP)**
- Open source, vendor-neutral standard
- In the 1990's, companies began adding OSI, TCP/IP, or both to their networks
- By the late 1990's, however, TCP/IP had become the de facto standard and OSI fell away

> ## **TCP/IP - Standardization**
- The TCP/IP Model both defines and references a large collection of tprotocols that alloows computer communication
- To define stardization protocols, TCP/IP uses documents called RFCs or Requests for Comments
- Computers taken out the box will connect to the network without a problem

> ## **TCP/IP Model - Layers**

- To help people understand a network model, each model breaks the function into a small number of categories called layers
- Each layer includes protocols and standards that relate to that category of functions

```text
        ---TCP/IP---   ---Protocol Data Unit---
    |-------------------|-------------------|
  5 |    Application    |       Data        |
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

> ## **Protocol Data Unit (PDU)**
- PDU is a term that is unique to the OSI model. In the world of networking, you will often hear the terms data, segment, packet, frame, and bits. 

- For example, when someone is talking about a packet, they are talking about data that is being transmitted at layer 3 (the Network layer) of the OSI model. This means that the data is encapsulated with a TCP (Transport layer) header and an IP (Network layer) header.

- When someone is talking about a frame, they are talking about data that is being transmitted at layer 2 (the Data-Link layer) of the OSI model. This means that the data is encapsulated with a TCP header, an IP header, as well as a Layer 2 (Data-Link) header and Layer 2 trailer.

- Finally, the fully encapsulated data is physically transmitted (wired or wirelessly) to its destination in the form of bits, which are the electrical impulses encoded in binary 1s and 0s.