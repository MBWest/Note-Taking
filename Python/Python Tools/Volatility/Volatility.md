# Volatility

- cd /opt/volatility
- source venv/bin/activate

## Exporting Variables

- Export VOLATILITY_LOCATION=file:///path/image
- Export VOLATILITY_PROFILE=profile

## Info

- **python vol.py --info**

## Addons

- **commandline**: Display the command lines for running programs
- **userassist**: Display a list of programs run from the Windows CLI
- **netscan**: Display network connections and listening programs
- **pslist**: Display process information using conventional memory analysis in a tree form
- **pstree**: Display process information using conventional memory analysis in a tree form
- **psscan**: Display process information using non-conventional memory analysis (possibly identifying
detection evasion techniques). Can find information about listening sockets that have been closed. 
- **hivelist**: Display registry hive information
- **printkey**: Display specified registry key and value information
- **svcscan**: Display Windows services
- **dlllist**: Display libraries associated with running Windows processes

- **imageinfo** - For a high level summary of the memory sample you’re analyzing, use the imageinfo command. Most often this command is used to identify the operating system, service pack, and hardware architecture (32 or 64 bit), but it also contains other useful information such as the DTB address and time the sample was collected.

        $ vol.py -f ~/Desktop/win7_trial_64bit.raw imageinfo
        Volatility Foundation Volatility Framework 2.4
        Determining profile based on KDBG search...
        Suggested Profile(s) : Win7SP0x64, Win7SP1x64, Win2008R2SP0x64, Win2008R2SP1x64
                            AS Layer1 : AMD64PagedMemory (Kernel AS)
                            AS Layer2 : FileAddressSpace (/Users/Michael/Desktop/win7_trial_64bit.raw)
                            PAE type : PAE
                                DTB : 0x187000L
                                KDBG : 0xf80002803070
                Number of Processors : 1
            Image Type (Service Pack) : 0
                        KPCR for CPU 0 : 0xfffff80002804d00L
                    KUSER_SHARED_DATA : 0xfffff78000000000L
                Image date and time : 2012-02-22 11:29:02 UTC+0000
            Image local date and time : 2012-02-22 03:29:02 -0800

> **pslist** - By default, pslist shows virtual offsets for the _EPROCESS but the physical offset can be obtained with the -P switch:

        sec504@slingshot:~$ vol.py pslist
        Offset(V)   Name            PID     PPID    Start
        ---------- -------------- ------ ------ ---------------------------
        0x8b1605c0 AdbeRdrEn_Upgr 2328 2588 2020-01-18 04:24:48 UTC+0000
        0x8ac91cc0 MpCmdRun.exe 1768 2088 2020-01-18 04:26:56 UTC+0000
        0x8b35a900 metsvc.exe 1872 520 2020-01-18 04:27:05 UTC+0000
        0x89772600 notepad.exe 2316 2588 2020-01-18 04:27:21 UTC+0000
        0x8b22ab80 taskhost.exe 2740 848 2020-01-18 04:28:55 UTC+0000
        0x89766cc0 cmd.exe 920 528 2020-01-18 04:29:17 UTC+0000

> **pstree** - To view the process listing in tree form, use the pstree command. This enumerates processes using the same technique as `pslist`, so it will also not show hidden or unlinked processes. Child process are indicated using indention and periods.

        sec504@slingshot~$ vol.py pstree
        Volatility Foundation Volatility Framework 2.6.1
        Name Pid PPid Time
        ----------------------------- ---- ---- ----
        0x8b1b4680:dllhost.exe 356 520 2020-01-18 04:19:55 UTC+0000
        . 0x89a412c0:csrss.exe 368 356 2020-01-18 04:19:48 UTC+0000
        . 0x802c26c0:wininit.exe 448 356 2020-01-18 04:19:48 UTC+0000
        .. 0x802f61c0:services.exe 520 448 2020-01-18 04:19:48 UTC+0000
        ... 0x8ac77040:svchost.exe 628 520 2020-01-18 04:19:49 UTC+0000
        .. 0x802fc500:lsass.exe 528 448 2020-01-18 04:19:48 UTC+0000
        ... 0x89766cc0:cmd.exe 920 528 2020-01-18 04:29:17 UTC+0000
        .... 0x8aeed040:PING.EXE 1004 920 2020-01-18 04:31:21 UTC+0000
        .... 0x8ae4d680:conhost.exe 1480 920 2020-01-18 04:29:17 UTC+0000
        .... 0x896a8600:find.exe 1208 920 2020-01-18 04:31:27 UTC+0000
        .... 0x8963b640:PING.EXE 3980 920 2020-01-18 04:31:27 UTC+0000
        .... 0x8b2113c0:PING.EXE 928 920 2020-01-18 04:31:19 UTC+0000

> **netscan** - Display network connections and listening programs

        sec504@slingshot:~$ vol.py netscan
        ...
        0x5093180 TCPv4 172.16.104.129:49172 172.16.104.128:3000 CLOSED 2116
        iexplore.exe
        0x50d22d0 TCPv4 172.16.104.129:49173 172.16.104.128:4444 ESTABLISHED 1700
        AdbeRdrEn_Upgr
        0x5004e180 TCPv4 172.16.104.129:49172 172.16.104.128:3000 CLOSED 2116
        iexplore.exe
        0x500c72d0 TCPv4 172.16.104.129:49173 172.16.104.128:4444 ESTABLISHED 1700
        AdbeRdrEn_Upgr
        0x4a19830 TCPv4 0.0.0.0:31337 0.0.0.0:0 LISTENING 1872
        metsvc.exe


