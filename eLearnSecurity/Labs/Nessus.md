# Nessus

In this lab you will have to use and configure Nessus in order to perform a vulnerability scan against the target machine. *However* you are not told where the target machine is in the network. You only know it is in the same lab network you are connected to. 

### Goal

The goal of this lab is to learn how to properly configure Nessus depending on the services running on the target machine

### Tools

**The best tools for this lab are:**

- [Nessus](https://www.notion.so/Nessus-2e1489acedc14b8a961818ef1c977072)
- [NMAP](https://www.notion.so/NMAP-d60aa586077a4e5483a9ad02abd4f32d)
- [Metasploit](https://www.notion.so/Metasploit-62bd5faab908412aae4f953252abef6a)

## Solutions

### Step 0 - Start Nessus

Using the following command start nessus:

```jsx
/bin/systemctl start nessusd.service
```

Then go to https://kali:8834

### Step 1 - Find the target in the network

We first need to verify what the remote network is.

- Run the *ifconifg* to check the IP address of our tap0 interface

![Nessus%2036d84/Untitled.png](Nessus%2036d84/Untitled.png)

- Run an nmap scan like the one below

```jsx
nmap -sn 192.168.99.0/24
```

![The screenshot shows that the only host alive in the network is 192.168.99.50 (besides our host)](Nessus%2036d84/Untitled%201.png)

The screenshot shows that the only host alive in the network is 192.168.99.50 (besides our host)

### Step 2 - Identify the target role

Run nmap in order to gather as much information as we can about our target using the following -A scan:

```jsx
namp -A 192.168.99.50
```

![Nessus%2036d84/Untitled%202.png](Nessus%2036d84/Untitled%202.png)

As we can see in the previous output, there are a few services enabled and the machine is windows based. 

### Step 3 - Configure Nessus and run the scan

In order to run the scan we need to:

- Visit Nessus's web interface on [http://localhost:8834/](http://localhost:8834/)
- Navigate to **Scans**
- Chose **New Scan → Advanced Scan**
- Specify the target and the desired name of the scan

![Nessus%2036d84/Untitled%203.png](Nessus%2036d84/Untitled%203.png)

After the scan finishes we can see the results. 

![Nessus%2036d84/Untitled%204.png](Nessus%2036d84/Untitled%204.png)

Clicking the first critical vulnerability provides us with a detailed list of the detected issues. 

![Nessus%2036d84/Untitled%205.png](Nessus%2036d84/Untitled%205.png)

**Note:** If we wanted to use Windows plugins only so that a faster and a more specific scan is performed, this can be done as follows:

**Policy → New Policy → Advanced Scan** and configure as below:

![Nessus%2036d84/Untitled%206.png](Nessus%2036d84/Untitled%206.png)

Then navigate to **My Scans → New Scans → User Defined** and launch the scan. 

### Step 4 - Analyze and export the scan results

From the scan results obtained in the previous step we can see that the machine has some critical vulnerabilities.
**The most interesting one is the MS08-067:**

![Nessus%2036d84/Untitled%207.png](Nessus%2036d84/Untitled%207.png)

This vulnerability allows attackers to execute code remotely! Keep it in mind if you want to exploit the machine!