# logrotate
- rotate compress and mail log files 
- automated way to manage log files

## Config File
- **/etc/logrotate.conf**

**Example lorotate.conf**
- weekly
- rotate 4
- create
- compress
- include /etc/logrotate.d

- *Example* > logrotate -fv /etc/logrotate.conf
    - **-f** - Force the rotation
    - **-v** - Verbose logging