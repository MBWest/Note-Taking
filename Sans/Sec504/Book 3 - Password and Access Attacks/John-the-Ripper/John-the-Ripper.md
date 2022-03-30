# John the Ripper

## Brief Intro

In this lab, we'll use John the Ripper as a password cracking tool on the Slingshot Linux VM.

## Requirements for This Lab

In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Create several temporary users with the addtmpusers script. Crack the passwords using John the Ripper, using single and wordlist mode. Remove the temporary users at the end of the lab using deltmpusers.

## Walkthrough

### Creating Passwords to Crack

First, create several accounts for the target of the password cracking exercise. Using sudo, run the addtmpusers script, as shown here:

    sec504@slingshot:~$ sudo addtmpusers
    Adding users ... done.

We'll remove these temporary user accounts at the end of the lab using the deltmpusers script.

### Create a Working Directory

When working with password hashes, it's a good idea to place the content in a directory that is only accessible to you and is separate from other target information. Create and modify the permissions of a hashes directory, as shown here, making the directory accessible only to you and the root user (mode 700):

    sec504@slingshot:~$ mkdir hashes
    sec504@slingshot:~$ chmod 700 hashes

Retrieve Passwords Hashes on Linux
Next, make a copy of the /etc/passwd and /etc/shadow files, saving them in the hashes directory, as shown here:

    sec504@slingshot:~$ cd hashes/
    sec504@slingshot:~/hashes$ cp /etc/passwd ./passwd_copy
    sec504@slingshot:~/hashes$ sudo cp /etc/shadow ./shadow_copy

Next, change the permissions for the shadow_copy file so that you can read it as the sec504 user account, as shown here:

    sec504@slingshot:~/hashes$ sudo chown sec504:sec504 shadow_copy

### Merge User and Password Hash Information

While the /etc/shadow file alone is sufficient to obtain username and password hash information, it does not include the user comment field (also known as the GECOS or gecos field, though there is no consensus on what the acronym form stands for) in the /etc/passwd file. John will take advantage of this field in the single crack mode that we'll examine shortly, so it is useful to merge the files together.

Fortunately, John includes the unshadow command to merge the two files. Run the unshadow command to produce the merged content as the file combined, as shown here:

    sec504@slingshot:~/hashes$ unshadow passwd_copy shadow_copy > combined
    Created directory: /home/sec504/.john

Examine a few lines from the end of the combined file using the tail command:

    sec504@slingshot:~/hashes$ tail -3 combined
    cghislai:$5$RronF95hMxfi5lIL$1xMtlh/pT4ta4:1018:1018:Colleen Ghislaine:/home/cghislai:/usr/sbin/nologin
    pemma:$6$o7Hk1AiVbtkncRdE$eFQ62anBONZQxfzR5qvcBKBmc4F51qtQZJN80:1019:1019:Preston Emma:/home/pemma:/usr/sbin/nologin
    aruben:$6$.N3Lcfz3g.TULr5W$kUmYm.tqoKM9.FbsK0Z2ZnHC1oofSv4Vvqx/:1020:1020:Alvar Ruben:/home/aruben:/usr/sbin/nologin

Note: The password hashes on your system will be different than the example shown here.
The unshadow command merges the passwd and the shadow files together, placing the user's password hash in the second column (delimited by colons). We'll use this information in the next step to examine the format of password hashes in more detail.

### Examine Password Hashes

