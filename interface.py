from user import *
import json

RED = "\033[31m"
BLUE = "\033[44m"
YELLOW = "\033[43m"
GREEN = "\033[42m"
RESET = "\033[0m"

sessionUser = None
operations = []

with open('objects.json', 'r') as file:
    data = json.load(file)
    for i in data:
        operations.append(object(i, data[i][0], data[i][1]))

def login():
    global sessionUser
    print("Please enter your Username and Password to login:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    verf,role = checkUser(username, password)
    if verf:
        sessionUser = user(username, password, role)
        print(GREEN+"ACCESS GRANTED!",RESET)
        return True
    print(RED+"Wrong Username or Password, please try again ...",RESET)
    return False

def signup():
    print("Please select one of these roles:\n1. Client\n2. Premium Client\n3. Financial Advisor\n4. Financial Planner\n5.Teller")
    while True:
        roleSelected = input("> ")
        if roleSelected in ["1", "2", "3", "4", "5"]:
            break
        print(RED+"Wrong input, try again ...",RESET)
    print("Please enter a Username and Password to sign up:\nMake sure that your password:\n"
          "* Doesn't contain your Username\n"
          "* Must be between 8 and 12 characters in length\n"
          "* Must contain: 1 Upper-Case letter, 1 lower-Case letter, 1 numerical digit and;\n"
          "one special character from the following: !, @, #, $, %, *, &")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if addUser(username, password, roleSelected):
        print(GREEN + "SIGNUP Success!", RESET)
    else:
        print(RED + "You didn't satisfy the requirements, please try again ...", RESET)


if __name__ == '__main__':
    print(BLUE,"Hello there! Welcome to justInvest Banking System",RESET)
    while True:
        print("Please Select one of these options:\n1: Login\n2: Sign-Up")
        sel1 = input("> ")
        if sel1 == "1":
            if login():
                print("Your Status is:", YELLOW+role(sessionUser.role).name+RESET)
                print("Here are the list of Authorized Operations:")
                for i, o in enumerate(operations):
                    view, edit = o.authorizedOperations(sessionUser.role)
                    if view:
                        print(i,"- View", o.title)
                    if edit:
                        print(i,"- Edit", o.title)

        elif sel1 == "2":
            signup()
        else:
            print("Unknown Selection")
            continue