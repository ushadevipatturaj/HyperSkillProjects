class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am {}!".format(self.name))

name_input = input()
my_person = Person(name_input)
my_person.greet()