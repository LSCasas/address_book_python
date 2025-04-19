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
