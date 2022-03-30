# SMB Sessions

## Brief Intro

By using built-in features of any OS, skillful and patient attackers can launch powerful attacks that will bypass many defensive tools.

### Requirements for This Lab

In this lab, you will use both your Slingshot Linux VM and the Windows 10 VM. Make sure both VMs are running before continuing with this lab exercise.

## Try It Yourself

Use smbclient and rpcclient on your Linux VM to attack your Windows VM. After enumerating local users and groups, run the user-gen.bat script to create multiple local Windows accounts, then attack them using a password spray attack using LocalPasswordSpray.ps1.

## Walkthrough

### Overview

In this exercise, you will use several tools included on the Slingshot Linux VM to interrogate data from the Windows VM over the SMB protocol. You will also create and attack local passwords on the Windows VM using a password spray technique.

These skills are helpful for incident handlers and are often used by computer attackers. You can also rely on them for the book 6 Workshop.

### Verify Connectivity

On the Linux VM, test connectivity to the Windows VM using the ping utility:

    sec504@slingshot:~$ ping -c 3 10.10.0.1
    PING 10.10.0.1 (10.10.0.1) 56(84) bytes of data.
    64 bytes from 10.10.0.1: icmp_seq=1 ttl=128 time=0.872 ms
    64 bytes from 10.10.0.1: icmp_seq=2 ttl=128 time=1.14 ms
    64 bytes from 10.10.0.1: icmp_seq=3 ttl=128 time=1.40 ms

    --- 10.10.0.1 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    rtt min/avg/max/mdev = 0.872/1.141/1.404/0.218 ms

Repeat this step, this time testing the connectivity from the Windows VM to the Linux VM:

    C:\Users\Sec504> ping 10.10.75.1

    Pinging 10.10.75.1 with 32 bytes of data:
    Reply from 10.10.75.1: bytes=32 time<1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time=1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time<1ms TTL=64
    Reply from 10.10.75.1: bytes=32 time=1ms TTL=64

    Ping statistics for 10.10.75.1:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 0ms, Maximum = 1ms, Average = 0ms

If you are unable to get a response from the Windows VM or the Linux VM, take a look at the Testing Virtual Machine Connectivity module for troubleshooting steps.

### Open a Terminal

From the Slingshot Linux VM, open a terminal.

It is not necessary to access root privileges for this lab. 

### Enumerate Shares with smbclient

We start by using smbclient on Linux to pull a list of shares from Windows.

Run the smbclient command shown below. When prompted, type your sec504 account's password:

    sec504@slingshot:~$ smbclient -L 10.10.0.1 -U sec504
    WARNING: The "syslog" option is deprecated
    Enter sec504's password: sec504

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
    Reconnecting with SMB1 for workgroup listing.
    Connection to 10.10.0.1 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
    Failed to connect with SMB1 -- no workgroup available

You should see a list of shares on the Windows box, including ADMIN$, IPC$, and C$. These are the default admin shares that the Windows net view command hides by default. You may see additional shares if you created any.

You may also see some warning messages at the bottom of the output (as shown in this example), including Called name not present, NetBIOS over TCP disabled, and more. You can safely ignore these. The share list is the focus of this lab. 

Tip: Some SMB servers will respond with an error protocol negotiation failed if they have disabled SMBv1. To work around this error, add the -m SMB2 argument to smbclient to force the use of the newer SMB protocol. 

### Enumerate Target Information with rpcclient

Let's dig into this target by using the Linux rpcclient program. Run rpcclient and enumerate the target Windows system, as shown here:

    sec504@slingshot:~$ rpcclient 10.10.0.1 -U sec504
    mkdir failed on directory /var/run/samba/msg.lock: Permission denied
    Enter WORKGROUP\sec504's password: sec504
    rpcclient $>

You can safely ignore the permission denied error message from rpcclient; it will not affect this lab. 

After authenticating to the server, you should see the rpcclient prompt. 

