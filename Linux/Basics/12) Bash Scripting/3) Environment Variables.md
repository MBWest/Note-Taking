# Linux - Bash Scripting - Environment Variables

> ## **Two Types of Environment Variables**

## **Global (Environment Variables)**

- Can be accessed by anything executing in that shell

#### **Create Variable**

- **export COUNT_GLOBAL=55** - Create global variable with the value 55
    - Check if variable was set using `echo $COUNT_GLOBAL`

## **Local (Shell Variables)**

- Can only be accessed by the local shell

#### **Create Variable**

- **COUNT_LOCAL=42** - Create local variable with the value 42
    - Check if variable was set using `echo $COUNT_LOCAL`

---

> ## **printenv Command**

- **printev** - See the variables in current shell

### **Format**

`VARIABLE=Value`
- Variables by default are all UPPERCASE

### **PATH**

- List of directories that are searched, in order, to find commands that are to be executed
    - The shell first checks if the command is a built in command then searches the PATH

> ## **Unset a Variable**

- **unset COUNT_GLOBAL** - Removes the COUNT_GLOBAL variable