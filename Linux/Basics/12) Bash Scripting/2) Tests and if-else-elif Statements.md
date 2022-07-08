# Linux - Bash Scripting - Tests and if-else-elif Statements


> ## **test [EXPRESSION]**

- Check file types and compare values 
- Returns a status of 0 or 1 depending on the evaluation of the conditional expression EXPRESSION.
- The brackets in the if statements are a synonym for the test command

To create a test use the sytax, `[ conditon-to-test-for ]`
    - Example, `[ -e /etc/passwd]` 

To view what items you can test for use the `man test` command

| `Command` | `Usage`|
|-----------|--------|
| **File Tests**|
| `-d FILE` | True if file is a directory |
| `-e FILE` | True if file exists |
| `-f FILE` | True if file exists and is a regular file |
| `-r FILE` | True if file is readable by you |
| `-s FILE` | True if file exists and is not empty |
| `-w FILE` | True if file is writable by you |
| `-x FILE` | True if file is executable by you | 
| `-z STRING` | True if string is empty |
| `-n STRING` | Trust if string is not empty |
| **String Tests**|
| `STRING1 = STRING2` | True if the strings are equal |
| `STRING1 != STRING2` | True if the strings are not equal |
| **Arithmetic Operators (Tests)**|
| `-eq` | True if arg1 is equal to arg2 |
| `-ne` | True if arg1 is not equal to arg2 |
| `-lt` | True if arg1 is less than arg2 |
| `-le` | True if arg1 is less than or equal to arg2 |
| `-gt` | True if arg1 is more than arg2 |
| `-ge` | True if arg1 is more than or equal to arg2

## **Example**


```
[root@CentOS ~]# test stuff == things

[root@CentOS ~]# echo $?
1

[root@CentOS ~]# test stuff == stuff

[root@CentOS ~]# echo $?
0
```

---
> ## **if Statements**

- If the expression in the if statement is true, then perform a given set of actions.  If the same expression is false, do not perform those actions.


## **Syntax**

```bash
#!/bin/bash

if [ condition-is-true]
then
    command 1
    command 2
    command N
fi
```

## **Example**

```bash
#!/bin/bash
MY_SHELL="bash"

if [ "$MY_SHELL" = "bash"]
then
    echo "You seem to like the bash shell."
fi
```
---

> ## **if/else Statements**

- Perform a set of actions in the event that is no other expression evaluates to true 

## **Syntax**

```bash
#!/bin/bash

if [ condition-is-true]
then
    command N
else
    command N
fi
```

## **Example**

```bash
#!/bin/bash
MY_SHELL="csh"

if [ "$MY_SHELL" = "bash" ]
then
    echo "You seem to like the bash shell."
else
    echo "You don't seem to like the bash shell."
fi
```
---
> ## **if/else/elif Statements**

## **Syntax**

```bash
#!/bin/bash

if [ condition-is-true]
then
    command N
elif [ conditon-is-true ]
    command N
then
    command N
else
    command N
fi
```

## **Example**

```bash
#!/bin/bash
MY_SHELL="csh"

if [ "$MY_SHELL" = "bash" ]
then
    echo "You seem to like the bash shell."
elif [ "$MY_SHELL" = "csh"]
then
    echo "You seem to like the csh shell."
else
    echo "You don't seem to like the bash or csh shells."
fi
```