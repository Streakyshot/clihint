cheats = [
    {
        "command": "print('Hello, world!')",
        "description": "Prints text to the screen. The most basic Python command.",
        "example": "Output: Hello, world!"
    },
    {
        "command": "name = input('Enter your name: ')",
        "description": "Gets user input and stores it in a variable.",
        "example": "User enters: Sam → Variable 'name' = 'Sam'"
    },
    {
        "command": "age = int(input('Enter age: '))",
        "description": "Takes input and converts it into an integer (typecasting).",
        "example": "Input: 15 → age is an int: 15"
    },
    {
        "command": "if age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "description": "Basic if-else condition. Checks if user is 18+.",
        "example": "age = 20 → Output: Adult"
    },
    {
        "command": "for i in range(5):\n    print(i)",
        "description": "Loops 5 times and prints numbers from 0 to 4.",
        "example": "Output: 0 1 2 3 4"
    },
    {
        "command": "while True:\n    break",
        "description": "An infinite loop that breaks immediately. Used for logic testing.",
        "example": "Breaks loop after 1 run"
    },
    {
        "command": "def greet(name):\n    return f'Hi {name}!'",
        "description": "Defines a function that returns a greeting.",
        "example": "greet('Sam') → 'Hi Sam!'"
    },
    {
        "command": "numbers = [1, 2, 3]",
        "description": "Creates a list of integers.",
        "example": "numbers[0] = 1"
    },
    {
        "command": "for n in numbers:\n    print(n)",
        "description": "Loops through a list and prints each item.",
        "example": "Output: 1 2 3"
    },
    {
        "command": "my_dict = {'name': 'Sam', 'age': 15}",
        "description": "Creates a dictionary with key-value pairs.",
        "example": "my_dict['name'] → 'Sam'"
    },
    {
        "command": "try:\n    1/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
        "description": "Handles exceptions to avoid crashing your program.",
        "example": "Output: Cannot divide by zero"
    },
    {
        "command": "import math\nprint(math.sqrt(16))",
        "description": "Uses the math module to get square root of a number.",
        "example": "Output: 4.0"
    },
    {
        "command": "class Dog:\n    def __init__(self, name):\n        self.name = name",
        "description": "Defines a class (Object-Oriented Programming).",
        "example": "Dog('Rex').name → 'Rex'"
    },
    {
        "command": "[x for x in range(5)]",
        "description": "List comprehension to generate a list.",
        "example": "Output: [0, 1, 2, 3, 4]"
    },
    {
        "command": "open('file.txt', 'r')",
        "description": "Opens a file in read mode. Useful for working with text files.",
        "example": "Returns a file object"
    },
    {
        "command": "with open('data.txt', 'w') as f:\n    f.write('Hello')",
        "description": "Writes data to a file. 'with' auto-closes the file.",
        "example": "Creates/overwrites file with: Hello"
    },
    {
        "command": "import random\nprint(random.randint(1, 10))",
        "description": "Generates a random integer between 1 and 10.",
        "example": "Output: 7 (random)"
    },
    {
        "command": "lambda x: x * 2",
        "description": "Creates an anonymous function (used for one-liners).",
        "example": "lambda(3) → 6"
    },
    {
        "command": "enumerate(['a', 'b', 'c'])",
        "description": "Returns index and value when looping through items.",
        "example": "for i, v in enumerate(['a','b']) → i=0, v='a'"
    },
    {
        "command": "set([1,2,2,3])",
        "description": "Creates a set (unique values only).",
        "example": "Output: {1, 2, 3}"
    }
]
