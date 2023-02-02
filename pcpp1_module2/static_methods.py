class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
    
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False

print("Valid:", Bank_Account.validate('123'))
print("Valid:", Bank_Account.validate('12345678901234567890'))

account_numbers = ['8' * 20, '7' * 4, '2222']

for acct in account_numbers:
    if Bank_Account.validate(acct):
        print('We can use', acct, 'to create a bank account.')
    else:
        print('The account number', acct, 'is not valid.')