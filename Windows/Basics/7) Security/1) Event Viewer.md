# Security - Event Viewer

## **Event Viewer – eventvwr.msc**

> ### **System**
- Contains events logged by the Windows system components that failed during startup
- Such as drivers or other system components 

> ### **Application**
- Contains events logged by applications or programs
- The program developer decides which events to record

> ### **Security**
- If configured to do so, records security events, such as valid and invalid logon attempts
- Events related to resource use-such as creating, opening, or deleting files—can also be logged

---


> ## **Application and System Logs**

> ### **Error**
- A significant problem, such as loss of data or loss of functionality

> ### **Warning**
- An event that is not necessarily significant but might indicate a possible future problem

> ### **Information**
- An event that describes the successful operation of an application, driver, or service

---


> ## **Found in Security Logs**

> ### **Success Audit**
- An audited security event in which a user’s attempt to access a resource succeeds

> ### **Failed Audit**
- An audited security event in which a user’s attempt to access a resource fails

---


> ## **Searching**

- Search for events with specified strings
- Accessing find:
    - Right click; select “Find”
    - Ctrl+f
    - Action menu; Select Find

---

> ## **Filtering**

- Filter events with specified criteria
- Accessing filter wizard:
    - Choose “Filter Current log” from the “Action” menu
    - OR Right click; select “Filter Current log”