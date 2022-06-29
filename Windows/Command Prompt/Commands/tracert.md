# tracert

- Traces each hop (next router interface) between the source and destination IPs

---

## Examples

| **Command** | **Description** |
|-------------|-----------------|
| `tracert /d www.google.com ` | Get a count of the number of hopes to google.com without resolving address to hosts |
| `tracert www.google.com` | Traces the number of hops to www.google.com |
| `tracert –d 192.168.0.11` | Traces hops to 192.169.0.100, won’t resolve hostnames |
| `tracert –w 50 www.google.com` | Traces hops to www.google.com – only waits 50 ms |