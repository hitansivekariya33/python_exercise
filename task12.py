'''
BankAccount:
o Initialization: __init__ () method
1. Account holder name
2. Account number
3. Balance
4. Pin
o Check the pin of the user: check_pin():
1. The method check_pin() checks if user has entered correct pin, then
his/her account details will be shown.
o Deposit the money: deposit(amount) 1. Arguments:
a. Amount: The amount to be added in the back account 2. Conditions:
a. Check the pin number before deposit the money
b. If user enters the correct pin:
i. Add the money to the current balance of the user and show the message that “X rupees are successfully added to your account.”:
balance = balance + amount
o Withdraw the money: withdraw(amount) 1. Arguments:
a. Amount: The amount to be withdrawn from the bank account
2. Conditions:
a. Check the pin number before withdrawing money
b. If pin number is correct:
i. Check if user has sufficient balance for withdraw i.e. if user has 1000 rupees in his bank and he tries to withdraw 1200 rupees then show the message that “Your account don’t have sufficient balance”.
ii. If user has sufficient balance, then withdraw the money from account and show message that “X rupees has been withdrawn successfully” balance = balance – amount
o __str__() method: Display the user account details: 1. It should be display like:
Account Holder Name: User name
Account Number: User Bank Account number Total Balance: User total balance
 Operations and their expected output:
b1 = BankAccount(name=“Ram”,acct_num “12345”, balance=1000, pin=3456)
o Print(b1)
Account Holder Name: Ram
Account Number: 12345 Total Balance: 10000
o b1.deposit(200)
1. It will ask user to enter the pin.
2. If entered pin is wrong, then it should be print:
Please enter correct pin.
3. Else add the money to account
200 rupees added to account successfully.
o Print(b1)
Account Holder Name: Ram Account Number: 12345 Total Balance: 10200
o b1.withdraw(12000)
1. It will ask user to enter the pin.
2. If pin is entered correctly,
a. Here Ram has 10000 rupees in his bank and he trying to withdraw 12000, then show the message:
Your account don’t have sufficient balance
o b1.withdraw(8000)
1. It will ask for the pin first
2. If pin is entered correctly,
a. 8000 will be withdrawn from the account.
o Print(b1)
Account Holder Name: Ram Account Number: 12345 Total Balance: 2200

'''
class BankAccount:
    def __init__(self,name,acct_num,balance,pin):
        self.name = name
        self.acct_num = acct_num
        self.balance = balance
        self.pin = pin 
    #display detail
    def __str__(self):
        return f'Account Holder Name :~ {self.name} \nAccount Holder Number :~ {self.acct_num}\nTotal balance :~ {self.balance}'
    
    def check_pin(self):
        input_pin = int(input("Enter a correct pin :~ "))
        if input_pin == self.pin:
            return self.__str__()
        else:
            print("Oops! Your pin is incorrect")
    #deposit money
    def deposit(self,amount):
        input_pin = int(input("Enter a correct pin :~ "))
        if input_pin == self.pin:
            self.balance = self.balance + amount 
            print(amount,"added successfully")
            print("available balance ",self.balance)
        else:
            print("Oops! Your pin is incorrect")
    #withdraw money
    def withdraw(self,amount):
        input_pin = int(input("Enter a correct pin :~ "))
        if input_pin == self.pin:
            if self.balance <= amount :
                print("Your account don’t have sufficient balance.")
            else:
                self.balance = self.balance - amount 
                print(amount,"will be withdrawn from the account")
                print("Available balance ",self.balance)

b1 = BankAccount("Ram","Ram2323",2000,2323) 
print(b1.check_pin())
add_amount= int(input("Enter what you want to deposite :~ "))
b1.deposit(add_amount)
withdraw_amt= int(input("Enter what you want to withdraw :~ "))
b1.withdraw(withdraw_amt)