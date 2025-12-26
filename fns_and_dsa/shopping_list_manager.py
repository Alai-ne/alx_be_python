shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"'{item}' added to the list.")

def remove_item(item):
    try:
        shopping_list.remove(item)
        print(f"'{item}' removed from the list.")
    except ValueError:
        print(f"'{item}' not found in the list.")

def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Current shopping list:")
        for item in shopping_list:
            print(f"- {item}")
