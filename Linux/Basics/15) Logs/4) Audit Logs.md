# Linux - Logs - Audit Logs

> ## **Audit Logs**

- Audit events are processed by the auditing daemon auditd
- Audit events are logged to one log file
    - `/var/log/audit/audit.log`
- Permanent auditing rules are stored in 
    - `/etc/audit/audit.rules` - audit rules to be loaded at startup
    - `/etc/audit/rules.d/` - rules to be compiled by augenrules 
- Auditing rules may be created on the fly using the auditctl command
- The audit log may be searched by using the ausearch command
    - `ausearch` searches ONLY the audit log

---

> ## **auditd**
- Userspace component to the Linux auditing system
- Responsible for writing audit events to disk
- Reads rules from /etc/audit/audit.rules when the service starts 
- Alternativley, `augenrules` program reads rules from `/etc/audit/rules.d/` and compliles them into `audit.rules`
- If you stop the service, auditing will stop