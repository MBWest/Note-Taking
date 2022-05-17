# VPS Setup

Whether we are on an internal or external penetration test, a VPS that we can use is of great importance to us in many different cases. We can store all our resources on it and access them from almost any point with internet access. Apart from the fact that we first have to set up the VPS, we also have to prepare the corresponding folder structure and its services. In this example, we will deal with the provider called Vultr and set up our VPS there. For the other providers, the configuration options look almost identical.

We should still read the individual information about their components carefully and understand what kind of VPS we will be working with in the future. In Vultr, we can choose one of the four different servers. For our purposes, the `Cloud Computer` server is sufficient for now.

![image](https://user-images.githubusercontent.com/87195021/166479260-3052b8e5-6fff-404d-99bb-1a716af86144.png)

Next, we need to select the location closest to us. This will ensure an excellent connection to our server. If we need to perform a penetration test on another continent, we can also set up a VPS there using our automation scripts and perform the penetration test from there.

![image](https://user-images.githubusercontent.com/87195021/166479291-d331c906-11a1-4009-b8a1-ef9e2b378ae6.png)

For the server type, we select which operating system should be installed on the VPS. ParrotOS is based on Debian, just like Ubuntu. Here we can choose one of these two or go to advanced options and upload our ISO.

![image](https://user-images.githubusercontent.com/87195021/166479321-78cc8e0a-3e18-413b-997a-44fa3909e2a9.png)

If we want to upload our ISO, we have to do it via a public link to that ISO. We can go to the ParrotOS website, copy the link to the mirror server for the appropriate version, and paste it into Vultr.

![image](https://user-images.githubusercontent.com/87195021/166479341-5a677892-ec7b-4811-ad64-f88c5cf51100.png)

Next, we need to choose the performance level for our VPS. This is one of the points where the cost can change a lot. For our purposes, however, we can choose one of the two options on the left. However, here we need to select the performance for which we want to use the VPS. If the VPS is to be used for advanced purposes and provides many requests and services, 1024MB memory will not be enough. Therefore, it is always advisable to first set up the installation of our OS locally in a VM and then check the services' load.

![image](https://user-images.githubusercontent.com/87195021/166479424-bbc7ea04-288f-48a2-9854-fa3134130fdb.png)

Next, we have the choice if we want to use IPv6 for our VPS. This is highly recommended because many firewalls are only protected against IPv4, and IPv6 is forgotten. We can also allow automatic backups, private networking, and DDOS protection, but at a higher cost.

![image](https://user-images.githubusercontent.com/87195021/166479424-bbc7ea04-288f-48a2-9854-fa3134130fdb.png)

After that, we can generate our SSH keys, which we can use to log in to the VPS via SSH later. We can also generate these keys later on our VPS or our VM or own host operating system. Let's use our VM to generate the key pair.

**Generate SSH Keys**

    ┌─[cry0l1t3@parrot]─[~]
    └──╼ $ ssh-keygen -t rsa -b 4096 -f vps-ssh

    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): ******************
    Enter same passphrase again: ******************
    Your identification has been saved in vps-ssh
    Your public key has been saved in vps-ssh.pub
    The key fingerprint is:
    SHA256:zXyVAWK00000000000000000000VS4a/f0000+ag cry0l1t3@parrot
    The key's randomart image is:
    ...SNIP...

With the command shown above, we generate two different keys. The vps-ssh is the private key and must not be shared anywhere or with anyone. The second vps-ssh.pub is the public key which we can now insert in the Vultr control panel.

**SSH Keys**

    ┌─[cry0l1t3@parrot]─[~]
    └──╼ $ ls -l vps*

    -rw------- 1 cry0l1t3 cry0l1t3 3434 Mar 30 12:23 vps-ssh
    -rw-r--r-- 1 cry0l1t3 cry0l1t3  741 Mar 30 12:23 vps-ssh.pub

![image](https://user-images.githubusercontent.com/87195021/166479653-ab2101d3-5ab1-446a-98be-8b2f970fa680.png)

Finally, we choose a hostname and the server label with which we want to name our VPS.

![image](https://user-images.githubusercontent.com/87195021/166479728-e868f200-0ab1-43f1-85ee-c3fbd9efdc43.png)

Once the VPS is installed, we can access it via SSH.

**SSH Using Password**

    MBWest@htb[/htb]$ ssh root@<vps-ip-address>

    root@<vps-ip-address>'s password: 

    [root@VPS ~]# 

After that, we should add a new user for the VPS to not run our services with root or administrator privileges. For this, we can then generate another SSH key and insert it for this user.

    Adding a New Sudo User
    Adding a New Sudo User
    [root@VPS ~]# adduser cry0l1t3
    [root@VPS ~]# usermod -aG sudo cry0l1t3
    [root@VPS ~]# su - cry0l1t3
    Password: 

    [cry0l1t3@VPS ~]$

**Adding Public SSH Key to VPS**

    [cry0l1t3@VPS ~]$ mkdir ~/.ssh
    [cry0l1t3@VPS ~]$ echo '<vps-ssh.pub>' > ~/.ssh/authorized_keys
    [cry0l1t3@VPS ~]$ chmod 600 ~/.ssh/authorized_keys

Once we have added this to the authorized_keys file, we can use the private key to log in to the system via SSH.

**Using SSH Keys**

    MBWest@htb[/htb]$ ssh cry0l1t3@<vps-ip-address> -i vps-ssh-cry0l1t3

    [cry0l1t3@VPS ~]$ 