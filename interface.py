from user import *

RED = "\033[31m"
BLUE = "\033[44m"
GREEN = "\033[42m"
RESET = "\033[0m"

def login():
    print("Please enter your Username and Password to login:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if checkUser(username, password):
        print(GREEN+"ACCESS GRANTED!",RESET)
    else:
        print(RED+"Wrong Username or Password, please try again ...",RESET)

def signup():
    print("Please enter a Username and Password to sign up:\nMake sure that your password:\n"
          "* Doesn't contain your Username\n"
          "* Must be between 8 and 12 characters in length\n"
          "* Must contain: 1 Upper-Case letter, 1 lower-Case letter, 1 numerical digit and;\n"
          "one special character from the following: !, @, #, $, %, *, &")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if addUser(username, password, "1"):
        print(GREEN + "ACCESS GRANTED!", RESET)
    else:
        print(RED + "You didn't satisfy the requirements, please try again ...", RESET)


if __name__ == '__main__':
    print(BLUE,"Hello there! Welcome to justInvest Banking System",RESET)
    while True:
        print("Please Select one of these options:\n1: Login\n2: Sign-Up")
        sel1 = input("> ")
        if sel1 == "1":
            login()
        elif sel1 == "2":
            signup()
        else:
            print("Unknown Selection")
            continue