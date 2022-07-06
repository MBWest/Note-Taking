# Variables

- By convention variables are uppercase and cannot start with a digit. Not can the name contain symbolbs such as "-" or "@"

To define a variable, use the syntax `VARIABLE_NAME="value"`
	- To make a variable a global variable, prefix the variable with **export**, `export VARIABLE_NAME="value"`

To test a varaible you can put a dollarsign in front of the variable name using the echo command...`echo "I like my new $VARIABLE_NAME"` or  `echo "I like my new ${VARIABLE_NAME}"`

---

To assign a command to a variable, use the syntax `SERVER_NAME=$(hostname)`

To test a varaible you can put a dollarsign in front of the variable name using the echo command...`echo "You are runnin this script on $SERVER_NAME"` or  `echo "You are runnin this script on ${SERVER_NAME}"`