From the rpcclient prompt, let's experiment with some commands to extract information from the target. First, note that the rpcclient prompt has Tab autocomplete. Type enum at the prompt with no space after it, and then hit the Tab key twice:

    rpcclient $> enum<TabTab>
    enumalsgroups      enumdomusers      enummonitors      enumprocs
    enumdata           enumdrivers       enumports         enumtrust
    enumdataex         enumforms         enumprinters
    enumdomains        enumjobs          enumprivs
    enumdomgroups      enumkey           enumprocdatatypes

You now see all the commands that rpcclient has that match the string enum. We can enumerate many things. Let's try enumerating users:

    rpcclient $> enumdomusers
    user:[Administrator] rid:[0x1f4]
    user:[DefaultAccount] rid:[0x1f7]
    user:[Guest] rid:[0x1f5]
    user:[Sec504] rid:[0x3e8]
    user:[WDAGUtilityAccount] rid:[0x1f8]

This command shows all users on the box (local users and any domain users the system knows about). We can see the users' names and their Relative Identifiers (RIDs), which are the suffix of the Security Identifier (SID) number for each account in hexadecimal form. (The admin account has a RID of 0x1f4, which is decimal 500.)

To get an idea of all the commands available within rpcclient, run the following:

    rpcclient $> help
    ------------------                ------------------
            CLUSAPI
    clusapi_open_cluster                bla
    clusapi_get_cluster_name                   bla
    clusapi_get_cluster_version                bla
    clusapi_get_quorum_resource                bla
    clusapi_create_enum                 bla
    clusapi_open_resource               bla
    clusapi_online_resource             bla
    clusapi_offline_resource                   bla
    clusapi_get_resource_state                 bla
    clusapi_get_cluster_version2               bla
    ------------------                ------------------
            WITNESS
    GetInterfaceList
            Register
            UnRegister
        AsyncNotify
            RegisterEx
    ------------------                ------------------

A huge number of commands are available. Let's explore some of the most useful ones.

### Enumerate Server Info and Groups with rpcclient

Let's use rpcclient to enumerate server info. Run the srvinfo command from the rpcclient prompt, as shown here:

    rpcclient $> srvinfo
            10.10.0.1      Wk  Sv  NT  PtB  LMB      Sec504Student
            platform_id     :          500
            os version      :          10.0
            server type     :          0x11003

Here you see the IP address and the OS version.

Now let's get a list of groups. First, we pull domain-related groups (typically groups created on the local machine either by an admin there or within the domain):

    rpcclient $> enumalsgroups domain
    user:[Ssh Users] rid:[0x3e9]

Remember, the als in the middle of enum and groups stands for alias. 

Next, we pull internal groups (typically the default groups defined by Microsoft):

    rpcclient $> enumalsgroups builtin
    group:[Access Control Assistance Operators] rid:[0x243]
    group:[Administrators] rid:[0x220]
    group:[Backup Operators] rid:[0x227]
    group:[Cryptographic Operators] rid:[0x239]
    group:[Distributed COM Users] rid:[0x232]
    group:[Event Log Readers] rid:[0x23d]
    group:[Guests] rid:[0x222]
    group:[Hyper-V Administrators] rid:[0x242]
    group:[IIS_IUSRS] rid:[0x238]
    group:[Network Configuration Operators] rid:[0x22c]
    group:[Performance Log Users] rid:[0x22f]
    group:[Performance Monitor Users] rid:[0x22e]
    group:[Power Users] rid:[0x223]
    group:[Remote Desktop Users] rid:[0x22b]
    group:[Remote Management Users] rid:[0x244]
    group:[Replicator] rid:[0x228]
    group:[System Managed Accounts Group] rid:[0x245]
    group:[Users] rid:[0x221]

Together, these are all the groups defined on the machine. Note that we have the group names and their RIDs in hexadecimal form.

### Looking Up SIDs

Let's look at a couple of other accounts with the rpcclient lookupnames feature, starting with our user account sec504.

