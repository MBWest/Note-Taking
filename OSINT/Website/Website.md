# OSINT - Website

> ## **WebCapture Tool**

- Hunchly - https://hunch.ly

---

> ## **General Info**

- BuiltWith - https://builtwith.com/

- Domain Dossier - https://centralops.net/co/

- DNSlytics - https://dnslytics.com/reverse-ip

- SpyOnWeb - https://spyonweb.com/

- Virus Total - https://www.virustotal.com/

- Visual Ping - https://visualping.io/

- Back Link Watch - http://backlinkwatch.com/index.php

- View DNS - https://viewdns.info/

---

> ## **Subdomains**

- Pentest-Tools Subdomain Finder - https://pentest-tools.com/information-gathering/find-subdomains-of-domain#

- Spyse - https://spyse.com/

- crt.sh - https://crt.sh/

---

> ## **CLI Tools**

```
whois tcm-sec.com

nano ~/.bashrc

export GOPATH=$HOME/go 
export GOROOT=/usr/lib/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin

source ~/.bashrc

go get -u github.com/tomnomnom/httprobe
go get -u github.com/tomnomnom/assetfinder
GO111MODULE=on go get -u -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
go get -u github.com/sensepost/gowitness
export GO111MODULE=on
go get -v github.com/OWASP/Amass/v3/...

subfinder -d tcm-sec.com
assetfinder tcm-sec.com
amass enum -d tcm-sec.com
cat tesla.txt | sort -u | httprobe -s -p https:443
gowitness file -f ./alive.txt -P ./pics --no-http
```

- Subfinder - https://github.com/projectdiscovery/subfinder

- Assetfinder - https://github.com/tomnomnom/assetfinder

- httprobe - https://github.com/tomnomnom/httprobe

- Amass - https://github.com/OWASP/Amass

- GoWitness - https://github.com/sensepost/gowitness/wiki/Installation

---
