# Burp Suite

# Description

A local police department has hired you to pentest their website. They had a new website created by a web development company and they want to make sure that everything is secure and in order.
In this lab you will practice with Burp Suite, configuring the scope of the engagement, intercepting the communications with a webserver and spidering a target web application. You can access the target web application at the following address **10.100.13.5**. 

# Goal

The goal of this lab is to test the given web application in order to find a hidden path that contains a restricted area. Once the hidden path is discovered, your goal will be to bypass the authentication exploiting a “**feature**” left over by the developers while “debugging” the area. 

# Tools

The best tools for this lab are

- Web browser
- Burp Suite

# Solution

### Step 1 - Explore the web application

You should see a page like this:

![Burp%20Suite%20e607a/Untitled.png](Burp%20Suite%20e607a/Untitled.png)

Welcome to Foo Police Department!

### Step 2 - Configuring your arsenal

In order to analyze the traffic, spider the targeted web application and discover the hidden path of the restricted area. You need to setup the proxy both in your browser and in Burp Proxy. 

***In your browser***

![Burp%20Suite%20e607a/Untitled%201.png](Burp%20Suite%20e607a/Untitled%201.png)

**In Burp Proxy**

![Burp%20Suite%20e607a/Untitled%202.png](Burp%20Suite%20e607a/Untitled%202.png)

In addition to the listener, it’s a best practice to configure the proxy to intercept request and responses that belongs to the **targets in scope:**

![Burp%20Suite%20e607a/Untitled%203.png](Burp%20Suite%20e607a/Untitled%203.png)

To configure the scope of engagement browse the tab **Target** and then **Scope**. To add a URL to the scope you can paste the link or type it manually. 

![Burp%20Suite%20e607a/Untitled%204.png](Burp%20Suite%20e607a/Untitled%204.png)

In latest version of Burp Suite, you will need to click the “Use advanced scope control” checkbox before you can specify the scope in that form, as shown in the screenshots below: 

![Burp%20Suite%20e607a/Untitled%205.png](Burp%20Suite%20e607a/Untitled%205.png)

In the **site map**, configure the filter by request type adding a tick to “Show only in-scope items”. This will show you only the resources that belong to the scope defined previously. 

![Burp%20Suite%20e607a/Untitled%206.png](Burp%20Suite%20e607a/Untitled%206.png)

To test if your configurations are working as intended, just refresh the link into the browser and verify that the intercept has captured your request. If not, be sure the Intercept button is toggled.

![Burp%20Suite%20e607a/Untitled%207.png](Burp%20Suite%20e607a/Untitled%207.png)

Once forwarded all the requests and responses, you should see the list of the resources exchanged in the *Target* > *Site* *map* tab: 

![Burp%20Suite%20e607a/Untitled%208.png](Burp%20Suite%20e607a/Untitled%208.png)

### Step 3 - Mapping the target application

In order to automatically map the target web application we can use the Burp Spider tool. To do this, just right click on the target host in the site map list. Then select “**Spider this host”:**

![Burp%20Suite%20e607a/Untitled%209.png](Burp%20Suite%20e607a/Untitled%209.png)

In the Spider tab you’ll see the status of this operation:

![Burp%20Suite%20e607a/Untitled%2010.png](Burp%20Suite%20e607a/Untitled%2010.png)

After a while, you should see a list of paths on the **Site** **Map** that were not listed before. One of them is the hidden area we are looking for: 

![Burp%20Suite%20e607a/Untitled%2011.png](Burp%20Suite%20e607a/Untitled%2011.png)

### Step 4 - The keyston

Visiting the *hidden* *path*, you should notice that the application exposes an authentication page. It requires a login and you don’t have one.

![Burp%20Suite%20e607a/Untitled%2012.png](Burp%20Suite%20e607a/Untitled%2012.png)

The next step needs to analyze this page in order to find something useful to bypass the authentication.

Analyzing the server response to the ***login***.php resource, you should have noticed that at the end of the file there is a debugging message. The developers implemented a simple login bypass to avoid the authentication during the debugging operations and forgot to remove the message in production. Requesting the login path with the parameters suggested by the developers: You will access the restricted area and reach the goal of this lab! You also notify your client of your findings and successfully close your engagement.