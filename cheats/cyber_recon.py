cheats = [
    {
        "command": "nmap -sS -Pn -T4 <target>",
        "description": "Stealth SYN scan without ping",
        "example": "nmap -sS -Pn -T4 192.168.1.1"
    },
    {
        "command": "nmap -A -T4 <target>",
        "description": "Aggressive scan with OS and script detection",
        "example": "nmap -A -T4 192.168.1.1"
    },
    {
        "command": "whois <domain>",
        "description": "Domain registration info",
        "example": "whois example.com"
    },
    {
        "command": "nslookup <domain>",
        "description": "Basic DNS query",
        "example": "nslookup google.com"
    },
    {
        "command": "dig <domain> ANY +noall +answer",
        "description": "All DNS records",
        "example": "dig example.com ANY +noall +answer"
    },
    {
        "command": "theHarvester -d <domain> -b all",
        "description": "Collect emails, hosts, subdomains",
        "example": "theHarvester -d domain.com -b all"
    },
    {
        "command": "sublist3r -d <domain>",
        "description": "Fast subdomain scanner",
        "example": "sublist3r -d site.com"
    },
    {
        "command": "amass enum -d <domain>",
        "description": "Passive + active recon",
        "example": "amass enum -d domain.com"
    },
    {
        "command": "dnsrecon -d <domain>",
        "description": "DNS record brute-forcing",
        "example": "dnsrecon -d test.com"
    },
    {
        "command": "nmap -p- <target>",
        "description": "Scan all ports",
        "example": "nmap -p- 10.0.0.5"
    }
]
