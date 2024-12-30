menu_card = ['dosa', 'idly', 'biriyani']

def display_menu():
    for item in menu_card:
        print(item)

def add_item(item):
    menu_card.append(item)
    print('Item added successfully.')
    display_menu()

def update_item(old_item, new_item):
    if old_item in menu_card:
        index = menu_card.index(old_item)
        menu_card[index] = new_item
        print('Item updated successfully.')
        display_menu()
    else:
        print('Invalid food item! Please try again.')

def delete_item(item):
    if item in menu_card:
        menu_card.remove(item)
        print('Item deleted successfully.')
        display_menu()
    else:
        print('Invalid food item! Please try again.')

def main():
    while True:
        print('-' * 50)
        print('Choose an option:', '\n1. Display', '\n2. Add', '\n3. Update', '\n4. Delete')
        choice = int(input())
        
        if choice == 1:
            display_menu()
        elif choice == 2:
            new_item = input('Enter a food item to add: ')
            add_item(new_item)
        elif choice == 3:
            display_menu()
            old_item = input('Enter the item to update: ')
            new_item = input('Enter the new item: ')
            update_item(old_item, new_item)
        elif choice == 4:
            item_to_delete = input('Enter the item to delete: ')
            delete_item(item_to_delete)
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    main()
