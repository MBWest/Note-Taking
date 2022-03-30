# Domain Password Audit Tool

## Brief Intro

In this lab exercise, you will conduct an assessment of domain passwords for the online retailer Wardrobe99. After cracking passwords, you will generate and evaluate the Domain Password Audit Tool (DPAT) report results to identify patterns of poor password selection practices among company employees, answering the following questions:

What percentage of current passwords did Hashcat crack?
How many non-unique passwords are in use in the organization?
What is the most common password length recovered in the password cracking process?
Which department (as seen through domain group membership) has the worst password selection practices (e.g., the greatest percentage of cracked passwords)?
What is the most commonly reused password in the organization?
Characterize the pervasive user password selection problem using password history data.

## Requirements for This Lab

In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Extract and crack passwords from the NTDS.dit and SYSTEM registry hive included for Wardrobe99 at /home/sec504/labs/Wardrobe99. Use the DPAT software in /home/sec504/labs/DPAT to assess the cracked password results.

## Walkthrough

### Introduction

Gaining insight into the nature of passwords revealed through password cracking can be a tremendously valuable tool for shaping policy regarding password use, including the priority for shifting away from passwords to more secure authentication mechanisms. In this lab, you will extract password hashes for a Windows domain controller, crack passwords using Hashcat, and then use DPAT to generate an analysis report. With the analysis report, you will answer several questions about password selection for the Wardrobe99 domain.

### Open a Terminal
From the Slingshot Linux VM, open a terminal.

### Extract Hashes and Password History with Secretsdump

