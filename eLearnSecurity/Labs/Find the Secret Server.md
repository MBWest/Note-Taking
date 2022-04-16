# Find the Secret Server

In this lab you will learn how **Network routes work**, and how they can be **manually added** in order to reach different networks

---

### Network Configuration of the Lab

![Find%20the%20S%20635fa/Untitled.png](Find%20the%20S%20635fa/Untitled.png)

---

### Connection

You are attached via VPN to the network at **10.175.34.0/24**

You can access the following IP addresses through your browser:

- **172.16.88.81** (CLEAN COMPANY)
- **192.168.241.12** (CLEAN COMPANY TEST SITE)
- **192.168.222.199** (Unable to access)

---

### Goal of the Lab

Configure your VPN lab envirornment in order to reach all the hosts in the network!

---

### Tools Used

- OpenVPN client
- Web Browser

---

# Solution

## Step 1

Check your current network configuration **prior** to connecting to the lab

Screenshot before connecting using the ***ifconfig*** command and the ***route*** command

---

## Step 2

Check your current network configuration **after** connecting to the lab

Screenshot after connecting using the ***ifconfig*** command and the ***route*** command

---

## Step 3

Visit the two webservers

You should be able to access 2 of the 3 IP addresses (see connection section above)

---

## Step 4

Add route manually by using the following command

```bash
ip route add 192.168.222.0/24 via 10.175.34.1
```

Here we are saying to our operating system to add a route for the 192.168.222.0/24 network and that the connections have to go through 10.175.34.1 (which is the gateway of the lab).

# Hail the Hypnotoad

![Find%20the%20S%20635fa/Untitled%201.png](Find%20the%20S%20635fa/Untitled%201.png)