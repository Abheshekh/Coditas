class user:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self._balance = balance

    def checkBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance

