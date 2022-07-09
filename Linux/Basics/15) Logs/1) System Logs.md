# Linux - Logs - System Logs

- Log files contain messages about the system 
- Messages may be logged by
    - The kernel 
    - System services
    - Applications
- syslog / rsyslog / syslog-ng / newsyslog
    - System services send their log events to a syslog daemon
    - The syslog daemon processes those events and sends them to the proper log file or log server, based on its configuration
    - /etc/rsyslog.conf 
        - Configuration for which messages are logged where they are sent

---

> ## **/var/log**
- Holds most system logs 
    - The convention is to log here, but it’s not a hard and fast rule
- Many log files are only accessible by root
---

> ## **/var/log/messages**
- General system activity log 
---

> ## **/var/log/dmesg**
- On boot, information about the kernel booting and the devices the kernel has found are logged here
- Viewed using the dmesg command

---

> ## **/var/log/anaconda.log**
- Linux installation related logs
---

> ## **/var/log/kern.log**
- Contains kernel logs
---

> ## **/var/log/maillog**
- Contains the system’s mail server logs
---

> ## **/var/log/secure**
- Contains information related to authentication and authorization privileges
---

> ## **/var/log/boot.log**
- Contains system boot logs
---

> ## **/var/log/cups**
- Contains printer and printing logs
---

> ## **/var/log/yum.log**
- Contains log entries related to package installation/removal using the `yum` command
---

> ## **/var/log/cron**
- Whenever crond (or anacron) starts a cron job, it creates a log entry about the cron job here
