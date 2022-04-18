# How to Connect

After seeing the numerous forum posts asking for help connecting to the Hera Labs I've decided to post this simple guide to help those still having issues.

Before Continuing Have you done these things already?

1. Read the Hera Lab manual provided by eLearnSecurity

2. **Downloaded a Kali VM** (This will be useful for all of the labs and should be done unless you are absolutely unable to. Do not just use your Windows or Mac OS unless you have no other option)

Guide:

0. Create your Hera Lab credentials (only needs to be done once, this is how you will connect to the vpn (they are different from your eLS credentials)

1. Start your lab

2. Download the .ovpn file for the lab

3. Open a terminal

4. Change into the directory where the .ovpn file was saved (This is typically the /Downloads folder)

5. Run *openvpn [FileName].ovpn*

6. You will be prompted in the terminal to enter your Hera lab credentials

7. To verify a successful connection, open another terminal and run *ifconfig* and look for a *tap0* interface (If it is missing, try connecting again)

8. Open */etc/resolv.conf* (You can use the terminal by running *gedit /etc/resolv.conf* or use your preferred text editor)

9 Add the nameserver specified in the lab manual to the top of the list (Do not delete any others as they are necessary to browse the internet normally)

10. When you have finished the lab, remember to stop your lab environment

Troubleshooting Basics:

1. If you restart the lab and download a new *.ovpn* file, you will need to use this new file as the previous one will no longer work

2. Do not try to configured a VPN outside of the Kali VM. All of the tools necessary to complete the labs can be found or installed within Kali.

3. When connecting to the VPN there may be a few messages in the terminal, these are normal. As long as you connect to the Lab VPN, you can ignore these messages.

4. If you are having issues connecting, delete the *.ovpn* file, download a new one, and retry.

5. Please refrain from simply posting asking for help with your issue. Look through the forum first to see if anyone else has encountered the same issue.