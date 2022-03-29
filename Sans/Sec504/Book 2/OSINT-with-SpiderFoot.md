# OSINT with SpiderFoot

## Brief Intro

In this lab, you will use SpiderFoot to evaluate data captured for the Counter Hack Challenges website at www.counterhackchallenges.com.
Requirements for This Lab

In this lab, you will use your Windows 10 VM. Make sure the VM is running before continuing with this lab exercise.

## Try It Yourself

Launch SpiderFoot from the desktop icon and evaluate the OSINT data results to identify Counter Hack affiliates, co-hosted websites, email addresses for employees, a hacked email account, and web technology in use.

## Walkthrough

In this lab, you will evaluate the SpiderFoot search results for the target site www.counterhackchallenges.com.

    Counter Hack Challenges is a company founded by Ed Skoudis, where he and his team perform information security consulting services for select customers, develop the NetWars product line for the SANS Institute, and publish the Holiday Hack Challenge every December. 

In this lab, you will use the SpiderFoot search results to identify several key pieces of information, including:

    Service providers and hosting companies that Counter Hack uses
    Three hostnames of websites also associated with the server at counterhack.com
    Three employee email addresses
    One hacked email account
    Web technology in use supporting the www.counterhackchallenges.com site

### Start SpiderFoot

First, launch the SpiderFoot application by double-clicking the Windows Desktop SpiderFoot icon.

    This launcher script will start the SpiderFoot application, then launch the web browser. SpiderFoot is a local, web-based application listening on TCP port 5001. 

### Examine SpiderFoot Search Results

When you run a SpiderFoot OSINT scan for a target site, SpiderFoot saves the search results in a local database file (spiderfoot.db). In the class Windows 10 VM, you will see search results for three targets. We'll focus our analysis on the first target, www.counterhackchallenges.com, but feel free to inspect the other search results as well.

    In the main SpiderFoot page, you will see the start and stop date and time for the different scans. Note that the scan for www.counterhackchallenges.com took 3 hours to complete. We won't be running a new scan today! Instead, we'll focus on getting useful data from the scan results. 

### Select the Counter Hack Scan Result

Click on the Counter Hack link to open the SpiderFoot scan results for this target. SpiderFoot will list the collected data in the Browse view, listing each of the OSINT plugins used to collect data about the target alphabetically, as shown here.

### Select the Status View

Instead of starting with the Browse results view, click on the Status view. This view will show a bar chart of all the plugins used to evaluate the target on the X axis, showing the number of results for each on the Y axis, as shown here.

    You may wish to maximize your VMware window to see more of the scan results at one time without scrolling. 

Scroll through the scan Status page results. Notice that the SpiderFoot scan for Search Engine's Web Content returned the most results, as shown here. This is not terribly surprising, and it's not the most useful plugin that SpiderFoot offers.

Spiderfoot Browse List Search Engine's Web Content Chart Element

Select the Graph View

Return to the top of the browser page and select the SpiderFoot Graph view. SpiderFoot will display a massive spiderweb view of all the search results, as shown here.

### Spiderfoot Graph View

At first glance, this may not seem terribly useful. However, it provides an interface to deduce how SpiderFoot collected information from one plugin and used it to seed another.

For example, the red dot indicates the beginning, or seed, value used to produce the scan results. In this scan, the seed value is www.counterhackchallenges.com, but it could otherwise be a name, email address, or domain name. Linked to the seed value, we see the domain counterhack.com, as well as the email address yori@counterhackchallenges.com, to which many other informational elements are linked.

    Tip: You can click and move any of the dots in the Graph view to move the labels to a location that is more legible. 

Spend a minute browsing through the Graph view and examine the relationships between the SpiderFoot seed value and the other search results. Try and follow a single path, starting from the seed value to the final information element discovered by SpiderFoot.

### Select the Browse View

Next, return to the Browse view to see the list of information elements gathered by SpiderFoot. Each of these elements represents a plugin used by SpiderFoot to collect information.

    To return to the list of SpiderFoot elements, click the Browse button. Clicking the Back button in your browser will bring you back to the main SpiderFoot page. 

Spend a few minutes investigating the different OSINT search results collected by SpiderFoot for the www.counterhackchallenges.com seed value.

### The Challenge

Use the Browse view to answer the following questions about the www.counterhackchallenges.com target:

    Identify the service providers and hosting companies that Counter Hack uses
    Identify three hostnames of websites also associated with the server at counterhack.com
    Identify three Counter Hack employee email addresses
    Identify the email address of a hacked email account
    Identify the web technology in use supporting the www.counterhackchallenges.com site

## Answers

In the sections that follow, we'll use the SpiderFoot results to answer each of the questions asked for this lab's challenge section. Continue with this lab to see the answers.

