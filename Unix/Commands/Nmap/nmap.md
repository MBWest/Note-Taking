# nmap

# Automated DNS Guessing Example

Note: Collection of lists that are useful for security assessments, including a longer list of host names than nmap default - https://github.com/danielmiessler/SecLists

- **sudo nmap --dns-servers 172.30.0.254 --script dns-brute --script-args dns-brute.domain=falsimentis.com**
    - **sudo nmap** - Run Nmap with root privileges using sudo
    - **--dns-servers 172.30.0.254** - Specify the DNS server to use for name resolution; this can be a local DNS server, the target organization's DNS server, or another DNS resolver (such as Google's public DNS resolver at 8.8.8.8)
    - **--script dns-brute** - Tell Nmap to run the dns-brute script
    - **--script-args dns-brute.domain=falsimentis.com** - Specify the falsimentis.com domain as an argument for the dns-brute.domain parameter