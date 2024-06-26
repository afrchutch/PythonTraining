# Training file 1
import time
name = input("What's your name?: ")
answers = ("Good", "Okay", "Alright", "Great")

print("Hello "+name)
time.sleep(0.5)

question1 = input("How is your day? ")

if question1 in answers:
    print("Glad to hear that, "+ name +" :)")
else:
    print("Sorry, "+name+ " :(")
