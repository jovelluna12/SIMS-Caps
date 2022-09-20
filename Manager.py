import Employee, EmployeeCRUD
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

    def selectEmp(self,id):
        result=EmployeeCRUD.ViewEmp(id)
        return result

    def AddEmp(self,EmpID,name, username, password, role):
        EmployeeCRUD.AddEmp(EmpID,name,username,password,role)

    def AddEmpMany(self,val):
        EmployeeCRUD.AddEmpMany(val)

    def EditEmp(self,id,name,username,password,role):
        EmployeeCRUD.EditEmp(id,name,username,password,role)

    def deleteEmp(self,id):
        EmployeeCRUD.deleteEmp(id)