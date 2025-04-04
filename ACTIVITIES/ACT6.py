class Item:
    # Constructor to initialize an item object
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = []

    # Create (Add) a new item
    def add_item(self, item_id, name, description, price):
        if not self.is_unique_item_id(item_id):
            print(f"Error: Item ID {item_id} already exists.")
            return
        if price <= 0:
            print("Error: Price must be a positive value.")
            return

        new_item = Item(item_id, name, description, price)
        self.items.append(new_item)
        print(f"Item '{name}' added successfully.")

    # Read (Display) all items
    def display_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items:
            print(item)

    # Read (Display) a specific item by ID
    def display_item(self, item_id):
        item = self.get_item_by_id(item_id)
        if item:
            print(item)
        else:
            print(f"Error: Item with ID {item_id} not found.")

    # Update an existing item by ID
    def update_item(self, item_id, name=None, description=None, price=None):
        item = self.get_item_by_id(item_id)
        if item:
            if name:
                item.name = name
            if description:
                item.description = description
            if price:
                if price <= 0:
                    print("Error: Price must be positive.")
                    return
                item.price = price
            print(f"Item '{item_id}' updated successfully.")
        else:
            print(f"Error: Item with ID {item_id} not found.")

    # Delete an item by ID
    def delete_item(self, item_id):
        item = self.get_item_by_id(item_id)
        if item:
            self.items.remove(item)
            print(f"Item '{item_id}' deleted successfully.")
        else:
            print(f"Error: Item with ID {item_id} not found.")

    # Helper method to get an item by ID
    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    # Check if the item ID is unique
    def is_unique_item_id(self, item_id):
        return self.get_item_by_id(item_id) is None


def display_menu():
    print("\nItem Management Application")
    print("1. Add Item")
    print("2. Display All Items")
    print("3. Display Item by ID")
    print("4. Update Item")
    print("5. Delete Item")
    print("0. Exit")


def main():
    manager = ItemManager()

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5, 0 to exit): "))
            if choice == 1:
                # Add Item
                item_id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.add_item(item_id, name, description, price)
            elif choice == 2:
                # Display all items
                manager.display_items()
            elif choice == 3:
                # Display item by ID
                item_id = int(input("Enter item ID to display: "))
                manager.display_item(item_id)
            elif choice == 4:
                # Update item
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new item name (leave blank to keep current): ")
                description = input("Enter new item description (leave blank to keep current): ")
                price = input("Enter new item price (leave blank to keep current): ")

                # If the price is entered, ensure it's a valid number
                price = float(price) if price else None
                manager.update_item(item_id, name or None, description or None, price)
            elif choice == 5:
                # Delete item
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            elif choice == 0:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Error: Invalid input. Please enter a valid number. ({e})")


if __name__ == "__main__":
    main()
