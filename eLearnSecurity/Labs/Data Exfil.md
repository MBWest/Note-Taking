# Data Exfiltration

### Scenario

A client gives you remote desktop access to a machine and wants you to identify all the
possible ways an attacker can exfiltrate data (that is - if he was able to compromise this
machine) **without changing any firewall setting.**

---

### Learning Objectives

**In this lab you will learn how to:**

- Assess firewall settings
- Leverage insufficiently secure firewall settings
- Encrypt interesting data and exfiltrate them using DNS
- Automatically identify all possible exfiltration ways

---

### Tools

**In this lab you will use the following tools:**

- Kali Linux
- Packet Whisper ([https://github.com/TryCatchHCF/PacketWhisper](https://github.com/TryCatchHCF/PacketWhisper))
- Wire Shark [Wireshark (Packet Analysis)](https://www.notion.so/Wireshark-Packet-Analysis-a6637171b41e429f8ae7b95d8b765508)
- rdesktop (command line utility) [rdesktop](https://www.notion.so/rdesktop-e640b2fe0ce24f1a96394ac266c80671)
- Egress framework ([https://labs.mwrinfosecurity.com/blog/egress-checking](https://labs.mwrinfosecurity.com/blog/egress-checking))

---

### Network configuration

- Intranet Subnet: **172.16.91.0/24**
- Under-investigation machine's IP: **172.16.91.100**
- Connection Type: **RDP**
    - Use Kali Linux to connect to the **172.16.91.100** Machine. You can do so by executing the code below:
    
    ```bash
    rdesktop 172.16.91.100
    ```
    

### Credentials

- Username: **AdminELS**
- Password: **Nu3pmkfyX**

---

### Task 1

Use the connection details documented above to connect to the **172.16.91.100** Machine

- Inspect the **172.16.91.100** Machine ****for any interesting files
- Identify all the available scripting languages, which could assist you during your assessment

### Task 2

Identify if any of the ports are allowed outbound connectivity by the **172.16.91.100** Machines firewall

**Hint:** You can use a [Python HTTP server](https://www.pythonforbeginners.com/modules-in-python/how-to-use-simplehttpserver/) or Wireshark (on your attacker machine) and the 172.16.91.100 machine's browser to help you with this task

### Task 3

Try to exfiltrate any interesting file you identified in **Task 1** and save it to your Kali machine. To do so, leverage the allowed outbound connectivity ports that you identified during **Task 2**

**Hints**:

1. Oftentimes, professional penetration testers exfiltrate data via DNS requests to evade
detection.
2. [PacketWhisper](https://github.com/TryCatchHCF/PacketWhisper) is a great tool to perform DNS exfiltration

### Task 4

Search for automated tools/frameworks that automate the process of identifying all the possible exfiltration paths and use one of them to identify an exfiltration path that is different than the one used in **Task 3.** 

**Hints**:

1. [https://github.com/stufus/egresscheck-framework.git](https://github.com/stufus/egresscheck-framework.git) is a nice solution to
automatically enumerate all the possible exfiltration ways
2. Another port exists which is allowed outbound connectivity. This port is between
8500 and 9500 (TCP).

---

# Solution

### Task 1 - Connect to and scrutinize the 172.16.91.100 machine

- Connection Type: **RDP**
    - Use Kali Linux to connect to the **172.16.91.100** Machine. You can do so by executing the code below:
    
    ```bash
    rdesktop 172.16.91.100
    ```
    

### Credentials

- Username: **AdminELS**
- Password: **Nu3pmkfyX**
- Once connected use "cmd.exe" to search for interesting files
    
    ```bash
    cd /
    dir /s /b passwords.txt
    dir /s /b credentials.txt
    ```
    

**Items Found**

- domainAdmin:s3cr3tP@ssw0rD
- Found that **Python** is installed by typing the following code into CMD
    
    ```bash
    python --version
    ```
    
- Found that **PowerShell** is installed by typing the following code into CMD
    
    ```bash
    powershell ls
    ```
    

### Task 2 - Identify if the 172.16.91.100 machine allows any of the commonly used ports outbound connectivity

**To accomplish this task follow the procedure below:**

For ports 80 (TCP), 443 (TCP), 8080 (TCP), 8443 (TCP) the procedure is as follows

- Launch a Python server specifying the port of choice, in your Kali machine

**In order to start a Python server, you need to:**

1. Launch a new terminal
    1. Go to a directory in Kali where you have files to be shared (for example /tmp), then type
    
    ```bash
    cd /tmp (**to navigate to the /tmp directory)**
    python -m SimpleHTTPServer 8080
    ```
    

In this case, port 8080 is open and waiting for a connection on your Kali machine, but you could specify any host the 1-65535 ports you want. 

![Data%20Exfil%20885b2/Untitled.png](Data%20Exfil%20885b2/Untitled.png)

**Identify the tap0 IP address of your Kali maching**

To see the tap0 IP address of your Kali machine, open a new terminal and execute the following

```bash
ifconfig
```

**Launch a browser on the 172.16.91.100 machine and navigate to http://[tap0 Kali IP]:port_of_choice**

This should show whether the target machine can connect to the attacker machines python server

The website will present you with the files of the /tmp directory (if any exists)

**To check ports 443, 8443, perform the steps above**

- This will identify that port 443 and 8443 are **not allowed** outbound connectivity

### For port 53 (UDP), the procedure is:

**Note**: If you were inside a real environment, you could simply launch Wireshark and see if you can “sniff” any DNS requests originating from the 172.16.91.100 machine. If this was the case, then port 53 (UDP) would have been allowed outbound connectivity.

In the context of this lab, you **cannot "sniff"** DNS requests due to virtualization restrictions. 

<aside>
💡 What you can do though is, change the **172.16.91.100** systems DNS settings and configure your Kali machine's tap0 as a **DNS server.**

</aside>

1. **More specifically, to check if port 53 (UDP) is allowed outbound connectivity, execute the code below:**

```bash
wireshark
```

In order to capture traffic from the labs network, click on *capture* and select *options,* then you will click the "tap0" interface and finally press *start* (as indicated in the screenshot below  

![Data%20Exfil%20885b2/Untitled%201.png](Data%20Exfil%20885b2/Untitled%201.png)

2.  **Configure the DNS server on the 172.16.91.100 machine to point to your Kali machine's tap0 (the same as previously used)**

In order to change the DNS settings of the 172.16.91.100 machine, double click the *Ethernet0* shortcut that is present on the AdminELS user's desktop and then:

- Select Properties
- Choose Internet Protocol Version 4

![Data%20Exfil%20885b2/Untitled%202.png](Data%20Exfil%20885b2/Untitled%202.png)

From the Internet Protocol Version 4 (TCP/IPv4) Properties window:

- Choose Properties
- Insert your Kali's tap0 IP address as preferred DNS and click OK

![Data%20Exfil%20885b2/Untitled%203.png](Data%20Exfil%20885b2/Untitled%203.png)

Launch your browser and navigate to any page (eg. Google.com)

Now, go to your Kali machine where you have started *wireshark*. Observe the DNS traffic issued by the 172.16.91.100 machine. It should look similar to the image below:

![Such captured traffic means that the firewall allows DNS traffic outbound (port 53 UDP)](Data%20Exfil%20885b2/Untitled%204.png)

Such captured traffic means that the firewall allows DNS traffic outbound (port 53 UDP)

### Task 3 - Try and exfiltrate an interesting file

Based on the previously identified ports, the stealthier exfiltration is through port 53 (UP). **PacketWhisper** can help you easily exfiltrate data via DNS requests. [PacketWhisper](https://www.notion.so/PacketWhisper-32d8f99c4a8646d5a957bedff5159e50) 

**NOTE**: *PacketWhisper* is a Python based tool. See link above on how to Git *PacketWhisper.* 

**You can then run a Python server in the directory where you saved the zipped version PacketWhisper, specifying the previously identified open port 8080:**

```bash
Python -m SimpleHTTPServer 8080
```

Finally you can again point the browser on the 172.16.91.100 machine to your tap0 IP and port 8080 in order to download the tool. 

<aside>
💡 Remember that the file you want to download must be in the directory inside which you started the Python server

</aside>

![Data%20Exfil%20885b2/Untitled%205.png](Data%20Exfil%20885b2/Untitled%205.png)

(To save you time, we have already downloaded PacketWhisper for you and placed it on the AdminELS user's desktop)

### Using PacketWhisper

- Launch *Wireshark* on your Kali Machine again and use the "tap0" interface to listen
- Launch *cmd.exce* on the 172.16.91.100 machine and go to the PacketWhisper directory
- Copy the *Credentials.txt* file to the PacketWhisper directory
- Launch *PacketWhisper*

![Data%20Exfil%20885b2/Untitled%206.png](Data%20Exfil%20885b2/Untitled%206.png)

You should see something similar to the below screenshot, where we can see an example of PacketWhisper's options:

![Data%20Exfil%20885b2/Untitled%207.png](Data%20Exfil%20885b2/Untitled%207.png)

![Data%20Exfil%20885b2/Untitled%208.png](Data%20Exfil%20885b2/Untitled%208.png)

![Data%20Exfil%20885b2/Untitled%209.png](Data%20Exfil%20885b2/Untitled%209.png)

**Transmission will now begin.**

Wait patiently until the end;It usually takes 15+ minutes to finish the ex-filtration. 

### Back to your Kali Machine

On Wireshark you should be able to see DNS queries to subdomains of [cloudfront.net](http://cloudfron.net) within the traffic.

- Save the Wireshark Capture file. **Remember:** To use the .pcap format as per the below screenshot.

![Data%20Exfil%20885b2/Untitled%2010.png](Data%20Exfil%20885b2/Untitled%2010.png)

- Next, copy the saved pcap filed inside the PacektWhisper's directory.
- Finally, open a new terminal and go to PacketWhisper's directory and execute the following.

```jsx
Python PacketWhisper.py
2
file.pcap
1
1
3
[enter]
```

![Data%20Exfil%20885b2/Untitled%2011.png](Data%20Exfil%20885b2/Untitled%2011.png)

**The file should now be successfully decrypted.** 

To view its content, you can execute the following command or double-click the decloaked.file file. 

```jsx
cat decloaked.file
```

### TASK 4 - Automate enumerating all the ex filtration paths and identify another one

Using the egresscheck framework to see how it can automate identifying the ports that are allowed outbound connectivity. 

- To download and launch the egresscheck framework, execute the below code inside any directory you want on your Kali machine

```jsx
git clone https://github.com/stufus/egresscheck-framework.git
cd egresscheck-framework/
./ecf.py
```

![Data%20Exfil%20885b2/Untitled%2012.png](Data%20Exfil%20885b2/Untitled%2012.png)

**You need to configure the tool by specifying:**

- The tap0 IP of your Kali machine (TARGETIP)
- the 172.16.91.100 machine's IP (SOURCEIP)
- A port range (PORTS)
- The Protocol (PROTOCOL)

```jsx
egresschecker> set PORTS 8500-9500
PORTS => 8500-9500 (1001 ports)

egresschecker> set TARGETIP 172.16.91.16
TARGETIP => 172.16.91.16

egresschecker> set SOURCEIP 172.16.91.100
SOURCEIP => 172.16.91.100

egresschecker> set PROTOCOL tcp
PROTOCOL => TCP

egresschecker> generate powershell-cmd
```

The generate powershell-cmd we see above was executed in order to get a single PowerShell
command that will help us automate the firewall assessment.

![This encrypted command contains code that will make PowerShell try to access every port from the given range from the 172.16.91.100 machine on your Kali machine](Data%20Exfil%20885b2/Untitled%2013.png)

This encrypted command contains code that will make PowerShell try to access every port from the given range from the 172.16.91.100 machine on your Kali machine

**Before initiating this procedure on the 172.16.91.100 machine the following requirements should be fulfilled:**

- Transfer this command to the 172.16.91.100 machine
- Run Wireshark on your Kali machine
- Execute the command on the 172.16.91.100 machine

**You can transfer the command using the Python server, and port 8080 like you did previously.**

To do so first, go to the directory where the egress check framework generated a BAT file [see the red rectangle in the image above]

Egresscheck informs you of this BAT file with a message, which will be similar to the one below:

"**Also written to:/tmp/egress_2019jan16_12152VNclt8.bat"**

To service this file using the Python server, execute the following:

```jsx
CD tmp
python -m SimpleHTTPServer 8080
```

Now go to the 172.16.19.100 machine and point the broswer to http://[tap0 Kali IP]:8080 again

![Data%20Exfil%20885b2/Untitled%2014.png](Data%20Exfil%20885b2/Untitled%2014.png)

Download the .bat file generated by the egress framework.

**Next, go back to your Kali machine, execute Wireshark again and point it to listen on the tap0 interface.** 

### **Finally, right click the downloaded BAT file on the 172.16.91.100 machine and click "run as administrator"**

- Observe the traffic on Wireshark

![Data%20Exfil%20885b2/Untitled%2015.png](Data%20Exfil%20885b2/Untitled%2015.png)

**After a short period of time, Wireshark will receive a packet destined to port 9000** – which means that this port is also allowed outbound connectivity on the 172.16.91.100 machine’s firewall; this is the third and last port which is allowed outbound connectivity.

![Data%20Exfil%20885b2/Untitled%2016.png](Data%20Exfil%20885b2/Untitled%2016.png)