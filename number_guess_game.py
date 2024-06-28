import random
import time

print("Let's play guess a number...")
time.sleep(1)
print("The number range will begin at 0")
time.sleep(1)
print("and end at a number you choose.")
time.sleep(1)

top_of_range = input("Choose a number to end the range with: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number, silly.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

time.sleep(1)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number, silly.")
        continue

    if user_guess == random_number:
        print("You got it correct!")
        break
    elif user_guess > random_number:
        print("You were too high.")
    else:
        print("You were too low.")

print("You got it in", guesses, "guesses!")
