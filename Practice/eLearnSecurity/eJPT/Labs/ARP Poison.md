# ARP Poisoning

# Description

In this lab you are connected to a switched network. Try to intercept network traffic and steal telnet credentials by performing an ARP poisoning attack.

# Goals

- Identify the telnet server and the client machine
- Intercept traffic between the two
- Analyze the traffic and steal valid credentials
- Login into the telnet server

# Tools

**The best tools for this lab are:**

- A Linux Machine
- arpspoof
- Wireshark

# Solution

### Step 1 - Find the network configuration

After connecting to the lab, check the network configuration of the TAP interface. Then use this information to configure your scans.

![ARP%20Poison%2071d0f/Untitled.png](ARP%20Poison%2071d0f/Untitled.png)

According to the netmask, the network part of the IP address is 24 bits long.

### Step 2 - Identify the server and client

Run a scan with nmap on the target network. Filter out your attacker machine.

![ARP%20Poison%2071d0f/Untitled%201.png](ARP%20Poison%2071d0f/Untitled%201.png)

**10.100.13.37 listens on port 23, so it is the server. 10.100.13.36 is the client.**

### Step 3 - Intercept the traffic

Configure your attacking machine to forward IP packets:

```bash
# echo 1 > /proc/sys/net/ipv4/ip_forward
```

Attack the victims by poisoning their ARP cache:

```bash
# arpspoof -i tap0 10.100.13.37 -t 10.100.13.36
```

Run Wireshark and display telnet traffic only:

![ARP%20Poison%2071d0f/Untitled%202.png](ARP%20Poison%2071d0f/Untitled%202.png)

Perform a **“Follow TCP Stream”** and extract the credentials:

![ARP%20Poison%2071d0f/Untitled%203.png](ARP%20Poison%2071d0f/Untitled%203.png)

### Step 4 - Login to the Telnet server

Use them to login into the server:

![ARP%20Poison%2071d0f/Untitled%204.png](ARP%20Poison%2071d0f/Untitled%204.png)

# Done!