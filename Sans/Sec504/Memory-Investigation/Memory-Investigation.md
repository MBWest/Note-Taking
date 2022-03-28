# Brief Intro

In this lab you will analyze memory evidence from the Falsimentis compromise. Feel free to add to any notes you took during the previous lab with information you discover in this lab.

## Requirements for This Lab

In this lab you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Read the continuation of the scenario at the start of the Walkthrough section. Once you've familiarized yourself with the updates, analyze the FM-TETRIS.mem file in the /home/sec504/labs/falsimentis directory using the Volatility profile Win10x86_15063. As you analyze the file try to answer the following questions:

    What is the name of the process making connections to http://www1-google-analytics.com?
    Where is the process located on the file system?
    What additional suspicious processes are there on the system?
    Identify an additional server used by the Midnite Meerkats

## Walkthrough

### Falsimentis Compromise Scenario Continued

    This section assumes you're already familiar with the first part of the scenario. You may want to re-read the scenario description in the Walk Through section of Lab 1.2: Network Investigation before continuing here. 

During conversations with the system administrator, they admitted to seeing something similar to the ransom note earlier in the day. They stated that they received an email with a link to a site that showed the same video that was in the ransom note. Concerned that they may have been the cause of the incident, they imaged the memory from their workstation. In this lab you will analyze this memory image assisted by the evidence description documentation shown here.
Evidence description document for FM-TETRIS memory image indicating Win10x86_15063 memory profile

### Getting Started with Volatility

To get started, switch into the /opt/volatility directory and activate the virtual environment as shown here:

    sec504@slingshot:~$ cd /opt/volatility
    sec504@slingshot:/opt/volatility$ source venv/bin/activate
    (vol) sec504@slingshot:/opt/volatility$

To avoid having to re-type the name and path of the memory image every time you run Volatility, set the VOLATILITY_LOCATION environment variable to the full path of the memory image FM-TETRIS.mem. This is shown below:

    (vol) sec504@slingshot:/opt/volatility$ export VOLATILITY_LOCATION=file:///home/sec504/labs/falsimentis/FM-TETRIS.mem

Next you will set the VOLATILITY_PROFILE environment variable to match the information supplied on the evidence description document. This is shown below:

    (vol) sec504@slingshot:/opt/volatility$ export VOLATILITY_PROFILE=Win10x86_15063

If you did not have an evidence description document that identifies the Windows version information, you could try and determine the correct profile version using the Volatility imageinfo command. Volatility may identify several possible profiles that match; you will have to experiment with the listed profiles to identify the best match. 

### Preprocessing

One common investigative practice is to preprocess evidence so that multiple searches through it become faster. Since you're analyzing memory images, this means running Volatility commands and saving the output. Do this for the netscan, pstree, filescan, and dlllist plugins as shown here:

    (vol) sec504@slingshot:/opt/volatility$ python vol.py netscan > ~/labs/falsimentis/fm-tetris.netscan.txt
    Volatility Foundation Volatility Framework 2.6.1
    (vol) sec504@slingshot:/opt/volatility$ python vol.py pstree > ~/labs/falsimentis/fm-tetris.pstree.txt
    Volatility Foundation Volatility Framework 2.6.1
    (vol) sec504@slingshot:/opt/volatility$ python vol.py filescan > ~/labs/falsimentis/fm-tetris.filescan.txt
    Volatility Foundation Volatility Framework 2.6.1
    (vol) sec504@slingshot:/opt/volatility$ python vol.py dlllist > ~/labs/falsimentis/fm-tetris.dlllist.txt
    Volatility Foundation Volatility Framework 2.6.1
    WARNING : volatility.debug    : NoneObject as string: Invalid Address 0x08C10000, instantiating LoadTime

The Volatility dlllist warning can be safely ignored. 

These commands all have the same structure, which breaks down as follows:

    python - Runs the Python interpreter
    vol.py - The main Volatility script
    plugin - This is the plugin to run, one of netscan, pstree, filescan, or dlllist.
    > - Saves the output from Volatility to a file.
    filename - The filename to save the output to. In these commands the files are saved in the /home/sec504/labs/falsimentis directory to keep all the evidence in one directory.

Next, change to the lab's directory in /home/sec504/labs/falsimentis:

    (vol) sec504@slingshot:/opt/volatility$ cd ~/labs/falsimentis

