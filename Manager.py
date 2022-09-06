import Employee

class Manager (Employee):

    def approveEmployee(self,AppID,status):
        print(AppID,status)

    def viewInventory(self):
        print("Viewing Inventory")

    def viewSalesTransaction(self):
        print("viewing Sales Transaction")

    def AddEmployees(self,name, username, password, role):
        print("new Employee Added")

