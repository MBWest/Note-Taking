# Streams, Pipes, Expansion, and Redirects -  Expansion

> ## **Expansion (Globbing)**

### **Resource**

| **Resource**   | **Website**   |
| --------------|-------------------|
| `Bash manual chapter on shell expansions` | https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Expansions |

### **Expansions** 

| **Expression**   | **Description**   |
| --------------|-------------------|
| **Expansion** |
| `*` | Represents zero or more characters in a filename |
| `?` | Represent one character in a filename |
| `[A-Z]` | Represents a range of characters in a filename ([A-Z], [a-z], [0-9], [a-zA-Z]) |
| `[^A-Z]` | Represents a range of characters to **NOT** match ([^A-Z], [^a-z], [^0-9]) |

---

> ## **Pathname Expansion (*)**

| **Example**   | **Description**   |
| --------------|-------------------|
| **Pathname Expansion (*)** |
| `echo press * to speak to operator` | The **(*)** will be replaced by all files that are in the current directory |
| `ls *html` | Matches any files that end with .html |
| `cat blue` | Matches any files that start with "blue" |
| `ls **/*.txt` |Searches the current directory and all sub directories for a file that matches the *.txt pattern; If this command doesnt run you need to set the following command `shopt -s globstar` |

---

> ## **Brace Expansion {}**

- `[preamble]{string1,string2}[postscript]`
- Generate arbitrary strings
- preamble is prefixed to each string contained within the braces, while the postscript is then appended to each resulting string

| **Example**   | **Description**   |
| --------------|-------------------|
| **ExpanBrace Expansion {}** |
| `touch page{1,2,3}.txt` | Generates three new files: page1.txt, page2.txt, page3.txt |
| `touch page{1..3}.txt` | Generates three new files: page1.txt, page2.txt, page3.txt |
| `touch page{2..10..2}` | Generates five new files: page2.txt, page4.txt, page6.txt, page8.txt, page10.txt |
| `touch page{A..E}` | Generates five new files: pageA.txt, pageB.txt, pageC.txt, pageD.txt, pageE.txt |

```
[guru@CentOS ~]$ mkdir ~/{dev,prod,staging}

[guru@CentOS ~]$ ls -ld ~/{dev,prod,staging}
drwxrwxr-x 2 guru guru 4096 Jan  1 13:14 /home/guru/dev
drwxrwxr-x 2 guru guru 4096 Jan  1 13:14 /home/guru/prod
drwxrwxr-x 2 guru guru 4096 Jan  1 13:14 /home/guru/staging

[guru@CentOS ~]$ ls /var/log/{last,mail,tally}log
/var/log/lastlog  /var/log/maillog  /var/log/tallylog
```

---

> ## **Single and Double Quoting**

- **Double quotes** `" "`
    - All characters will be literal characters except:
    - `$` - introduces expansion
    - `\`` - (back-tick) introduces command substitution
    - `\` - removes the special meaning of the character following it
    - `"` - closes the quoted string, unless escaped 
    - `!` - introduces history expansion (must be enabled)
- **Single quotes** `' '`
    - No characters have special meaning except the closing single quote

If you wrap text in a double quote `("wrapped")`, the shell will respect spacing and ignore special characters except: Dollar Sign ($), backslash (\), and backtick (`).

If you wrap text in a single quote `('wrapped')` you will suppress all forms of subsitution. 

---

> ## **Escape Character (\)**

- Removes the special meaning of the character following it
- Escape Sequences - produced using the escape character
    - `\n` – newline
    - `\t` - horizontal tab
    - `\v` - vertical tab
    - `\r` - carriage return
    - `\\` - backslash

```
[guru@CentOS ~]$ echo -e "City\tState\vZip Code\nBeverly Hills\tCA\v90210"
City	State
        	Zip Code
Beverly Hills	CA
                 90210
```

---

> ## **Command Substitution**

- $(command) or \`command\`
- You can use the **$(command)** syntax to dispay the output of another command
- Executes command and replaces command with the STDOUT of command, with any trailing newlines deleted
- Multiple substitutions may be nested

| **Example**   | **Description**   |
| --------------|-------------------|
| **Command Subsitution $()** |
| `echo "today is $(date)"` | This will echo out to the terminal "today is Thu 01 May 2021 03:10:31 PM PDT"; You can use the `command` syntax to dispay the output of another command. |
| `echo today is 'date'` | This will echo out to the terminal "today is Thu 01 May 2021 03:10:31 PM PDT". |
| `ls -l 'cat file-list.txt'` | The shell will execute what is inside the back ticks (`) first and send that output to the command outside the back ticks (This is the same as the **$(command)**) | 

