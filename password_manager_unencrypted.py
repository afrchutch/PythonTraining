from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key_file = file.read()
    file.close()
    return key_file


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as passwords:
        for line in passwords.readlines():
            print(line)


def add():
    pwd_file = "passwords.txt"
    name = input('Account: ')
    username = input("Username: ")
    pwd = input("Password: ")
    header = "Account | Username | Password"

    if header not in pwd_file:
        with open(pwd_file, 'a') as passwords:
            passwords.write(header + "\n")
            passwords.write(name + " | " + username + " | " + pwd + "\n" + "\n")

    else:
        with open(pwd_file, 'a') as passwords:
            passwords.write(name + " | " + username + " | " + pwd + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
