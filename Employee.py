import dbConnector
class Employee:
    def __init__(self):
        self.username=""
        self.password=""
        self.AccID=""
        self.name=""
        self.role=""

    def login(self,username,password):
        print(username," ",password)

    def attendance(self,date, timeIn, timeOut):
        print(date," ", timeIn," ",timeOut)

    def addNewTransaction(self,item,quantity,transactedBy,totalPrice,discount):
        print(item,quantity,transactedBy,totalPrice,discount)

    def viewDeliveryList(self,itemName,datePurchased,expectedArrivalDate,quantity,status):
        print(itemName,datePurchased,expectedArrivalDate,quantity,status)

    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price):
        print(productName,itemCode,Quantity,status,Price)