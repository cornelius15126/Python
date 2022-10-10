class Humans:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = Humans(name, age)

print(p1.name)
print(p1.age)