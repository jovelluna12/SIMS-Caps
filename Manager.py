import Employee
import dbConnector
class Manager (Employee.Employee):

    def approveEmp(self,AppID,status):
        print("approve employee")

    def viewInv(self):
        print("Viewing Inventory")

    def viewSales(self):
        print("viewing Sales Transaction")

    def AddEmp(self,EmpID,name, username, password, role):
        dbcursor =  dbConnector.db.cursor()
        query="INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        value=(EmpID,name,username,password,role)
        dbcursor.execute(query,value)
        dbcursor.close()
        dbConnector.db.commit()
        dbConnector.db.close()

    def AddEmpMany(self,val):
        dbcursor = dbConnector.db.cursor()
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        dbcursor.executemany(query,val)
        dbcursor.close()
        dbConnector.db.commit()
        dbConnector.db.close()
