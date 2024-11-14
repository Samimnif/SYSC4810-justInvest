import hashlib

def hashFunc(salt, psswd:str):
    h = hashlib.sha256()
    h.update((salt+psswd).encode())
    return h.hexdigest()

def validate(username:str, psswd:str):
    length = False
    upperCase = False
    lowerCase = False
    number = False
    special = False
    uname = False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    specialChar = ["!", "@", "#", "$", "%", "*", "&"]
    for i in psswd:
        #print(i)
        if i == i.upper():
            upperCase = True
        if i == i.lower():
            lowerCase = True
        if i in digits:
            number = True
        if i in specialChar:
            special = True
    if username.lower() not in psswd.lower():
        uname = True
    if len(psswd) >= 8 and len(psswd) <= 12:
        length = True
    if upperCase and lowerCase and number and special and uname and length:
        return True
    return False

def commonPassword(psswd:str):
    with open("weak_passwords.txt", "r") as file:
        weak_passwords = set(line.strip() for line in file)
        if psswd in weak_passwords:
            return False
    return True

def verification(userInfo:list[4], psswd:str):
    return str(userInfo[2]) == str(hashFunc(userInfo[1], psswd))

if __name__ == '__main__':
    print(validate("samimnif","SamiMnif123"))
    print(validate("hedimnif", "SamiMnif123"))
    print(validate("samimnif", "SamiMnif122!"))
    print(validate("hedimnif","SamiMnif122!"))
    print(validate("hedimnif", "SamiMnif1122!"))
    print(commonPassword("admin"))
    print(commonPassword("hello"))
    print(commonPassword("SamiMnif11223"))
    print(verification(['samimnif', '1', '925f9cb7bc3e181700668b83c6a2c164f2cdf0faa05f5f16d55b5929a34c9e04', 'role\n'],"adssd"))