def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Exit")

shopping_list = []

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))  # Convert input to int ✅
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")
        elif choice == 2:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
