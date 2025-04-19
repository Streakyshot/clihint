import os
from screens.logo import print_logo
from screens.menu import display_menu, show_cheats
from utils.loader import load_cheat_modules

def search_cheats(data, keyword):
    results = []
    keyword_lower = keyword.lower()

    for category, cheats in data.items():
        for cheat in cheats:
            if (
                keyword_lower in cheat["command"].lower()
                or keyword_lower in cheat["description"].lower()
                or keyword_lower in cheat["example"].lower()
            ):
                results.append((category, cheat))
    return results

def show_search_results(results):
    if not results:
        print("\n❌ No matches found.")
        input("\nPress Enter to return to menu...")
        return

    print("\n🔍 Search Results:")
    for i, (category, cheat) in enumerate(results, 1):
        print(f"\n[{i}] {category}")
        print(f"\033[1;36mCommand:\033[0m {cheat['command']}")
        print(f"\033[1;33mDescription:\033[0m {cheat['description']}")
        print(f"\033[1;34mExample:\033[0m {cheat['example']}")

    input("\n\033[1;36mPress Enter to return to menu...\033[0m")

def main():
    data = load_cheat_modules()
    categories = list(data.keys())

    while True:
        os.system("clear")
        print_logo()
        display_menu(categories)

        print("\n\033[1;32mS\033[0m. Search 🔍")
        choice = input("\nChoose a category or action: ").strip()

        if choice.lower() == "s":
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                os.system("clear")
                print_logo()
                results = search_cheats(data, keyword)
                show_search_results(results)
        elif choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            os.system("clear")
            print_logo()
            show_cheats(category, data[category])
        else:
            input("\n❌ Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()
