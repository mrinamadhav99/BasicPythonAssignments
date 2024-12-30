class MenuManager:
    def __init__(self, size):
        self.menu_card = []
        self.size = size

    def display_menu(self):
        if not self.menu_card:
            print("The menu is currently empty.")
        else:
            print("Menu:")
            for item in self.menu_card:
                print(item)

    def add_items(self):
        print(f'Enter {self.size} string values:')
        for i in range(self.size):
            value = input(f'Enter string {i + 1}: ')
            self.menu_card.append(value)
        print("Items added successfully.")
        self.display_menu()

    def add_item(self, item):
        self.menu_card.append(item)
        print('Item added successfully.')
        self.display_menu()

    def update_item(self, old_item, new_item):
        if old_item in self.menu_card:
            index = self.menu_card.index(old_item)
            self.menu_card[index] = new_item
            print('Item updated successfully.')
        else:
            print('Invalid food item! Please try again.')
        self.display_menu()

    def delete_item(self, item):
        if item in self.menu_card:
            self.menu_card.remove(item)
            print('Item deleted successfully.')
        else:
            print('Invalid food item! Please try again.')
        self.display_menu()

    def main(self):
        self.add_items()
        while True:
            print('-' * 50)
            print('Choose an option:', '\n1. Display', '\n2. Add', '\n3. Update', '\n4. Delete', '\n5. Exit')
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                self.display_menu()
            elif choice == 2:
                new_item = input('Enter a food item to add: ')
                self.add_item(new_item)
            elif choice == 3:
                self.display_menu()
                old_item = input('Enter the item to update: ')
                new_item = input('Enter the new item: ')
                self.update_item(old_item, new_item)
            elif choice == 4:
                item_to_delete = input('Enter the item to delete: ')
                self.delete_item(item_to_delete)
            elif choice == 5:
                print("Exiting... Goodbye!")
                break
            else:
                print('Invalid choice! Please try again.')

# Instantiate and start the program
if __name__ == '__main__':
    size = int(input("Enter the number of initial strings to input: "))
    menu_manager = MenuManager(size)
    menu_manager.main()
