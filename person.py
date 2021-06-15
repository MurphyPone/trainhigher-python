class person():
    # functions that are bookended by two underscores are reserved
    # __init__ is the "constructor" of a class
    # we call it to create an instance of a class
    def __init__(self, first_name, last_name, age, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.friends = []

    def change_name(self, first, last):
        self.first_name = first
        self.last = last 

    def is_birthday(self, day):
        if self.birthday == day:
            return True
        else:
            return False

    