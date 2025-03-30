cheats = [
    {
        "command": "class Dog:\n    def __init__(self, name):\n        self.name = name",
        "description": "Defines a class with an initializer. Used to create structured objects.",
        "example": "d = Dog('Rex') → d.name = 'Rex'"
    },
    {
        "command": "class Dog:\n    def speak(self):\n        print('Woof!')",
        "description": "Defines a method inside a class (self refers to the instance).",
        "example": "d = Dog(); d.speak() → Woof!"
    },
    {
        "command": "class Animal:\n    def eat(self): print('nom')\n\nclass Dog(Animal):\n    pass",
        "description": "Inherits from a parent class (Animal). Dog inherits eat().",
        "example": "d = Dog(); d.eat() → nom"
    },
    {
        "command": "class Dog:\n    def __str__(self):\n        return 'This is a dog.'",
        "description": "Customizes the string output of an object.",
        "example": "print(Dog()) → This is a dog."
    },
    {
        "command": "@staticmethod\ndef bark(): print('Static bark!')",
        "description": "A method that doesn’t need access to the class/instance.",
        "example": "Dog.bark() → Static bark!"
    },
    {
        "command": "@classmethod\ndef build(cls): return cls()",
        "description": "Accesses the class itself rather than the instance.",
        "example": "Dog.build() creates a new Dog"
    },
    {
        "command": "def decorator(fn):\n    def wrap():\n        print('Before')\n        fn()\n    return wrap",
        "description": "A decorator wraps a function with extra behavior.",
        "example": "@decorator\ndef hello(): print('Hi')"
    },
    {
        "command": "from module import function",
        "description": "Imports a specific function from a Python module.",
        "example": "→ Clean access: function()"
    },
    {
        "command": "import my_module as mm\nmm.run()",
        "description": "Imports a whole custom module with an alias.",
        "example": "→ mm.run() instead of my_module.run()"
    },
    {
        "command": "if __name__ == '__main__':\n    main()",
        "description": "Standard entry point for any Python program or script.",
        "example": "Prevents code from running on import"
    },
    {
        "command": "class Counter:\n    count = 0\n    def inc(self):\n        Counter.count += 1",
        "description": "Static/class variables shared across all instances.",
        "example": "→ Count shared across objects"
    },
    {
        "command": "class Locked:\n    __secret = 'shhh'",
        "description": "Double underscore makes a variable private (name mangled).",
        "example": "→ _Locked__secret"
    },
    {
        "command": "class Dog:\n    def __call__(self):\n        print('Called like a function!')",
        "description": "Overrides call behavior so an object can be run like a function.",
        "example": "Dog()() → Called like a function!"
    },
    {
        "command": "from dataclasses import dataclass\n@dataclass\nclass User:\n    name: str\n    age: int",
        "description": "Creates a clean, boilerplate-free class with built-in __init__, __repr__, etc.",
        "example": "User('Sam', 15)"
    },
    {
        "command": "from abc import ABC, abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def draw(self): pass",
        "description": "Defines an abstract class that must be subclassed.",
        "example": "Enforces method overrides in child classes"
    },
    {
        "command": "try:\n    raise ValueError('Oops!')\nexcept ValueError as e:\n    print(e)",
        "description": "Manually raises an error and catches it.",
        "example": "Output: Oops!"
    },
    {
        "command": "assert 2 + 2 == 4",
        "description": "Checks a condition and throws AssertionError if it fails.",
        "example": "Used in testing or safety checks"
    },
    {
        "command": "globals()['my_var'] = 42",
        "description": "Dynamically sets a global variable using a string name.",
        "example": "→ my_var = 42"
    },
    {
        "command": "__name__",
        "description": "Special built-in that equals '__main__' when a script runs directly.",
        "example": "Used to control module behavior"
    },
    {
        "command": "vars(my_object)",
        "description": "Returns the internal __dict__ of an object (its attributes).",
        "example": "→ {'name': 'Void'}"
    }
]
