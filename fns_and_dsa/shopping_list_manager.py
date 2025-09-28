def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == '1':
            item = input("Enter the item to add: ") # Prompt for and add an item
            pass
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == '2':
            item = input(str("Enter the item to remove: "))# Prompt for and remove an item
            pass
            if item not in shopping_list:
                print("Item is not found in the shopping list.")
            else:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
        elif choice == '3':
            print(shopping_list) # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()