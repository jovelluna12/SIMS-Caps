import Employee
import dbConnector
class Manager (Employee.Employee):

    def approveEmployee(self,AppID,status):
        print("approve employee")

    def viewInventory(self):
        print("Viewing Inventory")

    def viewSalesTransaction(self):
        print("viewing Sales Transaction")

    def AddEmployees(self,EmpID,name, username, password, role):
        dbcursor =  dbConnector.db.cursor()
        self.EmpID=EmpID
        self.name=name
        self.username=username
        self.password=password
        self.role=role
        query="INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        value=(self.EmpID,self.name,self.username,self.password,self.role)
        dbcursor.execute(query,value)
        dbcursor.close()
        dbConnector.db.commit()
        dbConnector.db.close()
