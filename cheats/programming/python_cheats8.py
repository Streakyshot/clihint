cheats = [
    {
        "command": "import argparse\nparser = argparse.ArgumentParser()\nparser.add_argument('--name')\nargs = parser.parse_args()\nprint(args.name)",
        "description": "Handles command-line arguments cleanly. Great for tools.",
        "example": "Run with: python script.py --name Void"
    },
    {
        "command": "import requests\nres = requests.get('https://httpbin.org/get')\nprint(res.status_code)",
        "description": "Performs an HTTP GET request. Used in web scraping, OSINT, etc.",
        "example": "→ 200 (OK)"
    },
    {
        "command": "res.json()['origin']",
        "description": "Parses JSON from an API response.",
        "example": "→ '123.45.67.89'"
    },
    {
        "command": "headers = {'User-Agent': 'Voidexec/1.0'}",
        "description": "Custom headers for HTTP requests (spoofing browser, etc.).",
        "example": "Used in requests.get(..., headers=headers)"
    },
    {
        "command": "import socket\nsocket.gethostbyname('google.com')",
        "description": "Resolves a domain name to an IP address.",
        "example": "→ '142.250.64.78'"
    },
    {
        "command": "socket.gethostbyaddr('8.8.8.8')",
        "description": "Does a reverse DNS lookup to get hostname from IP.",
        "example": "→ ('dns.google', ...)"
    },
    {
        "command": "res = requests.post('https://httpbin.org/post', data={'key': 'value'})",
        "description": "Sends data to a server via HTTP POST.",
        "example": "→ Check response with res.json()"
    },
    {
        "command": "from urllib.parse import urlencode\nurlencode({'q': 'python'})",
        "description": "Encodes data for use in a URL.",
        "example": "→ 'q=python'"
    },
    {
        "command": "open('recon.txt', 'r').readlines()",
        "description": "Reads lines of a file (like a subdomain list).",
        "example": "→ ['admin.site.com\\n', 'test.site.com\\n']"
    },
    {
        "command": "import base64\nbase64.b64encode(b'hello')",
        "description": "Encodes binary/text into base64 (used in payloads).",
        "example": "→ b'aGVsbG8='"
    },
    {
        "command": "base64.b64decode('aGVsbG8=')",
        "description": "Decodes base64 back into readable format.",
        "example": "→ b'hello'"
    },
    {
        "command": "import hashlib\nhashlib.md5(b'password').hexdigest()",
        "description": "Generates an MD5 hash from input. Used in CTFs and cracking.",
        "example": "→ '5f4dcc3b5aa765d61d8327deb882cf99'"
    },
    {
        "command": "hashlib.sha256(b'data').hexdigest()",
        "description": "Secure hashing with SHA-256.",
        "example": "→ '3a6eb...'"
    },
    {
        "command": "import re\nre.findall(r'[a-z]+', 'Void123Exec')",
        "description": "Finds all lowercase letter sequences using regex.",
        "example": "→ ['oid', 'xec']"
    },
    {
        "command": "re.match(r'V.*', 'Voidexec')",
        "description": "Checks if the string matches a pattern from the start.",
        "example": "→ Match object"
    },
    {
        "command": "import os\nos.system('whoami')",
        "description": "Executes a shell command from Python (not safest).",
        "example": "→ 'voiduser'"
    },
    {
        "command": "from subprocess import check_output\nprint(check_output(['id']))",
        "description": "Runs a shell command and captures its output.",
        "example": "→ b'uid=1000(...)'"
    },
    {
        "command": "with open('results.txt', 'a') as f:\n    f.write('Subdomain found: test.site.com\\n')",
        "description": "Appends results to a file, like a recon log.",
        "example": "Adds line to file"
    },
    {
        "command": "if 'admin' in url:\n    print('Admin panel detected')",
        "description": "Simple string condition—used in automation and scrapers.",
        "example": "→ Alerts when keyword is found"
    },
    {
        "command": "urls = ['site.com', 'login.site.com']\n[requests.get('https://' + u) for u in urls]",
        "description": "Scans multiple URLs in one line using list comp.",
        "example": "→ List of response objects"
    }
]
