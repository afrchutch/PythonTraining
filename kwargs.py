# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):  # "**kwargs" in this line can equal anything as long as the "**" precedes it
#    print("Hello, " + kwargs['first'] + " " + kwargs['last'])
     print("Hello,", end=" ")
     for key, value in kwargs.items():
         print(value, end=" ")


hello(title="Mr.", first="Cameron", middle="D", last="Hutchings")
