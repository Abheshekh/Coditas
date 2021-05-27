import os
import platform
import Users
import AllUsers


class invalidInput(Exception):
    def __init__(self, msg):
        self.errorMsg = msg

    def __str__(self):
        return str(self.errorMsg)


def wait():
    while True:
        char = input('Exit (Y/N) = ')
        if char == 'Y' or char == 'y':
            break


def operations(operation_to_be_performed, customers_list):
    if operation_to_be_performed == 1:
        customers_list.addUser()
    elif operation_to_be_performed == 2:
        customers_list.addMultipleUser()
    elif operation_to_be_performed == 3:
        checkBalance(customers_list)
    elif operation_to_be_performed == 4:
        getAllUsersDetails(customers_list)


def getAllUsersDetails(customers_list):
    customers_list.getAllUsersDetails()
    wait()


def checkBalance(customers_list):
    flag = True
    if len(customers_list.allCustomersList) >= 1:
        name = input('Name of customer whose balance to be found = ')
        surname = input('SurName of customer whose balance to be found = ')
        for customer in customers_list.allCustomersList:
            if customer.name == name and customer.surname == surname:
                print('Request user ==> ', name, surname)
                print('User Balance = ', customer.checkBalance())
                flag = False
        if flag:
            print('Request user ==> ', name, surname,'not found!')
    else:
        print("No customers,checkBalance")
    wait()


def clearScreen():
    print("\n" * 80)


if __name__ == '__main__':
    # if platform.system().lower() == 'linux' or platform.system().lower() == 'darwin':
    #     clearScreen = 'cls'
    # elif platform.system().lower() == 'windows':
    #     clearScreen = 'clear'
    customersList = AllUsers.allUsers()
    while True:
        clearScreen()
        try:
            optionsStr = '{}\n{}\n{}\n{}\n{}\n{}'.format('1. Add Single User',
                                                         '2. Add Multiple User',
                                                         '3. Check Balance Single User',
                                                         '4. Check Details of All User',
                                                         '5. Exit',
                                                         'Choose operation to be done = ')
            operationToBePerformed = input(optionsStr)

            if not operationToBePerformed.isdigit():
                raise invalidInput('Please Enter "Integer" for selecting the operation')
            elif int(operationToBePerformed) >= 6:
                raise invalidInput('Please Enter "Integer" between 1 to 5')
            elif int(operationToBePerformed) == 5:
                # os.system(clearScreen)
                clearScreen()
                print('=' * 50 + '\n', "Thanks!!", '\n' + '=' * 50 + '\n')
                break
            else:
                # os.system(clearScreen)
                clearScreen()
                operations(int(operationToBePerformed), customersList)
        except invalidInput as exception:
            # os.system(clearScreen)
            clearScreen()
            print('=' * 50 + '\n', exception.errorMsg, '\n' + '=' * 50 + '\n')
        except Exception as exception:
            # os.system(clearScreen)
            clearScreen()
            print('=' * 50 + '\n', exception, '\n' + '=' * 50 + '\n')
