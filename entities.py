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
    """Save the new content

    Args:
        file_name (_type_): name of the file
        data (_type_): dictionary

    Returns:
        The updated file 
    """
    content = files.read(file_name)
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
