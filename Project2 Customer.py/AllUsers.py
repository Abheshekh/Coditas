import Users


def clearScreen():
    print("\n" * 80)


class invalidInput(Exception):
    def __init__(self, msg):
        self.errorMsg = msg

    def __str__(self):
        return str(self.errorMsg)


class duplicate_error(Exception):
    def __init__(self, user_obj):
        self.errorMsg = 'Such Name Already exits'
        self.user_obj = user_obj

    def __str__(self):
        return str(self.errorMsg)


class allUsers:
    def __init__(self):
        self.allCustomersList = []

    def getAllUsersDetails(self):
        # print(len(self.allCustomersList) >= 1)
        if len(self.allCustomersList) >= 1:
            print("Details of all users:")
            for user in self.allCustomersList:
                print("Name = ", user.name, end=" ")
                print("SurName = ", user.surname, end=" ")
                print("Balance = ", user.checkBalance())
        else:
            print("No customers,all details")

    def addMultipleUser(self):
        while True:
            try:
                clearScreen()
                number_of_users = input('Please enter number of customers/users to be added = ')
                if not number_of_users.isdigit():
                    raise invalidInput('Please enter Integer Value')
                else:
                    break
            except invalidInput as error:
                print('=' * 50 + '\n', error.msg, '\n' + '=' * 50 + '\n')
        for user_count in range(0, int(number_of_users)):
            clearScreen()
            print('Enter details of User', user_count + 1)
            self.addUser()

    def check_user_name_for_duplicate(self, name):
        # print("in check_user_name_for_duplicate")
        for user in self.allCustomersList:
            # print(name, user.name, user.surname, user.name == name[0] and user.surname == name[1])
            if user.name == name[0] and user.surname == name[1]:
                return [True, user]
        return [False, None]

    def addUser(self):
        user_duplicate_flag = False
        while True:
            try:
                name = input('Name of customer to be added = ')
                surname = input('SurName of customer to be added = ')
                duplicate_stats = self.check_user_name_for_duplicate((name, surname))
                if duplicate_stats[0]:
                    raise duplicate_error(duplicate_stats[1])
                balance = int(input('Balance of customer to be added = '))
                clearScreen()
            except duplicate_error as duplicate:
                user_duplicate_flag = True
                clearScreen()
                print('=' * 50 + '\n', duplicate.errorMsg, '\n' + '=' * 50 + '\n')
                duplicate_choice = input("1. Do you want to update the value?\nOr re-enter details press any key = ")
                if duplicate_choice == '1':
                    balance = int(input('Balance of customer ({} {}) to be updated = '.format(duplicate.user_obj.name,
                                                                                              duplicate.user_obj.surname
                                                                                              )))
                    clearScreen()
                    duplicate.user_obj.setBalance(balance)
                    break
            except Exception as ERROR:
                if 'invalid literal for int() with base 10' in str(ERROR):
                    print('=' * 50 + '\n', "Please enter balance as Number.", '\n' + '=' * 50 + '\n')
            if not user_duplicate_flag:
                print('Name = ', name, end=" ")
                print('Surname = ', surname, end=" ")
                print('Balance = ', balance)
                char = input('Check details\nEnter (E/e) for edit \nPress Enter to continue = ')
                if char != 'e' and char != 'E':
                    break
        if not user_duplicate_flag:
            customer = Users.user(name, surname, balance)
            self.allCustomersList.append(customer)


def wait():
    while True:
        char = input('Exit (Y/N) = ')
        if char == 'Y' or char == 'y':
            break
