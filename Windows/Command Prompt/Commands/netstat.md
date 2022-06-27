# Netstat

# Examples

- `nestat -naob`
    - `n` - Do not resolve names; display IP addresses numerically
    - `a` -  Display all active TCP connections and listening TCP and UDP ports
    - `o` - See the process ID numbers for each line in the output
    - `b` - See the program name associated with each listening port

| **Command** | **Description** |
|-------------|-----------------|
| `netstat /a` | Display currently listening ports |
| `netstat /a /o` | Display currently listening ports, and PIDs associated with those ports |
| `netstat /e` | Display Ethernet statistics |
| `netstat /r` | Display the routing table for your system |
