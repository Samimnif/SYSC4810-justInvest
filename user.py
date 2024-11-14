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

class object:
    def __init__(self, title:str, view:list, edit:list):
        self.title = title
        self.__view = view
        self.__edit = edit
    def checkEditPermission(self, role:int)->bool:
        return role in self.__edit
    def checkViewPermission(self, role: int)->bool:
        return role in self.__view
    def authorizedOperations(self, role:int):
        return self.checkViewPermission(role), self.checkEditPermission(role)



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
            if userInfo[0] == username:
                return verification(userInfo, psswd), int(userInfo[3])
    return False

if __name__ == '__main__':
    checkUser("samimnif", "asdada")