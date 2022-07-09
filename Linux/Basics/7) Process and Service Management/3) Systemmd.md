# Linux Process and Service Management - systemmd

> ## **systemmd**

- New init system that improves upon older systems (upstart, SysV, etc…)
- First process started by the kernel, has a PID of 1
- Initializes the components that need to be started after the kernel is booted
- Responsible for service management while the OS is running
- Refers to system services (and everything else it manages) as units
    - We’re primarily concerned with service units and target units
    - A service unit is for managing daemons while a target unit is just a collection of other units

> ## **Example systemd service unit**

```
[root@wkstn ~]# cat /lib/systemd/system/sshd.service
[Unit]
Description=OpenSSH server daemon
After=syslog.target network.target auditd.service
 
[Service]
EnvironmentFile=/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd –D $OPTIONS
ExecReload=/bin/kill –HUP $MAINPID
 
[Install]
WantedBy=multi-user.target
```