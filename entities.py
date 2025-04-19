import json
import files

def file_log(func):
    """Register a log

    Args:
        func (_type_): function
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("activity.log", "a") as f:
            f.write("Contact created\n")
        return result
    return wrapper

def console_log(func):
    """Return a success message

    Args:
        func (_type_): function
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Contact Created")
        return result
    return wrapper

def save_data(file_name, data):
    """Save the new contect

    Args:
        file_name (_type_): name or path of the file
        data (_type_): new content

    Returns:
        _type_: create o overwrite the file_name
    """
    try:
        content = files.read(file_name)
    except FileNotFoundError:
        return files.create(file_name, [data])
    except Exception as e:
        return files.create(file_name, [data])
    
    return files.update(file_name, data)

class Contact:
    """Contact instance
    """
    def __init__(self, name, last_name, phone, email, street, Enum, Inum, col, mun, city, state, country):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.Enum = Enum
        self.Inum = Inum
        self.col = col
        self.mun = mun
        self.city = city
        self.state = state
        self.country = country

    @file_log
    @console_log
    def save(self):
        """Save the new instance
        """
        file_name = "contacts.json"
        return save_data(file_name, self.__dict__)

def find_contact(file_name, key, value):
    """Find a contact by key and value

    Args:
        file_name (str): name of the JSON file
        key (str): field to search
        value (str): value to match

    Returns:
        dict or str: contact or message
    """
    try:
        contacts = files.read(file_name)
        for c in contacts:
            if c.get(key) == value:
                return c
        return "Contact not found"
    except:
        return "File not found"

def total_contacts(file_name):
    """Return total number of contacts

    Args:
        file_name (str): name of the JSON file

    Returns:
        int: number of contacts
    """
    try:
        return len(files.read(file_name))
    except:
        return 0

def delete_contact(file_name, key, value):
    """Delete a contact by key

    Args:
        file_name (str): name of the JSON file
        key (str): field to match
        value (str): value to delete

    Returns:
        str: result message
    """
    try:
        contacts = files.read(file_name)
        new_list = [c for c in contacts if c.get(key) != value]
        with open(file_name, "w") as f:
            json.dump(new_list, f, indent=2)
        return "Contact deleted" if len(new_list) < len(contacts) else "Contact not found"
    except:
        return "File not found"

def list_contacts(file_name):
    """Return all contacts

    Args:
        file_name (str): name of the JSON file

    Returns:
        list: all contacts
    """
    try:
        return files.read(file_name)
    except:
        return []

def filter_contacts(file_name, key, value):
    """Filter contacts by field

    Args:
        file_name (str): name of the JSON file
        key (str): field to filter
        value (str): value to match

    Returns:
        list: filtered contacts
    """
    try:
        return [c for c in files.read(file_name) if c.get(key) == value]
    except:
        return []
