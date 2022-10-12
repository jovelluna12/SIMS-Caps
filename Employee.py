import dbConnector
class Employee:
    def __init__(self):
        self.username=""
        self.password=""
        self.AccID=""
        self.name=""
        self.role=""

    def login(self,username,password):
        dbcursor =  dbConnector.db.cursor(buffered=True)
        query="SELECT * FROM employees where username = %s and password = %s limit 1"
        value=(username,password)
        dbcursor.execute(query,value)

        if dbcursor.rowcount > 0:
            row = dbcursor.fetchone()
            print("User found; returning 1")
            return {'result': 1, 'user': row}
        else:
            print("Not found; returning 0")
            return {'result': 0, 'user': None}

    def attendance(self,date, timeIn, timeOut):
        print(date," ", timeIn," ",timeOut)

    def addNewTransaction(self,item,quantity,transactedBy,totalPrice,discount):
        print(item,quantity,transactedBy,totalPrice,discount)

    def viewDeliveryList(self,itemName,datePurchased,expectedArrivalDate,quantity,status):
        print(itemName,datePurchased,expectedArrivalDate,quantity,status)

    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price):
        print(productName,itemCode,Quantity,status,Price)