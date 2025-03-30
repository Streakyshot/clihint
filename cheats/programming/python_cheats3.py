cheats = [
    {
        "command": "file = open('file.txt', 'r')\ndata = file.read()\nfile.close()",
        "description": "Reads the entire contents of a file. Always close after!",
        "example": "Print the content: print(data)"
    },
    {
        "command": "with open('file.txt') as f:\n    lines = f.readlines()",
        "description": "Context manager. Reads all lines from a file into a list.",
        "example": "Access line 1: lines[0]"
    },
    {
        "command": "with open('file.txt', 'a') as f:\n    f.write('New line\\n')",
        "description": "Appends a new line to the end of a file.",
        "example": "Adds line without erasing existing content"
    },
    {
        "command": "'{0} scored {1}/100'.format('Sam', 95)",
        "description": "Formats strings using placeholders and variables.",
        "example": "Output: 'Sam scored 95/100'"
    },
    {
        "command": "f'{name} is {age} years old'",
        "description": "f-strings: Cleaner way to format strings with variables.",
        "example": "name='Void', age=16 → 'Void is 16 years old'"
    },
    {
        "command": "x, y = 5, 10\nif x < y and y > 0:\n    print('Valid')",
        "description": "Uses logical AND to combine multiple conditions.",
        "example": "Both must be True to run"
    },
    {
        "command": "if not user_input:\n    print('Empty!')",
        "description": "`not` checks for empty string, None, 0, or False.",
        "example": "If user_input = '', prints 'Empty!'"
    },
    {
        "command": "items = ['a', 'b', 'c']\nfor i, item in enumerate(items):\n    print(i, item)",
        "description": "Enumerate gives both index and value in a loop.",
        "example": "Output: 0 a\n1 b\n2 c"
    },
    {
        "command": "for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)",
        "description": "Skips printing number 3 using continue.",
        "example": "Output: 1 2 4 5"
    },
    {
        "command": "for i in range(1, 6):\n    if i == 4:\n        break\n    print(i)",
        "description": "Breaks the loop when i equals 4.",
        "example": "Output: 1 2 3"
    },
    {
        "command": "nums = [1, 2, 3, 4]\neven = [x for x in nums if x % 2 == 0]",
        "description": "List comprehension with condition to filter evens.",
        "example": "Output: [2, 4]"
    },
    {
        "command": "msg = 'Hello'\nreversed_msg = msg[::-1]",
        "description": "Reverses a string using slicing.",
        "example": "'olleH'"
    },
    {
        "command": "total = 0\nfor x in range(10):\n    total += x",
        "description": "Cumulative sum using a loop.",
        "example": "total → 45"
    },
    {
        "command": "print(', '.join(['a', 'b', 'c']))",
        "description": "Joins list items into a single string separated by commas.",
        "example": "'a, b, c'"
    },
    {
        "command": "text = 'VOIDEXEC'\nprint(text.lower())",
        "description": "Converts text to lowercase (great for normalization).",
        "example": "'voidexec'"
    },
    {
        "command": "name = input('Name: ').strip().capitalize()",
        "description": "Cleans up input and capitalizes it properly.",
        "example": "Input: '  sam' → 'Sam'"
    },
    {
        "command": "import time\ntime.sleep(2)",
        "description": "Pauses script for 2 seconds. Great for delays.",
        "example": "Useful in loops or terminal effects"
    },
    {
        "command": "print('Loading...', end='')",
        "description": "Prevents newline so output stays on same line.",
        "example": "Terminal UX control"
    },
    {
        "command": "dir(object)",
        "description": "Shows all properties and methods of an object.",
        "example": "Try dir('abc') or dir([])"
    },
    {
        "command": "help(str)",
        "description": "Opens Python’s built-in help for a given class or function.",
        "example": "help(str) → docs about strings"
    }
]
