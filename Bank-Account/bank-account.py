class BankAccount():
    def __init__(self, name, surnames, address, phone_number, nif, balance):
        self.name = name
        self.surnames = surnames
        self.address = address
        self.phone_number = phone_number
        self.nif = nif
        self.balance = balance

    def set():
        pass
    
    def get():
        pass

    def withdrawMoney(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            raise ValueError

    



if __name__ == '__main__':

    assert