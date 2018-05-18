class User:
    id = None
    pw = None
    money = None
    str = ""
    # Constructor for user instance
    def __init__(self):
        self.name = "null"
        self.id = "null"
        self.pw = "null"
        self.money = -1

    # Set user data
    def setUser(self, id, pw, money):
        self.id = id
        self.pw = pw
        self.money = money
        self.str = id+pw+ str(money)

    def getStr(self):
        return self.str
