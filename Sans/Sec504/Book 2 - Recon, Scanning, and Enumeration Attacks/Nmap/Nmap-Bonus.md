# Bonus (If Time Permits or Homework)

## Unidentified Scan Target

Your Slingshot Linux VM is configured with an additional scan target that runs in a Docker container. To launch the target, open a terminal and run the goscantgt command, as shown here:

    sec504@slingshot:~$ goscantgt
    Starting Docker service ..... Done.

Note that the output of the goscantgt command will produce limited output and does not return the shell prompt. This is normal. 

Open a second terminal. While the goscantgt command is running, a second Linux instance is running on the local 172.30.0.0 network (the Slingshot Linux VM is 172.30.0.1; the target is in the range 172.30.0.2-254).

## Question: What is the IP address of the target system?

### Click to see Hint #1

Run the Nmap scan using the `-sn` argument to test for reachable hosts. Specify the range of hosts from 172.30.0.2-254.

### Click to see solution - IP address of the target system
Perform the Nmap scan, identifying reachable hosts in the specified network range, as shown here.

    sec504@slingshot:~$ sudo nmap -sn 172.30.0.2-254

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:25 UTC
    Nmap scan report for scantgt (172.30.0.20)
    Host is up (0.000032s latency).
    MAC Address: 02:42:AC:1E:00:14 (Unknown)
    Nmap done: 253 IP addresses (1 host up) scanned in 2.59 seconds


## Question: Which TCP ports listening on the target system using a TCP connect scan?

### Click to see Hint #1

Nmap defaults to a list of 1,024 common TCP ports; you can perform an exhaustive TCP port scan by adding the argument .

### Click to see Hint #2

To perform a connect scan, specify the argument. This is necessary for our Docker target to complete the scan is a relatively short time.

### Click to see solution - TCP ports on the target system using a TCP connect scan

Perform the Nmap scan using all TCP ports for the host at 172.30.0.20, as shown here.

Feel free to experiment with connecting to the listening ports using different tools and other scan techniques including -sV or -A. After you have finished experimentation, return to the goscantgt process and press CTRL+C to stop the Docker container.

## Comparing Nmap Scan Results with ndiff

Try using ndiff, a utility that ships with Nmap. It allows one to quickly compare Nmap scan results. (Hint: This is a great way to compare a baseline scan against a weekly, daily, or hourly scan to look for new services or hosts.)

First, run an Nmap scan, saving the results in an XML file using the -oX argument, as shown here.

    sec504@slingshot:~$ nmap 127.0.0.1 -oX baseline.xml

    Starting Nmap 7.60 ( https://nmap.org ) at 2020-01-14 21:02 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.0000060s latency).
    Not shown: 998 closed ports
    PORT     STATE SERVICE
    9001/tcp open  tor-orport
    9002/tcp open  dynamid

    Nmap done: 1 IP address (1 host up) scanned in 1.69 seconds

Next, start the SSH service and run the scan again, this time saving the XML formatted results to newscan.xml, as shown here.

    sec504@slingshot:~$ sudo service ssh start
    sec504@slingshot:~$ nmap 127.0.0.1 -oX newscan.xml

    Starting Nmap 7.60 ( https://nmap.org ) at 2021-07-09 00:42 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00029s latency).
    Not shown: 997 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    9001/tcp open  tor-orport
    9002/tcp open  dynamid

    Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds

Finally, compare the two XML files using the ndiff utility:

    sec504@slingshot:~$ ndiff baseline.xml newscan.xml
    -Nmap 7.60 scan initiated Fri Jul 09 00:41:57 2021 as: nmap -oX baseline.xml 127.0.0.1
    +Nmap 7.60 scan initiated Fri Jul 09 00:42:26 2021 as: nmap -oX newscan.xml 127.0.0.1

    localhost (127.0.0.1):
    -Not shown: 998 closed ports
    +Not shown: 997 closed ports
    PORT   STATE SERVICE VERSION
    +22/tcp open  ssh

The output of ndiff reveals that the second scan has an additional TCP port (the SSH service on port 22, as noted with the leading + sign to indicate an additional listening port). This is useful information for an analyst, as the presence of a new listening port warrants additional analysis to identify why the service was added to the host.

To complete the lab, stop the SSH service, as shown here.

    sec504@slingshot:~$ sudo service ssh stop
    sec504@slingshot:~$

## Additional Resources

For a deeper dive on Nmap commands and what they do, try the commands in this blog posting: https://www.cyberciti.biz/security/nmap-command-examples-tutorials/