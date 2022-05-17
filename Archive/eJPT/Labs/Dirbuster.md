# Dirbuster

### Description

You are a Penetration Tester hired by the company AwdMgmt to perform security tests on
their internal Web Application and machines. You are asked to perform the penetration
test on the client premises. During this engagement you are not given a well-defined scope.
You are sitting in the client corporate building, directly attached to the client network.

![Dirbuster%202b0cb/Untitled.png](Dirbuster%202b0cb/Untitled.png)

### Goal

The goal of this lab is to first find the web servers in the network you are directly attached.
Then to test the Web Application running on it in order to check if you can access restricted
areas (such as the login page)!

### Tools

The best tools for this lab are:
• [DirBuster ](https://www.notion.so/DirBuster-48f78f7c57e242ec9b7a90517b4f92b1) 
• [SQL / Ms-SQL ](https://www.notion.so/SQL-Ms-SQL-bae7741259c140a1ad280193f8f86730) 
• Web browser

# Solutions

### Step 1 - Find all the machines in the network

We first need to find the address of the corporate network we are connected to. We can do so by running *ifconfig* and check the IP address of tap0 interface.

![Dirbuster%202b0cb/Untitled%201.png](Dirbuster%202b0cb/Untitled%201.png)

As we can see the target network is 10.104.11.0/24.

**To discover all the available host on the network you can run nmap:**

```jsx
nmap -sn 10.104.11.0/24
```

![Dirbuster%202b0cb/Untitled%202.png](Dirbuster%202b0cb/Untitled%202.png)

The previous screenshot shows that there are two hosts alive in the network:

- 10.104.11.96
- 10.104.11.198

### Step 2 - Identify the machines role

Lets run nmap in order to gather information about the services listening on our targets. To do this we will run a **-sV** scan as follows:

![Dirbuster%202b0cb/Untitled%203.png](Dirbuster%202b0cb/Untitled%203.png)

**Gathered information:**

- 10.104.11.96 is running **Apache** on port 80 (potential web application)
- 10.104.11.198 is running **MySQL**

Since the scope of the engagement is to check if an attacker can access restricted areas of
the web application, let’s focus our tests on the machine **10.104.11.96**

### Step 3 - Explore the web application

Type **10.104.11.96** into the browser. Notes taken:

- We can not access the *Sign up* page
- We do not have valid credentials
- the form seems not vulnerable to any SQL injection attack

### Step 4 - Find hidden files

Since we do not want to brute force the login form, we can try to run discovery tools such as *dirbuster* in order to find hidden files that may help us with our goal.

![Dirbuster%202b0cb/Untitled%204.png](Dirbuster%202b0cb/Untitled%204.png)

**Start Dirbuster and run a scan using the *directory-list-2.3.-small.txt file.*** 

![Dirbuster%202b0cb/Untitled%205.png](Dirbuster%202b0cb/Untitled%205.png)

**Findings:**

- In the *Include* folder there is a file name *config.old* (inspect this file)

![This file contains some database credentials!](Dirbuster%202b0cb/Untitled%206.png)

This file contains some database credentials!

**Try to connect to the DB machine using the credentials found:**

![Dirbuster%202b0cb/Untitled%207.png](Dirbuster%202b0cb/Untitled%207.png)

Unfortunately, it seems that the credentials are not working. Let us keep investigating the
files found with dirbuster. If we check the previous screenshot, we can see that there is a
page named signup.php that we were not able to access from the links in the web
application:

![This is even better than the previous file found!](Dirbuster%202b0cb/Untitled%208.png)

This is even better than the previous file found!

### Step 5 - Test the credentials found

Try the credentials found in the *signup.php* file and see if we are able to access the DB. 

![This time we are successfully logged into the database!](Dirbuster%202b0cb/Untitled%209.png)

This time we are successfully logged into the database!

### Step 6 - Retrieve the correct admin password

Let us use some simple *mysql* commands to navigate the database and check if there is
anything interesting in it. First, we will have to select the database to use and then inspect
its tables and data:

![Dirbuster%202b0cb/Untitled%2010.png](Dirbuster%202b0cb/Untitled%2010.png)

With the information just obtained, let us try to log into the web application:

![Dirbuster%202b0cb/Untitled%2011.png](Dirbuster%202b0cb/Untitled%2011.png)