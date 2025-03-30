cheats = [
    {
        "command": "'hello'.capitalize()",
        "description": "Capitalizes the first letter of the string.",
        "example": "'hello' → 'Hello'"
    },
    {
        "command": "'HELLO'.isupper()",
        "description": "Checks if the string is all uppercase.",
        "example": "→ True"
    },
    {
        "command": "'python'.startswith('py')",
        "description": "Checks if a string starts with a given substring.",
        "example": "→ True"
    },
    {
        "command": "'data.csv'.endswith('.csv')",
        "description": "Checks if a string ends with a certain suffix.",
        "example": "→ True"
    },
    {
        "command": "'abc,def'.split(',')",
        "description": "Splits a string into a list by delimiter.",
        "example": "→ ['abc', 'def']"
    },
    {
        "command": "'-'.join(['a','b','c'])",
        "description": "Joins a list into a string with '-' in between.",
        "example": "→ 'a-b-c'"
    },
    {
        "command": "my_dict = {'a': 1, 'b': 2}\nmy_dict.keys()",
        "description": "Returns all keys in the dictionary.",
        "example": "→ dict_keys(['a', 'b'])"
    },
    {
        "command": "my_dict.values()",
        "description": "Returns all values in the dictionary.",
        "example": "→ dict_values([1, 2])"
    },
    {
        "command": "my_dict.items()",
        "description": "Returns key-value pairs as tuples.",
        "example": "→ dict_items([('a', 1), ('b', 2)])"
    },
    {
        "command": "my_dict.get('c', 'Not found')",
        "description": "Safely gets a value. Returns fallback if key doesn’t exist.",
        "example": "→ 'Not found'"
    },
    {
        "command": "default = {'name': 'Void', 'role': 'hacker'}\ndefault.update({'age': 16})",
        "description": "Adds or updates values in a dictionary.",
        "example": "→ {'name': 'Void', 'role': 'hacker', 'age': 16}"
    },
    {
        "command": "for key in my_dict:\n    print(key)",
        "description": "Loop through dictionary keys.",
        "example": "→ 'a'\n→ 'b'"
    },
    {
        "command": "for key, value in my_dict.items():\n    print(key, value)",
        "description": "Loop through both keys and values.",
        "example": "→ a 1\n→ b 2"
    },
    {
        "command": "reversed_list = list(reversed([1, 2, 3]))",
        "description": "Reverses a list.",
        "example": "→ [3, 2, 1]"
    },
    {
        "command": "sorted(['c', 'a', 'b'])",
        "description": "Sorts a list alphabetically.",
        "example": "→ ['a', 'b', 'c']"
    },
    {
        "command": "sorted(['c', 'a', 'b'], reverse=True)",
        "description": "Sorts a list in reverse order.",
        "example": "→ ['c', 'b', 'a']"
    },
    {
        "command": "my_dict = {k: v*2 for k,v in {'a':1, 'b':2}.items()}",
        "description": "Dictionary comprehension to transform values.",
        "example": "→ {'a': 2, 'b': 4}"
    },
    {
        "command": "names = ['sam', 'alex']\ncap_names = [n.capitalize() for n in names]",
        "description": "Capitalizes every name in a list using list comp.",
        "example": "→ ['Sam', 'Alex']"
    },
    {
        "command": "range(5, 0, -1)",
        "description": "Creates a countdown from 5 to 1.",
        "example": "→ 5, 4, 3, 2, 1"
    },
    {
        "command": "for _ in range(3):\n    print('Repeat')",
        "description": "Loop 3 times, ignoring index using underscore.",
        "example": "→ Repeat\n→ Repeat\n→ Repeat"
    }
]
