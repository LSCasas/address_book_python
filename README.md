# Address Book Python

> This is the **first final challenge** of the **Kodemia Master Bootcamp - Backend with Python**.

A simple contact management system built in Python, using Object-Oriented Programming, decorators, and JSON file handling. This project allows you to create, list, search, filter, and delete contacts, with proper logging and error handling.

---

## 📁 Project Structure

```
├── entities.py       # Core logic: Contact class and operations
├── files.py          # File operations: create, read, update
├── main.py           # Example usage and execution
├── contacts.json     # JSON file where contacts are stored
├── activity.log      # Log file for activity tracking
```

---

## Features

- Create and save contact information
- Search contact by any key (e.g., email, phone)
- Delete contact by value match
- List all contacts
- Filter contacts by city, country, or any field
- Console and file logging using decorators
- Basic error handling for file operations

---

## Technologies

- Python 3
- JSON for storage (no external database required)

---

## How to Use

1. Clone or download the repo:

   ```bash
   git clone https://github.com/LSCasas/address_book_python.git
   cd address_book_python
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. Check `contacts.json` to see stored contacts.

---

## Example

```python
from entities import Contact

contact = Contact(
    "Emily", "Johnson", "9876543210", "emily.johnson@example.com",
    "Maple Street", "45", "Apt 3B", "Downtown", "Brooklyn", "New York", "NY", "USA"
)
contact.save()
```

---

## Requirements

- Python 3.x
- No third-party libraries required

---
