# Volatility

- cd /opt/volatility
- source venv/bin/activate

## Exporting Variables

- Export VOLATILITY_LOCATION=file:///path/image
- Export VOLATILITY_PROFILE=profile

## Info

- **python vol.py --info**

## Addons

- **pslist** -

        sec504@slingshot:~$ vol.py pslist
        Offset(V)   Name            PID     PPID    Start
        ---------- -------------- ------ ------ ---------------------------
        0x8b1605c0 AdbeRdrEn_Upgr 2328 2588 2020-01-18 04:24:48 UTC+0000
        0x8ac91cc0 MpCmdRun.exe 1768 2088 2020-01-18 04:26:56 UTC+0000
        0x8b35a900 metsvc.exe 1872 520 2020-01-18 04:27:05 UTC+0000
        0x89772600 notepad.exe 2316 2588 2020-01-18 04:27:21 UTC+0000
        0x8b22ab80 taskhost.exe 2740 848 2020-01-18 04:28:55 UTC+0000
        0x89766cc0 cmd.exe 920 528 2020-01-18 04:29:17 UTC+0000

- **pstree** - 

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

- **netscan** - 

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


- **cmdline** - 

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