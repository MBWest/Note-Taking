# SQL Injection

## Description

In this lab you can practice the SQL Injection techniques and tools studied during the
course. You can access the target web application at the following address **10.124.211.96**.

## Goal

The goal of this lab is to test the web application in order to find all the vulnerable injection
points. Once you find them, you should be able to dump all the data and successfully log
into the web application.

## Tools

**The best tools for this lab are:**

- Web Browser
- SQL map

# Solutions

### Step 1 - Explore the web application

In order to explore the web application we just need to type the IP address in our browser.

Now that we are able to access it, let us navigate the application in order to find all the possible injection points.

Right now, we do not know any working credential, so if we login we will get a messages similar to the following:

![SQL%20Inject%20ca670/Untitled.png](SQL%20Inject%20ca670/Untitled.png)

If we keep digging the application, we can see a very interesting page at the following address: **http://10.124.211.96/news.php.**

Here we have a list of news and by clicking on any of the links listed, we can see a very interesting page:

![SQL%20Inject%20ca670/Untitled%201.png](SQL%20Inject%20ca670/Untitled%201.png)

As you can see in the address bar of our browser, it seems that the application accepts a parameter (**id**). This is probably used to retrieve the news from a database.

Let’s then use this injection point for our tests!

### Step 2 - Test and Exploit the injection points

The first test we can run against the page found in the previous step is the following:

![SQL%20Inject%20ca670/Untitled%202.png](SQL%20Inject%20ca670/Untitled%202.png)

We just added a single quote in the address bar, and as shown in the screenshot above, we obtained a *mysql error*. It is time to get our hands dirty! Let us create few payloads in order to test if the parameter is vulnerable to SQL Injections.

We want to test it against Boolean conditions, so let us use the following payload:

```jsx
10.124.211.96/newsdetails.php?id=26 and 1=1; -- -
```

![SQL%20Inject%20ca670/Untitled%203.png](SQL%20Inject%20ca670/Untitled%203.png)

Then let us try with the following payload *(we changed the Boolean condition from 1=1 to 1=2):*

```jsx
10.124.211.96/newsdetails.php?id=26 and 1=2; -- -
```

![SQL%20Inject%20ca670/Untitled%204.png](SQL%20Inject%20ca670/Untitled%204.png)

As we can see from the previous two screenshots, we obtain two different results. When the condition is true, the application returns the news. With a false condition the page returns no content. This means that the parameter is vulnerable to SQL Injection!

### Step 3 - Dump the Data

Now that we know a vulnerable injection point, let us use **sqlmap** to exploit it and retrieve all the data from the application database:

```jsx
sqlmap -u http://10.124.211.96/newsdetails.php?id=1
```

![SQL%20Inject%20ca670/Untitled%205.png](SQL%20Inject%20ca670/Untitled%205.png)

As we can see from the previous screenshot, sqlmap identifies the parameter as vulnerable! Now we just have to get the structure of the database and dump the data.

First, let us get a list of tables:

```jsx
sqlmap -u http://10.124.211.96/newsdetails.php?id=1 --tables
```

![SQL%20Inject%20ca670/Untitled%206.png](SQL%20Inject%20ca670/Untitled%206.png)

Then dump all the data from the accounts table with the following command:

```jsx
sqlmap -u http://10.124.211.96/newsdetails.php?id=1 -D awd -T accounts --dump
```

![SQL%20Inject%20ca670/Untitled%207.png](SQL%20Inject%20ca670/Untitled%207.png)

As we can see, we now have a list of usernames and password to use in order to log into the web application! Let us try one of these:

![SQL%20Inject%20ca670/Untitled%208.png](SQL%20Inject%20ca670/Untitled%208.png)

Great, we successfully logged into the web application!

### Step 4 - Login without using any credential

Until now, we focused our tests against the newsdetails.php page and its parameter, but the
web application has one more injection point to test: the login form!

Let us run some tests and see if we are able to bypass the login! To do this we will use the
following payload:

```jsx
' or 1=1; -- -
```

![SQL%20Inject%20ca670/Untitled%209.png](SQL%20Inject%20ca670/Untitled%209.png)

As we can see the form is vulnerable too, indeed the “*Welcome*!” message appears!