from enum import Enum
from passwd_validation import *
import secrets

class role(Enum):
    CLIENT = 1
    PREMIUM_CLIENT = 2 #Premium Client
    FINANCIAL_PLANNER = 3 #Financial Advisor
    FINANCIAL_ADVISOR = 4 #Financial Planner
    TELLER = 5

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
    def checkOperation(self, role:int, viewP, editP):
        return False

class user:
    def __init__(self, username: str, password: str, role: role):
        self.__username = username
        self.__password = password
        self.role = role
        self.__authorizedOp = []
    def addOp(self, oj: object, viewP: bool, editP: bool):
        self.__authorizedOp.append([oj, viewP, editP])
    def checkPerm(self, numO:int):
        if numO >= len(self.__authorizedOp):
            return [None, False, False]
        return self.__authorizedOp[numO]



def addUser(username:str, psswd:str, role):
    """
    Problem 2
    This functions handles adding a user to the passwd.txt file.
    Before adding the user to teh file, we make sure that their password
    is valid according to the requirements. We also make sure that the username doesn't already exist.

    :param username: user's username
    :param psswd: user's password
    :param role: user's role
    :return: Return True if success or false otherwise
    """
    strong = False
    strong = validate(username, psswd)
    #strong = strong and commonPassword(psswd)
    if strong:
        salt = secrets.token_hex(32)
        hashPsswd = hashFunc(salt, psswd)
        with open("passwd.txt", "a") as file:
            file.write(username+","+salt+","+hashPsswd+","+str(role)+"\n")
        return True
    return False

def checkUser(username:str, psswd:str):
    """
    Problem 2
    This function handles the retrieval of user information from the passwd.txt file
    and make sure that the username matches and then check if the password hash matches using the same hash
    function. verification function used below verify the username and the password.

    :param username:
    :param psswd:
    :return: TRUE/FALSE, ROLE/FALSE
    """
    with open("passwd.txt", "r") as file:
        for line in file:
            userInfo = line.split(",")
            if userInfo[0] == username:
                return verification(userInfo, psswd), int(userInfo[3])
    return False, False

if __name__ == '__main__':
    print(addUser("Test1", "Carleton12@",1))
    print(addUser("Test2", "Carleton12",1))
    print(addUser("Test3", "Carl12@",1))
    print(addUser("Test4", "hello12@",1))
    checkUser("samimnif", "asdada")