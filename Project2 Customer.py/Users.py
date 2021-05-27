# User class to contain Name Surname and Balance
class user:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self._balance = balance

# Getter Method to check balance
    def checkBalance(self):
        return self._balance

# Setter Method to check balance
    def setBalance(self, balance):
        self._balance = balance

