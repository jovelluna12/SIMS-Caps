import Employee, dbConnector, ROP, Product
from datetime import datetime
class Manager (Employee.Employee):
    def __init__(self):
        self.dbcursor = dbConnector.dbcursor
        self.ROP=ROP
    def inventoryList(self):
        dbcursor = self.dbcursor
        query = "SELECT ProductID,ProductName,status,price,Quantity FROM products"
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        return result

    def productSales(self):
        dbcursor = self.dbcursor
        query = "SELECT purchasedproducts.PurchaseID,products.ProductName,purchasedproducts.Quantity,products.price, products.price*purchasedproducts.Quantity, salestransaction.DatePurchased FROM purchasedproducts,products,salestransaction WHERE purchasedproducts.InvoiceNumber=salestransaction.InvoiceNumber GROUP BY purchasedproducts.PurchaseID;"
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        return result
        
    def viewInv(self):
        dbcursor = self.dbcursor
        query="SELECT ProductID as ProdID ,ProductName,price,batch_code, quantity FROM products,deliverylist WHERE quantity!=0 AND products.status = 'Sellable' ORDER BY deliverylist.datepurchased ASC"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def get_export_data(self,report,date):
        dbcursor = self.dbcursor
        if report=="Sales":
            query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item,purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.DatePurchased FROM salestransaction, purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND DatePurchased=%s;"
        if report=="Inventory":
            query="SELECT products_directory.ref_id, products_directory.product_name,products_directory.price,SUM(products.quantity) FROM products_directory, products, deliverylist WHERE products.ref_id=products_directory.ref_id AND deliverylist.datepurchased=%s AND deliverylist.status='Under Delivery' AND products.status='Under Delivery';"
        if report=="Delivery":
            query="SELECT batch_code,ProductName,quantity,price,deliverylist.status FROM products,deliverylist WHERE deliverylist.status='Under Delivery' AND deliverylist.datepurchased=%s AND products.batch_code=deliverylist.BatchCode;"
        dbcursor.execute(query,(str(date),))
        return dbcursor.fetchall()

    def notify_low_quantity(self):
        ROP=self.ROP.calculate_ROP()
        quantity=0
        if quantity<=ROP:
            return "Low Product"

    def notify_expired(self):
        dbcursor=self.dbcursor
        query="SELECT ProductID,ProductName,expiry_date,batch_code FROM products WHERE status!='Expired'"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        id=[]
        name=[]
        batch=[]
        x=0
        
        for i in result:
            if result[x][2]==datetime.today().date():
                id.append(result[x][0])
                name.append(result[x][1])
                batch.append(result[x][3])
                return f"Product {result[x][1]} is Unsellable"
            x+=1
        # return list(zip(id,name,batch))

    def notify_expiry(self):
        dbcursor=self.dbcursor
        query="SELECT ProductID,ProductName,expiry_date,batch_code FROM products WHERE status!='Expired' AND status!='Unsellable'"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        id=[]
        name=[]
        batch=[]
        x=0

        notif_list=[]
        expire_list=[]

        for i in result:
            days_left=7
            if result!=None:
                diff=result[x][2]-datetime.today().date()
                today_left=diff.days

                if today_left<=0:
                    man=Product.product()
                    man.editStatus('Unsellable',result[x][0])
                else:
                    id.append(result[x][0])
                    name.append(result[x][1])
                    batch.append(result[x][3])
                        
                    notif_list.append(result[x][1])  
                    expire_list.append(today_left)

            x+=1
        return notif_list, batch, expire_list
        
    def viewSales(self):
        dbcursor = self.dbcursor
        query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item, purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.attendedBy,salestransaction.DatePurchased FROM salestransaction,purchasedproducts"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def viewEMPList(self):
        dbcursor = self.dbcursor
        query="SELECT EmpID,Name,username,role FROM employees"
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        return result

    def selectEmp(self,EmpID):
        query = "SELECT * FROM employees where EmpID=%s"
        id = EmpID
        cursor=self.dbcursor
        cursor.execute(query, id)
        result = cursor.fetchall()

        dbConnector.db.commit()
        dbConnector.db.close()
        return result

    def AddEmp(self,EmpID,name, username, password, role):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        value = (EmpID, name, username, password, role)
        dbcursor.execute(query, value)

        dbConnector.db.commit()
        dbConnector.db.close()

    def AddEmpMany(self,val):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        dbcursor.executemany(query, val)

        dbConnector.db.commit()
        dbConnector.db.close()


    def EditEmp(self,id,name,username,password,role):
        dbcursor = self.dbcursor
        query = "UPDATE employees SET Name='%s', username='%s', password='%s',role='%s' WHERE EmpID=%s"
        value = (name, username, password, role, id)
        dbcursor.execute(query, value)

        dbConnector.db.commit()
        dbConnector.db.close()

    def deleteEmp(self,id):
        dbcursor = dbConnector.db.cursor()
        query = "DELETE FROM employees where EmpID=%s"
        value = (id)
        dbcursor.execute(query, value)

        dbConnector.db.commit()
        dbConnector.db.close()