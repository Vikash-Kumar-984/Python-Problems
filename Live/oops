# Modular Coding

class Account:
    # constructors to initialize the account details
    # __init__ -> gets automatically called when a new object is created
    def __init__(self, account_number, account_holder, balance):
        # self refers to the current instance/object of the class
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    # add the method named 'deposit' 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}. New balance is {self.balance}')
        else:
            print('Deposit amount should be positive.')
    
    # add the method named "withdraw"
    def withdraw(self, withdrawl_amt):
        if withdrawl_amt <= self.balance and withdrawl_amt > 0:
            self.balance -= withdrawl_amt
            print(f'{withdrawl_amt} withdrawl')
        else:
            print('Insufficient fund.')
    
    # add the method named "display"
    def display(self):
        print(f'Account Number: {self.account_number}, Account Holder Name: {self.account_holder}, Balance: {self.balance}')

# Inheritance: SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # polymorphism: display method to display the account details
    def display(self):
        print(f'Account Number: {self.account_number}, Account Holder Name: {self.account_holder}, Balance: {self.balance}, Interest Rate: {self.interest_rate}')

    # added the interest in the savings account
    def add_interest(self):
        interest_value = self.balance * self.interest_rate / 100
        self.balance += interest_value
        print(f'Interest added: {interest_value}. New balance: {self.balance}')
    
# driver code
if __name__=='__main__':
    # object is created
    acc1 = SavingsAccount('SA123', 'Vikash Kumar', 10000, 3)
    acc1.deposit(2000)
    acc1.add_interest()
    acc1.display()
    '''
    obj1 = Account('AC123', 'Vikash Kumar', 10000)
    obj1.deposit(5000)
    obj1.withdraw(2000)
    obj1.display()
    '''