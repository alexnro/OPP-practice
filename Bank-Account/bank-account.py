class BankAccount():
    def __init__(self, name, surnames, address, phone_number, nif, balance):
        self.name = name
        self.surnames = surnames
        self.address = address
        self.phone_number = phone_number
        self.nif = nif
        self.balance = balance

    def getName(self):
        return self.name
    
    def getSurnames(self):
        return self.surnames

    def getAddress(self):
        return self.address
    
    def getPhoneNumber(self):
        return self.phone_number
    
    def getNif(self):
        return self.nif
    
    def getBalance(self):
        return self.balance

    def withdrawMoney(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            raise ValueError

    def depositMoney(self, money):
        self.balance += money

    def checkBalance(self):
        return self.balance

    def negativeBalance(self):
        if self.balance >= 0:
            return True
        else:
            return False

    



if __name__ == '__main__':

    myBankAccount = BankAccount('Alex', 'Navarro', 'C/ Despuig', 652147852, '4158746G', 350)