Now extract the ASCII, 16-bit little endian, and 16-bit big endian strings from the memory image. This can be done with the following three commands:

    (vol) sec504@slingshot:~/labs/falsimentis$ strings FM-TETRIS.mem > fm-tetris.strings-asc.txt
    (vol) sec504@slingshot:~/labs/falsimentis$ strings -e l FM-TETRIS.mem > fm-tetris.strings-unile.txt
    (vol) sec504@slingshot:~/labs/falsimentis$ strings -e b FM-TETRIS.mem > fm-tetris.strings-unibe.txt

By default, the strings command extracts printable ASCII text. The -e l and -e b options have strings look for 16-bit little endian, and 16-bit big endian (English) Unicode.

### Examining Network Connections

From the previous exercise (Lab 1.2: Network Investigation) we know there was beacon traffic from many of the Falsimentis systems sent to the site www1-google-analytics.com, which had the IP address 167.172.201.123. To search for processes communicating with this address, search the Volatility netscan output using grep for the www1-google-analytics.com IP address, as shown here:

    (vol) sec504@slingshot:~/labs/falsimentis$ grep 167.172.201.123 fm-tetris.netscan.txt
    0xb08a4da8         TCPv4    172.16.42.103:55418            167.172.201.123:80   CLOSED           5736     analytics.exe
    0xc18db2b8         TCPv4    172.16.42.103:55419            167.172.201.123:80   ESTABLISHED      5736     analytics.exe

Notice the name of the process that connected to the suspicious IP address, analytics.exe with process ID 5736. Given that the domain was www1-google-analytics.com, the name analytics.exe seems like it would be a natural fit.

Next, see if analytics.exe is communicating with any other sites using grep again, this time by searching for the process name rather than IP address, as shown here:

    (vol) sec504@slingshot:~/labs/falsimentis$ grep 'analytics.exe' fm-tetris.netscan.txt
    0xa69ae7a8         UDPv4    0.0.0.0:0                      *:*                                   5736     analytics.exe  2020-03-19 20:16:13 UTC+0000
    0xa69ae7a8         UDPv6    :::0                           *:*                                   5736     analytics.exe  2020-03-19 20:16:13 UTC+0000
    0xa79bca58         UDPv4    0.0.0.0:0                      *:*                                   5736     analytics.exe  2020-03-19 20:16:18 UTC+0000
    0xa79bca58         UDPv6    :::0                           *:*                                   5736     analytics.exe  2020-03-19 20:16:18 UTC+0000
    0xb08a4da8         TCPv4    172.16.42.103:55418            167.172.201.123:80   CLOSED           5736     analytics.exe
    0xc18db2b8         TCPv4    172.16.42.103:55419            167.172.201.123:80   ESTABLISHED      5736     analytics.exe

From examining the output, it appears the only remote systems analytics.exe connected to was 167.172.201.123, at least at the time of capture.

For purposes of completeness, it would normally be a good idea to examine all of the output of netscan. For now, we'll move forward, but feel free to examine all of the output if you have extra time during this exercise. 

### Examining Processes

Let's examine the processes that were running when the memory image was collected. The pslist and pstree plugins will show this information, including fields such as the process name, process ID, parent process ID, and so on. When looking at the parent-child relationship between processes, it is sometimes easier to examine the output of pstree since the relationship is shown visually.

You can view the output of the pstree command as shown here:

    (vol) sec504@slingshot:~/labs/falsimentis$ cat fm-tetris.pstree.txt
    (... omitted for space ...)

    ... 0xa0868bc0:ONENOTE.EXE                           8016   4952     22      0 2020-03-19 14:52:51 UTC+0000
    .... 0x972fdbc0:cmd.exe                              4452   8016      0 ------ 2020-03-19 17:34:06 UTC+0000
    ..... 0x8b2e2bc0:analytics.exe                       2532   4452      1      0 2020-03-19 17:34:09 UTC+0000
    ...... 0x8b1fb100:analytics.exe                      5736   2532      3      0 2020-03-19 17:34:10 UTC+0000
    ....... 0xa795bbc0:cmd.exe                           5804   5736      0 ------ 2020-03-19 18:08:06 UTC+0000
    .... 0x8b147bc0:bJKRJiSAnPkf.e                       5568   8016      0 ------ 2020-03-19 17:33:03 UTC+0000

    (... omitted for space ...)

