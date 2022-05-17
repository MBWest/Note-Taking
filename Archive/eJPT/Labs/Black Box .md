# Black Box (1)

# Scenario

- You have been engaged in a Black-box Penetration Test **(172.16.64.0/24 range).**
- Your goal is to read the flag file on each machine. On some of them, you will be required to exploit a remote code execution vulnerability in order to read the flag.
- Some machines are exploitable instantly but some might require exploiting other ones first. Enumerate every compromised machine to identify valuable information, that will help you proceed further into the environment.
- If you are stuck on one of the machines, don’t overthink and start pentesting another one.
- When you read the flag file, you can be sure that the machine was successfully compromised. But keep your eyes open – apart from the flag, other useful information may be present on the system.

---

### IP Addresses

- **Kali Machine (172.16.64.10)**
- **172.16.64.101**
    - SSH (22)
    - Apache (8080)
    - Apache (9080)
- **172.16.64.140**
    - HTTP (80)
- **172.16.64.182**
    - SSH (22)
- **172.16.64.199**
    - MSRPC (135)
    - NETBIOS (139)
    - Microsoft ds (445)
    - SQL (1433)