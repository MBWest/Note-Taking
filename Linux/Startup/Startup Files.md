# Startup Files

## Login Session

| **File**   | **Description**   |
| --------------|-------------------|
| **Login Sessions** |
| `/etc/profile` | Global config for all users. |
| `~/.bash_profile` | user's personal config file. |
| `~/.bash_login` | read if bash_profile isn't found. |
| `~/.profile` | used if previous two aren't found. |
| **Non-login Session (ypical session when you launch the terminal via the GUI)** |
| `etc/bash.bashrc` | Global config for all users. |
| `~/.bashrc` | Specific settings for each user. This is where you can define your own settings and configurations. |
| **Resources** |
| `Bash manual chapter on startup files` | https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html |
