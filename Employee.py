import dbConnector,randomNumGen
class Employee:
    def __init__(self):
        self.cursor=dbConnector.dbcursor
        self.Db=dbConnector.db

    def login(self,username,password):
        dbcursor =  self.cursor
        query="SELECT * FROM employees where username = %s and password = %s limit 1"
        value=(username,password)
        dbcursor.execute(query,value)
    
        rows = dbcursor.fetchall()
        if dbcursor.rowcount > 0:
            row = rows[0]
            return {'result': 1, 'user': row}
        else:
            return {'result': 0, 'user': None}

    def getAttendance(self, employeeID):
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
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def attendance(self,date, timeIn, timeOut,employeeID):
        dbcursor =  self.cursor
        query="INSERT INTO attendance (Date, TimeIn, TimeOut, employee) VALUES(%s,%s,%s,%s)"
        value=(date,timeIn, timeOut, employeeID)
        dbcursor.execute(query,value)
        # print(date," ", timeIn," ",timeOut, " ",employeeID)
        # print(dbcursor.lastrowid)

        dbConnector.db.commit()
        return dbcursor.lastrowid


    def addNewTransaction(self,TotalPrice,Discount,attendedBy,items):
        PurchaseID, InvoiceNumber = randomNumGen.generateNum()

        dbcursor=self.cursor
        query1="insert into salestransaction (InvoiceNumber,TotalPrice,Discount,attendedBy) values (%s,%s,%s,%s)"
        values=(InvoiceNumber,TotalPrice,Discount,attendedBy)
        dbcursor.execute(query1,values)

        query2="insert into purchasedproducts values (%s,%s,%s,%s,%s)"
        n1=0
        n2=1
        n3=2
        id=[]
        item=[x[n1] for x in items]
        quantity=[x[n2] for x in items]
        id=[x[n3] for x in items]

        query3="update products set quantity=quantity-%s where ProductName LIKE %s and ProductID=%s"
        for x in range(len(item)):

            PurchaseID=randomNumGen.generatePurchaseID()
            items=(PurchaseID,item[x],quantity[x],InvoiceNumber,id[x])
            dbcursor.execute(query2,items)
            query3val=(quantity[x],item[x],id[x])
            dbcursor.execute(query3,query3val)

        dbConnector.db.commit()

    def viewDeliveryList(self):
        dbcursor=self.cursor
        query="SELECT deliverylist.BatchCode,products.ProductName,deliverylist.status,price,quantity,deliverylist.expectedarrivaldate FROM deliverylist, products WHERE deliverylist.status!='Arrived' AND products.status='Under Delivery' AND deliverylist.status!='Expired' AND products.batch_code=deliverylist.BatchCode;"
        dbcursor.execute(query)

        result=dbcursor.fetchall()
        return result

    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price,ExpiryDate):
        dbcursor = self.cursor
        ProductCode=randomNumGen.generateID()
        query="INSERT INTO productsindelivery VALUES (%s,%s,%s,%s,%s,%s)"
        values=(ProductCode,productName,itemCode,Quantity,status,Price,ExpiryDate)

        dbcursor.execute(query,values)
        dbConnector.db.commit()

    def addManyDeliveryList(self,items,batch_code,order_date,arrival_date,var):
        dbcursor = self.cursor

        query_list="INSERT INTO deliverylist VALUES(%s,%s,%s,%s)"
        dbcursor.execute(query_list, (batch_code,order_date,arrival_date,var))

        query = "INSERT INTO productsindelivery VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = items
        dbcursor.executemany(query, values)
        dbConnector.db.commit()

        return "success"

    def ListAllBatches(self):
        dbcursor = self.cursor
        query="SELECT BatchCode,datepurchased,expectedarrivaldate FROM deliverylist WHERE status='Under Delivery'"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result
