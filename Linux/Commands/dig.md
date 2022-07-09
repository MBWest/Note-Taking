# dig (domain information groper)

DNS lookup utility

---

> ## **Syntax**

- dig [@server] [-b address] [-c class] [-f filename] [-k filename] [-m] [-p port#] [-q name] [-t type] [-x addr] [-y [hmac:]name:key] [-4] [-6] [name] [type] [class] [queryopt...]

---

> ## **Example**

| **Command**   | **Description**   |
| --------------|-------------------|
| **Example** |
| `dig @172.30.0.254 A www.falsimentis.com` |
| `@172.30.0.254` | The @ sign indicates that the query should be sent the server identified by a host name or IP address; here the DNS request is sent to 172.30.0.254. |
| `A` | The DNS record type to interrogate; an A record is an address record, returning an IPv4 address. |
| `www.falsimentis.com` | The value to interrogate; here we are asking the DNS server to return the IP address for www.falsimentis.com. |
|**Zone Transfer Example**|
| `dig +short @172.30.0.254 AXFR falsimentis.com` |
|**Mail Exchange Records Request Example**|
|`dig +short @172.30.0.254 MX falsimentis.com`|
| **A Record Request Example** |
|`dig +short @172.30.0.254 A mail.falsimentis.com`|

