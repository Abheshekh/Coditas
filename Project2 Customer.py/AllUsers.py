import Users


# Simple function to clear screen as terminal functions not working in IDE
def clearScreen():
    print("\n" * 80)


# User based/ My Exception for invalid inputs
class invalidInput(Exception):
    def __init__(self, msg):
        self.errorMsg = msg

    def __str__(self):
        return str(self.errorMsg)


# User based/ My Exception for duplicate data at time of adding users`
class duplicate_error(Exception):
    def __init__(self, user_obj):
        self.errorMsg = 'Such Name Already exits'
        self.user_obj = user_obj

    def __str__(self):
        return str(self.errorMsg)


# Class allUsers for store all user created with user class from user.py file
class allUsers:
    def __init__(self):
        self.allCustomersList = []

    def getAllUsersDetails(self):
        # get details of users/customers
        # print(len(self.allCustomersList) >= 1)
        if len(self.allCustomersList) >= 1:
            print("Details of all users:")
            for user in self.allCustomersList:
                print("Name = ", user.name, end=" ")
                print("SurName = ", user.surname, end=" ")
                print("Balance = ", user.checkBalance())
        else:
            print("No customers,all details")

    # to add multiple users at a time one after oter
    def addMultipleUser(self):
        while True:
            try:
                clearScreen()
                # Requesting number of user to be added
                number_of_users = input('Please enter number of customers/users to be added = ')
                # check for invalid input
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

    # Method to check duplicate data/names
    def check_user_name_for_duplicate(self, name):
        # iterates through all names as return True / False as per duplicate data
        # and user object if such name exists
        for user in self.allCustomersList:
            if user.name == name[0] and user.surname == name[1]:
                return [True, user]
        return [False, None]

    # Method to add single user
    def addUser(self):
        user_duplicate_flag = False
        while True:
            try:
                name = input('Name of customer to be added = ')
                surname = input('SurName of customer to be added = ')
                # Requesting name and surname and checking for duplicates
                duplicate_stats = self.check_user_name_for_duplicate((name, surname))
                if duplicate_stats[0]:
                    raise duplicate_error(duplicate_stats[1])
                balance = int(input('Balance of customer to be added = '))
                clearScreen()
            except duplicate_error as duplicate:
                user_duplicate_flag = True
                clearScreen()
                print('=' * 50 + '\n', duplicate.errorMsg, '\n' + '=' * 50 + '\n')
                # User is given choice to update existing value or re-enter name if duplication found
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
        # finally created users are added to Total User List
        if not user_duplicate_flag:
            customer = Users.user(name, surname, balance)
            self.allCustomersList.append(customer)


# Wait function so that screen doesn't get cleared before user id ready
def wait():
    while True:
        char = input('Exit (Y/N) = ')
        if char == 'Y' or char == 'y':
            break
