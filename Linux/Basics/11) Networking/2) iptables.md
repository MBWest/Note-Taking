# Linux Networking - iptables

> ## **iptables [-t table] [OPTIONS]**
- Administration tool for IPv4 packet filtering and NAT
- Linux host-based firewall
- `-L CHAIN` - list all rules in the selected CHAIN
- `-A CHAIN RULE` - append a rule to CHAIN
- `-I CHAIN [#] RULE` - insert a rule in CHAIN at the given #
- `-D  CHAIN RULE|#` - delete a rule from CHAIN
- `-R CHAIN # RULE` - replace a rule in CHAIN 
- `-F [CHAIN]` - flush the rules in CHAIN, or all chains

### **Filter**
- This is the `default` table. It is used to make decisions about whether a packet should be allowed to reach its destination.
### **Mangle**
- This table allows you to alter packet headers in various ways, such as changing TTL values.
### **NAT**
- This table allows you to route packets to different hosts on NAT network
### **Raw**
- allows you to work with packets before the kernel starts tracking its state


```text
                    |-------------------PREROUTING---------------------------------------|--------------------INPUT----------------|
                                       
|----------------|      |---------|      |---------|      |---------|      |---------|             |---------|      |---------|                |----------------|
|                |----->|   Raw   |----->|  Conn.  |----->|  Mangle |----->|   NAT   |------------>|  Mangle |----->|  Filter |--------------->|                |
|                |      |         |      | Tracking|      |         |      |         |             |         |      |         |                |                |
|                |      |---------|      |---------|      |---------|      |---------|             |---------|      |---------|                |                |
|                |                                                              |                                                              |                |
|                |                                                              V       -------                                                |                |
|                |                                                         |---------|     |                                                   |                |
|                |                                                         |  Mangle |     |                                                   |                |
|                |                                                         |         |     |                                                   |                |
|    Network     |                                                         |---------|     |                                                   |     Local      |
|   Interface    |                                                              |        FORWARD                                               |    Process     |
|                |                                                              V          |                                                   |                |
|                |                                                         |---------|     |                                                   |                |
|                |                                                         |  Filter |     |                                                   |                | 
|                |                                          /--------------|         |     |                                                   |                |
|                |                                         /               |---------|     |                                                   |                |
|                |                                        /                                |                                                   |                |
|                |                                       /                               ------                                                |                |
|                |                                      /                                                                                      |                |
|                |                                     /                                                                                       |                |
|                |                                    /                                                                                        |                |
|                |      |---------|      |---------| /    |---------|      |---------|      |---------|      |---------|      |---------|      |                |
|                |<-----|   NAT   |<-----|  Mangle |<-----|  Filter |<-----|   NAT   |<-----|  Mangle |<-----|  Conn.  |<-----|   Raw   |<-----|                |
|                |      |         |      |         |      |         |      |         |      |         |      | Tracking|      |         |      |                |
|----------------|      |---------|      |---------|      |---------|      |---------|      |---------|      |---------|      |---------|      |----------------|
     
                    |-----POSTROUTING-----------------|---------------------------------------OUTPUT---------------------------------------|     
```
---

> ## **Chains**

### **PREROUTING**
- Apply to packets as they just arrive on the network interface	

### **`INPUT`**
- Apply to packets just before they’re given to a local process

### **`OUTPUT`**
- Apply to packets just after they’ve been produced by a process. 

### **`FORWARD`**
- Apply to any packets that are routed through the current host

### **POSTROUTING**
- Apply to packets as they just leave the network interface

---

> ## **Targets**

- Decides what to do after a packet has been matched on in a chain.
### **Non-Terminating**
- LOG
- RETURN
- GOTO
### **Terminating**
- `ACCEPT`
- `DROP`
- `REJECT`

```
root@wrsk01$ iptables –I INPUT 1 –p tcp –m multiport --dport 20,21 -s 59.45.175.0/24 –j ACCEPT
```
**Table** - Since no table is specified the default is used `Filter`

**Chain** - The INPUT chain `-I INPUT 1`

**Rules** - A rule is being inserted at line 1 on the INPUT chain `–p tcp –m multiport --dport 20,21 -s 59.45.175.0/24`

**Target** -The terminating target ACCEPT `-j ACCEPT`

---

> ## **Edit Tables**
- Edits `tables` used to store sets of firewall rules
- Each table has `chains` of rules for treatment of packets
- Packets traverse the chain, checking each rule
- What chain it enters is based on the packet’s origin
    - 3 standard chains:  `INPUT`, `FORWARD`, `OUTPUT`
- Enabled by netfilter modules
- Must be root to view/edit tables
- Permanent changes need to be made in the following file
    - /etc/sysconfig/iptables

---

> ## **3 Main Actions to Take**
- `ACCEPT` - allow the connection
- `REJECT` - don’t allow the connection, but send an error
- `DROP` - silently act like the connection never happened
- Every chain has a default rule, known as the policy
    - `iptables --policy INPUT ACCEPT`
    - Only used if no other rule applies

```
[root@CentOS ~]# iptables –A INPUT –i lo –j ACCEPT

[root@CentOS ~]# iptables –A INPUT –m state --state RELATED,ESTABLISHED –j ACCEPT

[root@CentOS ~]# iptables -A INPUT -p tcp --dport 22 -j ACCEPT

[root@CentOS ~]# iptables –P INPUT DROP

[root@CentOS ~]# iptables –P FORWARD DROP

[root@CentOS ~]# iptables -nvL
Chain INPUT (policy DROP 0 packets, 0 bytes) 
pkts bytes target prot opt in   out	source   	destination
0    0	  ACCEPT all  --  lo   any	anywhere	anywhere	
0    0 	  ACCEPT all  --  any  any  anywhere 	anywhere 	state RELATED,ESTABLISHED
0    0	  ACCEPT tcp  --  any  any  anywhere 	anywhere 	tcp dpt:22

Chain FORWARD (policy DROP 0 packets, 0 bytes) 
target prot opt source destination 

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes) 
target prot opt source destination
```