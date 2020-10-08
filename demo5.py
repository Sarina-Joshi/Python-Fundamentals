#Passing  arguments
'''def add(x, y):
    print(x*y)
add(100, 200)
add(925, 789)

add("sam",3)'''

# Return value

'''def add(x,y):
    z = x+y
    return z
sum = add(200,400)
print(sum )'''


# Passing function in argument

'''x = input("Enter the value of x:")
y = input("Enter the value of y:")

x = int(x)
y = int(y)

def add(x, y):
    return x + y
def square(z):
    return z * z

result = square(add(x,y))
print("The result is", result )
#print(result)'''

# Modules in python
'''import random

for x in range(5):
    result = random.randint(1,1000)
    print(result)'''


# File Handling
'''file = open("demoo.txt", 'r')
content = file.read()
print(content)
file.close()'''

file = open("demoo.txt", 'w')
file.write("This is the text written to the file")
file.close()
file = open("demoo.txt", 'r')
content = file.read()
print(content)
file.close()
