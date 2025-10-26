# Inventory Management System

# Empty dictionary to store product details
inventory = {}

# Function to add a product
def add_product(product_id, name, price, quantity):
    inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
    print(f"Product {name} added successfully!")

# Function to update product details (price or quantity)
def update_product(product_id, key, value):
    if product_id in inventory:
        inventory[product_id][key] = value
        print(f"Product {product_id} updated successfully!")
    else:
        print("Product not found!")

# Function to remove a product
def remove_product(product_id):
    if product_id in inventory:
        del inventory[product_id]
        print(f"Product {product_id} removed successfully!")
    else:
        print("Product not found!")

# Function to display all products
def display_inventory():
    if inventory:
        for product_id, details in inventory.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")
    else:
        print("No products in inventory.")

# Example Usage
add_product(1, "Laptop", 800, 10)
add_product(2, "Mouse", 20, 50)
update_product(1, "price", 750)
remove_product(2)
display_inventory()
