# Section 7 # functional Programming

# LAMBDA: anonymous function

result = (lambda x: x**2)(360)
print(result)

# MAP
def square(x):
    return x**2
newlist = [10, 22, 33, 45, 60]
result = list(map(square, newlist))
print(result)
answer = list(map(lambda x: x**2, newlist))
print(answer)

# Filter
newlist = [1, 9, 2, 16, 4, 78]
result = list(filter(lambda x: x % 2 == 0, newlist))
print(result)