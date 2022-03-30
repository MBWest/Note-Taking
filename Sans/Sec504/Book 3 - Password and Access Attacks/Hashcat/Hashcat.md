# Hashcat

## Brief Intro

In this lab, we're going to use Hashcat to crack some password hashes using the Windows VM. Hashcat is probably the most flexible and powerful password cracker available to the public today, widely used by attackers, but also by defenders for understanding the risks associated with weak passwords.

Optionally, you may choose to complete this lab exercise from your Slingshot Linux VM. A companion Hashcat exercise with steps for Linux is also available.

Note that in this lab exercise we use Hashcat running in a virtual machine, leveraging only the host CPU to crack passwords. In practice, it is better to use Hashcat on the native host system, taking advantage of available GPU resources to significantly improve cracking performance.

## Requirements for This Lab

In this lab, you will use your Windows 10 VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Run hashcat to crack the sam.txt and md5.txt files located in your Windows VM in the C:\Tools\hashcat directory.

## Walkthrough

### Running Hashcat on Windows

Now we are going to run Hashcat on some Windows LM and NT password hashes. To do this, open a Command Prompt on the Windows VM. Change to the C:\Tools\hashcat directory, as shown here.

    C:\Users\Sec504> cd \tools\hashcat

    C:\Tools\hashcat>

Next, let's look at some Hashcat command line parameters. To crack the sam.txt password hashes, we will specify the following options:

- **-a** – Specify the Hashcat attack mode; here we use -a 0 for a straight wordlist attack
- **-m** – Specify the hash type; here -m 3000 indicates that we will perform LANMAN password hash cracking
- **-r** – Specify a Hashcat rules file; here -r rules\Incisive-leetspeak.rule tells Hashcat to utilize the Incisive-leetspeak rules file, located in the rules directory
- **sam.txt** – The list of password hashes to crack
- **password.lst** – The wordlist file

Run Hashcat using these options, as shown here:

    C:\Tools\hashcat> hashcat.exe -a 0 -m 3000 -r rules\Incisive-leetspeak.rule sam.txt password.lst
    hashcat (v6.2.3) starting

    OpenCL API (OpenCL 1.2 ) - Platform #1 [Intel(R) Corporation]
    =============================================================
    * Device #1: Intel(R) Core(TM) i9-9980HK CPU @ 2.40GHz, 4031/4095 MB (1023 MB allocatable), 2MCU

    Minimum password length supported by kernel: 0
    Maximum password length supported by kernel: 7

    Hashfile 'sam.txt' on line 4 (Guest:...PASSWORD*********************:::): Token encoding exception
    Hashes: 16 digests; 14 unique digests, 1 unique salts
    Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
    Rules: 15487

    Optimizers applied:
    * Zero-Byte
    * Not-Iterated
    * Single-Salt

    Watchdog: Hardware monitoring interface not found on your system.
    Watchdog: Temperature abort trigger disabled.

    INFO: Removed 1 hash found as potfile entry or as empty hash.

    Host memory required for this attack: 0 MB

    Dictionary cache built:
    * Filename..: password.lst
    * Passwords.: 6255
    * Bytes.....: 29772
    * Keyspace..: 96871185
    * Runtime...: 0 secs

    3eacdee7e4395079:INTERNE
    7584248b8d2c9f9e:A
    af83dbf0052ee471:VIRGINI
    ...

When plaintext passwords are revealed, they will be displayed on the screen. Continue with the next section while Hashcat is running.

### Hashcat Running

While Hashcat is running, it will give you an overall status of cracking.

In this Hashcat session, the maximum length of passwords it can crack is seven characters. This matches our understanding of the LANMAN password hash format, since LANMAN password hashes are only two seven-character strings.
Hashcat also displays the current cracking status. In the example shown earlier, Hashcat has cracked a few passwords such as INTERNE, A, and VIRGINI. Remember that LANMAN password hashes are always uppercase, and will never be longer than 7 characters.
Finally, Hashcat will present some options while it is running. Hashcat will offer to show the status by pressing the s key. It can pause with p. It can provide a checkpoint with c, and you can kill the current cracking session with q. Please note, you do not have to press anything; it will just keep on cracking in the background.

