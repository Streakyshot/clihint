B = "\033[1;34m"
C = "\033[1;36m"
G = "\033[1;32m"
Y = "\033[1;33m"
R = "\033[1;31m"
N = "\033[0m"

def display_menu(categories):
    print(f"\n{B}=== CLIHINT MAIN MENU ==={N}")
    for i, category in enumerate(categories, start=1):
        print(f"{Y}{i}.{N} {category}")
    print(f"{R}0.{N} Exit")

def show_cheats(category, cheats):
    print(f"\n{G}=== {category.upper()} ==={N}")
    for c in cheats:
        print(f"\n{C}Command:{N} {c['command']}")
        print(f"{Y}Description:{N} {c['description']}")
        print(f"{B}Example:{N} {c['example']}")
    input(f"\n{C}Press Enter to return to menu...{N}")
