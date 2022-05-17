# Null Session

# Description

In this lab you can practice different techniques and tools against  machine vulnerable to null session!

# Goal

The final goal of the lab is retrieve information from the target  machine such as shares, users, groups and so on! Moreover by navigating the remote machine, you should be able to find a file name "***Congratulations.txt***". Download it and explore its content.

# Tools

The best tools for this lab are:

[Null Session Attack](https://www.notion.so/Null-Session-Attack-cc22bc1b007741d490dc2dcad9d87d81) 

- emun4linux [Enum4linux](https://www.notion.so/Enum4linux-b9dd926b65f9426b8d61f6fd4b033412)
- samrdump
- smbclient [SMB Enumerating ](https://www.notion.so/SMB-Enumerating-e179260322064d3d8e68be9db8af21b9)
- nmap [NMAP](https://www.notion.so/NMAP-d60aa586077a4e5483a9ad02abd4f32d)

# Solutions

### Step 1 - Find the target network

We first need to verify which the remote network is. We can do it by running *ifconfig* and check the IP address of our *tap0* interface.

```bash
ifconfig
```

![Null%20Sessi%202c5e2/Untitled.png](Null%20Sessi%202c5e2/Untitled.png)

As we can see the target network is **192.168.99.0**/**24** (note that your IP address may be different from the previous screenshot). 

Let's run nmap in order to discover alive hosts on the network:

```bash
nmap -sn 192.168.99.0/24
```

![Null%20Sessi%202c5e2/Untitled%201.png](Null%20Sessi%202c5e2/Untitled%201.png)

The previous screenshot shows that the only host alive on the network is **192.168.99.162** (besides our host: 192.168.99.20).

### Step 2 - Check for null session

Let us target the host found in the previous step and check if it is vulnerable to null sessions. In the following screenshot, we are using **enum4linux**, but you can use any tool you prefer. 

```bash
enum4linux -n 192.168.99.162
```

![Null%20Sessi%202c5e2/Untitled%202.png](Null%20Sessi%202c5e2/Untitled%202.png)

<aside>
💡 **We can see that the File Server Service is active and the string <20> appears in the list.**

</aside>

### Step 3 - Exploit null session

Let us try to gather as much information as we can. To do this we can simply r**un enum4linux with the -a switch**:

```bash
enum4linux -a 192.168.99.162
```

![Null%20Sessi%202c5e2/Untitled%203.png](Null%20Sessi%202c5e2/Untitled%203.png)

As we can see in the previous screenshots, we were able to gather a lot of information from the machine.

### Step 4 - Use SMCLIENT to navigate the target machine

A very useful tool that we can use to access remote shares and browser the remote machine is **smbclient**.

First let us get the list of shares using smbclient:

```bash
smbclient -L WORKGROUP -I 192.168.99.162 -N -U ""
```

![Null%20Sessi%202c5e2/Untitled%204.png](Null%20Sessi%202c5e2/Untitled%204.png)

Let us now try to access the WorkSharing share and see what files are stored in there:

```bash
smbclient \\\\192.168.99.162\\WorkSharing -N
```

![Null%20Sessi%202c5e2/Untitled%205.png](Null%20Sessi%202c5e2/Untitled%205.png)

As we can see in the previous screenshot there is a file named **Congratulations**.**txt**. Let us download it into our machine and then use the *cat* command to display its content.

```bash
get Congratulations.txt
cat Congratulations.txt
```

![Null%20Sessi%202c5e2/Untitled%206.png](Null%20Sessi%202c5e2/Untitled%206.png)

> Congratulations! You have successfully exploited a null session!
>