cheats = [
    {
        "command": "print('Option 1\\nOption 2')",
        "description": "Prints multiple lines in one string. Good for menus.",
        "example": "→\nOption 1\nOption 2"
    },
    {
        "command": "from colorama import Fore\nprint(Fore.RED + 'Error!')",
        "description": "Adds terminal color (great for CLI tools).",
        "example": "→ Red text"
    },
    {
        "command": "from tqdm import tqdm\nfor i in tqdm(range(10)):\n    time.sleep(0.1)",
        "description": "Progress bar in terminal. Visual feedback during loops.",
        "example": "→ Loading bar appears"
    },
    {
        "command": "assert 1 == 1",
        "description": "Built-in test to ensure a condition is true.",
        "example": "Used in scripts for debugging or safety checks"
    },
    {
        "command": "import unittest\nclass TestX(unittest.TestCase):\n    def test_a(self):\n        self.assertEqual(2+2, 4)",
        "description": "Unit testing framework to check code automatically.",
        "example": "Run with: python3 -m unittest"
    },
    {
        "command": "import pickle\nwith open('data.pkl', 'wb') as f:\n    pickle.dump(my_data, f)",
        "description": "Serializes Python objects to binary file.",
        "example": "→ Save custom data for reuse"
    },
    {
        "command": "with open('data.pkl', 'rb') as f:\n    data = pickle.load(f)",
        "description": "Loads pickled data back into Python.",
        "example": "→ Deserialize object"
    },
    {
        "command": "import json\nprint(json.dumps(my_dict, indent=2))",
        "description": "Converts Python dict to formatted JSON string.",
        "example": "→ Clean readable JSON"
    },
    {
        "command": "import sys\nprint(sys.version)",
        "description": "Prints the current Python version info.",
        "example": "→ Python 3.10.6"
    },
    {
        "command": "import timeit\ntimeit.timeit('x = sum(range(10))')",
        "description": "Benchmarks how fast code runs.",
        "example": "→ Runtime in seconds"
    },
    {
        "command": "import cProfile\ncProfile.run('main()')",
        "description": "Profiles your script and shows what takes time.",
        "example": "→ Function-by-function performance breakdown"
    },
    {
        "command": "from pprint import pprint\npprint(my_nested_dict)",
        "description": "Prints nested structures in an easy-to-read way.",
        "example": "→ Indented, clean output"
    },
    {
        "command": "from pathlib import Path\nPath('logs').mkdir(exist_ok=True)",
        "description": "Makes a directory safely if it doesn’t exist.",
        "example": "→ Creates logs/ folder"
    },
    {
        "command": "Path('logs/output.txt').write_text('Done!')",
        "description": "Creates or overwrites a file with text using Pathlib.",
        "example": "→ logs/output.txt created"
    },
    {
        "command": "import os\nos.getenv('HOME')",
        "description": "Gets environment variable values (like paths, secrets).",
        "example": "→ /home/void"
    },
    {
        "command": "from functools import lru_cache\n@lru_cache\ndef fib(n): return n if n<=1 else fib(n-1)+fib(n-2)",
        "description": "Caches function results to boost performance.",
        "example": "→ Speeds up recursive calls"
    },
    {
        "command": "import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info('Script started')",
        "description": "Logs events instead of printing them. Great for large tools.",
        "example": "→ INFO:root:Script started"
    },
    {
        "command": "from getpass import getpass\npassword = getpass()",
        "description": "Safely prompts for password without showing input.",
        "example": "→ Terminal input is hidden"
    },
    {
        "command": "from rich import print\nprint('[bold magenta]Void Loaded[/]')",
        "description": "Adds color and style with the rich library.",
        "example": "→ Void Loaded in bold purple"
    },
    {
        "command": "exit()",
        "description": "Ends a script early. Same as sys.exit() but cleaner.",
        "example": "→ Script stops here"
    }
]