This is an odd looking process tree. ONENOTE.EXE (process ID 8016) spawned cmd.exe (process ID 4452). This cmd.exe spawned analytics.exe (process ID 2532). This copy of analytics spawned another copy of analytics.exe (process ID 5736). The second analytics.exe spawned another cmd.exe (process ID 5804). ONENOTE.EXE also spawned a random-looking process named bJKRJiSAnPkf.e (process ID 5568).

Note that, due to the structure of the Windows executive process (EPROCESS) data structure used to track processes in memory, executable names are often truncated to 14 characters. 

One thing to keep in mind is that the order of the parent-child relationships shown by pstree may not be in chronological (time) order. For instance, the process bJKRJiSAnPkf.e (process ID 5568) was started before the cmd.exe (process ID 4452).

The timestamps are shown in UTC time. To convert them to local time you can use the --tz=America/Los_Angeles when calling Volatility, or manually account for the offset from UTC in your notes. 

### Examining File Objects

Now let's examine file objects, to see if there is anything else useful. To search the output of filescan for analytics.exe you can use the grep command.

    (vol) sec504@slingshot:~/labs/falsimentis$ grep 'analytics.exe' fm-tetris.filescan.txt
    0x00000000944d7940      5      0 R--r-d \Device\HarddiskVolume2\Windows\System32\analytics.exe
    0x00000000c18c5348      1      0 R--r-d \Device\HarddiskVolume2\Windows\System32\analytics.exe

Reviewing the output, it appears analytics.exe is under the \Windows\System32 directory. This information can be useful when building indicators (signatures) that the malware may be installed on a system.

Searching for the string bJKRJiSAnPkf.e yields no results.

    (vol) sec504@slingshot:~/labs/falsimentis$ grep 'bJKRJiSAnPkf.e' fm-tetris.filescan.txt

### Examining Loaded DLLs

Now, let's take a look at loaded DLLs and command lines for the processes of interest (analytics.exe and bJKRJiSAnPkf.e). The dlllist plugin can show this information. as shown here:

    (vol) sec504@slingshot:~/labs/falsimentis$ grep -A 10 -B 10 'analytics.exe' fm-tetris.dlllist.txt
    ************************************************************************
    firefox.exe pid:   3844
    Unable to read PEB for task.
    ************************************************************************
    bJKRJiSAnPkf.e pid:   5568
    Unable to read PEB for task.
    ************************************************************************
    cmd.exe pid:   4452
    Unable to read PEB for task.
    ************************************************************************
    analytics.exe pid:   2532
    Unable to read PEB for task.
    ************************************************************************
    analytics.exe pid:   5736
    Command line :



    Base             Size  LoadCount LoadTime                       Path
    ---------- ---------- ---------- ------------------------------ ----
    ************************************************************************
    cmd.exe pid:   5804
    Unable to read PEB for task.
    ************************************************************************
    firefox.exe pid:   4900

The grep command is slightly different than the ones before, so let's break it down:

    -A 10 - show 10 lines after any pattern matches
    -B 10 - show 10 lines before any pattern matches
    'analytics.exe' - the pattern to match
    fm-tetris.dlllist.txt - the (previously-captured) output of Volatility's dlllist plugin.

Unfortunately, Volatility isn't able to get the command lines for our processes. There are different reasons for this, such as the relevant memory pages being swapped out to disk, smear issues (problems caused because the memory is changing while it is being captured), and so on.

### Examining Strings

Using a tool like Volatility allows you to extract and interpret information from memory images in an accessible format. Sometimes the ability to use such tools is not available, and you must rely on lower resolution techniques. One popular approach is to use the strings utility.

#### Searching for analytics.exe

Since the Midnite Meerkats appear to be using a program named analytics.exe let's search through the (previously-extracted) strings to see if there is anything else relevant.

    (vol) sec504@slingshot:~/labs/falsimentis$ grep -i 'analytics.exe' fm-tetris.strings-*.txt
    fm-tetris.strings-asc.txt:analytics.exe.manifest
    fm-tetris.strings-asc.txt:analytics.exe.manifest
    fm-tetris.strings-asc.txt:analytics.exe
    fm-tetris.strings-asc.txt:dows\system32\analytics.exe"
    fm-tetris.strings-asc.txt:analytics.exe
    fm-tetris.strings-asc.txt:DxgKanalytics.exe
    fm-tetris.strings-asc.txt:analytics.exe
    fm-tetris.strings-asc.txt:C:\Windows\system32\analytics.exe

    (... omitted for space ...)

