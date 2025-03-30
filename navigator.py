import os
from screens.logo import print_logo
from screens.menu import display_menu, show_cheats
from utils.loader import load_cheat_modules

def main():
    data = load_cheat_modules()
    categories = list(data.keys())

    while True:
        os.system("clear")
        print_logo()
        display_menu(categories)
        choice = input("\nChoose a category: ")

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            os.system("clear")
            print_logo()
            show_cheats(category, data[category])
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()