Issue the lookupnames sec504 command at the rpcclient prompt, as shown here:

    rpcclient $> lookupnames sec504
    sec504 S-1-5-21-2977773840-2930198165-1551093962-1000 (User: 1)

We see the SID of the sec504 account with the RID 1000 (at the end of the SID output). Next, let's look up the administrator account:

    rpcclient $> lookupnames administrator
    administrator S-1-5-21-2977773840-2930198165-1551093962-500 (User: 1)

We see the administrator SID (with its RID of 500).

Now let's look up a name that is a group, not a user, by adding an s at the end of administrator:

    rpcclient $> lookupnames administrators
    administrators S-1-5-32-544 (Local Group: 4)
    rpcclient $>

Here we see the SID of the administrator's group (group SIDs are usually shorter than user SIDs).

### Enumerate Admin Account Details

We can get even more info about a given user account using the rpcclient queryuser command. Let's run it with a RID of 500, which is the RID of the original administrator account in Windows. Even if the administrator account is renamed, it still has a RID of 500.

From the rpcclient prompt, issue the command queryuser 500, as shown here:

    rpcclient $> queryuser 500
            User Name   :   Administrator
            Full Name   :
            Home Drive  :
            Dir Drive   :
            Profile Path:
            Logon Script:
            Description :   Built-in account for administering the computer/domain
            Workstations:
            Comment     :
            Remote Dial :
            Logon Time               :      Thu, 01 Jan 1970 00:00:00 UTC
            Logoff Time              :      Thu, 01 Jan 1970 00:00:00 UTC
            Kickoff Time             :      Thu, 14 Sep 30828 02:48:05 UTC
            Password last set Time   :      Thu, 01 Jan 1970 00:00:00 UTC
            Password can change Time :      Thu, 01 Jan 1970 00:00:00 UTC
            Password must change Time:      Thu, 14 Sep 30828 02:48:05 UTC
            unknown_2[0..31]...
            user_rid :      0x1f4
            group_rid:      0x201
            acb_info :      0x00000211
            fields_present: 0x00ffffff
            logon_divs:     168
            bad_password_count:     0x00000000
            logon_count:    0x00000000
            padding1[0..7]...
            logon_hrs[0..21]...

In the output, we see the account's name and other details, such as the last time the user set the password for this account! We can also see the bad_password_count for logon failures and more. Repeat this command using the first user account RID of 1000:

    rpcclient $> queryuser 1000
        User Name   :   Sec504
        Full Name   :
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:
        Description :
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :  Sat, 07 Sep 2019 10:21:03 UTC
        Logoff Time              :  Thu, 01 Jan 1970 00:00:00 UTC
        Kickoff Time             :  Thu, 01 Jan 1970 00:00:00 UTC
        Password last set Time   :  Fri, 16 Dec 2016 15:33:39 UTC
        Password can change Time :  Fri, 16 Dec 2016 15:33:39 UTC
        Password must change Time:  Thu, 14 Sep 30828 02:48:05 UTC
        unknown_2[0..31]...
        user_rid :  0x3e8
        group_rid:  0x201
        acb_info :  0x00000010
        fields_present: 0x00ffffff
        logon_divs: 168
        bad_password_count: 0x00000000
        logon_count:    0x00000090
        padding1[0..7]...
        logon_hrs[0..21]...

In the output for RID 500, the timestamps are all empty values (01 Jan 1970, indicating a 32-bit time_t counter set to 0 or -1 and 14 Sep 30828, indicating a 64-bit FILETIME counter set to -1). This is because the Administrator account has not interactively logged in on the Windows system. However, the output for RID 1000 does reveal valid timestamps for the logon, password last set, and password can change fields.

### Disconnect SMB Sessions

Finally, let's see what happens if we disconnect the rpcclient SMB session on the Windows box.

