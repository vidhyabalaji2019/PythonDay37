# Contact Book Application

# Dictionary to store contacts
contacts = {
    "John Doe": {"phone": "9876543210", "email": "john@example.com"},
    "Alice Smith": {"phone": "9123456789", "email": "alice@example.com"},
}

# Function to add a new contact
def add_contact(name, phone, email):
    if name in contacts:
        print(f"{name} already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"{name} added successfully!")

# Function to update contact details
def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"{name}'s contact updated successfully!")
    else:
        print(f"{name} not found in contacts.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} not found in contacts.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("\n📒 Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print("-" * 30)
    else:
        print("No contacts available.")

# ------------------- Example Usage -------------------
add_contact("Bob Johnson", "9988776655", "bob@example.com")
update_contact("Alice Smith", phone="9111223344")
delete_contact("John Doe")
search_contact("Alice Smith")
display_contacts()
