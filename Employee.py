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


    def addNewTransaction(self,item,quantity,transactedBy,totalPrice,discount):
        print(item,quantity,transactedBy,totalPrice,discount)

    def viewDeliveryList(self,itemName,datePurchased,expectedArrivalDate,quantity,status):
        print(itemName,datePurchased,expectedArrivalDate,quantity,status)

    def addProducttoDeliveryList(self,productName,itemCode,Quantity,status,Price):
        print(productName,itemCode,Quantity,status,Price)