Use the cat, awk, and sort utilities to examine a list of unique password hashes in the combined file, as shown here:

    sec504@slingshot:~/hashes$ cat combined | awk -F: '{print $2}' | sort -u
    !
    *
    $1$CcnsCfGe$Hx4pkK9ZjxvyWjIXRHbIK.
    $1$DYqac84V$.dzFJxfWvByfSUmhnahZ71
    $1$l63otE1T$DPtL0YeiZclZu73zqS3K//
    $1$M57qRnDk$.nSJ.3omLvyd7MmJTMwLs/
    $1$PKdxjqEc$aumEoq2hrgPPvTMB/jtaB0
    $1$zrf7UfLe$SLsXBkoerKR.3OBithCdQ0
    27PaiLNzLhaaM
    5aAGszs4QfbwY
    $5$P7wLccB3neRh80mU$FxsUiWP4GcNK/HyOkFO1GjlP40Wk7qp90uHqq/LBzx1
    $5$TdtFWi106yksnyH1$MyC7cGi2Ps6VVeGQMzk2dcSN0.mNHyRdt0SX2D6IIM2
    $5$ycK6UlsRBK2JYWfq$Pqc4daYMQ/ZKTwOrBmUp/jmzlDYdL7hwxeYeHUDA5W5
    $6$d00ppRsw/JYiR8TC$hS/BVaIYroQqHNi0a63XTZxlMm4Hn5XsWB6s2GIfcOu/XGUZG.VxMjr7ANMhHIs8yi70xoeNruawSwny9DQi8.
    $6$dFuuj9lL4gSzGhtO$1h5gvHnY2cPimNmJsd79QXbdWCHU279Nhio3iGw5WZtjUBsYiFCsSW3z2udYKEvhx/8pSqEnW8IOWJph5iIXk.
    $6$DObnvXa5cAMyOZDP$aoYoEcPb0cLNL9V83AIXb4K9ja8gyDcG46tbEyh7M1yyUl5fXSMYsgT16PwHxc3C2N/9dOoy54QU1ZU/BUPCr/
    $6$XTIUjAAE1BQOiHCm$WXOUEzk5OBkX54UdPX49O2fOHpsL7To1/1j/vCDyZBUoHSCf2F6lSyRJ5q4KVA/.ie4kt7SyhS1yf5R9R0qJ00
    GFMJwdepOX1T6
    Hswx8Go63UtOQ
    kyoT0yOd.ntuI
    SmWiXRrFhAa5I
    X067Lw9B.batQ

Note: The password hashes on your system will be different than the example shown here.
Let's break down this command piece by piece:

- **cat combined** - Display the file contents
- **awk -F** - '{print $2}': Display data from the second column, delimited by colons
- **sort -u** - Sort the results and display unique lines
The list of password hashes shows two examples of disabled accounts (* and !). The rest of the values are password hashes for different user accounts. The shortest values are legacy DES crypt password hashes, a weak password hashing function.

The other password hashes all have a similar format. Some are a DES hash calculation with a common length. Others are delimited by $ with the following fields:

- The hash type
- The password salt
- The password hash

For the hash type field, we see three values:

- $1: MD5 crypt password hashes
- $5: SHA256 crypt password hashes
- $6: SHA512 crypt password hashes

We'll use the different capabilities of John to recover passwords for all four hash types.

### Examine John Hash Support

Run John with the --list=formats argument to see a list of supported password hashes, as shown here:

    sec504@slingshot:~/hashes$ john --list=formats
    descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS,
    tripcode, AndroidBackup, adxcrypt, agilekeychain, aix-ssha1, aix-ssha256,
    aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5,
    AxCrypt, AzureAD, BestCrypt, bfegg, Bitcoin, BitLocker, bitshares, Bitwarden,
    ...
    ZIP-opencl, dummy, crypt

Of these, the relevant password hashes to us are:

- descrypt
- md5crypt
- sha256crypt
- sha512crypt

Next, we'll apply these different password hash types to recover passwords from the combined file.

### John Single Crack - DES Crypt

Let's start by using John to crack the legacy DES crypt password hashes using the --format=descrypt argument. First, we'll start with John's single crack mode (e.g., using variations of the comment or GECOS field in the /etc/passwd file as password guesses), as shown here:

    sec504@slingshot:~/hashes$ john --format=descrypt --single combined
    Using default input encoding: UTF-8
    Loaded 7 password hashes with 7 different salts (descrypt, traditional crypt(3) [DES 128/128 AVX])
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    harukori         (hrio)
    alucasta         (alucasta)
    Almost done: Processing the remaining buffered candidate passwords, if any.
    2g 0:00:00:00 DONE (2020-01-11 22:02) 20.00g/s 254570p/s 264680c/s 264680C/s bbeva192..eva1900
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Here John is able to recover two passwords for the users hrio and alucasta. Both passwords are variations of the username or full name information disclosed in the combined file. John's status output indicates that it is able to crack at a rate of 254,570 passwords/second using this hash type (this cracking performance will differ depending on the host used when running John).

Note: In our next lab, we'll also examine Hashcat, which is arguably a faster password cracking tool than John the Ripper, but it notably lacks the single mode attack method, which is often sufficient to recover plaintext passwords from large password hash dumps.
Next, we'll continue to target the DES crypt hashes using a wordlist.