### Click to see solution - Service Providers and Hosting Companies

    SpiderFoot includes several plugins to identify affiliates, or companies associated with the target. The plugin of primary interest is Affiliate - Internet Name.

    From SpiderFoot, navigate to the Browse section, then click the Affiliate - Internet Name link.

    In the list of results, you will see that several source modules have returned results that indicate affiliates, all relating to the use of DNS interrogation (sfp_dnsraw, sfp_dnsresolve, and sfp_dnsneighbor). Examining this list, there are several hostnames that identify service providers or hosting companies used for various services associated with www.counterhackchallenges.com:

    ALT1.ASPMX.L.GOOGLE.com (Google MX or Mail Exchange for email hosting)
    dns21a.sans.org (SANS Institute DNS services)
    li1015-10.members.linode.com (Linode virtual host services)

    Spiderfoot Affiliate - Internet Name Module

    Answer: Google, SANS, Linode

### Click to see solution - Associated Websites

    The SpiderFoot module Co-Hosted Site - Domain Name reveals any DNS names associated with discovered targets using a variety of DNS interrogation techniques.

    From SpiderFoot, navigate to the Browse section, then click the Co-Hosted Site - Domain Name link.

    In the list of results, you will see several hostnames resolved by the SpiderFoot sfp_dnsresolve plugin, disclosing virtual host aliases for the counterhack.com server:

    designer.counterhack.com
    status.counterhack.com
    www.counterhack.com

    This information can be very useful to an attacker, since it discloses the presence of multiple websites all running on the same server. Each website is another opportunity to identify a vulnerability that can expose the server and all the sites it serves. 

    Answer: designer.counterhack.com, status.counterhack.com, www.counterhack.com

### Click to see solution - Employee Email Addresses

    The SpiderFoot module Email Address reveals any email addresses associated with the specified target seed. Email addresses are harvested using a variety of plugins, including sfp_builtwith, sfp_email, and sfp_pgp.

    From SpiderFoot, navigate to the Browse section, then click the Email Address link.

    In the list of results, you will see several email addresses. Some are generic (info@counterhackchallenges.com), but others are quickly identified as relating to an employee account:

        josh@counterhackchallenges.com
        tom@counterhackchallenges.com
        yori@counterhackchallenges.com

    Answer: josh@counterhackchallenges.com, tom@counterhackchallenges.com, yori@counterhackchallenges.com

### Click to see solution - Hacked Email Account

    The SpiderFoot module Hacked Email Address reveals any email addresses that are known to be hacked. This does not indicate that the account associated with any services provided by Counter Hack was hacked (services such as email, remote login, etc.) Instead, this indicates that the email address is used by a site that was hacked, likely revealing password or password hash information from the compromised site.

    It's important to remember that any entries in the Hacked Email Address plugin do not indicate any fault of the user whose account is reported. The result here is from a lack of security on a different site, exposing the user who had an account on that site. 

    From SpiderFoot, navigate to the Browse section, then click the Hacked Email Address link.

    In the list of results, you will see a single email address:

        tom@counterhackchallenges.com [Verifications.io]

    The Verifications.io indicator reveals the site that was compromised, exposing this email address. This particular breach is a massive data disclosure for the enterprise email validation service, revealing 763 million records. Additional information about this breach is available at https://www.bankinfosecurity.com/breach-verificationsio-exposes-763-million-records-a-12158.

    Answer: tom@counterhackchallenges.com

### Click to see solution - Web Technology

    The SpiderFoot module Web Technology reveals information about the web platforms, server technology, and web frameworks used to build and serve web content. This information is collected by the SpiderFoot sfp_builtwith and sfp_websvr plugins.

    Information about web technology in use is an important information point for an attacker, guiding much of the subsequent analysis for vulnerability identification.

    From SpiderFoot, navigate to the Browse section, then click the Web Technology link.

    In the list of results, you will see several indicators revealing supporting web technology used by the site:

        Apache
        Gentoo Linux
        GoDaddy SSL
        Google Apps for Business
        iPhone/Mobile device compatibility
        Linode
        Meteor
        PHP (many with version indicators)
        SPF
        Verizon
        YouTube
        ... and others

    Answer: Apache web server, Gentoo Linux, Meteor Framework, PHP Framework, integration with external web components, including YouTube, Google Apps, etc.

### Why This Lab Is Important

OSINT is a tremendously useful resource for an attacker, guiding much of the subsequent decisions for how they will scan and exploit the target organization. As a defender, tools such as SpiderFoot can provide useful information about the nature of the data available for a specific target. Developing an understanding of the OSINT available for your site is useful for recognizing the information an attacker has accessible prior to an attack.