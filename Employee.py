import dbConnector,randomNumGen
class Employee:
    def __init__(self):
        self.username=""
        self.password=""
        self.AccID=""
        self.name=""
        self.role=""
        self.cursor=dbConnector.dbcursor

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

    def getAttendance(self, employeeID):
        dbcursor =  dbConnector.db.cursor(buffered=True)
        query=f"""
            SELECT 
                AttendanceCode, 
                t2.name, 
                cast(Date as CHAR), 
                cast(DATE_FORMAT(TimeIn, "%H:%i:%S") as CHAR), 
                cast(DATE_FORMAT(TimeOut, "%H:%i:%S") as CHAR) 
            FROM `attendance` t1 
            left join employees t2 on t1.employee = t2.EmpID 
            WHERE employee = {employeeID}
            """
        dbcursor.execute(query)
        rows = dbcursor.fetchall()

        return rows

    def attendance(self,date, timeIn, timeOut,employeeID):
        dbcursor =  dbConnector.db.cursor()
        query="INSERT INTO attendance (Date, TimeIn, TimeOut, employee) VALUES(%s,%s,%s,%s)"
        value=(date,timeIn, timeOut, employeeID)
        dbcursor.execute(query,value)
        dbcursor.close()
        print(date," ", timeIn," ",timeOut, " ",employeeID)

        print(dbcursor.lastrowid)

        dbConnector.db.commit()
        return dbcursor.lastrowid


    def addNewTransaction(self,TotalPrice,Discount,attendedBy,items):
        PurchaseID, InvoiceNumber = randomNumGen.generateNum()

        dbcursor=self.cursor
        query1="insert into salestransaction (InvoiceNumber,TotalPrice,Discount,attendedBy) values (%s,%s,%s,%s)"
        values=(InvoiceNumber,TotalPrice,Discount,attendedBy)
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

        return "done"

    def viewDeliveryList(self,itemName,datePurchased,expectedArrivalDate,quantity,status):
        print(itemName,datePurchased,expectedArrivalDate,quantity,status)



    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price):
        print(productName,itemCode,Quantity,status,Price)



