cheats = [
    {
        "command": "theHarvester -d example.com -b all",
        "description": "Harvests emails, names, subdomains from multiple sources.",
        "example": "→ Emails, hosts from Google, Bing, etc."
    },
    {
        "command": "whois example.com",
        "description": "Shows domain registration info: owner, dates, registrar.",
        "example": "→ Admin contact: John Doe, Country: US"
    },
    {
        "command": "dnsenum example.com",
        "description": "Performs DNS enumeration with zone transfers, brute force.",
        "example": "→ Found subdomain: dev.example.com"
    },
    {
        "command": "recon-ng",
        "description": "Modular web recon framework with CLI and modules.",
        "example": "→ Use marketplace to install modules: market search linkedin"
    },
    {
        "command": "subfinder -d example.com",
        "description": "Passive subdomain enumeration using fast APIs.",
        "example": "→ blog.example.com, test.example.com"
    },
    {
        "command": "emailrep example@example.com",
        "description": "Checks email reputation, leaks, social profiles.",
        "example": "→ Reputation: High Risk, Found on LinkedIn"
    },
    {
        "command": "github-dorks -q 'password filename:.env'",
        "description": "Search GitHub for secrets using dork queries.",
        "example": "→ Found .env file with DB_PASS=..."
    },
    {
        "command": "curl https://crt.sh/?q=%.example.com",
        "description": "Grabs SSL certificate transparency logs for subdomains.",
        "example": "→ ssl.example.com, api.example.com"
    },
    {
        "command": "googler --n 10 'site:example.com login'",
        "description": "Command-line Google search with filters.",
        "example": "→ Found login panel links on site"
    },
    {
        "command": "python3 sherlock.py username",
        "description": "Searches for a username across 300+ social networks.",
        "example": "→ Found @voidexec on GitHub, Twitter, Reddit"
    }
]
