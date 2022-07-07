# Linux System Information - Gather System Information

> ## **hostname [OPTION] [hostname]**
- Show or set the system's hostname

```
[guru@CentOS ~]$ hostname
anakin.skywalker.com

[guru@CentOS ~]$ sudo hostname darth.vader.com

[guru@CentOS ~]$ hostname
darth.vader.com
```

---

> ## **uname [OPTION]...**
- Print certain system information
- Kernel name, release version, and kernel version
- Operating system, processor type, hardware platform, hostname

```
[guru@CentOS ~]$ uname
Linux

[guru@CentOS ~]$ uname -a
Linux Station1.1B4OSANDARCH.com 2.6.32-358.el6.x86_64 #1 SMP Fri Feb 22 00:31:26 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux

[guru@CentOS ~]$ uname -r
2.6.32-358.el6.x86_64
```

---

> ## **date [OPTION]... [+FORMAT]**
- Display current time in the given FORMAT, or set the system date
- FORMAT sequences
    - `%A`- full weekday name (e.g., Sunday)
    - `%B`- full month name (e.g., January)
    - `%d`- day of the month (e.g., 01)
    - `%Y`- year

```
[guru@CentOS ~]# date
Fri Jan 13 18:29:05 UTC 2017

[guru@CentOS ~]# date "+%A, %B %d"
Friday, January 13

[guru@CentOS ~]# date "+%A, %B %d %Y @ %H:%M"
Friday, January 13 2017 @ 18:33
```

---

> ## **Shell Variables**
- Variables contained exclusively within the shell in which they were set
    - Implemented as strings that represent key-value pairs
- Often used to keep track of ephemeral data (cwd etc…)
- Set using `KEY=VALUE` syntax

```
[guru@CentOS ~]$ STUDENT_ONE=Larry

[guru@CentOS ~]$ STUDENT_TWO=Moe

[guru@CentOS ~]$ STUDENT_THREE=Curly
```

---

> ## **set [option] [arg ...]**
- Set or unset values of shell options and positional parameters, or display the names and values of shell variables
- Alternatively, use `echo` to view a single variable

```
[guru@CentOS ~]$ STUDENT_ONE=Larry

[guru@CentOS ~]$ set
... LONG LIST OF VARIABLES ... 

STUDENT_ONE=Larry
... STILL MORE VARIABLES ... 

[guru@CentOS ~]$ echo $STUDENT_ONE
Larry
```

---

> ## **unset [-f] [-v] [name ...]**
- Unset values and attributes of shell variables and functions

```
[guru@CentOS ~]$ STUDENT_ONE=Larry

[guru@CentOS ~]$ set
... LONG LIST OF VARIABLES ... 
STUDENT_ONE=Larry
... STILL MORE VARIABLES ... 

[guru@CentOS ~]$ unset STUDENT_ONE

[guru@CentOS ~]$ set
... LONG LIST OF VARIABLES (but no STUDENT_ONE) ... 

[guru@CentOS ~]$ echo $STUDENT_ONE
```

---

> ## **Environment Variables**
- Defined for the current shell and are inherited by any child shells or processes
- Used to pass information into processes that are spawned from the shell
- Set using the `export` and `env` commands

```
[guru@CentOS ~]$ STUDENT_ONE=Larry

[guru@CentOS ~]$ export STUDENT_ONE

[guru@CentOS ~]$ export STUDENT_TWO=Moe

[guru@CentOS ~]$ env STUDENT_THREE=Curly bash
```

---

> ## **env [OPTION]... [NAME=VALUE]... [COMMAND [ARG]...]**
- Run a program in a modified environment
- env when run without arguments, prints all environment variables; it does not alter your current environment 
- Alternatively, can print single variables with printenv

```
[guru@CentOS ~]$ export STUDENT_ONE=Larry

[guru@CentOS ~]$ env 
... LONG LIST OF VARIABLES ... 
STUDENT_ONE=Larry
... STILL MORE VARIABLES ... 

[guru@CentOS ~]$ printenv STUDENT_ONE
Larry
```

---

> ## **export [-fn] [name[=value] ...]**
- Set export attribute for shell variables
- Makes each name available to the environment of subsequently executed commands

```
[guru@CentOS ~]$ export STUDENT_ONE=Larry

[guru@CentOS ~]$ export 
... LONG LIST OF VARIABLES ... 
declare -x STUDENT_ONE="Larry"
... STILL MORE VARIABLES ... 
```