### John Wordlist Crack - DES Crypt

Next, continue to crack the DES crypt password hashes, this time using the words in the default John wordlist file, as shown here:

    sec504@slingshot:~/hashes$ john --format=descrypt --wordlist=/usr/local/share/john/password.lst combined
    Using default input encoding: UTF-8
    Loaded 7 password hashes with 7 different salts (descrypt, traditional crypt(3) [DES 128/128 AVX])
    Remaining 5 password hashes with 5 different salts
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Victoria         (lrenate)
    Front242         (jorestes)
    Wolverin         (beva)
    3g 0:00:00:00 DONE (2020-01-11 22:02) 42.85g/s 50600p/s 253000c/s 253000C/s 123456..sss
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Note that John does not show you the previously cracked passwords from the single crack mode. To display all of the previously cracked passwords for a given hash file, specify the --show argument and the hash file, as shown here:

    sec504@slingshot:~/hashes$ john --show combined
    beva:Wolverin:1002:1002:Bridget Eva:/home/beva:/usr/sbin/nologin
    lrenate:Victoria:1006:1006:Lea Renate:/home/lrenate:/usr/sbin/nologin
    jorestes:Front242:1007:1007:Jerald Orestes:/home/jorestes:/usr/sbin/nologin
    hrio:harukori:1009:1009:Haruko Rio:/home/hrio:/usr/sbin/nologin
    alucasta:alucasta:1014:1014:Arthur Lucasta:/home/alucasta:/usr/sbin/nologin

    5 password hashes cracked, 15 left

We can also examine the passwords we have not yet cracked using the --show=left argument with the specific hash format, as shown here:

    sec504@slingshot:~/hashes$ john --show=left --format=descrypt combined
    asayaka:27PaiLNzLhaaM
    rkaede:SmWiXRrFhAa5I

    5 password hashes cracked, 2 left

Next, let's attack the password hashes using the MD5 crypt algorithm.

### John Single Crack - MD5 Crypt

The MD5 crypt password hashes are indicated with the $1 marker. First, start with the John single crack mode again:

Tip: Save some typing by pressing the up arrow to recall the command history where you previously perform the John single crack mode (e.g., the line with the argument --single), then use your arrow keys to change the hash type from descrypt to md5crypt.

    sec504@slingshot:~/hashes$ john --format=md5crypt --single combined
    Using default input encoding: UTF-8
    Loaded 6 password hashes with 6 different salts (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 AVX 4x3])
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    ghajsson         (ghajsson)
    Almost done: Processing the remaining buffered candidate passwords, if any.
    1g 0:00:00:02 DONE (2020-01-11 22:04) 0.4201g/s 22026p/s 22057c/s 22057C/s vjulius1902..vjulius1900
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Note how the MD5 crypt password hash type is considerably slower at 22,026 passwords/second, compared to the 50,600 passwords/second for DES crypt passwords.

In this attack, one additional password is learned.

### John Wordlist Crack - MD5 Crypt

Next, perform the wordlist mode attack for the MD5 crypt password hashes:

    sec504@slingshot:~/hashes$ john --format=md5crypt --wordlist=/usr/local/share/john/password.lst combined
    Using default input encoding: UTF-8
    Loaded 6 password hashes with 6 different salts (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 AVX 4x3])
    Remaining 5 password hashes with 5 different salts
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Elizabeth        (prosa)
    ChangeMe         (jviktori)
    2g 0:00:00:00 DONE (2020-01-11 22:04) 10.00g/s 17730p/s 77160c/s 77160C/s !@#$%..sss
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    Because John is reading from a file (instead of mutating the GECOS information), the password/second rate drops to 17,730 p/s.

Here we recovered two additional passwords from the hash file. Examine the list of remaining password hashes using --show=left for the MD5 crypt hash type:

    sec504@slingshot:~/hashes$ john --show=left --format=md5crypt combined
    ejonah:$1$l63otE1T$DPtL0YeiZclZu73zqS3K//
    ayoshie:$1$M57qRnDk$.nSJ.3omLvyd7MmJTMwLs/
    rlucian:$1$CcnsCfGe$Hx4pkK9ZjxvyWjIXRHbIK.

    3 password hashes cracked, 3 left

Next, target the password hashes using the SHA256 crypt hash type.

### John Single Crack - SHA256 Crypt

