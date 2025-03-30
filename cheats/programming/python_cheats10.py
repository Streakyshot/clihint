cheats = [
    {
        "command": "import threading\ndef run(): print('Thread active')\nt = threading.Thread(target=run)\nt.start()",
        "description": "Creates a separate thread to run a function in parallel.",
        "example": "→ Thread active"
    },
    {
        "command": "import requests\nres = requests.get('https://example.com')\nprint(res.text[:100])",
        "description": "Pulls HTML content from a webpage. Used in scraping and automation.",
        "example": "→ '<!doctype html>...'"
    },
    {
        "command": "from bs4 import BeautifulSoup\nsoup = BeautifulSoup(res.text, 'html.parser')",
        "description": "Parses HTML content using BeautifulSoup.",
        "example": "→ soup.title → <title>Example</title>"
    },
    {
        "command": "for link in soup.find_all('a'):\n    print(link.get('href'))",
        "description": "Extracts all links from a web page.",
        "example": "→ '/about', 'https://site.com/page'"
    },
    {
        "command": "import shlex\ncmd = 'ls -la /home'\nprint(shlex.split(cmd))",
        "description": "Safely splits a command string into shell-safe tokens.",
        "example": "→ ['ls', '-la', '/home']"
    },
    {
        "command": "import random\nrandom.seed(1337)",
        "description": "Sets a seed so random values are predictable (for testing).",
        "example": "→ Same 'random' results every time"
    },
    {
        "command": "import ipaddress\nip = ipaddress.ip_network('192.168.1.0/24')\nprint(list(ip.hosts()))",
        "description": "Handles IP calculations and subnetting.",
        "example": "→ List of 254 usable IPs"
    },
    {
        "command": "from subprocess import run\nrun(['ping', '-c', '1', '1.1.1.1'])",
        "description": "Runs external commands with subprocess (safer than os.system).",
        "example": "→ Terminal ping output"
    },
    {
        "command": "with open('targets.txt') as f:\n    hosts = [line.strip() for line in f]",
        "description": "Reads a file line by line and cleans each line.",
        "example": "→ ['192.168.1.1', '10.0.0.5']"
    },
    {
        "command": "import difflib\ndifflib.get_close_matches('passwrd', ['password', 'passwd', 'admin'])",
        "description": "Finds close matches in a list (fuzzy matching).",
        "example": "→ ['password', 'passwd']"
    },
    {
        "command": "import uuid\nuuid.uuid4()",
        "description": "Generates a random UUID (used in tokens, device IDs).",
        "example": "→ 'f81d4fae-7dec-11d0-a765-00a0c91e6bf6'"
    },
    {
        "command": "import socket\ns = socket.socket()\ns.connect(('example.com', 80))",
        "description": "Creates a raw socket connection (used in backdoor/payload code).",
        "example": "→ Manual TCP connection"
    },
    {
        "command": "from urllib.parse import urlparse\nurlparse('https://voidexec.net/tools')",
        "description": "Breaks a URL into parts: scheme, domain, path.",
        "example": "→ scheme='https', netloc='voidexec.net', path='/tools'"
    },
    {
        "command": "open('/etc/passwd', 'r').readlines()",
        "description": "Reads the system user file on Linux (used in privilege checks).",
        "example": "→ List of user entries"
    },
    {
        "command": "try:\n    eval('2+2')\nexcept:\n    pass",
        "description": "Evaluates a string as Python code (dangerous, use with caution).",
        "example": "→ 4"
    },
    {
        "command": "import os\nfor root, dirs, files in os.walk('.'):\n    for file in files:\n        print(file)",
        "description": "Recursively walks through directories and lists files.",
        "example": "→ Lists every file in project"
    },
    {
        "command": "list(set(['a', 'a', 'b']))",
        "description": "Removes duplicates by converting list to set.",
        "example": "→ ['a', 'b']"
    },
    {
        "command": "list(filter(None, [0, 1, '', 'ok']))",
        "description": "Filters out all falsy values (0, '', False, None).",
        "example": "→ [1, 'ok']"
    },
    {
        "command": "__import__('os').system('echo stealth')",
        "description": "Dynamically imports a module and runs a command.",
        "example": "→ stealth"
    },
    {
        "command": "exec('print(\"Dynamic code!\")')",
        "description": "Runs code stored in a string. Powerful, dangerous.",
        "example": "→ Dynamic code!"
    }
]
