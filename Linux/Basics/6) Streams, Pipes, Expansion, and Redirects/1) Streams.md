# Streams, Pipes, Expansion, and Redirects - Streams

> ## **grep [OPTIONS] PATTERN [FILE...] || grep [OPTIONS] [-e PATTERN|-f FILE] [FILE...]**
- Search FILE(s) or STDIN if no FILE(s) are named for lines containing a match to the given PATTERN
- `-i` - ignore case
- `-v` - invert match; to select non-matching lines
- `-r` or `-R` - read all files under each directory

```
[guru@CentOS ~]$ grep guru /etc/group
guru:x:500:

[guru@CentOS ~]$ cat /etc/group | grep guru
guru:x:500:
```

---

> ## **wc [OPTION]... [FILE]...**
- Print newline, word, and byte counts for each FILE
- `-c` - display byte count
- `-l` - display line count
- `-L` - display length of longest line
- `-w` - display the word count

```
[guru@CentOS yum-3.2.29]$ wc README 
  35  136 1078 README

[guru@CentOS yum-3.2.29]$ wc -l README 
35 README

[guru@CentOS yum-3.2.29]$ wc -L README 
74 README

[guru@CentOS yum-3.2.29]$ cat README | wc -L 
74
```

---
> ## **sort [OPTION]... [FILE]...**
- Write sorted concatenation of all FILE(s) to STDOUT
- `-r` - reverse the result of comparisons
- `-u` - sort and display only one occurrence of repeated lines
- `-M` - compare months ( unknown < JAN < … < DEC )

```
[guru@CentOS yum-3.2.29]$ sort /etc/group | head -n 3
adm:x:4:adm,daemon
audio:x:63:
bin:x:1:bin,daemon

[guru@CentOS yum-3.2.29]$ head -n 3 /etc/group | sort
bin:x:1:bin,daemon
daemon:x:2:bin,daemon
root:x:0:
```

---

> ## **tr [options]... set1 [set2]**
- Performs substitution or deletion of selected characters
- With no options, tr will replace characters in set1 with characters in the same position in set2
- `-d` – used to remove particular characters
- `-cd` – remove all except for specified characters
- `-s` – squeeze repetition of characters

```
[guru@CentOS ~]$ echo –e It\'s a trap\! | tr a-z A-Z
IT'S A TRAP!

[guru@CentOS ~]$ echo "C3PO is talking to R2D2" | tr –d [:digit:]
CPO is talking to RD

[guru@CentOS ~]$ echo "C3PO is talking to R2D2" | tr –cd [:digit:]
322

[guru@CentOS ~]$ echo "Perhaps A Special Squadron of Warriors should Organize and Rally to Defend" | tr -cd [:upper:]
PASSWORD

[guru@CentOS ~]$ echo "Chewbacca replied WWWRRRRRRRRGWWWWRRRR" | tr –s RW
Chewbacca replied WRGWR

[guru@CentOS ~]$ ps -ef | grep flag
student  26182 24129  0  19:57  pts/0      00:00:00   grep flag

[guru@CentOS ~]$ ps -ef | grep flag | tr -s ' '
student 26182 24129 0 19:57 pts/0 00:00:00 grep flag

[guru@CentOS ~]$ ps -ef | grep flag | tr -s ' ' | cut -d ' ' -f 2,8
26182 grep

```

---

> ## **cut [OPTION]... [FILE]...**
- Print selected parts of lines from each FILE to STDOUT
- `-d DELIM` - use DELIM instead of TAB for field delimiter
- `-f LIST`  - select only these fields

```
[guru@CentOS ~]$ cut -d : -f 1 /etc/passwd | head -n 3
root
bin
daemon

[guru@CentOS ~]$ cut -d : -f 1,3,6 /etc/passwd | head -n 5
root:0:/root
bin:1:/bin
daemon:2:/sbin
adm:3:/var/adm
lp:4:/var/spool/lpd
```

---

> ## **paste [OPTION]... [FILE]...**
- Write lines consisting of sequentially corresponding lines from each FILE, separated by TABs, to STDOUT
- `-d LIST` - reuse characters from LIST instead of TABs

```
[guru@CentOS ~]$ cat file1
cat
dog

[guru@CentOS ~]$ cat file2
meow
woof

[guru@CentOS ~]$ paste file1 file2
cat	meow
dog	woof

[guru@CentOS ~]$ paste file1 file2 file1
cat	meow	 cat
dog	woof	 dog

[guru@CentOS ~]$ paste file1 file2 file1 -d :
cat:meow:cat
dog:woof:dog

[guru@CentOS ~]$ paste file1 file2 file1 -d :,
cat:meow,cat
dog:woof,dog

[guru@CentOS ~]$ paste -s file1 file2 -d -
cat-dog
meow-woof
```

---

> ## **xargs [OPTION]... [command [intial-args]]**
- Reads items from STDIN and executes command one or more times with any initial-args followed by items read from STDIN
 - Default command is echo
- `-I STR` - replace occurrences of STR w/ names from STDIN

```
[guru@CentOS ~]# cut -d: -f1 < /etc/passwd | sort | xargs 
adm bin chewie daemon dbus ftp games gopher guru halt lp mail nobody operator palpatine postfix princessleia r2-d2 root saslauth shutdown sshd 

[guru@CentOS ~]$ sudo find /var/log -type f
/var/log/messages
/var/log/secure
/var/log/audit/audit.log
... LONG LIST OF FILES ...

[root@CentOS ~]# find /var/log | xargs grep passwd
/var/log/secure:Jan  7 11:48:59 CentOS passwd: password changed for chewbacca
/var/log/audit/audit.log:type=USER_CHAUTHTOK pid=28889 msg=audit(1483789739.816:211108): acct="chewbacca" exe="/usr/bin/passwd" res=success

[root@CentOS ~]# cut -d : -f 1 /etc/passwd | xargs -I user crontab -l -u user
no crontab for root
no crontab for bin
no crontab for daemon
... CRONTAB LISTING FOR EACH USER ...
no crontab for chewie
no crontab for r2-d2
no crontab for princessleia
no crontab for palpatine
```

---

> ## **cat using streams**
- - - display STDIN, used when piping to cat
- > or >> FILE - create new files or append to existing files with specified text
- When finished, use ^D on a line by itself
    - ^D is the End of File (EOF) special control character
        - If used on a line by itself, it will signify the end of the transmission and close the stream
        - If used on a line with text that has not been sent by pressing the ENTER key, it will send that text to the file
            - A second ^D will close the stream

```
[guru@CentOS ~]$ cat > stuff 
things

[guru@CentOS ~]$ cat stuff 
things

[guru@CentOS ~]$ cat >> stuff  
stuff
or
something

[guru@CentOS ~]$ cat stuff 
things
andstuff
or
something
```