# Lab Guide (Forum)

After completing the first 14 PTS course labs (except the c++ & python assisted exploitation labs), I thought it would be helpful for new beginners to have an insight into what to expect from the labs, and what potential problems they could face when attempting to complete the lab tutorials.

**OVERALL LAB EXPERIENCE**

Most Labs generally work fine and have no issues connecting and accessing them, however, some of the tools used and techniques are outdated which needs updating to bring them in line with the current/newer version of the pen testing tools used.

**ADVICE FOR NEW BEGINNERS**

Treat Labs as tutorials if you are completely new to pen testing, as personally that was the case when I started this PTS course. I did not have any knowledge about the pen testing field, so attempting to complete a lab without looking at the solutions was impossible. As a novice to this field I would suggest to follow the lab solutions as a tutorial instead of endeavouring to complete labs without looking at solutions. Follow all the steps described in the lab solutions and try to understand what exactly is happening with every single step and why you are doing these steps, what are you trying to achieve i.e. the ultimate objective by executing the commands in the lab tutorial. This approach of treating Lab solutions as a tutorial will save the **valuable Lab time**, as you don't realise how quickly the time goes when doing labs. Once you have finished the tutorial, try to redo it but this time without looking at the guidance, and complete all the required tasks mentioned in the objectives section. This strategy/approach will solidify the concepts, save the lab time, and optimise learning plus it will motivate you to continue rather than being stuck at a lab trying to figure out blindly what you need to do.

**BEFORE STARTING A LAB**

1. Read the Lab solution in full prior to starting a lab.

2. Try to understand all the steps

3. Make a note of the required tools for the lab.

4. Check if you have the tools needed for the lab installed in your Kali virtual machine.

5. Try to figure out if any other steps which can be completed before starting a lab e.g. getting word lists for password cracking etc.

6. Launch your browser if it is needed for the lab, as Kali virtual machine can be slow on laptops and takes some time to load up.

7. Most importantly check your Kali machine has internet connectivity, put it on NAT settings and make sure it pings hosts and has no DNS issues etc.

**PRE-REQUISITES FOR THE PTS COURSE**

This PTS course is described as a course for beginners with only basic knowledge of computer science and security needed, but personally I feel that if you don't have a good understanding of the Linux and networking you would struggle to comprehend topics as slides provided in the course are just a very brief description of the topics, which is not enough to fully understand the topic and concepts in depth. Therefore, I would suggest to have good understanding of networking and Linux, especially the Linux bash terminal. There is courses for both of these domains on udemy which would be really helpful prior to starting this course.

**LAB TIPS**

I experienced some issues while trying to complete some of the labs, the anomalies are easily found in this forum and can be addressed without a lot of hassle. Below, I have compiled a list of potential problems which you are likely to encounter when trying to complete the labs.

**PRE LAB TIPS**

1. Make sure your Kali machine is updated by running *sudo apt-get update* and *sudo apt-get upgrade*

*2.* Remove firefox by *sudo apt-get purge firefox* and install Firefox Developer Edition, before removing firefox make sure you have downloaded and installed the firefox dev verion.

3. Remove Burp suite and install Burp suite V 1.7.36 Community edition, more on this explained in my Burp suite lab tips below.

4.Install Packet whisper, Egress check framework, seclists, update wireshark, update metaspolit, Dsniff, Register and install nessus.

5. Take screenshots of every lab for personal record and understanding of the steps.

6. Add firefox and burp suite to the terminal PATH, so that when you type theses tools they are executed from the terminal, it saves from opening and navigating the programmes menu every time.

7.The addition of these tools to PATH is a simple process of adding few lines to the .bashrc file. I added the following lines to my .bashrc file.

sudo nano ~/.bashrc

add the following to the end of the .bashrc file

PATH="$PATH:~/Desktop/firefox"

PATH="$PATH:~/Desktop/burpsuite"8. I renamed my burp suite community to simple burp suite before adding it to the path. Mine are at the desktop so specify your location according to where your programmes are located.

**HTTP TRAFFIC SNIFFING**

1. Make sure you have the latest wireshark tool installed on your Kali machine.

2. Familiarise yourself with the wireshark controls. Starting and stopping traffic intercept sessions, traffic filters etc., saving .pcap files and the knowledge of different interfaces.

2. Take screenshots at the completion of every goal i.e. after successfully intercepting HTTP and HTTPs traffic. It would help you to refer to in future if you need to recheck anything or refresh your knowledge.

3. Save all screenshots and .pcap file in a dedicated folder on your Kali machine to have a personal record of lab completion.

**SECRET SERVER**

Didn't face particular issues completing this lab, it's quite an easy and straight forward lab as doesn't really use any complicated pen testing tools. i posted this lab's walk-through on the forum in the past.

**DATA EXFILTRATION**

1. Some familiarity with the windows command line prompt would be really useful as this lab uses this aspect.

2. Download packet whisper and egress check framework tools prior to starting this lab, as it will save some lab time to download and install when the lab is running.

3. File transfer from the Windows machine takes a while so be patient and wait for it finish, it does finish eventually. It's a slow process and feels like something is wrong and it's not working, but it does complete itself.

**BURP SUITE BASICS**

