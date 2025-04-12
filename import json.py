import json

# Load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    for name, details in contacts.items():
        print(f"{name}: {details['Phone']} | {details['Email']} | {details['Address']}")

# Search contact by name
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]['Phone']} | {contacts[name]['Email']} | {contacts[name]['Address']}")
    else:
        print("Contact not found!")

# Update a contact
def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Delete a contact
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main menu
contacts = load_contacts()
while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again!")
