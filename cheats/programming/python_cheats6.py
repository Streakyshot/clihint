cheats = [
    {
        "command": "import json\nwith open('data.json') as f:\n    data = json.load(f)",
        "description": "Reads JSON data from a file and converts it to Python objects.",
        "example": "data['key'] → value"
    },
    {
        "command": "with open('output.json', 'w') as f:\n    json.dump(data, f, indent=4)",
        "description": "Writes Python data into a JSON file with formatting.",
        "example": "Creates 'output.json' with readable JSON"
    },
    {
        "command": "import csv\nwith open('data.csv') as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)",
        "description": "Reads CSV file line by line using csv.reader.",
        "example": "Each row is a list: ['name', 'email']"
    },
    {
        "command": "import csv\nwith open('out.csv', 'w') as f:\n    writer = csv.writer(f)\n    writer.writerow(['user', 'pass'])",
        "description": "Writes a single row into a CSV file.",
        "example": "CSV line → user,pass"
    },
    {
        "command": "import os\nprint(os.getcwd())",
        "description": "Gets the current working directory.",
        "example": "→ /home/voidexec/clihint"
    },
    {
        "command": "os.listdir('.')",
        "description": "Lists all files and folders in the current directory.",
        "example": "→ ['main.py', 'README.md']"
    },
    {
        "command": "os.path.exists('file.txt')",
        "description": "Checks if a file or path exists.",
        "example": "→ True or False"
    },
    {
        "command": "from sys import argv\nprint(argv)",
        "description": "Reads command-line arguments passed to a script.",
        "example": "Run as: python3 script.py arg1 → argv[1] = 'arg1'"
    },
    {
        "command": "import time\nstart = time.time()\n# code here\ntime.sleep(1)\nprint(time.time() - start)",
        "description": "Measures how long a block of code takes to run.",
        "example": "→ ~1.00 seconds"
    },
    {
        "command": "from datetime import datetime\nnow = datetime.now()\nprint(now.strftime('%Y-%m-%d %H:%M'))",
        "description": "Formats current date/time into a readable string.",
        "example": "→ 2025-03-30 22:44"
    },
    {
        "command": "import sys\nsys.exit()",
        "description": "Stops script execution manually.",
        "example": "Can use in if-checks or exceptions"
    },
    {
        "command": "import platform\nplatform.system()",
        "description": "Returns your OS name: Windows, Linux, Darwin (macOS).",
        "example": "→ 'Linux'"
    },
    {
        "command": "import subprocess\nsubprocess.run(['ls', '-la'])",
        "description": "Executes shell commands from Python.",
        "example": "Equivalent to running 'ls -la' in terminal"
    },
    {
        "command": "from getpass import getpass\npassword = getpass('Enter password: ')",
        "description": "Takes user input without showing it (good for login tools).",
        "example": "Output: (hidden input)"
    },
    {
        "command": "import shutil\nshutil.copy('a.txt', 'b.txt')",
        "description": "Copies a file from source to destination.",
        "example": "Makes a duplicate file"
    },
    {
        "command": "from pathlib import Path\nPath('folder').mkdir(exist_ok=True)",
        "description": "Creates a folder if it doesn’t already exist.",
        "example": "Safer than os.mkdir"
    },
    {
        "command": "def main():\n    print('Running...')\n\nif __name__ == '__main__':\n    main()",
        "description": "Sets the main entry point for a script. Only runs when script is directly executed.",
        "example": "Common structure for Python CLI tools"
    },
    {
        "command": "from typing import List\n\ndef sum_list(numbers: List[int]) -> int:\n    return sum(numbers)",
        "description": "Uses type hints to define expected input and output.",
        "example": "→ Static type checking with tools like mypy"
    },
    {
        "command": "import random\nrandom.choice(['red', 'blue', 'green'])",
        "description": "Randomly selects one item from a list.",
        "example": "→ 'blue'"
    },
    {
        "command": "from pprint import pprint\npprint(my_dict)",
        "description": "Pretty-prints complex data like nested dicts or JSON.",
        "example": "Clean formatted output"
    }
]
