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
        if isinstance(birth, date) == False:
            raise TypeError
        self.name = name
        self.birth = birth
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Returns the initials of a name
        """
        initials = ""
        for words in self.name.split():
            initials = initials + words[0]
        return initials.upper()

    def is_birthday(self):
          """
          Validates if the users birthday is today
          """
          today = date.today()
          return today.month == self.birth.month and today.day == self.birth.day
                      

                
                
