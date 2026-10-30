"""
Mini-Project: Command-Line Contact Book
-----------------------------------------
Practice organizing a real-world script using modular functions.
Complete the TODO sections to make the contact book fully functional.
"""

# Global storage for contacts
contacts = {}

def add_contact(name, phone, email):
    """
    Adds a new contact to the dictionary.
    If the contact already exists, print a warning message.
    """
    # TODO: Implement this function
    pass


def view_contacts():
    """
    Displays all stored contacts in a clean, readable format.
    If the contact book is empty, inform the user.
    """
    # TODO: Implement this function
    pass


def search_contact(name):
    """
    Searches for a contact by name and prints their phone and email.
    If the contact doesn't exist, let the user know.
    """
    # TODO: Implement this function
    pass


def delete_contact(name):
    """
    Deletes a contact by name if they exist in the dictionary.
    """
    # TODO: Implement this function
    pass


# --- Interactive Menu Loop (Starter Code Provided) ---
def main():
    """Runs the main application loop."""
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_contacts()
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()