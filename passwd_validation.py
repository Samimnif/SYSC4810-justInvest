import hashlib

def hashFunc(salt, psswd:str):
    """
    Problem 2
    This function gets the salt and the password as params, and then
    it combines them both and hash them using teh SHA-256 algorithm.

    :param salt:
    :param psswd:
    :return: hashed password
    """
    h = hashlib.sha256()
    h.update((salt+psswd).encode())
    return h.hexdigest()

def getAllUsernames():
    """
    This function just returns all usernames that were already used for signup

    :return: list if usernames from passwd.txt
    """
    listUser = []
    with open("passwd.txt", "r") as file:
        for line in file:
            userInfo = line.split(",")
            listUser.append(userInfo[0].lower())
    return listUser

def validate(username:str, psswd:str):
    """
    Problem 3
    This function takes in the username and the password and then validates them.
    This is done by checking if the username isn't one of the previously used usernames,
    then it checks if the password complies with the requirements
    (8 to 12 characters, 1 Upper, 1 lower, 1 number, 1 special character [!, @, #, $, %, *, &])

    :param username:
    :param psswd:
    :return:
    """
    length = False
    upperCase = False
    lowerCase = False
    number = False
    special = False
    uname = False
    notExistingUserName = False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    specialChar = ["!", "@", "#", "$", "%", "*", "&"]
    for i in psswd:
        #print(i)
        if i.isupper():
            upperCase = True
        if i.islower():
            lowerCase = True
        if i in digits:
            number = True
        if i in specialChar:
            special = True
    if username.lower() not in psswd.lower():
        uname = True
    if username.lower() not in getAllUsernames():
        notExistingUserName = True
    if len(psswd) >= 8 and len(psswd) <= 12:
        length = True
    if upperCase and lowerCase and number and special and uname and length and notExistingUserName and commonPassword(psswd):
        return True
    return False

def commonPassword(psswd:str):
    """
    Problem 3
    This function takes in the password to be used for signup and checks if it parts of the common
    passwords.

    :param psswd:
    :return: True if it's not part of common passwords, False otherwise
    """
    with open("weak_passwords.txt", "r") as file:
        weak_passwords = set(line.strip() for line in file)
        if psswd in weak_passwords:
            return False
    return True

def verification(userInfo:list[4], psswd:str):
    """
    Problem 2
    This function takes in user info from teh psswd.txt file and the plain text psswd from the user input
    Then compares the hashes between the output from the function (using user's passwd)
    and the passwd hash saved in the file (userInfo[2])

    :param userInfo:
    :param psswd:
    :return: True if it is correct, False otherwise
    """
    return str(userInfo[2]) == str(hashFunc(userInfo[1], psswd))

if __name__ == '__main__':
    #print(getAllUsernames())
    print(validate("samimnif","SamiMnif123")) #missing charachter
    print(validate("smnif", "SamiMnif#")) #missing number
    print(validate("samimnif", "SamiMnif122!")) #username is in password
    print(validate("smnif","SamiMnif122!")) # This one is valid
    print(validate("smnif", "SamiMnif1122!")) #more than 12 char
    print(validate("smnif", "g00dPa$$w0rD")) #Althought password adheres to requirement it's common
    print(commonPassword("admin")) #common
    print(commonPassword("hello")) #common
    print(commonPassword("SamiMnif122!")) #not common
    print(commonPassword("g00dPa$$w0rD")) #common
    #print(verification(['samimnif', '1', '925f9cb7bc3e181700668b83c6a2c164f2cdf0faa05f5f16d55b5929a34c9e04', 'role\n'],"adssd"))