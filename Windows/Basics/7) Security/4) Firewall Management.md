# Security - Windows Firewall

## **The Basics**

> ### **Stateful, Host-Based Firewall**
- Filter network packets based on the full context of a connection
- Stateful inspection available in Vista+

> ### **Ingress and Egress filtering**
- Egress filtering available in Vista+
- Older OS’s could not block malware from “phoning home”

> ### **IPSec Support**
- Allow/Deny connections based on certificates/authentication

> ### **Network Awareness**
- Custom rules for Public, Private, or Domain profiles
- Deny traffic for one profile, allow on another

---
---
---

## **Firewall Management Options**

> ### **Windows Defender Firewall GUI**
- No centralized Management
- Designed to be consumer friendly, not for enterprise use
- Shortcut: “firewall.cpl”

> ### **Windows Defender Firewall with Advanced Security**
- Much more flexibility than the Windows Defender interface
- API integration for management by other security solutions
- Shortcut: “wf.msc”

> ### **Command Line options: netsh advfirewall, PowerShell**
- More granular means to interact with the underlying components

---
---
---

## **netsh**

- Introduced with Windows 2000
- Interacts with underlying services, just like GUI/PowerShell
- Support may be removed by Microsoft in the future
- Included as reference, we will not cover netsh in this block

---
---
---

## **PowerShell**

- Commands interact with the local firewall – no builtin remote option
- Remote management can be done with Invoke-Command

> ### **Retrieving the Firewall’s status with Get-NetFirewallProfile**
- Returns current Profiles and their status
- Yields results for Domain, Private, and Public (only Domain shown below)

> ### **Disabling a Firewall Profile with Set-NetFirewallProfile**
- Determine the currently active Profile with Get-NetConnectionProfile first

> ### **Viewing the rule created earlier with Get-NetFirewallRule**

> ### **Disable/Enable the rule with Disable/Enable-NetFirewallRule**

> ### **Can pipe the results of Get-NetFirewallRule**
- Be cautious…you can disable all rules at once this way
- Or maybe that’s your goal! `Get-NetFireWallRule | Disable-NetFirewallRule`

> ### **Create a rule with New-NetFirewallRule**

> ### **Modify a rule with Set-NetFirewallRule**

> ### **Remove a rule with Remove-NetFirewallRule**

> ### **Viewing port information with Get-NetFirewallPortFilter**
- Port information can only be revealed using the PortFilter function

> ### **Changing port filters with Set-NetFirewallPortFilter**