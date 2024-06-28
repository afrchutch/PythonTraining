name = input("Type your name: ")
print("Welcome to this adventure,", name)

answer = input("You are on a dirt road and it has come to an end. You can go left or right. Which way would you like "
               "to go?: ").lower()
if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type walk to walk around, or swim to "
                   "swim across: ")

    if answer == "swim":
        print("You swam across and were eaten an alligator.")

    elif answer == "walk":
        print("You walked for many miles and ran out of water. You died.")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge that looks wobbly. Do you want to cross it or go back (cross/back)? ")

    if answer == "back":
        print("You go back to the main road. You lost.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ")
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You win the game!")

        elif answer == "no":
            print("You ignored the stranger and they are offended and kill you. You lose.")

    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")