From the terminal, change to the labs directory where the Wardrobe99 Active Directory backup files are saved:

    sec504@slingshot:~$ cd /home/sec504/labs/Wardrobe99/
    sec504@slingshot:~/labs/Wardrobe99$
    Next, run the Impacket secretsdump.py tool to extract the password hashes and password hash history, as shown here:

    sec504@slingshot:~/labs/Wardrobe99$ secretsdump.py -system registry/SYSTEM -ntds "Active Directory/ntds.dit" LOCAL -outputfile w99 -history
    Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

    [*] Target system bootKey: 0x3b53edaa727f0bbbc56bed5beb9a9530
    [*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
    [*] Searching for pekList, be patient
    [*] PEK # 0 found and decrypted: 05b651dcf420b842402b9d3cf3508e6a
    [*] Reading and decrypting hashes from Active Directory/ntds.dit
    Administrator:500:aad3b435b51404eeaad3b435b51404ee:c3db44d312f154d162607ee52628ace3:::
    Guest:501:aad3b435b51404eeaad3b435b51404ee:2a9fa667f0d1b99b758767e68ea4ec52:::
    Guest_history0:501:aad3b435b51404eeaad3b435b51404ee:2fce1b7ee85c756dfa504d74c147bd1a:::
    ... omitted for space

In addition to displaying the password hash information on the screen, secretsdump.py will also write the hash data to the w99.ntds file, as shown here:

    sec504@slingshot:~/labs/Wardrobe99$ ls w99*
    w99.ntds  w99.ntds.cleartext  w99.ntds.kerberos
We'll focus on the password hashes in the w99.ntds file.

### Examine Password Hashes

Before starting to crack passwords, examine the password hash file for LANMAN password hashes. We can use an awk command with the Linux sort and uniq utilities to count how many unique LANMAN password hashes are present in the w99.ntds file, as shown here:

    sec504@slingshot:~/labs/Wardrobe99$ cat w99.ntds | awk -F: '{print $3}' | sort | uniq -c
    2258 aad3b435b51404eeaad3b435b51404ee

Let's break down this command step by step:

- **cat w99.ntds** - Display the contents of the w99.ntds file with the hashes
- **awk -F: '{print $3}'** -  Using colon delimiters, display the third column of information from the file (the LANMAN hash)
- sort: Sort the results
- **uniq -c** - Make the results unique, with a count for repeated occurrences

The result is only a single hash, the empty LANMAN password value aad3b435b51404eeaad3b435b51404ee. This tells us that we don't need to try any LANMAN password cracking and can focus our assessment on NT hashes alone.

### Remove Machine Accounts

The w99.ntds file has NT passwords for all domain users, but it also includes machine account passwords. These are 120 character passwords that are randomly selected and frequently changed within the domain. It is not likely we will crack these passwords, so it is a good idea to exclude them from the password hash list to optimize Hashcat efficiency.

Machine account names end in $ followed by the colon delimiter. Remove these accounts using sed, as shown here:

    sec504@slingshot:~/labs/Wardrobe99$ sed -i '/$:/d' w99.ntds
    sec504@slingshot:~/labs/Wardrobe99$

Note that there will be no output on the screen from this sed command.
Let's break down this command step by step:

- **sed -i** - Use the stream editor (sed) to edit a file in place (e.g. inline mode, with -i)
- '/$:/d' - Match any line with $: (such as WIN-93C2ORV5KSP$:..., representing a domain machine account) and delete the line (/d)
- **w99.ntds** - Read from and replace the w99.ntds file using sed inline mode.

### Crack NT Passwords

Next, start Hashcat, targeting the NT password hashes in the w99.ntds file, using the wordlist mode and the /usr/share/wordlists/rockyou.txt file, as shown here.

    sec504@slingshot:~/labs/Wardrobe99$ hashcat -m 1000 -a 0 w99.ntds /usr/share/wordlists/rockyou.txt --potfile-path ./w99.potfile --force
    hashcat (v4.0.1) starting...

    OpenCL Platform #1: The pocl project
    ====================================
    * Device #1: pthread-Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz, 512/1495 MB allocatable, 2MCU

    Hashes: 2258 digests; 1846 unique digests, 1 unique salts
    Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
    Rules: 1
    ... omitted for space

In this Hashcat invocation, we have added two options we haven't examined previously:

- **--potfile-path** - Specify the location of the potfile where Hashcat saves the cracked passwords, placing it in the current directory
- **--force** - VMware virtual machines cannot access a GPU that may be accessible on your host system; we force Hashcat to crack using the CPU only by adding --force
Allow Hashcat to run for a minute or two on your system before continuing to the next step. Hashcat should quickly exhaust all of the password options in the specified wordlist file, exiting when it reaches the end of the wordlist.

### Generate the DPAT Report

Next, change to the directory where DPAT is installed, as shown here:

    sec504@slingshot:~/labs/Wardrobe99$ cd /home/sec504/labs/DPAT/
    sec504@slingshot:~/labs/DPAT$

Next, run DPAT and generate the password analysis report. Answer y when prompted to open the report, as shown here:

    sec504@slingshot:~/labs/DPAT$ python dpat.py -n ../Wardrobe99/w99.ntds -c ../Wardrobe99/w99.potfile -g ../Wardrobe99/groups/*.txt
    Doesn't look like the Group Files are in the form output by PowerView, assuming the files are already in domain\username list form
    Doesn't look like the Group Files are in the form output by PowerView, assuming the files are already in domain\username list form
    ... repeated warning omitted; this warning can be safely ignored
    Doesn't look like the Group Files are in the form output by PowerView, assuming the files are already in domain\username list form
    The Report has been written to the "_DomainPasswordAuditReport.html" file in the "DPAT Report" directory
    Would you like to open the report now? [Y/n]
    y

Let's break down this command piece by piece:

python dpat.py: Run the DPAT Python script
- **-n ../Wardrobe99/w99.ntds** - Read from the hash file
- **-c ../Wardrobe99/w99.potfile** - Read the cracked passwords
- **-g ../Wardrobe99/groups/*.txt** - Retrieve a list of groups where each file name is the group name with a list of member usernames, one per line
DPAT will launch Firefox with the report content, as shown here.

### Assess DPAT Report

Examine the DPAT report for the Wardrobe99 domain. Answer the following questions:

What percentage of current passwords did Hashcat crack?
How many non-unique passwords are in use in the organization?

What is the most common password length recovered in the password cracking process?

Which department (as seen through domain group membership) has the worst password selection practices (e.g., the greatest percentage of cracked passwords)?

What is the most commonly reused password in the organization?

Characterize the pervasive user password selection problem using password history data.

#### Click to see solution

What percentage of current passwords did Hashcat crack?
DPAT Report for Wardrobe99

How many non-unique passwords are in use in the organization?

The DPAT report reveals that there are 551 password hashes observed in the Impact secretsdump.py output, and 479 of the password hashes are unique. This indicates that 72 user passwords are non-unique within the organization.

What is the most common password length recovered in the password cracking process?

The most common password length is 8 characters, with 138 occurrences.

Which department (as seen through domain group membership) has the worst password selection practices (e.g., the greatest percentage of cracked passwords)?
Glancing at the numbers for Members of count and Passwords Cracked for the same group reveals that the HR Staff group has the highest percentage of cracked passwords (97%).

What is the most commonly reused password in the organization?

Sales321 is the most common password, followed by Password4 and other near variations.

Characterize the pervasive user password selection problem using password history data.

Many users reuse passwords following a predictable pattern of PasswordN where N is an incrementing or repeating digit.

## Why This Lab Is Important

This lab illustrates the benefits of password cracking with Hashcat to identify weaknesses in user password selection, but it also characterizes systemic issues within an organization through the reporting capabilities of DPAT. Consider adding DPAT reporting to your defensive password analysis tasks to best prioritize corrective actions within your organization.