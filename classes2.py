"""This module contains a basic User class, an Admin subclass and
a Permission class used by the Admin subclass."""

class User():
    """Basic characteristics of a user"""

    def __init__(self, firstname, lastname, age, sex):
        """Initialize a specific user"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def user_description(self):
        """if called, provides basic info about the user"""
        print(f"Name: {self.firstname.title()} {self.lastname.title()}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
    

class Admin(User):
    """Example of a kind of user that inherits from the parent class"""
    def __init__(self, firstname, lastname, age, sex):
        """make an instance of an admin user with certain permissions"""
        super().__init__(firstname, lastname, age, sex)
        self.permissions = PermissionsClass()


class PermissionsClass():
    """different way of printing which permissions an admin user has"""
    
    def __init__(self, permissions = ["edit", "ban"], header = None):
        self.permissions = permissions
        self.header = header
            
    def show_admin_permissions(self, number_of_line_breaks = None):
        """Lists which permissions an admin user has."""
        """add an optional number of for clarity"""
        self.number_of_line_breaks = number_of_line_breaks
        for line_break in range(number_of_line_breaks):
            print("")
        """add an optional header for the permission data"""
        print(self.header)
        """print the actual permission data"""
        print(f"This admin user has the following permissions:")
        for permission in self.permissions:
            print(f"- {permission}")

user01 = Admin('fanny', 'pack', 22, 'female')
user01.user_description()
user01.permissions.permissions = [
# first '.permissions' refers to the Admin class;
# the second refers to the PermissionsClass class that's called from within the Admin class.
    'can edit posts',
    'can delete posts',
    'can ban users',
    'can lock threads',
]
# '.permissions' refers to the permissions attribute in the Admin class
# the permissions attribute calls the PermissionsClass class
# this class allows an optional header atrribute
# '.header' refers to that attribute
user01.permissions.header = "---PERMISSION OVERVIEW---" # this is the optional header
user01.permissions.show_admin_permissions(1) # print the permissions puls an optional number of line breaks

