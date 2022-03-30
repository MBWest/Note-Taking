# Live-Windows-Examiniation Lab

**KNOW THY SYSTEM!**

**Open a second CMD prompt as an Administrator and run netstat -nao on your host so you know what your system looks like before it is "infected."**
**Verify your firewall and AV are disabled.  I am about to start a non-malicious backdoor for you to find.**

**After you have run netstat press ENTER to continue**

`netstat -ano > before.txt`

*`Enter`*

**Please wait: A TCP Backdoor is being started on your host.**
**Backdoor Started.  Please answer the following questions.**

**What TCP port is the backdoor listening on?**

`fc before.txt after.txt`

        C:\Users\Sec504\Desktop>fc before.txt after.txt
        Comparing files before.txt and AFTER.TXT
        ***** before.txt
        TCP    0.0.0.0:1542           0.0.0.0:0              LISTENING       632
        TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING       4184
        ***** AFTER.TXT
        TCP    0.0.0.0:1542           0.0.0.0:0              LISTENING       632
        TCP    0.0.0.0:1572           0.0.0.0:0              LISTENING       6180
        TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING       4184
        *****

`1572`

**What is the process id number of the backdoor?**

`6180`

**What is the Parent process id number of the backdoor?**

`wmic process where processid=6180 get name,parentprocessid`

        C:\Users\Sec504\Desktop>wmic process where processid=6180 get name,parentprocessid
        Name            ParentProcessId
        powershell.exe  4280

`4280`

**Use Netcat to connect to the backdoors TCP port.**
**What flag is printed when you connect to the backdoor?**

        C:\Users\Sec504\Desktop>nc localhost 1572
        TheFlagisBlack73857643

`TheFlagisBlack73857643`
`^C`

**What TCP port is the backdoor listening on now?**

`netstat -ano > after2.txt`

`fc before.txt after2.txt`

        C:\Users\Sec504\Desktop>fc before.txt after2.txt
        Comparing files before.txt and AFTER2.TXT
        ***** before.txt
        TCP    0.0.0.0:1542           0.0.0.0:0              LISTENING       632
        TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING       4184
        ***** AFTER2.TXT
        TCP    0.0.0.0:1542           0.0.0.0:0              LISTENING       632
        TCP    0.0.0.0:1574           0.0.0.0:0              LISTENING       6180
        TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING       4184
        *****

`1574`

**Now use wmic to kill the process.**
**Press enter after you have killed the process.**

`wmic process where processid=6180 delete`

        C:\Users\Sec504\Desktop>wmic process where processid=6180 delete
        Deleting instance \\SEC504STUDENT\ROOT\CIMV2:Win32_Process.Handle="6180"
        Instance deletion successful.

**This Powershell backdoor was easy to find because it listened on a TCP port.  A more typical Powershell backdoor will not.  Instead it makes periodic client connections to a command and control server.  Now I'm creating a new Powershell process that does not listen on a port.**

**What is the process id number of the backdoor?**

`wmic process where name="powershell.exe" get processid,commandline,parentprocessid`

        C:\Users\Sec504\Desktop>wmic process where name="powershell.exe" get processid,commandline,parentprocessid
        CommandLine                                                                                                                                                                                                                                                         ParentProcessId  ProcessId
        powershell.exe -nop -exec bypass -enc dwBoAGkAbABlACgAJAB0AHIAdQBlACkAewAkAGYAbABhAGcAIAA9ACAAIgBTAGEAcwBxAHUAYQBjAGgAZQA4ADMANgAyADkAOAA4ADUAMwAiADsAIABbAFMAeQBzAHQAZQBtAC4AVABoAHIAZQBhAGQAaQBuAGcALgBUAGgAcgBlAGEAZABdADoAOgBTAGwAZQBlAHAAKAAxADAAMAAwADAAKQB9ADsA  4280             6580

`6580`

**Use wmic to retrieve the CommandLine and answer the following.**

**What is the flag contained in the script executed by the backdoor?**

`notepad flag.b64`
*`Copy b64 text to notepad`*

`certutil -decode flag.b64 flag.txt`

        C:\Users\Sec504\Desktop>certutil -decode flag.b64 flag.txt
        Input Length = 224
        Output Length = 168
        CertUtil: -decode command completed successfully.

`flag.txt`

        while($true){$flag = "Sasquache836298853"; [System.Threading.Thread]::Sleep(10000)};

`Sasquache836298853`

**Now use wmic to kill the process.**
**Press enter after you have killed the process.**

`wmic process where processid=6580 delete`

        C:\Users\Sec504\Desktop>wmic process where processid=6580 delete
        Deleting instance \\SEC504STUDENT\ROOT\CIMV2:Win32_Process.Handle="6580"
        Instance deletion successful.

**You have done well. The evil hackers have been thwarted.**
**Press enter to end this lab.**