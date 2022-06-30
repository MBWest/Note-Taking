# Security - Group Policy Editor

## **Group Policy Editor**
- Local group policy editor (gpedit.msc) 
- Expand to "computer\windows settings" to see security settings
- Our focus is on the first two:
    - Account Policies
        - Contains password requirements
    - Local Policies
        - Configure auditing for event logs

---
---

## **Security Settings > Local Policies > Audit Policy**

## **Account logon events**
- Logs an event each time a user attempts to use this machine to authenticate
- Can log failed as well as successful attempts
- In an enterprise environment, these logs will be written on a Domain Controller. No Account Logon Events logs are stored on end-user systems for domain authentication
- On a standalone system, these logs will be written locally

> **Account management**
- Logs an event each time an account is managed
- This is a useful function if you are concerned about changes being made to user accounts in your environment
- Examples:
    - Changing a users password
    - adding a user

> **Directory service access**
- Can be used to track access to specific fields of objects in Active Directory
- Only way to track changes to Active Directory Organizational Unit’s (OU’s) and Group Policy Objects (GPO’s)
- Crucial for change-control auditing of enterprise environments

> **Policy changes**
- Logs an event each time a policy is successfully or unsuccessfully changed in your environment.
    - Example:  Changing Policy Change to success, Changing the max password age to 30

> **Privilege use**
- Logs an event each time a user attempts, successfully or unsuccessfully, to use special privileges
    - Example:  changing system time