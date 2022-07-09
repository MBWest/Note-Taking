# logrotate

- Rotate compress and mail log files 
- Automated way to manage log files

> ## **Config File**
- `/etc/logrotate.conf`


---

> ## **Example**

**Example lorotate.conf**
- `weekly`
- `rotate 4`
- `create`
- `compress`
- `include /etc/logrotate.d`

| **Command**   | **Description**   |
| --------------|-------------------|
| `logrotate -fv /etc/logrotate.conf` |
| `-f` | Force the rotation |
| `-v` | Verbose logging |