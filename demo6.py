# Dictionaries
'''age = {"Ram": 32, "Laxman": 28, "Bharat": 30}
print(age["Ram"])

numbers ={1: "one",
          2: "two",
          3: "three"
          }
print(5 in numbers) # To check whether a no is present in dictionary
print(numbers.get(5,"Key not found")) '''

# Tuples
'''fruits = ("apple", "banana", "cherry") # use small brackets for tuples
fruits[0] = "moonpie"
print(fruits[0])
'''
# List Slicing
'''numbers = [0, 100, 200, 300, 400, 500, 600]
print(numbers[0::3]) # [start:end:interval]
# List Comprehension
list = [x**2 for x in range(10) if x**2 % 2 ==0]
print(list)'''

# String Formatting
list = [12, 12, 2020]
string = "Date:{0}/{1}/{2}".format(list[0], list[1], list[2])
print(string)
# String Functions
'''print(":".join(["Apple", "Banana", "Cherry"])
# print("Hello World".replace("Hello","Hi"))


string = "Hello World."
print(string.replace("World", "there"))
'''

string = "This is the string"
print(string.startswith("this"))
print(string.upper())
print(string.lower())

# Numeric Functions

print(min(1,2,10,100))
print(max(100,1000,2000,250,350))
print(abs(-900))