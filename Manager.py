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

    def inventory(self):
        dbcursor=self.dbcursor
        query="SELECT * FROM inventory;"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def get_AllProducts(self):
        dbcursor = self.dbcursor
        query="SELECT * from products_directory"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result
    
    def get_ProductInventHistory(self, name):
        dbcursor = self.dbcursor
        query="SELECT * from inventory WHERE item=%s"
        dbcursor.execute(query,(name,))
        result=dbcursor.fetchall()
        return result

    def get_inTransit(self,dateFrom,dateTo,batch):
        dbcursor = self.dbcursor
        if dateFrom is not None and dateTo is None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status='In Transit';"
            dbcursor.execute(query,(dateFrom,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status='In Transit' AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s AND products.status='In Transit' AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,dateTo,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s AND products.status='In Transit';"
            dbcursor.execute(query,(dateFrom,dateTo,))
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch=="None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND products.status='In Transit';"
            dbcursor.execute(query)
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND products.status='In Transit' AND products.batch_code=%s;"
            dbcursor.execute(query,(batch,))
            result = dbcursor.fetchall()
            
        return result
    
    def get_OnHand(self,dateFrom,dateTo,batch):
        dbcursor = self.dbcursor
        if dateFrom is not None and dateTo is None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status='On Hand';"
            dbcursor.execute(query,(dateFrom,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status='On Hand' AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s AND products.status='On Hand' AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,dateTo,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s AND products.status='On Hand';"
            dbcursor.execute(query,(dateFrom,dateTo,))
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch=="None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND products.status='On Hand';"
            dbcursor.execute(query)
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND products.status='On Hand' AND products.batch_code=%s;"
            dbcursor.execute(query,(batch,))
            result = dbcursor.fetchall()
            
        return result

    def get_Vendor_ID(self,name):
        query="SELECT id FROM vendor WHERE vendor_name=%s"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(name,))
        result=dbcursor.fetchone()
        return result

    def get_Vendors(self):
        dbcursor = self.dbcursor
        query="SELECT * FROM vendor"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result


    def addVendor_logic(self,vendor_details):
        dbcursor = self.dbcursor
        query="INSERT INTO vendor VALUES(%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query,vendor_details)
        dbConnector.db.commit()

    def listNone(self,dateFrom,dateTo,batch):
        dbcursor = self.dbcursor
        if dateFrom is not None and dateTo is None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE();"
            dbcursor.execute(query,(dateFrom,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s AND products.batch_code=%s;"
            dbcursor.execute(query,(dateFrom,dateTo,batch,))
            result = dbcursor.fetchall()
        elif dateFrom is not None and dateTo is not None and batch == "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and %s;"
            dbcursor.execute(query,(dateFrom,dateTo,))
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch=="None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode;"
            dbcursor.execute(query)
            result = dbcursor.fetchall()
        elif dateTo is None and dateFrom is None and batch != "None":
            query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND products.batch_code=%s;"
            dbcursor.execute(query,(batch,))
            result = dbcursor.fetchall()
            
        return result

    def get_list_from_date_now(self,date,filter):
        query="SELECT products.ProductID,products.ProductName,products.status,products.price,products.Quantity FROM products,deliverylist WHERE products.batch_code=deliverylist.BatchCode AND deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status=%s;"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(date,filter,))
        result = dbcursor.fetchall()
        return result

    def get_returnlist_from_date_now(self,date):
        query="SELECT return_to_sender.ProductID, products.ProductName,return_to_sender.remarks,products.price, return_to_sender.qty FROM return_to_sender, products,deliverylist WHERE return_to_sender.ProductID=products.ProductID AND return_to_sender.BatchCode=deliverylist.BatchCode and deliverylist.datepurchased BETWEEN %s and CURDATE() AND products.status=%s;"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(date,filter,))
        result = dbcursor.fetchall()
        return result

    def return_to_sender_list(self):
        query="SELECT return_to_sender.ProductID, products.ProductName,return_to_sender.remarks,products.price, return_to_sender.qty FROM return_to_sender, products WHERE return_to_sender.ProductID=products.ProductID;"
        dbcursor = self.dbcursor
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        return result

    def get_Transaction_Details(self,invoice_number):
        dbcursor = self.dbcursor
        query="SELECT TotalPrice, PWD_SC_Disc, Custom_Discount, DatePurchased,Cash, calculated_change FROM salestransaction WHERE InvoiceNumber=%s;"
        dbcursor.execute(query,(invoice_number,))
        result=dbcursor.fetchall()
        return result

    def get_sales_Attended(self,invoice_number):
        dbcursor = self.dbcursor
        query="SELECT employees.Name FROM employees, salestransaction WHERE salestransaction.attendedBy = employees.EmpID AND salestransaction.InvoiceNumber=%s;"
        dbcursor.execute(query,(invoice_number,))
        result=dbcursor.fetchone()
        return result

    def get_itemsSold(self,invoice_number):
        dbcursor = self.dbcursor
        query="SELECT purchasedproducts.Item,products.price, purchasedproducts.Quantity,products.price*purchasedproducts.Quantity as TOTAL FROM purchasedproducts, products WHERE purchasedproducts.InvoiceNumber=%s AND purchasedproducts.ProductID=products.ProductID;"
        dbcursor.execute(query,(invoice_number,))
        result=dbcursor.fetchall()
        return result
    
    def get_sale_via_id(self, id):
        dbcursor = self.dbcursor
        query="SELECT salestransaction.InvoiceNumber, employees.name, products.price*purchasedproducts.Quantity, salestransaction.DatePurchased FROM salestransaction, employees, products,purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND purchasedproducts.ProductID=products.ProductID AND salestransaction.attendedBy=employees.EmpID AND salestransaction.InvoiceNumber=%s;"
        dbcursor.execute(query,(id,))
        result = dbcursor.fetchall()
        return result


    

    def getPO_Items(self,id):
        # query="SELECT delivery_items.id, products.ProductName, products.price, delivery_items.qty, delivery_items.qty_in, delivery_items.qty_out, delivery_items.remark FROM delivery_items,products WHERE delivery_items.list=%s AND delivery_items.list=products.batch_code;"
        # query="SELECT products.ProductID, products.ProductName, products.price, products.quantity, delivery_items.qty_in, delivery_items.qty_out, return_to_sender.remarks FROM products,delivery_items,return_to_sender,deliverylist WHERE products.ProductID=return_to_sender.ProductID AND products.batch_code=%s and products.batch_code=return_to_sender.BatchCode GROUP BY products.ProductID;"
        query="SELECT products.ProductID, products.ProductName, products.price, delivery_items.qty, delivery_items.qty_in, delivery_items.qty_out, return_to_sender.remarks FROM products,delivery_items,return_to_sender,deliverylist WHERE products.ProductID=return_to_sender.ProductID AND products.batch_code=%s and products.batch_code=return_to_sender.BatchCode AND delivery_items.Product_Id=products.ProductID GROUP BY delivery_items.Product_Id;"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(id[0],))
        result = dbcursor.fetchall()
        return result

    def getDateArrived_Purchased(self,id):
        query="SELECT datepurchased, expectedarrivaldate, status FROM deliverylist WHERE BatchCode=%s"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(id[0],))
        result = dbcursor.fetchone()
        return result

    def getPO_details(self,id):
        query="SELECT GrossAmount, VAT, Discount, NET_Amount FROM deliverylist WHERE BatchCode=%s"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(id,))
        result = dbcursor.fetchone()
        return result

    def getPO_Vendor(self,id):
        query="SELECT vendor.vendor_name, vendor.vendor_address, vendor.contact_num, vendor.email_add, vendor.shipping_fee FROM vendor, deliverylist WHERE deliverylist.vendor_id=vendor.id AND deliverylist.BatchCode=%s"
        dbcursor = self.dbcursor
        dbcursor.execute(query,(id,))
        result = dbcursor.fetchone()
        return result

    def productSales(self):
        dbcursor = self.dbcursor
        # query = "SELECT purchasedproducts.PurchaseID,purchasedproducts.Item,purchasedproducts.Quantity,products.price, products.price*purchasedproducts.Quantity, salestransaction.DatePurchased FROM purchasedproducts,products,salestransaction WHERE purchasedproducts.InvoiceNumber=salestransaction.InvoiceNumber AND purchasedproducts.ProductID=products.ProductID GROUP BY purchasedproducts.PurchaseID;"
        query="SELECT salestransaction.InvoiceNumber, employees.name, salestransaction.DatePurchased FROM salestransaction, employees, products,purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND purchasedproducts.ProductID=products.ProductID AND salestransaction.attendedBy=employees.EmpID GROUP BY salestransaction.InvoiceNumber ORDER BY salestransaction.DatePurchased DESC;"
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        return result

    def view_onHand(self):
        dbcursor=self.dbcursor
        query="SELECT id, item, price, qty FROM products_onhand"
        dbcursor.execute(query)
        result= dbcursor.fetchall()
        return result
        
    def viewInv(self):
        dbcursor = self.dbcursor
        # SELECT ProductID as ProdID ,ProductName,price,batch_code, SUM(quantity) FROM products,deliverylist WHERE quantity!=0 AND products.status = 'On Hand' AND products.batch_code=deliverylist.BatchCode GROUP BY ProductName ORDER BY deliverylist.datepurchased ASC
        query="SELECT ProductID ,ProductName,price,batch_code,quantity FROM products,deliverylist WHERE quantity!=0 AND products.status = 'On Hand' AND products.batch_code=deliverylist.BatchCode GROUP BY ProductName ORDER BY deliverylist.datepurchased ASC"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def get_export_data(self,report,scope_from,scope_to):
        dbcursor = self.dbcursor
        if report=="Sales":
            # query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item,purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.DatePurchased FROM salestransaction, purchasedproducts WHERE salestransaction.InvoiceNumber=purchasedproducts.InvoiceNumber AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) ORDER BY DatePurchased;"
            query= "SELECT products_directory.ref_id, products_directory.product_name,products_directory.price,deliverylist.expectedarrivaldate,salestransaction.DatePurchased,delivery_items.qty_in, purchasedproducts.Quantity FROM products_directory, products, delivery_items,salestransaction ,purchasedproducts WHERE products.ref_id=products_directory.ref_id GROUP BY products.ref_id;"
            
            dbcursor.execute(query,(scope_from,scope_to))
            return dbcursor.fetchall()

        if report=="Inventory" and scope_from==None and scope_to==None:
            # query="SELECT products_directory.ref_id, products_directory.product_name,products_directory.price,deliverylist.expectedarrivaldate,salestransaction.DatePurchased,delivery_items.qty_in, purchasedproducts.Quantity FROM products_directory,deliverylist, products, delivery_items,salestransaction ,purchasedproducts WHERE products.ref_id=products_directory.ref_id;"
            query="SELECT * FROM inventory;"
            dbcursor.execute(query)

            return dbcursor.fetchall()
        if report=="Delivery" and scope_from==None and scope_to==None:
            query="SELECT batch_code,ProductName,quantity,price,deliverylist.status FROM products,deliverylist WHERE deliverylist.status='In Transit' AND products.batch_code=deliverylist.BatchCode;"
            dbcursor.execute(query)

            return dbcursor.fetchall()

        if report=="Forecast" and scope_from==None and scope_to==None:
            query="SELECT products.ProductID,products.ProductName,products.Quantity+SUM(purchasedproducts.Quantity ) as Quantity,products.price,SUM(purchasedproducts.Quantity ) AS NumberOfItemsSold FROM products, purchasedproducts,salestransaction WHERE STRCMP(purchasedproducts.Item , products.ProductName)=0 AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) GROUP BY purchasedproducts.Item;"
            dbcursor.execute(query)

            result=dbcursor.fetchall()
            df=pd.DataFrame(result,columns=["ProductID","item","Quantity","Price","NumberOfItemsSold"])

            X=df[["Quantity","Price"]]
            y=df["NumberOfItemsSold"]
            
            res,value=forecast.forecast()
            return res,value

    def addNote(self,val):
        dbcursor=self.dbcursor
        query="UPDATE products SET note=%s WHERE ProductID=%s"
        dbcursor.execute(query,val)
        dbConnector.db.commit()

    def get_Ave_LeadTime(self):
        dbcursor = self.dbcursor
        query="SELECT AVG(DATEDIFF(datepurchased,expectedarrivaldate)) FROM deliverylist"
        dbcursor.execute(query)
        result=dbcursor.fetchone()
        return result

    def get_SafetyStock(self):
        dbcursor = self.dbcursor
        query="SELECT "

    def notify_expiry(self):
        dbcursor=self.dbcursor
        # query="SELECT ProductID,ProductName,expiry_date,batch_code FROM products WHERE status!='Expired' AND status!='Unsellable' AND status!='In Transit' AND note!='Checked'"
        query="SELECT * FROM products_onhand"
        ROP_query='SELECT MAX(RemainBalance) FROM inventory WHERE item="%s";'
        dbcursor.execute(query)
        result=dbcursor.fetchall()

        query_date='SELECT expiry_date FROM products WHERE ProductName=%s GROUP BY expiry_date ASC LIMIT 1'
        
    
        x=0
        messages=[]
        id=[]
        name=[]
        batch=[]
        for i in result:
            print(i[1])
            # print(ex_date)
            dbcursor.execute(query_date, (i[1],))
            ex_date=dbcursor.fetchall()
            print(ex_date)
            
            dbcursor.execute(ROP_query,i[1])
            ROP=dbcursor.fetchone()
            days_left=7
            if result!=None:
                diff=ex_date[x][0]-datetime.today().date()
                today_left=diff.days
                
                if today_left<=0:
                    man=Product.product()
                    man.editStatus('Unsellable',result[x][0])
                    
                    message=str("Product "+result[x][1])+ "is Expired and Unsellable"
                    messages.append(message)
                    name.append(result[x][1])

                elif today_left<=days_left:
                    message=str(result[x][1])+ " is about to Expire in "+str(today_left)+" days"

                elif result[x][3] <=ROP[0]:
                    message=str(result[x][1])+ " needs Reordering"
                    messages.append(message)
                    name.append(result[x][1])
            x+=1
        # return messages,name,batch,id
        return messages,name

    

    def viewSales(self):
        dbcursor = self.dbcursor
        query="SELECT salestransaction.InvoiceNumber, purchasedproducts.PurchaseID, purchasedproducts.Item, purchasedproducts.Quantity, salestransaction.TotalPrice, salestransaction.Discount,salestransaction.attendedBy,salestransaction.DatePurchased FROM salestransaction,purchasedproducts"
        dbcursor.execute(query)
        result=dbcursor.fetchall()
        return result

    def viewEMPList(self):
        dbcursor = self.dbcursor
        query="SELECT EmpID,Name,username,role FROM employees WHERE role!='Owner'"
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