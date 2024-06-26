# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


print(add(1, 2, 3, 4))
