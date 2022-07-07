# Linux Process and Service Management - systemctl


> ## **systemctl [OPTIONS...] COMMAND [NAME...]**
- Control the systemd system and service manager 
- Common COMMANDs:
    - `status` – provides a wealth of information about the unit
    - `start` – start the unit
    - `stop` – stop the unit 
    - `enable` – set the unit to run at system startup
    - `disable` – set the unit to not run at system startup 
    - `is-enabled` – reports if the unit is enabled or not
    - `is-active` – reports if the unit is running or not
    - `list-unit-files` – provides a list of all units (includes inactive, disabled, etc)

```
[root@wkstn ~]# systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2015-01-27 19:41:23 EST; 22h ago
 Main PID: 495 (nginx)
   CGroup: /system.slice/nginx.service
           ├─495 nginx: master process /usr/bin/nginx -g pid /run/nginx.pid; error_log stderr;
           └─496 nginx: worker process
Jan 27 19:41:23 desktop systemd[1]: Starting A high performance web server and a reverse proxy server...
Jan 27 19:41:23 desktop systemd[1]: Started A high performance web server and a reverse proxy server.

[root@wkstn ~]# systemctl is-enabled nginx
enabled

[root@wkstn ~]# systemctl is-active nginx
active

[root@wkstn ~]# systemctl stop nginx

[root@wkstn ~]# systemctl is-active nginx
inactive

[root@wkstn ~]# systemctl disable nginx
Removed symlink /etc/systemd/system/multi-user.target.wants/nginx.service 

[root@wkstn ~]# systemctl is-enabled nginx
disabled
```