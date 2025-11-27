shopping_list = []

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print("'{item}' added to the list ")

    def remove_item():
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("'{}' removed from the list")
        else:
            print("'{item}' not found in the list")

            def view_list():
                if not shopping_list:
                    print("the shopping list is empty")
                else:
                    print("current shoppinglist ")
                for item in shopping_list:
                    print("-{item}")

    def main_menu():
        while True:
            print("\nMenu:")
            print("1. add an item")
            print("2. remove an item")
            print("3. view the list")
            print("4. Exit")
            choice = input("Enter yourr choice (1-4): ")

            if choice == '1':
                add_item()
            elif choice == '2':
                remove_item()
            elif choice == '3':
                view_list()
            elif choice == '4':
                print("exiting the shopping list manager. Goobye")
                break
            else:
                print("invalid choice. please enter a number between 1 and 4")

                main_menu()
