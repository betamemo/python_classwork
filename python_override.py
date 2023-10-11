class Parent:
    def __init__(self):
        self.from_parent = True
        print('Hello from parent')

    def get_eye_color(self):
        return 'blue'

    def hi(self):
        return f'Hi, my eyes are {self.get_eye_color()}'


class Child(Parent):
    def __init__(self):
        super().__init__()
        print('From child')

    def get_eye_color(self):
        return 'green'

    def get_hair_color(self):
        return super().get_eye_color()


child = Child()
print(child.hi())
print(child.get_hair_color())
