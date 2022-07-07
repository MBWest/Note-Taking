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
