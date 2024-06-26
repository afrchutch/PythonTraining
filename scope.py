# scope = the region that a variable is recognized
#         a variable is only available form inside the region it is created
#         a global and locally scoped version of a variable can be created


name = "Cam" # global scope (available inside & outside functions)

def display_name():
    name = "Hutchings"  # local scope (available only inside this function)
    print(name)


display_name()
print(name)
