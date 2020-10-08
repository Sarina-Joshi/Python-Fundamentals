# Coding challenge 2

'''food = ["toast", "sandwich", "burger", "pizza", "momo"]
#print(food[2])
food.append("sausage")
print(food)
food.insert(3, "tacos")
print(food)'''

# Coding challenge 3
# task 1
'''for x in range(0, 5):
    print("I am a programmer")
# task 2
def square():
    for x in range(1,10):
        y = x * x
        print(y)
square()
'''
# Coding Challenge part 3
'''
m = float(input("Enter mass:"))
h = float(input("Enter height:"))

def calc(m, h):
    bmi = m/(pow(h, 2))
    return bmi

result = calc(m,h)
print(result)
'''

# Exception Handling
'''
try:
    a = 20
    b = 0
    print(a/b)

except ZeroDivisionError:
    print("Please enter a non zero value")
'''
# Coding challenge part 4
'''def div(a,b):
    try:

       return a/b

    except ZeroDivisionError:
       print("Please enter a non zero value!!!")
    return 0
x = float(input("Enter the dividend:"))
y = float(input("Enter the divisor:"))
z = div(x, y)
print(z)
'''
# Coding challenge part 7
'''
product = {"book": 200, "copy": 20, "pencil": 5, "eraser": 2, "sharpener": 3}
print(product["eraser"])

products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}

newproduct = input('Enter product name')

if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
'''
# print(x for x in range(100) if x % 2 != 0)
'''new_list = list(range(1, 100))
for x in new_list:
    if x % 2 != 0:
        print(x)
'''

# C-8
# print((lambda x: x*(x+5)**2)(5))
'''def discount(x):
    return x-(0.1*x)

price = [100, 250, 350, 500]
result = list(map(discount, price))
print(result)

def student_discount(price):
    price = price - (price * 10) / 100
    return price

def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice

selling_price = 100

#applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))
'''
'''
# C-12
class Computer:
    def __init__(self,height, width):
        self.height = height
        self.width = width
    def getspecs(self):
        self.height = input("Enter computer's height:")
        self.width = input("Enter computer's width:")
    def displayspecs(self):
        print("Height:"+self.height, "\nWidth:"+self.width)
class Desktop(Computer):
    def __init__(self, color):
        self.color = color
    def info(self):
        print("Color: Black")
class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight
    def info1(self):
        print("Weight(in kg): 6")

Lenovo = Desktop("blank")
Dell = Laptop(0)
Lenovo.getspecs()
Dell.info1()
'''
# C-13

class Number:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        x = self.x + other.x
        return x
num1 = Number(12)
num2 = Number(22)
print(num1 * num2)