import Employee, dbConnector, Product, forecast
from datetime import datetime
import pandas as pd
class Manager (Employee.Employee):

    def __init__(self):
        self.dbcursor = dbConnector.dbcursor
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
        # SELECT ProductID as ProdID ,ProductName,price,batch_code, SUM(quantity) FROM products,deliverylist WHERE quantity!=0 AND products.status = 'Sellable' AND products.batch_code=deliverylist.BatchCode GROUP BY ProductName ORDER BY deliverylist.datepurchased ASC
        query="SELECT ProductID ,ProductName,price,batch_code,quantity FROM products,deliverylist WHERE quantity!=0 AND products.status = 'Sellable' AND products.batch_code=deliverylist.BatchCode GROUP BY ProductName ORDER BY deliverylist.datepurchased ASC"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def get_export_data(self,report,scope_from,scope_to):
        dbcursor = self.dbcursor
        if report=="Sales":
            # query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item,purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.DatePurchased FROM salestransaction, purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) ORDER BY DatePurchased;"
            query= "SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item,purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.DatePurchased FROM salestransaction, purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND salestransaction.DatePurchased >= %s AND salestransaction.DatePurchased <=%s ORDER BY DatePurchased;"
            
            dbcursor.execute(query,(scope_from,scope_to))
            return dbcursor.fetchall()

        if report=="Inventory" and scope_from==None and scope_to==None:
            query="SELECT products_directory.ref_id, products_directory.product_name,products_directory.price,SUM(products.quantity) AS QUANTITY FROM products_directory, products WHERE products.ref_id=products_directory.ref_id GROUP BY products.ref_id;;"
            dbcursor.execute(query)

            return dbcursor.fetchall()
        if report=="Delivery" and scope_from==None and scope_to==None:
            query="SELECT batch_code,ProductName,quantity,price,deliverylist.status FROM products,deliverylist WHERE deliverylist.status='Under Delivery' AND products.batch_code=deliverylist.BatchCode;"
            dbcursor.execute(query)

            return dbcursor.fetchall()

        if report=="Forecast" and scope_from==None and scope_to==None:
            query="SELECT products.ProductID,products.ProductName,products.Quantity+SUM(purchasedproducts.Quantity ) as Quantity,products.price,SUM(purchasedproducts.Quantity ) AS NumberOfItemsSold FROM products, purchasedproducts,salestransaction WHERE STRCMP(purchasedproducts.Item , products.ProductName)=0 AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) GROUP BY purchasedproducts.Item;"
            dbcursor.execute(query)

            result=dbcursor.fetchall()
            df=pd.DataFrame(result,columns=["ProductID","item","Quantity","Price","NumberOfItemsSold"])

            X=df[["Quantity","Price"]]
            y=df["NumberOfItemsSold"]
            
            res,value=forecast.forecast(X,y)
            return res,value

    def addNote(self,val):
        dbcursor=self.dbcursor
        query="UPDATE products SET note=%s WHERE ProductID=%s"
        dbcursor.execute(query,val)
        dbConnector.db.commit()

    def notify_expiry(self):
        dbcursor=self.dbcursor
        query="SELECT ProductID,ProductName,expiry_date,batch_code FROM products WHERE status!='Expired' AND status!='Unsellable' AND status!='Under Delivery' AND note!='Checked'"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
    
        x=0
        messages=[]
        id=[]
        name=[]
        batch=[]
        for i in result:
            days_left=7
            if result!=None:
                diff=result[x][2]-datetime.today().date()
                today_left=diff.days

                if today_left<=0:
                    man=Product.product()
                    man.editStatus('Unsellable',result[x][0])
                    
                    message=str(result[x][1])+ "of Batch "+str(result[x][3])+" is Expired and Unsellable"
                    messages.append(message)
                    id.append(result[x][0])
                    name.append(result[x][1])
                    batch.append(result[x][3])

                if today_left<=days_left:
                    message=str(result[x][1])+ "of Batch "+str(result[x][3])+" is about to Expire in "+str(today_left)+" days"
                    messages.append(message)
                    id.append(result[x][0])
                    name.append(result[x][1])
                    batch.append(result[x][3])
            x+=1
        return messages,name,batch,id

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
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        dbConnector.db.commit()
        return result

    def AddEmp(self,EmpID,name, username, password, role):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        value = (EmpID, name, username, password, role)
        dbcursor.execute(query, value)

        dbConnector.db.commit()

    def AddEmpMany(self,val):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        dbcursor.executemany(query, val)

        dbConnector.db.commit()

    def EditEmp(self,id,name,username,password,role):
        dbcursor = self.dbcursor
        query = "UPDATE employees SET Name='%s', username='%s', password='%s',role='%s' WHERE EmpID=%s"
        value = (name, username, password, role, id)
        dbcursor.execute(query, value)

        dbConnector.db.commit()

    def deleteEmp(self,id):
        dbcursor = dbConnector.db.cursor()
        query = "DELETE FROM employees where EmpID=%s"
        value = (id)
        dbcursor.execute(query, value)

        dbConnector.db.commit()