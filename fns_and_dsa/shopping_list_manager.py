shopping_list = []

def show_items():
    for item in shopping_list:
        print(item)

def add_items(item):
    shopping_list.append(item)

def remove_items(item):
    shopping_list.remove(item)




def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")






def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item name you wish to add: ")
            add_items(item)

        elif choice == 2:
            item = input("Enter the item you wish to remove: ")
            remove_items(item)
        
        elif choice == 3:
            show_items()
           
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
