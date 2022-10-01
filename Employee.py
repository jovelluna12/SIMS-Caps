import randomNumGen, dbConnector,random
class Employee:
    def __init__(self):
        self.username=""
        self.password=""
        self.AccID=""
        self.name=""
        self.role=""
        self.cursor=dbConnector.dbcursor

    def login(self,username,password):
        print("Login Logic")

        username , password


    def attendance(self,date, timeIn, timeOut):
        print(date," ", timeIn," ",timeOut)

    def addNewTransaction(self,TotalPrice,Discount,attendedBy,DatePurchased,items):
        PurchaseID, InvoiceNumber = randomNumGen.generateNum()

        dbcursor=self.cursor
        query1="insert into salestransaction values (%s,%s,%s,%s,%s)"
        values=(InvoiceNumber,TotalPrice,Discount,attendedBy,DatePurchased)
        dbcursor.execute(query1,values)

        query2="insert into purchasedproducts values (%s,%s,%s,%s)"
        n1=0
        n2=1
        item=[x[n1] for x in items]
        quantity=[x[n2] for x in items]

        query3="update products set Quantity=Quantity-%s where ProductName LIKE %s"
        for x in range(len(item)):
            PurchaseID=randomNumGen.generatePurchaseID()
            items=(PurchaseID,item[x],quantity[x],InvoiceNumber)
            dbcursor.execute(query2,items)
            query3val=(quantity[x],item[x])
            dbcursor.execute(query3,query3val)

        dbConnector.db.commit()
        dbConnector.db.close()
        return "done"

    def viewDeliveryList(self,itemName,datePurchased,expectedArrivalDate,quantity,status):
        print(itemName,datePurchased,expectedArrivalDate,quantity,status)



    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price):
        print(productName,itemCode,Quantity,status,Price)



