# Class, Attributes, Methods
'''class Students:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print("Accepting Data...")
        self.name = input("Enter name:")
        self.contact = input("Enter contact")

    def putdata(self):
        print("The name is: "+self.name, "\nThe contact is:"+self.contact)

class Science_student(Students): # Inheritance Science_student inherits from Students
    def __init__(self,age):
        self.age = age

    def info(self):
        print("I am a science student")

John = Science_student(20)
John.info()
John.getdata()
John.putdata()
'''
# Recursion
'''def factorial(x):
    if x == 1:
        return 1
    else :
        return x * factorial(x-1)
result = factorial(12)
print(result)'''

# Sets
'''numbers = {1, 2, 3, 4, 5, 6}
print(5 in numbers)
numbers.add(10)
numbers.remove(3)
print(numbers)
seta = {1, 2, 3, 4}
setb = {4, 5, 9, 7}
print(seta | setb)
print(seta & setb)
print(seta - setb)'''

# Itertools

'''from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break
'''
'''
from itertools import accumulate, takewhile

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))
'''
# Operator overloading
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = Point(x, y)
        return z
    def __str__(self):
         return"({0}, {1})".format(self.x, self.y)
point1 = Point(1, 4)
point2 = Point(2, 8)
point3 = point1 + point2
print(point3)

# Data Hiding
'''
class MyClass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable+= increment
        print(self.__hiddenvariable)
object = MyClass()
# object.__hiddenvariable Data encapsulation is done by writing dunders before variable
object.add(5)'''