class AccountException(Exception):
    pass

class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0
    
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @account_number.setter
    def account_number(self, acct_num):
        raise AccountException('Fraud detected! Account numbers can not be changed.')
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountException('Account balance can not be negative.')
        else:
            if amount > 100000:
                print('Audit record for amounts exceeding $100,000')
            self.__balance = amount
    
    @account_number.deleter
    def account_number(self):
        if self.__balance > 0:
            raise AccountException('Warning: Account balance must be 0 to close the account.')
        else:
            self.__account_number = None
            self.__balance = None

my_account = Account(12345)
print('Account Number: {} has balance: ${:,.2f}'.format(my_account.account_number,  my_account.balance))

try:
    my_account.account_number = 98754
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    my_account.balance = 1000
    print('Account Number: {} has balance: ${:,.2f}'.format(my_account.account_number,  my_account.balance))
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    my_account.balance = -200
    print('Account Number: {} has balance: ${:,.2f}'.format(my_account.account_number,  my_account.balance))
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    my_account.balance += 1000000
    print('Account Number: {} has balance: ${:,.2f}'.format(my_account.account_number,  my_account.balance))
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    del my_account.account_number
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    my_account.balance = 0
    print('Account Number: {} has balance: ${:,.2f}'.format(my_account.account_number,  my_account.balance))
except AccountException as e:
    print("Account error ocurred:", e)

try:    
    del my_account.account_number
    print('Account Number: {} has balance: {}'.format(my_account.account_number,  my_account.balance))
    print('Account closed')
except AccountException as e:
    print("Account error ocurred:", e)