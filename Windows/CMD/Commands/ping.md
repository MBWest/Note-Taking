# ping

- Sends four ICMP requests and waits for a response to see if the specified system is up (is there connectivity to the device?)

---

## Examples


| **Command** | **Description** |
|-------------|-----------------|
| `ping www.cnn.com` | Ping cnn.com |
| `ping 127.0.0.1 /n 6` | Ping 127.0.0.1 6 times |
| `ping www.google.com` | Pings www.google.com 4 times |
| `ping –n 2 10.10.0.3` | Pings 10.10.0.3 2 times |
| `ping –t 10.10.0.3` | Pings 10.10.0.3 until it’s stopped |