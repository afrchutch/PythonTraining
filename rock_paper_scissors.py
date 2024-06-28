import random
import time

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #  rock is 0, paper is 1, scissors is 2

    computer_pick = options[random_number]
    print("Computer picked,", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        time.sleep(0.5)
        continue

    if user_input == "rock" and computer_pick == "rock":
        print("Tie!")
        time.sleep(0.5)
        continue

    if user_input == "paper" and computer_pick == "paper":
        print("Tie!")
        time.sleep(0.5)
        continue

    if user_input == "scissors" and computer_pick == "scissors":
        print("Tie!")
        time.sleep(0.5)
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        time.sleep(0.5)

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        time.sleep(0.5)

    else:
        print("You lost!")
        computer_wins += 1
        time.sleep(0.5)

print("You won,", user_wins, "times.")
time.sleep(0.5)
print("The computer won", computer_wins, "times.")
time.sleep(0.5)
print("Goodbye!")
