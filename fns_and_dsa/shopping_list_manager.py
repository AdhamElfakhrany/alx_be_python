# shopping_list_manager.py

# -------- Menu Display Function --------
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Exit")

# -------- Shopping List Array --------
shopping_list = []

# -------- Main Logic --------
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))  # ✅ Input as number
        except ValueError:
            print("⚠️ Please enter a valid number (1-3).")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"✅ '{item}' added to your shopping list.")
        elif choice == 2:
            if not shopping_list:
                print("🛒 Your shopping list is empty.")
            else:
                print("\n🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == 3:
            print("👋 Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 3.")

# -------- Entry Point --------
if __name__ == "__main__":
    main()
