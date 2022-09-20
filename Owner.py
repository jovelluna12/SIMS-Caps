import Employee, EmployeeCRUD
import dbConnector

class Owner(Employee.Employee):

    def generateSalesReport(self):
        print("Now Viewing Latest Sales Report")

    def forecastSales(self):
        print("now Forecasting Data")

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