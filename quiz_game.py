import time

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Awww too bad :(")
    quit()
print("Okay let's play! Remember to spell correctly!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    time.sleep(1)
    print("I'm sorry, that is incorrect.")

answer = input("What GPU stand for? ")
if answer.lower() == "graphics processing unit":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    time.sleep(1)
    print("I'm sorry, that is incorrect.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    time.sleep(1)
    print("I'm sorry, that is incorrect.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    time.sleep(1)
    print("I'm sorry, that is incorrect.")
    time.sleep(1)

print("You got " + str(score) + " questions correct!")
time.sleep(1)
print("You got " + str((score/4) * 100) + "%")
time.sleep(1)

if score >= 3:
    print("You did pretty well!")
else:
    print("You didn't do well :(")
