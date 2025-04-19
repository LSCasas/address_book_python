"""File management"""
import json
import os

def create(file_name: str, content: dict = None):
    """Create a new contact file in JSON

    Args:
        file_name (str): The name of the file to create
        content (dict, optional): The content to write. Defaults to None.
    """
    mode = "w" if content else "x"
    try:
        with open(file_name, mode) as file:
            if content:
                json.dump(content, file, indent=2)
    except Exception as error:
        raise OSError(f"Error creating the file: {error}")
    


def update(file_name: str, content: dict):
    """Add a new contact

    Args:
        file_name (str): The name of the file to create
        content (dict): The content to add.
    """
    file = open(file_name)
    file_content = json.loads(file.read())
    file_content.append(content)
    file = open(file_name, "w")
    file.write(json.dumps(file_content))
    file.close()


def read(file_name: str)-> list:
    """Returns the content of the contact book

    Args:
        file_name (str): File name

    Returns:
        Contact Book
    """
    content = open(file_name).read()
    return json.loads(content)