> **cmdline** - Display the command lines for running programs

        sec504@slingshot~$ vol.py cmdline
        ...
        ************************************************************************
        AdbeRdrEn_Upgr pid: 2328
        ************************************************************************
        MpCmdRun.exe pid: 1768
        Command line : "C:\Program Files\Windows Defender\MpCmdRun.exe" ...
        ************************************************************************
        metsvc.exe pid: 1872
        Command line : "C:\Users\mike\AppData\Local\Temp\vuQtZvzVUAG\metsvc.exe"
        service
        ************************************************************************

> **psscan** - To enumerate processes using pool tag scanning `(_POOL_HEADER)`, use the `psscan` command. This can find processes that previously terminated (inactive) and processes that have been hidden or unlinked by a rootkit. The downside is that rootkits can still hide by overwriting the pool tag values (though not commonly seen in the wild).

        $ vol.py --profile=Win7SP0x86 -f win7.dmp psscan
        Volatility Foundation Volatility Framework 2.0
        Offset     Name             PID    PPID   PDB        Time created             Time exited             
        ---------- ---------------- ------ ------ ---------- ------------------------ ------------------------ 
        0x3e025ba8 svchost.exe        1116    508 0x3ecf1220 2010-06-16 15:25:25                              
        0x3e04f070 svchost.exe        1152    508 0x3ecf1340 2010-06-16 15:27:40                              
        0x3e144c08 dwm.exe            1540    832 0x3ecf12e0 2010-06-16 15:26:58                              
        0x3e145c18 TPAutoConnSvc.     1900    508 0x3ecf1360 2010-06-16 15:25:41                              
        0x3e3393f8 lsass.exe           516    392 0x3ecf10e0 2010-06-16 15:25:18                              
        0x3e35b8f8 svchost.exe         628    508 0x3ecf1120 2010-06-16 15:25:19                              
        0x3e383770 svchost.exe         832    508 0x3ecf11a0 2010-06-16 15:25:20                              
        0x3e3949d0 svchost.exe         740    508 0x3ecf1160 2010-06-16 15:25:20                              
        0x3e3a5100 svchost.exe         872    508 0x3ecf11c0 2010-06-16 15:25:20                              
        0x3e3f64e8 svchost.exe         992    508 0x3ecf1200 2010-06-16 15:25:24                              
        0x3e45a530 wininit.exe         392    316 0x3ecf10a0 2010-06-16 15:25:15                              
        0x3e45d928 svchost.exe        1304    508 0x3ecf1260 2010-06-16 15:25:28                              
        0x3e45f530 csrss.exe           400    384 0x3ecf1040 2010-06-16 15:25:15                              
        0x3e4d89c8 vmtoolsd.exe       1436    508 0x3ecf1280 2010-06-16 15:25:30                              
        0x3e4db030 spoolsv.exe        1268    508 0x3ecf1240 2010-06-16 15:25:28                              
        0x3e50b318 services.exe        508    392 0x3ecf1080 2010-06-16 15:25:18                              
        0x3e7f3d40 csrss.exe           352    316 0x3ecf1060 2010-06-16 15:25:12                              
        0x3e7f5bc0 winlogon.exe        464    384 0x3ecf10c0 2010-06-16 15:25:18                              
        0x3eac6030 SearchProtocol     2448   1168 0x3ecf15c0 2010-06-16 23:30:52      2010-06-16 23:33:14     
        0x3eb10030 SearchFilterHo     1812   1168 0x3ecf1480 2010-06-16 23:31:02      2010-06-16 23:33:14 

> **dlllist** - To display a process’s loaded DLLs, use the `dlllist` command. It walks the doubly-linked list of `_LDR_DATA_TABLE_ENTRY` structures which is pointed to by the PEB's `InLoadOrderModuleList`. DLLs are automatically added to this list when a process calls LoadLibrary (or some derivative such as LdrLoadDll) and they aren't removed until `FreeLibrary` is called and the reference count reaches zero. The load count column tells you if a DLL was statically loaded (i.e. as a result of being in the exe or another DLL's import table) or dynamically loaded.

        $ vol.py -f ~/Desktop/win7_trial_64bit.raw --profile=Win7SP0x64 dlllist 
        ************************************************************************
        wininit.exe pid:    332
        Command line : wininit.exe
        Base                             Size          LoadCount Path
        ------------------ ------------------ ------------------ ----
        0x00000000ff530000            0x23000             0xffff C:\Windows\system32\wininit.exe
        0x0000000076d40000           0x1ab000             0xffff C:\Windows\SYSTEM32\ntdll.dll
        0x0000000076b20000           0x11f000             0xffff C:\Windows\system32\kernel32.dll
        0x000007fefcd50000            0x6b000             0xffff C:\Windows\system32\KERNELBASE.dll
        0x0000000076c40000            0xfa000             0xffff C:\Windows\system32\USER32.dll
        0x000007fefd7c0000            0x67000             0xffff C:\Windows\system32\GDI32.dll
        0x000007fefe190000             0xe000             0xffff C:\Windows\system32\LPK.dll
        0x000007fefef80000            0xca000             0xffff C:\Windows\system32\USP10.dll
        0x000007fefd860000            0x9f000             0xffff C:\Windows\system32\msvcrt.dll
    
