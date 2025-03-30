cheats = [
    {
        "command": "ping -c 4 1.1.1.1",
        "description": "Sends 4 ICMP echo requests to test if a host is reachable.",
        "example": "→ Reply from 1.1.1.1: time=10ms"
    },
    {
        "command": "traceroute example.com",
        "description": "Shows the path packets take to reach a target.",
        "example": "→ 13 hops to reach example.com"
    },
    {
        "command": "netstat -tuln",
        "description": "Displays active TCP/UDP ports and listening services.",
        "example": "→ LISTEN 0.0.0.0:22 (SSH)"
    },
    {
        "command": "nmap -p 1-1000 192.168.1.1",
        "description": "Scans first 1000 ports on a target IP.",
        "example": "→ Open: 22/tcp (SSH), 80/tcp (HTTP)"
    },
    {
        "command": "arp -a",
        "description": "Displays IP-to-MAC address mappings on the local network.",
        "example": "→ 192.168.1.1 → 00:11:22:33:44:55"
    },
    {
        "command": "ip addr show",
        "description": "Shows all IP addresses assigned to your system interfaces.",
        "example": "→ inet 192.168.1.100/24"
    },
    {
        "command": "netcat -vnlp 4444",
        "description": "Sets up a TCP listener on port 4444 (used in reverse shells).",
        "example": "→ Listening on 0.0.0.0:4444"
    },
    {
        "command": "nc <ip> 80",
        "description": "Connects to a host’s port (like telnet but cleaner).",
        "example": "→ Banner grabbing, raw HTTP testing"
    },
    {
        "command": "import socket\ns = socket.socket()\ns.connect(('example.com', 80))",
        "description": "Python: Creates a raw TCP connection to a host.",
        "example": "→ s.send(b'GET / HTTP/1.1\\r\\n\\r\\n')"
    },
    {
        "command": "tcpdump -i eth0",
        "description": "Captures packets on interface eth0 for analysis.",
        "example": "→ Sniffs all traffic (root required)"
    }
]
