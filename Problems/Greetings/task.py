class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am {}!".format(self.name))

user_in = input()
output = Person(user_in)

Person.greet(output)
