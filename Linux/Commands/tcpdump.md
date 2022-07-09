# tcpdump

Capture and display network traffic

---

> ## **Example**

| **Command**   | **Description**   |
| --------------|-------------------|
| `tcpdump -i [interface]` |  Cappture traffic for an internface. Can also use *any* |
| `tcpdump -i [interface] -w [files]` |  Capture traffic for an interfaceand write to a file |
| `tcmpdump -r [file] -n` |  Read packets from a file and don't resolve hosts and ports |
| `tcpdump -r [file] -n -A` |  Read packets from a file, don't resolve, show as ASII |
| **Examples with Berkely Packet Filters (BPFs)** |
| `tcpdump -r [file] 'host 8.8.8.8'` |  Traffic going to or from host 8.8.8.8 |
| `tcpdump -r [file] 'src host 8.8.8.8` |  Traffic coming from host 8.8.8.8 |
| `tcpdump -r [file] 'not src host 8.8.8.8'` |  Traffic where the src is not 8.8.8.8 |
| `tcpdump -r [file] 'icmp and (src host 8.8.8.8)'` |  Only ICMP from 8.8.8.8 |
| `tcpdump -nr falsimentis.pcap dst host 167.172.201.123 \| cut -d ' ' -f 3 \| cut -d '.' -f 1-4 \| sort -u` |
| `tcpdump -nr falsimentis.pcap dst host 167.172.201.123` |  print packets from the file falsimentis.pcap that are destined for host 167.172.201.123 |