Return to your Windows VM. At the administrative Command Prompt, rerun the net session command, as shown here:

    C:\Windows\system32> net session

    Computer               User name            Client Type       Opens Idle time

    -------------------------------------------------------------------------------
    \\10.10.75.1           sec504                                     5 00:01:57

    The command completed successfully.

You should see an inbound session from a client with the username sec504. The rpcclient tool made this session from Linux to Windows. Let's drop it by adding \\10.10.75.1 /del to the net session command, as shown here:

    C:\> net session \\10.10.75.1 /del
    The session from 10.10.75.1 has open files.

    Do you want to continue this operation? (Y/N) [N]: Y
    The command completed successfully.


    C:\Windows\system32>

        Enter Y at the prompt to complete the command. 

Rerun the net session command to see that the session has been terminated:

    C:\Windows\system32> net session
    There are no entries in the list.

Optionally, return to the rpcclient session on the Slingshot Linux host. Rerunning the last command will return an NT_STATUS_CONNECTION_DISCONNECTED error.

### Finding Weak Passwords

Next, we are going to see just how dangerous SMB access can be.

For this part of this lab, we are going to create 100 users with a user generation script, then attack the passwords. From your administrative Command Prompt, change to the C:\Tools directory, as shown here:

    C:\Windows\system32> cd \Tools
    C:\Tools>

Next, run the user-gen.bat script to create multiple user accounts.

    C:\Tools> user-gen.bat
    The command completed successfully.

    The command completed successfully.

    The command completed successfully.

    The command completed successfully.

    The command completed successfully.
    ...

If you see lots of The command completed successfully messages, it means the script is working. If you see errors, double-check that you are running your Command Prompt as an administrator. 

### Configure a Password Spray Attack using PowerShell

Next, we will use a PowerShell module to implement a password spray attack against the Windows VM.

From the administrative Command Prompt (still in the C:\Tools directory), start PowerShell, as shown here:

    C:\Tools> powershell
    Windows PowerShell
    Copyright (C) Microsoft Corporation. All rights reserved.

Next, load the module to implement the password spray attack, as shown here:

    PS C:\Tools> Import-Module .\LocalPasswordSpray.ps1

### Start the Password Spray Attack

From the PowerShell prompt, start the password spray attack. Run the Invoke-LocalPasswordSpray script, specifying a single password to use as a password guess on all local accounts. Start with a password guess of Winter2021, as shown here:

    PS C:\Tools> Invoke-LocalPasswordSpray -Password Winter2021
    ##### Making a list of all local users  #####
    A subdirectory or file C:\temp\ already exists.
    [*] Using C:\temp\UserList.txt as userlist to spray with
    [*] Password spraying has started. Current time is 1:29 PM
    [*] This might take a while depending on the total number of users
    [*] SUCCESS! User:Dennis Password:Winter2021
    [*] SUCCESS! User:Jack Password:Winter2021
    [*] SUCCESS! User:Jerry Password:Winter2021
    [*] Password spraying is complete
    [*] Any passwords that were successfully sprayed have been output to C:\temp\sprayed-creds.txt

See if you can find any other weak passwords. Please note that you can just look at the .bat script. But that is not fun, nor is it what you would do in an assessment. Take a few moments and see how many of the weak passwords you can find with this script.

Note: Try guessing at least six passwords! We'll examine the logging evidence of password guessing in the next exercise. 

Remove Temporary Users

After you finish password guessing, remove the temporary users by running the user-remove.bat script, as shown here.

Note that, when running a command in the current directory using PowerShell, a leading .\ is required, as shown in this example. 

    PS C:\Tools> .\user-remove.bat
    The command completed successfully.

    The command completed successfully.

    The command completed successfully.
    ...

## Why This Lab Is Important

Using nothing but native components, attackers can launch powerful attacks that are can be devastating. These attacks will almost never be caught with traditional security products. After all, these techniques are using built-in parts of the operating system... anti-virus cannot alert on these executables. IDS/IPS and firewalls typically cannot help because these tools use expected ports and protocols that are required for business use.