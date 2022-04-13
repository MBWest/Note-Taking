# sudo 

Execute a command as another user

## Format

     sudo -h | -K | -k | -V
     sudo -v [-ABknS] [-g group] [-h host] [-p prompt] [-u user]
     sudo -l [-ABknS] [-g group] [-h host] [-p prompt] [-U user]
          [-u user] [command]
     sudo [-ABbEHnPS] [-C num] [-D directory] [-g group] [-h host]
          [-p prompt] [-R directory] [-T timeout] [-u user] [VAR=value]
          [-i | -s] [command]
     sudoedit [-ABknS] [-C num] [-D directory] [-g group] [-h host]
          [-p prompt] [-R directory] [-T timeout] [-u user] file ...o 

## Examples

| **Command**   | **Description**   | 
| --------------|-------------------|
| **Examples** |
| `sudo` | Execute a command as another user or root |
| `sudo -l` | Shows all commands that the current user can run as the super user |
| `sudo su -` | Switch to root user for this instance |
| `sudo -u sally cat /home/sally/sample.txt` | Allows the current user to read the sample.txt as the user sally |