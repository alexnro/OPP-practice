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
        self.balance -= money


    def depositMoney(self, money):
        self.balance += money


    def checkAccount(self):
        return f'{self.name}, {self.surnames}, {self.address}, {self.phone_number}, {self.nif}, {self.balance}'


    def negativeBalance(self):
        if self.balance >= 0:
            return False
        else:
            return True
    

    
if __name__ == "__main__":


    myBankAccount = BankAccount("Alex", "Navarro", "C/ Despuig", 635789521, "46851294D", 600)

    assert myBankAccount.getName() == "Alex"
    assert myBankAccount.getSurnames() == "Navarro"
    assert myBankAccount.getAddress() == "C/ Despuig"
    assert myBankAccount.getPhoneNumber() == 635789521
    assert myBankAccount.getNif() == "46851294D"
    assert myBankAccount.getBalance() == 600

    myBankAccount.withdrawMoney(200)
    assert myBankAccount.getBalance() == 400

    myBankAccount.depositMoney(500)
    assert myBankAccount.getBalance() == 900

    assert myBankAccount.checkAccount() == "Alex, Navarro, C/ Despuig, 635789521, 46851294D, 900"

    assert myBankAccount.negativeBalance() == False

    myBankAccount.withdrawMoney(900)
    assert myBankAccount.negativeBalance() == False

    myBankAccount.withdrawMoney(100)
    assert myBankAccount.negativeBalance() == True