Repeat the John single crack mode attack again, this time targeting the SHA256 crypt hashes, as shown here:

    sec504@slingshot:~/hashes$ john --format=sha256crypt --single combined
    Using default input encoding: UTF-8
    Loaded 3 password hashes with 3 different salts (sha256crypt, crypt(3) $5$ [SHA256 128/128 AVX 4x])
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Ghislaine        (cghislai)
    Almost done: Processing the remaining buffered candidate passwords, if any.
    1g 0:00:00:20 DONE (2020-01-11 22:07) 0.04766g/s 1147p/s 1147c/s 1147C/s ferdinandogrant1900..gferdinando1900
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Notice how the cracking process is considerably slower here. John indicates that the cost is 1 based on the hash iteration count of 5000. That is, John must hash each password guess 5000 times using SHA256 to determine if it is a match. Since there are salt values associated with the password hashes as well, John must repeat this 5000-hash calculation process for every user account, for every password. This makes the work of the attacker significantly more difficult and time-consuming.

### John Wordlist Crack - SHA256 Crypt

Repeat the wordlist attack again, this time for SHA256 crypt password hashes:

    sec504@slingshot:~/hashes$ john --format=sha256crypt --wordlist=/usr/local/share/john/password.lst combined
    Using default input encoding: UTF-8
    Loaded 3 password hashes with 3 different salts (sha256crypt, crypt(3) $5$ [SHA256 128/128 AVX 4x])
    Remaining 2 password hashes with 2 different salts
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Princess         (fgrant)
    1g 0:00:00:02 DONE (2020-01-11 22:07) 0.4484g/s 1590p/s 2278c/s 2278C/s modem..sss
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Again, examine the remaining passwords for this hash type:

    sec504@slingshot:~/hashes$ john --show=left --format=sha256crypt combined
    tamando:$5$P7wLccB3neRh80mU$FxsUiWP4GcNK/HyOkFO1GjlP40Wk7qp90uHqq/LBzx1

    2 password hashes cracked, 1 left

Finally, complete the initial pass of password hash attacks on the last remaining hash type, the SHA512 crypt hashes.

### John Single Crack - SHA512 Crypt
Repeat the single crack mode attack, this time specifying the SHA512 crypt hash type:

    sec504@slingshot:~/hashes$ john --format=sha512crypt --single combined
    Using default input encoding: UTF-8
    Loaded 4 password hashes with 4 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Ogechukwukama    (rogechuk)
    sec504           (sec504)
    Almost done: Processing the remaining buffered candidate passwords, if any.
    2g 0:00:00:15 DONE (2020-01-11 22:09) 0.1269g/s 1521p/s 1522c/s 1522C/s rubenaruben1900..ralvar1900
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Notice that the performance of SHA512 password cracking is roughly the same as SHA256 password cracking. Both require 5000 iterations per password per user, and both are roughly comparable in terms of performance for a single hash calculation.

### John Wordlist Crack - SHA512 Crypt

Finally, finish the initial pass of attacks using the John wordlist mode with the SHA512 password hash type:

    sec504@slingshot:~/hashes$ john --format=sha512crypt --wordlist=/usr/local/share/john/password.lst combined
    Using default input encoding: UTF-8
    Loaded 4 password hashes with 4 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
    Remaining 2 password hashes with 2 different salts
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    ChangeMe         (pemma)
    1g 0:00:00:04 DONE (2020-01-11 22:09) 0.2183g/s 774.2p/s 1548c/s 1548C/s !@#$%..sss
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Notice that performance dropped again here compared to single crack mode SHA512 crypt hashes, due to the file I/O overhead associated with reading from the password wordlist file.

Next, examine the remaining password hashes for the SHA512 crypt hash type:

    sec504@slingshot:~/hashes$ john --show=left --format=sha512crypt combined
    aruben:$6$dFuuj9lL4gSzGhtO$1h5gvHnY2cPimNmJsd79QXbdWCHU279Nhio3iGw5WZtjUBsYiFCsSW3z2udYKEvhx/8pSqEnW8IOWJph5iIXk.

    3 password hashes cracked, 1 left

### Examine Cracked Passwords

