import Employee
import dbConnector

class Owner(Employee.Employee):

    def generateSalesReport(self):
        print("Now Viewing Latest Sales Report")

    def forecastSales(self):
        print("now Forecasting Data")