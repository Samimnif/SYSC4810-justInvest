from user import *
import json
from datetime import datetime, time

RED = "\033[31m"
BLUE = "\u001B[34m"
YELLOW = "\033[43m"
GREEN = "\033[42m"
PURPLE = "\u001B[35m"
RESET = "\033[0m"

sessionUser = None
operations = []
SYSTEM_TIME = datetime.now().strftime("%H:%M")

start_Teller = time(9, 0)  # 9:00 AM
end_Teller = time(17, 0)   # 5:00 PM

with open('objects.json', 'r') as file:
    data = json.load(file)
    for i in data:
        operations.append(object(i, data[i][0], data[i][1]))

def login():
    """
    Problem 4
    This function just handles the login interface, where it displays the options and the inputs
    to the user to be able to login and then if authenticated correctly, then it show sthe user information, role
    and a list of access rights/permissions according to access control.

    :return: True if the login is correct, False otherwise
    """
    global sessionUser
    print("Please enter your Username and Password to login:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    verf,role = checkUser(username, password)
    if verf:
        if role == 5:
            current_time = datetime.strptime(SYSTEM_TIME, "%H:%M").time()
            if start_Teller <= current_time <= end_Teller:
                print("Teller system access"+GREEN+" GRANTED", RESET)
            else:
                print(RED+"Teller is not allowed to login at this time", RESET)
                return False

        sessionUser = user(username, password, role)
        print(GREEN+"ACCESS GRANTED!",RESET)
        return True
    print(RED+"Wrong Username or Password, please try again ...",RESET)
    return False

def signup():
    """
    Problem 3
    This function handles the signup process using the interface to request details from the user.
    It will check if the username and password are valid and then saves it to the passwd.txt file

    :return:
    """
    print("Please select one of these roles:\n1. Client\n2. Premium Client\n3. Financial Advisor\n4. Financial Planner\n5. Teller")
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

def set_time():
    """
    This function will help us test the Teller account where the TA can adjust the system time
    by entering a new time using the 24hr system (17:00 or 21:00)

    :return:
    """
    global SYSTEM_TIME
    print("Set System Time in 24h format:"+PURPLE+" (FOR TESTING PURPOSES ONLY)", RESET)
    time = input("> ")
    try:
        SYSTEM_TIME = datetime.strptime(time, "%H:%M").strftime("%H:%M")
        print(GREEN + "System time updated successfully to " + SYSTEM_TIME + RESET)
    except ValueError:
        print(RED+"Invalid time format. Please use HH:MM",RESET)

if __name__ == '__main__':
    print(BLUE,"Hello there! Welcome to justInvest Banking System",RESET)
    while True:
        print("System Clock: " + BLUE + SYSTEM_TIME + RESET)
        print("Please Select one of these options:\n1: Login\n2: Sign-Up\n3: Change System Clock")
        sel1 = input("> ")
        if sel1 == "1":
            if login():
                print("Your Status is:", YELLOW+role(sessionUser.role).name+RESET)
                print("Here are the list of Authorized Operations: (Type 'exit' to exit this selection)")
                for i, o in enumerate(operations):
                    view, edit = o.authorizedOperations(sessionUser.role)
                    if view:
                        print(i,"- View", o.title)
                        sessionUser.addOp(o, True, False)
                    elif edit:
                        print(i,"- Edit", o.title)
                        sessionUser.addOp(o, False, True)
                    else:
                        sessionUser.addOp(o, False, False)

                while True:
                    option_sel = input("> ")
                    if option_sel == "exit":
                        break
                    permCheckO = sessionUser.checkPerm(int(option_sel))
                    if permCheckO[1] or permCheckO[2]:
                        print("Operation "+GREEN+"GRANTED"+RESET)
                    else:
                        print("Operation " + RED + "DENIED" + RESET)

        elif sel1 == "2":
            signup()
        elif sel1 == "3":
            set_time()
        else:
            print("Unknown Selection")
            continue