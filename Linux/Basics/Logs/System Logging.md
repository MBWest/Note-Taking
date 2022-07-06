# System Logging

## The Syslog Standard

- Aids in the processing of messages
- Allows Logging to be centrally controlled
- Uses facilities and severities to categorize messages

## rsyslog
 
- Default config file location: **/etc/rsyslog.conf**

**Logging Rules**
- **Selector Field [Facility.Severity]** - Lists the facilities and the severity to include in the rule
    - Wild cards are supported (*)
    - Facility.none will not match any facilites
- **Action Field** - Determines how a message is processed
    - Most common action is to write the message to a log file

## Caching vs Non-caching

- Caching is used if the path starts with a hypen
    - mail.info (-/var/log/mail.info)
- If the system crashes you may lose some messages
- Can improve I/O performance