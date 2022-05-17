## Gobuster

So Let’s first enumerate port 80 using `gobuster`. 

`gobuster dir -x php,txt,html,bak,zip -e -t 100 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u [IP]/[directory]`