1. Uninstall your current version of the burp suite tool, and install v 1.7.36 from here [https://portswigger.net/burp/releases](https://portswigger.net/burp/releases) .Just scroll down the page and locate version 1.7.36 and community edition from the drop down.

2. The newer or the current community version of the burp suite does not have the SPIDER tool function, but the above older version has this functionality. This function is used in the next lab which is the Burp suite lab itself, but it will be useful to have burp suite ready and optimised to finish both burp suite labs with one stable and fully functional version of the software which is in line with the lab solutions guidance.

3.There was no other major hurdles encountered during this lab.

4. Don't forget to change the manual proxy settings back to no proxy after finishing the lab, as not doing so will prevent your browser from accessing internet.

**BURP SUITE**

1. As mentioned above in the Burp suite lab tips, use the v 1.7.36 of the burp suite which allows the facility of the SPIDER function. Otherwise the ZAP tool can be used.

2. Newer version of the burp suite has a different methodology and technique which replaced the SPIDER function, it can be utilised to complete the Lab, but I preferred to finish the lab with the old version of the Burp suite i.e. Version 1.7.36 community edition.

3. Here's a link [https://hackersonlineclub.com/burpsuite-spider-feature-working/](https://hackersonlineclub.com/burpsuite-spider-feature-working/) and [this one](https://portswigger.net/blog/burp-2-0-where-are-the-spider-and-scanner) if you are interested to read the SPIDER tool replacement and the new method.

**SCANNING AND OS FINGERPRINTING**

1. Familiarise yourself with the different NMAP switches.

2. NMAP scans take time, so be patient.

3. This is another very easy and straight forward lab and I didn't face any challenges to complete.

**NESSUS**

1. It is paramount to sort out nessus tool BEFORE staring this lab as it took me a long time to register, install and configure this tool. The registration and installation process is shown in the course video for this topic.

2. Pre installtion and registration process of the nessus tool will save huge amount of the lab time.

3. When this tool is started, it takes a while to update and load all the plugins, so be patient and let it finish. After it has finished loading up, it will present a nice web interface.

4. Take screenshots of the vulnerabilities identified and save the scan from the nessus tool as a PDF to your local drive for reading. The PDF version of the nessus vulnerability report looks great and shows everything found in the scan as a report in a detailed and breakdown structured style.

**DIRBUSTER**

I didn't face any major challenges to complete this lab, just follow the lab guidance and it should be ok.

**CROSS SITE SCRIPTING XSS**

1. This lab needs the firefox Dev version, so remove your current firefox from Kali machine, download and install firefox dev version.

2. The firebug plugin has been discontinued and it was replaced with the Firefox Developer Edition, which provides this functionality in a lot more depth and much more aesthetically better looking way.

3. Just right click on the page when you intend to view the cookies, select inspect element Q from the menu and it will open up a nice big console or dashboard at the bottom of the page. Navigate to storage tab, that's where cookies are located.

4. Reset lab if it's not pushing the admin cookie to the /jar.txt file. This is a known issue with this lab and I got it working after resetting the lab as it would not kick the admin cookie to the jar.txt file on the webserver setup for this particular purpose. Keep refreshing the jar.txt file page and it will eventually appear. Render the code in the contacts menu and keep checking for the admin cookie in the jar.txt file, it does work eventually.

5. After resetting the lab, try to just run the script/code in the contacts on its own(fill the other fields as described in the lab guide) without checking for the stored vulnerability check step.

6. More detailed infomation and solution explanation can be found [HERE ON THIS LINK](https://community.elearnsecurity.com/topic/3987-cross-site-scripting-lab-ptsv3/) of the forum.

**SQL INJECTION**

I didn't face any major challenges to complete this lab, just follow the lab guidance and it should be ok.

**BRUTE FORCE AND PASSWORD CRACKING**

1. Get the seclists tool before starting this tool. sudo apt-get install seclists

2. Get the two wordlist files mentioned in the lab guidance (rockyou-10.txt and rockyou-15.txt) and save them in    /usr/share/seclists/Passwords/rockyou-10.txt/          usr/share/seclists/Passwords/rockyou-15.txt

3.  I didn't face any major challenges to complete this lab, just follow the lab guidance and it should be ok.

**NULL SESSION**

1. I found that this lab had a slight issue as it was throwing up protocol negotiation failed error when the enum4linux and smbclient tool commands were executed. I found that there is a very easy fix for this issue which is mentioned here in [THIS](https://community.elearnsecurity.com/topic/7829-null-session-enum4linux-a-in-lab/?page=2) post of the forum. Just edit      /etc/samba/smb.conf

Add the following under global section of the file:

client min protocol = CORE

client max protocol = SMB3

2. Close all terminals and restart your Kali machine, redo the lab and it should work this time without any issues, only do this step if you encountered the above issue and now you have tweaked the smb.conf file after having tried it first time.

3. If you are reading this Null session lab guidance before attempting the lab, then just do what's suggested in step and it should be all ok.

**ARP POISONING**

1. Before attempting to do this lab, make sure you have dsniff package installed on your Kali machine. The Dsniff package comes with the arpspoof tool which is needed to complete this lab.

2. I didn't have arpspoof tool installed on my kali rolling 2020.3

3. I completed this lab as a root user as for some reason the arpspoof tool wouldn't run as a normal user with sudo command.

4. Do this lab as root user and make sure ip forwarding is set to 1 as shown in the lab. This can be checked with the cat /proc/sys/net/ipv4/ip_forward. The output must show 1.

**METASPLOIT**

1.  The only small issue I encountered during this lab was right towards the end, once you have run the hashdump command in meterpreter, it shows all the hashed passwords output. I didn't know what to do in order to crack the password hashes as this step was skipped in the lab solution manual, so a video on youtube helped to solve this one last little hurdle. If you don't know how to crack the hashed passwords then just select and copy all the displayed output, save it in a simple text file and then crack this file with JTR in your terminal as usual.

sudo john <HASH_PASSWORD_FILE>

2. I didn't face any other major challenges to complete this lab, just follow the lab guidance and it should be ok.