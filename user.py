from enum import Enum
from passwd_validation import *
import secrets

class role(Enum):
    CLIENT = 1
    PCLIENT = 2 #Premium Client
    FADVISOR = 3 #Financial Advisor
    FPLANNER = 4 #Financial Planner
    TELLER = 5

class user:
    def __init__(self, username:str, password:str, role:role):
        self.__username = username
        self.__password = password
        self.role = role

def addUser(username:str, psswd:str, role):
    strong = False
    strong = validate(username, psswd)
    strong = strong and commonPassword(psswd)
    if strong:
        salt = secrets.token_hex(32)
        hashPsswd = hashFunc(salt, psswd)
        with open("passwd.txt", "a") as file:
            file.write(username+","+salt+","+hashPsswd+","+role)
        return True
    return False

def checkUser(username:str, psswd:str):
    with open("passwd.txt", "r") as file:
        for line in file:
            userInfo = line.split(",")
            print(userInfo)
            if userInfo[0] == username:
                return verification(userInfo, psswd)
    return False

if __name__ == '__main__':
    checkUser("samimnif", "asdada")