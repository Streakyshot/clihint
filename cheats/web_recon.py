cheats = [
    {
        "command": "gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt",
        "description": "Brute-forces directories on a website using a wordlist.",
        "example": "→ Found: /admin, /login, /images"
    },
    {
        "command": "ffuf -u http://target.com/FUZZ -w wordlist.txt",
        "description": "Fast web fuzzer to find hidden files/directories.",
        "example": "→ Discovered: /.git/, /backup.zip"
    },
    {
        "command": "dirb http://target.com /usr/share/wordlists/dirb/small.txt",
        "description": "Classic directory brute-force tool.",
        "example": "→ Directories found with status codes"
    },
    {
        "command": "nikto -h http://target.com",
        "description": "Scans for known vulnerabilities, headers, and misconfigurations.",
        "example": "→ X-XSS-Protection not set"
    },
    {
        "command": "whatweb http://target.com",
        "description": "Detects CMS, frameworks, and technologies used on a site.",
        "example": "→ WordPress, jQuery, Apache"
    },
    {
        "command": "wafw00f http://target.com",
        "description": "Detects if the site is protected by a WAF (Web Application Firewall).",
        "example": "→ WAF detected: Cloudflare"
    },
    {
        "command": "curl -I http://target.com",
        "description": "Fetches HTTP headers to analyze server info, cookies, etc.",
        "example": "→ Server: nginx, Set-Cookie: sessionid=123"
    },
    {
        "command": "httpx -l targets.txt -title -status -tech-detect",
        "description": "Mass web scanner with title/status/tech detection.",
        "example": "→ 200 OK | Apache | Login Page"
    },
    {
        "command": "waybackurls target.com",
        "description": "Pulls historical URLs from the Wayback Machine.",
        "example": "→ /admin-old, /test-login.php"
    },
    {
        "command": "curl -sL http://target.com/robots.txt",
        "description": "Fetches robots.txt to find disallowed or sensitive paths.",
        "example": "→ Disallow: /private/, /beta/"
    }
]
