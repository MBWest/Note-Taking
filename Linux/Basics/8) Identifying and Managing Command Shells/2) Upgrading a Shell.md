# Linux - Identifying and Managing Command Shells - Upgrading a shell

> ## **Upgrade**

**In our `netcat` shell, we will use the following command to use python to upgrade the type of our shell to a full TTY:**

    MBWest@htb[/htb]$ python -c 'import pty; pty.spawn("/bin/bash")'

**Note:** Python3 Equivalent

    python3 -c 'import pty; pty.spawn("/bin/bash")'

**After we run this command, we will hit `ctrl+z` to background our shell and get back on our local terminal, and input the following `stty` command:**


    www-data@remotehost$ ^Z

    MBWest@htb[/htb]$ stty raw -echo
    MBWest@htb[/htb]$ fg

    [Enter]
    [Enter]
    www-data@remotehost$

---
> ## **Resize**

**We can open another terminal window on our system, maximize the windows or use any size we want, and then input the following commands to get our variables:**

    MBWest@htb[/htb]$ echo $TERM
    xterm-256color


    MBWest@htb[/htb]$ stty size
    67 318

**The first command showed us the TERM variable, and the second shows us the values for rows and columns, respectively. Now that we have our variables, we can go back to our netcat shell and use the following command to correct them:**


    www-data@remotehost$ export TERM=xterm-256color
    www-data@remotehost$ stty rows 67 columns 318

    