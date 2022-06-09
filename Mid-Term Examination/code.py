"""
Student Name: {atiikah saesoh}
ID: {364211760045}
Grop: {MIT212}
"""

class Student:
    class Vehicle:
        def __init__(self, name, id, age, weight, height):
            # object Student
            self.name = name  # str
            self.id = id # str
            self.age = age  # int
            self.weight = weight  # float
            self.height = height  # int

        def displayDetail(self):
            print(f'f{self.name} {self.id} {self.age} {self.weight} {self.height }')

A = input('Student Name ?: ')
O = int(input('id ?:'))
T = int(input('Age ?: '))
K = float(input('Weight ?: '))
R = int(input('Height ?: '))
print('^^')