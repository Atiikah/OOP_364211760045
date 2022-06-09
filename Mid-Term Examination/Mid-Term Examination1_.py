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
            self.id = id  # str
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
vac = input('How many are you vaccianted? : ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
A1 = int(input('select: '))
B1 = input('Date(dd/mm/yyyy): ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
A2 = int(input('select: '))
B2 = input('Date(dd/mm/yyyy): ')

print('Student Infomation: ')
print('Student Name: ',A)
print('Age: ',T)
print('Weight: ',K)
print('vaccine 1: ',A1,'date: ',B1 )
print('vaccine 2: ',A1,'date: ',B2 )

print('^^')