```
[guru@CentOS ~]$ echo This system is running $(uname -sr)
This system is running Linux 2.6.32-642.11.1.el6.i686

[guru@CentOS ~]$ LOGFILES=$(ls /var/log)

[guru@CentOS ~]$ echo $LOGFILES
audit boot.log btmp btmp-20170101 cloud-init.log cloud-init-output.log cron cron-20170101 dmesg dmesg.old dracut.log lastlog maillog maillog-20170101 messages messages-20170101 secure secure-20170101 spooler spooler-20170101 tallylog wtmp yum.log yum.log-20170101
```

### **Resources**

| **Resource**   | **Website**   |
| --------------|-------------------|
| `Bash manual section on command substitution` | https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html |

---

> ## **Arithmetic Expansion**

The shell will perform arithmetic via expansion using the **$((expression))** syntax. Inside the parentheses the user can write artithmetic expression using:

| **Expression**   | **Description**   |
| --------------|-------------------|
| **Arthmetic Expansion** |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Exponentiation |
| `%` | Modulo |
| **Example** |
| `(echo $((10+7)))` | 
---

> ## **Tilde Expansion**

| **Expression**   | **Description**   |
| --------------|-------------------|
| **Tilde Expansion** |
| `echo ~` | Returns the current users home directory |
| `echo ~User` |Returns the specific users home directory |

---

> ## **Parameter Expansion**

- `${parameter}`
- The value of parameter is substituted

```
[guru@CentOS ~]$ STUDENT=First.Last

[guru@CentOS ~]$ echo $STUDENT
First.Last
```

---

> ## **Substring Expansion**
- `${parameter:offset:length}`
- Expands up to length characters of parameter starting at the character specified by offset.
    - **offset** 
        - offset < 0? The negative value is used as an offset from the end of parameter
        - Indexing for the offset starts at 0
        - Must be separated from the colon by at least 1 space
            - No space means you are using default value syntax
    - **length** - must be a number >= 0
        - No length? Will return parameter starting at offset


|**F**|**i**|**r**|**s**|**t**|**.**|**L**|**a**|**s**|**t**|
|-|-|-|-|-|-|-|-|-|-|
|0|1|2|3|4|5|6|7|8|9|
|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

```
[guru@CentOS ~]$ STUDENT=First.Last

[guru@CentOS ~]$ echo ${STUDENT:3}
st.Last

[guru@CentOS ~]$ echo ${STUDENT:3:1}
s

[guru@CentOS ~]$ echo ${STUDENT:3:2}
st

[guru@CentOS ~]$ echo ${STUDENT:3:5}
st.La

[guru@CentOS ~]$ echo ${STUDENT:0:5}
First

[guru@CentOS ~]$ echo ${STUDENT::5}
First

[guru@CentOS ~]$ echo ${STUDENT: -4}
Last

[guru@CentOS ~]$ echo ${STUDENT: -4:4}
Last

[guru@CentOS ~]$ echo ${STUDENT: -5:4}
.Las

[guru@CentOS ~]$ echo ${STUDENT:-4:3}
First.Last

[guru@CentOS ~]$ echo ${STUDENT: -4:3}
Las
```

---



