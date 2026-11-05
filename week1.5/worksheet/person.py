# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Constructor method for Person Class
        """
        if name == "":
            raise ValueError
        if isinstance(name, str) == False:
            raise TypeError
        if isinstance(birth, str) == False:
            raise TypeError
        self.name = name
        self.birth = birth
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Returns the initials of a name
        """
        name_list = self.name.split()
        first_name = name_list[0]
        surname = name_list[1]
        initials = first_name[0]
        initials = initials + surname[0]
        return initials.upper()

    def is_birthday(self):
          """
          Validates if the users birthday is today
          """
          date = date.today()
          date = date[5:9]
          if date == self.birth[0:]

p = Person("James Malone", "26-052008")
            
                      

                
                
