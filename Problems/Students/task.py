class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year

fn = input()
ln = input()
by = input()

identificaton = Student(fn, ln, by)

print(identificaton.id)
