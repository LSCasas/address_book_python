from entities import Contact, save_data, find_contact, total_contacts, delete_contact, list_contacts, filter_contacts

# Example of saving a contact
contact = Contact(
    "Emily", "Johnson", "9876543210", "emily.johnson@example.com",
    "Maple Street", "45", "Apt 3B", "Downtown", "Brooklyn", "New York", "NY", "USA"
)
contact.save()

# Search for a contact by email
print(find_contact("contacts.json", "email", "emily.johnson@example.com"))

# Total number of contacts
print("Total contacts:", total_contacts("contacts.json"))

# List all contacts
print(list_contacts("contacts.json"))

# Delete a contact by email
print(delete_contact("contacts.json", "email", "emily.johnson@example.com"))

# Bonus: filter contacts by city
print(filter_contacts("contacts.json", "city", "New York"))