Examine all of the cracked passwords for the combined file:

    sec504@slingshot:~/hashes$ john --show combined
    sec504:sec504:1001:1001::/home/sec504:/bin/bash
    beva:Wolverin:1002:1002:Bridget Eva:/home/beva:/usr/sbin/nologin
    fgrant:Princess:1003:1003:Ferdinando Grant:/home/fgrant:/usr/sbin/nologin
    prosa:Elizabeth:1004:1004:Phyliss Rosa:/home/prosa:/usr/sbin/nologin
    ghajsson:ghajsson:1005:1005:Gertrud Hajsson:/home/ghajsson:/usr/sbin/nologin
    lrenate:Victoria:1006:1006:Lea Renate:/home/lrenate:/usr/sbin/nologin
    jorestes:Front242:1007:1007:Jerald Orestes:/home/jorestes:/usr/sbin/nologin
    hrio:harukori:1009:1009:Haruko Rio:/home/hrio:/usr/sbin/nologin
    rogechuk:Ogechukwukama:1010:1010:Riya Ogechukwukama:/home/rogechuk:/usr/sbin/nologin
    alucasta:alucasta:1014:1014:Arthur Lucasta:/home/alucasta:/usr/sbin/nologin
    jviktori:ChangeMe:1015:1015:Julius Viktoria:/home/jviktori:/usr/sbin/nologin
    cghislai:Ghislaine:1018:1018:Colleen Ghislaine:/home/cghislai:/usr/sbin/nologin
    pemma:ChangeMe:1019:1019:Preston Emma:/home/pemma:/usr/sbin/nologin

    13 password hashes cracked, 7 left

Here we see 13 successfully recovered passwords of the 20 total from the /etc/shadow file. This is excellent progress!

The remaining passwords that you have not yet cracked can be recovered using a wordlist attack with the /usr/share/wordlists/rockyou.txt wordlist file. Use this wordlist file to recover the remaining passwords for the DES crypt and MD5 crypt hash types for the remaining period of the lab exercise time.

If you are really ambitious, you can also crack the remaining passwords for the SHA256 crypt and SHA512 crypt hashes, though this will take more time than we can allocate to the lab exercise.

## Answers

### Click to see solution

In the sections that follow, we'll examine the results of the password cracking process for the uncracked password hashes.

First, the DES crypt passwords will crack quickly:

    sec504@slingshot:~/hashes$ john --format=descrypt --wordlist=/usr/share/wordlists/rockyou.txt combined
    Using default input encoding: UTF-8
    Loaded 7 password hashes with 7 different salts (descrypt, traditional crypt(3) [DES 128/128 AVX])
    Remaining 2 password hashes with 2 different salts
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    lestadmi         (rkaede)
    5pid3rw0         (asayaka)
    2g 0:00:00:02 DONE (2020-01-11 14:17) 0.7782g/s 4127Kp/s 6279Kc/s 6279KC/s 5tequero..59999907
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    sec504@slingshot:~/hashes$ john --show=left --format=descrypt combined

    7 password hashes cracked, 0 left

Repeat this command for the MD5 crypt password hash type, as shown here. Note that this command will take several minutes to complete, and may exceed the time allotted to the lab exercise. You may optionally continue to run the password cracker after the lab time is up as desired until the passwords are cracked.

    sec504@slingshot:~/hashes$ john --format=md5crypt --wordlist=/usr/share/wordlists/rockyou.txt combined
    Using default input encoding: UTF-8
    Loaded 6 password hashes with 6 different salts (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 AVX 4x3])
    Remaining 3 password hashes with 3 different salts
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    0g 0:00:02:36 33.20% (ETA: 22:22:35) 0g/s 31017p/s 93053c/s 93053C/s onedeep26..onecrip1
    jyro210383       (ejonah)
    2162639mc        (ayoshie)
    023731066        (rlucian)
    3g 0:00:06:08 DONE (2020-01-11 22:20) 0.008147g/s 37768p/s 90346c/s 90346C/s 023734947***..023703251
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

### Cleanup

When you are finished cracking the passwords for this lab exercise, remove the temporary users by running the deltmpusers script with sudo privileges, as shown here:

    sec504@slingshot:~/hashes$ sudo deltmpusers
    Removing users ... done.

## Why This Lab Is Important

Understanding password cracking tools is a necessary component to establish an overall password policy for an organization. With password hashes, an attacker can leverage password cracking tools to perform offline password guessing. The speed of the attack, and the attacker's ability to recover passwords, depends on the length and complexity of the password selection, the password hash storage mechanism, and the computing resources of the attacker.