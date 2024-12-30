class Bank_Account:
    BankName = "ICICI Bank"
    ROI = 5
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0
    def CreateAccount(self):
        self.Name = input('Enter the account Holder Name:')
        self.Amount = int(input('Enter the Amount'))
        self.Address = input('Enter the Adress')
        self.AccountNo = int(input('Eanter Account Number'))

    @classmethod
    def DisplayInformation(self):
        print('------Your Account Information----')
        print('Name of the Account Holder:',self.Name)
        print('Address:',self.Address)
        print('Account number:',self.AccountNo)
        print('Current Balance:',self.Amount)
        
        
    @staticmethod
    def DisplayBankInfo(cls):
        print('-------Display Bank Info---------')
        print('Bank Info',cls.BankName)
        print('ROI on FD',cls.ROI)

def main():
    Bank_Account.DisplayInformation();
    print('Bank Name:',Bank_Account.BankName)
    print("ROI:",Bank_Account.ROI)
    User_1 = Bank_Account()
    print('Creating First Account:')
    User_1.CreateAccount()
    User_1.DisplayInformation()
    print()
    User_2 = Bank_Account()
    print('Creating Second Account:')
    User_2.CreateAccount()
    User_2.DisplayInformation()
    
        