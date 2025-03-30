cheats = [
    {
        "command": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
        "description": "Handles specific errors so your code doesn’t crash.",
        "example": "Output: Cannot divide by zero"
    },
    {
        "command": "try:\n    open('missing.txt')\nexcept FileNotFoundError:\n    print('File not found')",
        "description": "Catches file opening errors like missing files.",
        "example": "Output: File not found"
    },
    {
        "command": "try:\n    x = int('not a number')\nexcept ValueError:\n    print('Invalid number')",
        "description": "Handles bad conversions like str → int.",
        "example": "Output: Invalid number"
    },
    {
        "command": "my_list = [10, 20, 30]\nslice = my_list[1:3]",
        "description": "Slices list from index 1 up to (not including) 3.",
        "example": "slice → [20, 30]"
    },
    {
        "command": "my_list[:2]",
        "description": "Slices the first two items.",
        "example": "→ [10, 20]"
    },
    {
        "command": "my_list[::2]",
        "description": "Slicing with steps: take every 2nd element.",
        "example": "→ [10, 30]"
    },
    {
        "command": "from datetime import datetime\ndatetime.now()",
        "description": "Gets the current date and time.",
        "example": "→ 2025-03-30 21:12:00"
    },
    {
        "command": "from datetime import timedelta\nfuture = datetime.now() + timedelta(days=7)",
        "description": "Adds 7 days to the current time.",
        "example": "→ next week’s datetime object"
    },
    {
        "command": "set([1,2,2,3])",
        "description": "Creates a set (only unique values allowed).",
        "example": "→ {1, 2, 3}"
    },
    {
        "command": "a = True\nb = False\nprint(a and b)",
        "description": "Boolean logic. `and` only returns True if both are True.",
        "example": "→ False"
    },
    {
        "command": "any([False, True, False])",
        "description": "Returns True if *any* item is True.",
        "example": "→ True"
    },
    {
        "command": "all([True, True, False])",
        "description": "Returns True only if *all* items are True.",
        "example": "→ False"
    },
    {
        "command": "bool('text')",
        "description": "Converts values into boolean. Empty = False, non-empty = True.",
        "example": "→ True"
    },
    {
        "command": "reversed([1, 2, 3])",
        "description": "Returns a reversed iterator.",
        "example": "→ [3, 2, 1]"
    },
    {
        "command": "zip([1,2], ['a','b'])",
        "description": "Pairs items from two lists.",
        "example": "→ [(1, 'a'), (2, 'b')]"
    },
    {
        "command": "from collections import Counter\nCounter('banana')",
        "description": "Counts occurrences of each item/character.",
        "example": "→ {'a': 3, 'b': 1, 'n': 2}"
    },
    {
        "command": "list(map(str.upper, ['a', 'b']))",
        "description": "Maps a function over a list.",
        "example": "→ ['A', 'B']"
    },
    {
        "command": "list(filter(lambda x: x > 2, [1, 2, 3, 4]))",
        "description": "Filters list to only values > 2.",
        "example": "→ [3, 4]"
    },
    {
        "command": "del my_list[0]",
        "description": "Deletes item at index 0 from list.",
        "example": "→ removes first element"
    },
    {
        "command": "my_dict = dict(name='Sam', age=15)",
        "description": "Creates a dictionary using keyword syntax.",
        "example": "my_dict['name'] → 'Sam'"
    }
]
