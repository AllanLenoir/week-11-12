class CashRegister :
# Comment 1 : Defining the constructor 
    def __init__(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
        self._payment = 0   

# Comment 2 : method that count number of item and defining their price 
    def addItem(self, price) :
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

# Comment 3 : method that return the total price
    def getTotal(self) :
        return self._totalPrice
 
# Comment 4 : method that return the number of item
    def getCount(self) :
        return self._itemCount
    
# Comment 5 : getting ready for the next customer 
    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
        
    def giveChange(self, payment):
        self._payment = payment + self._totalPrice
        
register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)        
register2 = CashRegister()
register2.addItem(1.90)

print("number of item register1: " + str(register1._itemCount))
print()
print("number of item register2: " + str(register2._itemCount))
print()

print("total price register1: " + str(register1._totalPrice))
print()
print("total price register2: " + str(register2._totalPrice))
print()

reg = register1._totalPrice + register2._totalPrice


def getPounds():
        
    print("the amount of the total sale is: £ " + str(int(reg + 0.25)))

getPounds()
print(register1._payment)


