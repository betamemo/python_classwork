class Person:
    def __init__(self, name, family_name, sex):
        self.name = name
        self.family_name = family_name
        self.sex = sex

    def greeting(self):
        return f'Hello {"Mr." if self.sex == "M" else "Ms."} {self.name}'

    def __str__(self):
        return f'Person {self.name} {self.family_name}'


person = Person('Jane', 'Doe', 'F')
print(isinstance(person, Person))
print(person)  # __str__
print(person.greeting())