That is too much data to sift through by hand. Instead search for something less likely to generate voluminous amounts of output. Recall that the filescan output showed the analytics.exe process having the file analytics.exe open in \Windows\System32.

Try performing a case-insensitive search for strings that contain Windows\System32\Analytics to see if there are additional related files.

    (vol) sec504@slingshot:~/labs/falsimentis$ grep -i -h 'windows\\system32\\analytics' fm-tetris.strings-*.txt | sort -u
    <Command>C:\Windows\System32\analyticsbackup.bat</Command>
    C:\Windows\system32\analytics.exe
    C:\Windows\System32\analytics.exe
    C:\Windows\system32\analytics.exe?6844055
    C:\Windows\system32\AnalyticsInstaller.exe
    \device\harddiskvolume2\windows\system32\analytics.exe
    \Device\HarddiskVolume2\Windows\System32\analytics.exe
    \device\harddiskvolume2\windows\system32\analyticsinstaller.exe
    \Windows\System32\analytics.exe

This command is broken down as follows:

    grep -i -h 'windows\\system32\\analytics' fm-tetris.strings-*.txt - perform a case-insensitive search (-i), omitting the file name information (-h) for lines of text that contain windows\system32\analytics in the strings files
    sort -u - sort the lines of output, returning unique lines (-u)

Examining the output, it appears there are two more files that might be of interest: C:\Windows\System32\analyticsbackup.bat and C:\Windows\system32\AnalyticsInstaller.exe.

    It would be a good idea to add an entry in your notes about these two files. You will see them in the next lab (Lab 1.4: Malware Investigation). 

#### Searching for bJKRJiSAnPkF.e

Now perform the same type of search for the oddly named executable bJKRJiSAnPkf.e without the .e extension (to increase the chance of finding related files):

    (vol) sec504@slingshot:~/labs/falsimentis$ grep -i -h bJKRJiSAnPkf fm-tetris.strings-*.txt | sort -u
        bbJKRJiSAnPkf.
    bJKRJiSAnPkf
    bJKRJiSAnPkf.e
    BJKRJISANPKF.EXE
    bJKRJiSAnPkf.exe.lo
    C:\Users\JCHADW~1\AppData\Local\Temp\bJKRJiSAnPkf.exe
    \Device\HarddiskVolume2\Users\JCHADW~1\AppData\Local\Temp\bJKRJiSAnPkf.exe
    \device\harddiskvolume2\users\jchadwick\appdata\local\temp\bjkrjisanpkf.exe

This command is the same as the previous grep and sort command sequence, except that it searches for the oddly named executable. 

From looking at a few of the entries, it appears bJKRJiSAnPkf.exe is located in the \Users\jchadwick\appdata\local\temp directory.

    The location and file name of bJKRJiSAnPkf are also facts that are worth adding to your notes. 

### Cleanup

At the end of this lab exercise, close the terminal used to run Volatility. This will also unload the Volatility virtual environment.

## Summary

There have been several important pieces of information discovered about the Falsimentis incident. They can be summarized as:

    The system administrator admitted to viewing a web page earlier in the day that contained the same video that was seen on the ransom note page.
    The video was referenced by an unknown page hosted at http://lolcats.org.
    The program analytics.exe (process ID 5736) was seen communicating with www1-google-analytics.com.
    There is a suspicious looking program named bJKRJiSAnPkf.exe located in \Users\jchadwick\appdata\local\temp.
    At 10:33:03 AM local time, it appears ONENOTE.EXE spawned a copy of bJKRJiSAnPkf.exe (process ID 5568).
    At 10:34:06 AM local time, it appears ONENOTE.EXE spawned a copy of cmd.exe (process ID 4452).
    At 10:34:09 AM local time, it appears cmd.exe (process ID 4452) spawned analytics.exe (process ID 2532).
    At 10:34:10 AM local time, it appears analytics.exe (process ID 2532) spawned analytics.exe (process ID 5736).
    At 11:08:06 AM local time, it appears analytics.exe (process ID 5736) spawned cmd.exe (process ID 5804).

## Why This Lab is Important

Memory can hold valuable evidence that is not easily, if at all, obtained through other means. The evidence of threat actor activity you find from memory can be used to augment evidence found from other sources, including the network. This allows you to build an even better understanding of what happened and provide proper scoping when attempting to contain an incident.

This lab also demonstrated some of the realities of incident response, notably that incidents are often messy. That is, you can encounter a wide myriad of problems. Being able to adapt and think out-of-the-box are vital skills for any investigator.