### Cracking NT Hashes with Hashcat

Next let's crack NT password hashes. Run the same Hashcat command again, this time changing the -m argument to indicate mode 1000 to target the NT hashes, as shown:

    C:\Tools\hashcat>hashcat.exe -a 0 -m 1000 -r rules\Incisive-leetspeak.rule sam.txt password.lst
    hashcat (v6.2.3) starting

    ...

    Dictionary cache built:
    * Filename..: password.lst
    * Passwords.: 3557
    * Bytes.....: 29772
    * Keyspace..: 55087259
    * Runtime...: 0 secs


    a65c3da63fdb6ca22c172b13169d62a5:virginia
    18da6c2895c549e266745951d5dc66cb:newpass
    Approaching final keyspace - workload adjusted.
    ...

Notice the difference in the output? NT password hashes preserve the password case sensitivity. Also, the maximum length is much longer for NT password hashes.

### Hashcat Cracking MD5 Hashes

Next, let's crack some MD5 password hashes. Repeat the last command again, this time specifying the mode 0 (-m 0) for MD5 password hashes, and the hash file md5.txt, as shown here:

    C:\Tools\hashcat>hashcat.exe -a 0 -m 0 -r rules\Incisive-leetspeak.rule md5.txt password.lst
    hashcat (v6.2.3) starting

    ...

    e10adc3949ba59abbe56e057f20f883e:123456
    d8578edf8458ce06fbc5bb76a58c5ca4:qwerty
    0d107d09f5bbe40cade3de5c71e9e9b7:letmein
    4297f44b13955235245b2497399d7a93:123123
    c33367701511b4f6020ec61ded352059:654321
    5f4dcc3b5aa765d61d8327deb882cf99:password
    e99a18c428cb38d5f260853678922e03:abc123
    21232f297a57a5a743894a0e4a801fc3:admin
    Approaching final keyspace - workload adjusted.

    Session..........: hashcat
    Status...........: Exhausted
    Hash.Name........: MD5
    Hash.Target......: md5.txt
    Time.Started.....: Tue Aug 10 02:26:16 2021 (6 secs)
    Time.Estimated...: Tue Aug 10 02:26:22 2021 (0 secs)
    Kernel.Feature...: Pure Kernel
    Guess.Base.......: File (password.lst)
    Guess.Mod........: Rules (rules\Incisive-leetspeak.rule)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........:  9463.0 kH/s (5.98ms) @ Accel:256 Loops:128 Thr:1 Vec:8
    Recovered........: 8/10 (80.00%) Digests
    Progress.........: 55087259/55087259 (100.00%)
    Rejected.........: 0/55087259 (0.00%)
    Restore.Point....: 3557/3557 (100.00%)
    Restore.Sub.#1...: Salt:0 Amplifier:15360-15487 Iteration:0-128
    Candidate.Engine.: Device Generator
    Candidates.#1....: ma++1ngly -> sss

By changing the attack mode from 3000 (LM) to 0 (MD5), we are now cracking MD5 password hashes.

Note the password cracking rate of 9463 kH/s (9.4 million hashes/second). MD5 is an older, weak hashing algorithm that offers little resistance to hash cracking attacks.

### Hashcat: Going Further

There are many, many options for Hashcat. Run Hashcat with the -h argument to get the built-in help documentation. Examine the list of password hashes that Hashcat supports for cracking.

## Why This Lab Is Important

Defenders often overestimate the level of effort required to break passwords using the techniques we discussed in this module. In the past several years, the performance of GPUs for password cracking continues to improve significantly, with a single NVIDIA RTX GeForce 2080i card cracking NT hashes at a rate of nearly 96 million hashes/second.