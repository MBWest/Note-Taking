# Linux - Partitions and Disk Management

> ## **NFS Server Configuration**

| **Location**   | **Description**   |
| --------------|-------------------|
| **NFS Server Configuration** |
| `/etc/exports/` |  Which file systems are exported, permissions and which host may mount them |
| `/etc/host.allow` |  Which hosts are permitted to mount exported file systems |
| `/etc/host.deny` |  Which host are explicity denied permissions to mount exported file systems |

> ##  **Mounting**
- Mount an NFS file system to access it

```
mount -t nfs computer:fs /mount_point
```

---

> ## **Network File System (NFS)**
- - Default Port 2049
- Internet standard protocol created by Sun in 1984 for file sharing between systems
- Can be used across any Unix-based system
- Allows file sharing by mounting remote directories using Remote Procedure Call(s)
- Must have the nfs service running 
- Setup your share in the /etc/exports file
    - Serves as an access control list for the file systems that are being exported
    - `Field 1` -- Share folder location (must be an absolute path)
    - `Field 2` -- Who is allowed access (single host, network, wildcards)
    - `Field 3` -- Options (ro, rw, squash_root, all_squash, sync)
    - `Field 4` -- Comments

```
[guru@CentOS ~]$ grep pracPC /etc/exports
/media/pracPC	33.30.0.0/24(ro,sync) 	#Comments go here
```
---
> ## **showmount [OPTION] [host]**
- Queries a host for information about the state of the NFS server on that machine
    - Displays entries in the etab file
    - Only returns entries that are exported and to which the querying host has access
- `-e` - Show the NFS server’s export list

```
[guru@CentOS ~]$ showmount -e 33.30.150.217
Export list for 33.30.150.217
/media/shared 33.30.150.0/24
```
---

> ## **mount [OPTION] device directory**
- Tells the kernel to attach the filesystem  found on device at directory 
    - Previous contents (if any) become invisible
- Remote shares are treated as folders mounted under /
- `-e` - Show the NFS server’s export list

```
[guru@CentOS ~]$ showmount -e 33.30.150.217
Export list for 33.30.150.217
/media/shared 33.30.150.0/24

[guru@CentOS ~]$ mkdir my_shared_dir

[guru@CentOS ~]$ mount 33.30.150.217:/media/shared my_shared_dir
```
---

> ## **lsof [OPTION] [names]**
- List open files
    - Without arguments, shows all open files belonging to all processes
- `-P` - do not convert port numbers to port names
- `-n` - do not convert ip addresses to hostnames
- `-i` - lists all established connections and listening ports 
    - -iTCP
    - -i:443
    - -i@192.168.1.100
- `+D` – recursively show all open instances of dir and files within
- `+d` - equivalent to +D, except non-recursive
- `-R` - adds the PPID column to output

```
[root@CentOS ~]# lsof +d /var/log
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
rsyslogd 1031 root    1w   REG  252,1      307   80 /var/log/messages
rsyslogd 1031 root    2w   REG  252,1    41884   48 /var/log/cron
rsyslogd 1031 root    4w   REG  252,1     2665 6604 /var/log/secure

[root@CentOS ~]# ls -al /proc/1031/fd
dr-x------ 2 root root  0 Jan  4 03:15 .
dr-xr-xr-x 8 root root  0 Dec 31 03:14 ..
lrwx------ 1 root root 64 Jan  7 14:12 0 -> socket:[8278]
l-wx------ 1 root root 64 Jan  7 14:12 1 -> /var/log/messages
l-wx------ 1 root root 64 Jan  7 14:12 2 -> /var/log/cron
lr-x------ 1 root root 64 Jan  7 14:12 3 -> /proc/kmsg
l-wx------ 1 root root 64 Jan  7 14:12 4 -> /var/log/secure

[root@CentOS ~]# lsof -Pn | grep 8278
rsyslogd   1031    root    unix 0xdf511040      0t0       8278 /dev/log

[root@CentOS ~]# lsof -i
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd     1167 root    3u  IPv4   8744      0t0  TCP *:ssh (LISTEN)
sshd     1167 root    4u  IPv6   8746      0t0  TCP *:ssh (LISTEN)
sshd    15788 ... 104.236.58.12:ssh->108-234-171-194:46798 (ESTABLISHED)
python  15905 root    3u  IPv4 935363      0t0  TCP *:irdmi (LISTEN)

[root@CentOS ~]# lsof -Pni:8000
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  15905 root    3u  IPv4 935363      0t0  TCP *:8000 (LISTEN)

[root@CentOS ~]# lsof -R +d /tmp
COMMAND   PID  PPID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
python  15905 15790 root  cwd    DIR  252,1     4096 258564 /tmp
```