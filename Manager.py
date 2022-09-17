import Employee
import dbConnector
class Manager (Employee.Employee):

    def approveEmp(self,AppID,status):
        print("approve employee")

    def viewInv(self):
        dbcursor = dbConnector.db.cursor()
        query="SELECT * FROM products"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def viewSales(self):
        dbcursor = dbConnector.db.cursor()
        query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item, purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.attendedBy,salestransaction.DatePurchased FROM salestransaction,purchasedproducts"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

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

    def EditEmp(self,id,name,username,password,role):
        dbcursor = dbConnector.db.cursor()
        query="UPDATE employees SET Name='%s', username='%s', password='%s',role='%s' WHERE EmpID=%s"
        value=(name,username,password,role,id)
        dbcursor.execute(query,value)
        dbcursor.close()
        dbConnector.db.commit()
        dbConnector.db.close()

    def deleteEmp(self,id):
        dbcursor = dbConnector.db.cursor()
        query="DELETE FROM employees where EmpID=%s"
        value=(id,)
        dbcursor.execute(query,value)
        dbcursor.close()
        dbConnector.db.commit()
        dbConnector.db.close()