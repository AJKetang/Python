class Customer:
    def __init__(self, ID, name, value=0):
        self.ID = ID
        self.name = name
        self.value = value

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def get_discount(self, cost):
        pass

    def displayCustomer(self):
        print("ID: {} \n name:{} \n value:{} \n".format(self.ID, self.name, self.value))

class Member(Customer):
    def __init__(self, ID, name, value=0, rate_of_discount=0.05):
        super().__init__(ID, name, value)
        self.rate_of_discount = rate_of_discount

    def get_discount(self, cost):
        return(self.rate_of_discount, cost * self.rate_of_discount)

    def getRateOfDiscount(self):
        return self.rate_of_discount

    def displayCustomer(self):
        print("ID: {} \n name:{} \n value:{} \n discount rate:{}".format(self.ID, self.name,
                                                            self.value, self.rate_of_discount))

    def setRate(self, rate):
        self.rate_of_discount = rate
