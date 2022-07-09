# Linux -  Bash Scripting 


> ## **Bash Basics**

- A bash script is a file that contains a series of commands
- Anything you can run through the CLI can be put into a script
- Bash scripts end in .sh by convention
- Bash scripts may begin with a shebang line
    - `#!/bin/bash`
    - Defines the interpreter to be used to run the rest of the script
    - If omitted, the script can be passed as an argument to the appropriate interpreter
- Comment out lines by placing the `#` character at the beginning of the line

---

> ## **Executing a Bash Script**

- To execute a bash script, you should set the execute bit

```
[root@CentOS ~]# cat > today.sh
#!/bin/bash
date "+%F"

[root@CentOS ~]# chmod 755 today.sh 

[root@CentOS ~]# ./today.sh 
2017-02-10

[root@CentOS ~]# bash today.sh 
2017-02-10
```

---

> ## **Variables**

- Variables are used to store a value and later read back or modify the value
- Values are assigned to variables using the `=` character
- There cannot be whitespace on either side of the `=` 
- Values are accessed with the `$`character 


- By convention variables are uppercase and cannot start with a digit. Not can the name contain symbolbs such as "-" or "@"

To define a variable, use the syntax `VARIABLE_NAME="value"`
	- To make a variable a global variable, prefix the variable with **export**, `export VARIABLE_NAME="value"`

To test a varaible you can put a dollarsign in front of the variable name using the echo command...`echo "I like my new $VARIABLE_NAME"` or  `echo "I like my new ${VARIABLE_NAME}"`

To assign a command to a variable, use the syntax `SERVER_NAME=$(hostname)`

To test a varaible you can put a dollarsign in front of the variable name using the echo command...`echo "You are running this script on $SERVER_NAME"` or  `echo "You are running this script on ${SERVER_NAME}"`

```
[root@CentOS ~]# cat > variables.sh
name=yoda
echo "$name"
echo name
rank = master

[root@CentOS ~]# ./variables.sh 
yoda
name
./variables.sh: line 4: rank: command not found
```