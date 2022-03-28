# tcpdump

Capture and display network traffic

## Examples

- **tcpdump -i *interface*** - Cappture traffic for an internface. Can also use *any*
- **tcpdump -i *interface* -w *files*** - Capture traffic for an interfaceand write to a file 
- **tcmpdump -r *file* -n** - Read packets from a file and don't resolve hosts and ports
- **tcpdump -r *file* -n -A** - Read packets from a file, don't resolve, show as ASII
- **tcpdump -nr falsimentis.pcap dst host 167.172.201.123 | cut -d ' ' -f 3 | cut -d '.' -f 1-4 | sort -u**
    - **tcpdump -nr falsimentis.pcap dst host 167.172.201.123** - print packets from the file falsimentis.pcap that are destined for host 167.172.201.123
    - **cut -d ' ' -f 3** - return the third space-delimited field from the tcpdump output (the IP address and port number).
    - **cut -d '.' -f 1-4** - cut the IP address and port number combination into pieces at the . character, and then select the first four fields (the IP address).
    - **sort -u** - Sort the IP addresses with sort, displaying only unique lines (-u).


## Examples with Berkely Packet Filters (BPFs)

- **tcpdump -r *file* 'host 8.8.8.8'** - Traffic going to or from host 8.8.8.8
- **tcpdump -r *file* 'src host 8.8.8.8** - Traffic coming from host 8.8.8.8
- **tcpdump -r *file* 'not src host 8.8.8.8'** - Traffic where the src is not 8.8.8.8
- **tcpdump -r *file* 'icmp and (src host 8.8.8.8)'** - Only ICMP from 8.8.8.8
