# Meow Tasks

## TASK 1

What does the acronym VM stand for?

`Virtual Machine`

## TASK 2

What tool do we use to interact with the operating system in order to start our VPN connection?

`Terminal`

## TASK 3

What service do we use to form our VPN connection?

`OpenVPN`

## TASK 4

What is the abreviated name for a tunnel interface in the output of your VPN boot-up sequence output?

`tun`

## TASK 5

What tool do we use to test our connection to the target?

`Ping`

## TASK 6

What is the name of the tool we use to scan the target's ports?

`nmap`

## TASK 7

What service do we identify on port 23/tcp during our scans?

`telnet`

## TASK 8

What username ultimately works with the remote management login prompt for the target?

`root`

## SUBMIT FLAG

Submit root flag

![image](https://user-images.githubusercontent.com/87195021/164076344-37a7f295-06f9-493a-b0bc-20ddf6ebd86b.png)

# Meow Box

## Make a new directory to work out of

mkdir -p htb/Meow/nmap

## Reconnaissance

First thing first, we run a quick initial nmap scan to see which ports are open and which services are running on those ports.

    sudo nmap -sC -sV -O --reason -oA /home/htb-mbwest/my_data/htb/Meow/nmap/initial 10.129.92.25

| **Flag** | **Description** |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port** | **Description** |
| --------------|-------------------|
| `23` | Telnet  |

## Background Scan

Before we start investigating these ports, let’s run more comprehensive nmap scans in the background to make sure we cover all bases.

    sudo nmap -sC -sV -O -p- --reason -oA /home/htb-mbwest/my_data/htb/Meow/nmap/full 10.129.92.25

| **Flag** | **Description** |
| --------------|-------------------|
| `-sC` | Run default nmap scripts |
| `-sV` | Detect service version |
| `-O` | Detect OS |
| `-p-` |All Ports |
| `--reason` | Determine the port and host state |
| `-oA` | Output all formats and store in file nmap/initial |

We get back the following results:

| **Port** | **Description** |
| --------------|-------------------|
| `23` | Telnet  |

## Gaining an Initial Foothold

Log into telnet using the `telnet 10.129.92.25` command as `root`.

![image](https://user-images.githubusercontent.com/87195021/164076679-21bf4ed4-b6bf-4adb-bb3d-5d4fa43dae21.png)