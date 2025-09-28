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
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input(str("What item would you like to add? \n")) # Prompt for and add an item
            pass
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == '2':
            item = input(str("What item would you like to remove? \n"))# Prompt for and remove an item
            pass
            if item not in shopping_list:
                print("Item is not found in the shopping list.")
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