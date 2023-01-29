import dbConnector

# Add , Edit, Delete and View Product
import randomNumGen


class product:
    def __init__(self):
    #     self.productName = productName
    #     self.quantity = quantity
    #     self.status = status
    #     self.Price = Price
        self.dbcursor = dbConnector.db.cursor()
    def retrieveBatch(self,code):
        dbcursor = self.dbcursor
        query = "SELECT ProductID,ProductName,price,quantity,deliverylist.datepurchased,expiry_date, deliverylist.status FROM products,deliverylist WHERE products.batch_code=%s AND deliverylist.BatchCode=products.batch_code "

        dbcursor.execute(query, code)
        result=dbcursor.fetchall()
        return result


    def add(self,value):
        dbcursor = self.dbcursor
        query = "INSERT INTO products (ProductID,ProductName,Quantity,price,batch_code,status) VALUES(%s,%s,%s,%s,%s,%s)"

        dbcursor.execute(query, value)
        dbConnector.db.commit()

    def addReference(self,vals):
        dbcursor = self.dbcursor
        query = "INSERT INTO products_directory (ref_id,product_name,price) VALUES(%s,%s,%s)"

        vals=tuple(list(vals))
        dbcursor.executemany(query, vals)
        dbConnector.db.commit()

    def editDelivery(self,id, name, price,qty,expiry_date):
        dbcursor = self.dbcursor
        query = "UPDATE products SET ProductName=%s, price=%s, quantity=%s,expiry_date=%s ,status='On Hand' WHERE ProductID=%s"

        vals=(name, price,qty,expiry_date,id)

        dbcursor.execute(query, vals)

        query2="UPDATE deliverylist,products SET deliverylist.status='On Hand' WHERE deliverylist.BatchCode=products.batch_code"
        dbcursor.execute(query2)
        dbConnector.db.commit()

    def confirm_all(self,val):
        dbcursor = self.dbcursor
        query = "UPDATE products SET ProductName=%s, price=%s, quantity=%s,expiry_date=%s ,status='On Hand' WHERE ProductID=%s"

        dbcursor.execute(query, val)
        dbConnector.db.commit()


    def editReference(self,id, name, price):
        dbcursor = self.dbcursor
        query = "UPDATE products_directory SET product_name=%s, price=%s WHERE ref_id=%s"

        vals=(name, price,id)

        dbcursor.execute(query, vals)
        dbConnector.db.commit()


    def addMany(self,vals):
        dbcursor = self.dbcursor
        query = "INSERT INTO products (ProductID,ProductName,Quantity,price,batch_code,status) VALUES(%s,%s,%s,%s,%s,%s)"

        vals=tuple(list(vals))

        dbcursor.executemany(query, vals)
        dbConnector.db.commit()

    def delivery_qtyIN(self,qtyIN,listt):
        dbcursor = self.dbcursor
        query3="UPDATE delivery_items SET qty_in=%s WHERE list=%s"
        dbcursor.execute(query3,(qtyIN,listt[0]))
        dbConnector.db.commit()

    def return_to_sender(self,return_goods,items2,items3,items4):
        dbcursor = self.dbcursor
        query="INSERT INTO return_to_sender(ProductID,BatchCode,ref_id,qty,remarks) VALUES(%s,%s,%s,%s,%s)"
        query2="UPDATE delivery_items SET qty_out=%s WHERE list=%s"

        query4="UPDATE delivery_items SET remark=%s WHERE list=%s"
        dbcursor.executemany(query,return_goods)    
        dbcursor.executemany(query2,items2)
        dbcursor.executemany(query4,items4)

        dbConnector.db.commit()

    def getRemainingBal(self,id):
        dbcursor = self.dbcursor
        query="SELECT qty FROM products_onhand WHERE item=%s;"
        dbcursor.execute(query,(id,))
        result=dbcursor.fetchall()
        res=dbcursor.rowcount
        print(result)
        return result

    def Inventory(self,items,InventType):
        dbcursor = self.dbcursor
        print(items)
        query="INSERT INTO inventory (item,price,date_in,date_out,Qty_in,Qty_out,RemainBalance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query,items)
        
        query2="SELECT item FROM products_onhand WHERE item=%s"
        dbcursor.execute(query2,(items[0],))
        res=dbcursor.fetchall()
        result=dbcursor.rowcount
        print(result)

        if result !=0 and InventType=='Sale':
            query="UPDATE products_onhand SET qty=qty-%s WHERE item=%s"
            dbcursor.execute(query, (items[5],items[0]))
        elif result !=0 and InventType=='Inventory':
            query="UPDATE products_onhand SET qty=qty+%s WHERE item=%s"
            dbcursor.execute(query, (items[4],items[0]))
        elif result ==0 and InventType=='Inventory': 
            query="INSERT INTO products_onhand(item,price,qty) VALUES(%s,%s,%s)"
            dbcursor.execute(query,(items[0],items[1],items[4]))
        elif result ==0 and InventType=="Sale":
            return None
                
        dbConnector.db.commit()

    def get_batch_Codes(self):
        query="SELECT batch_code from products LEFT JOIN return_to_sender ON products.batch_code=return_to_sender.BatchCode;"
        dbcursor = self.dbcursor
        dbcursor.execute(query) 
        return dbcursor.fetchall()

    def add_deliveryBatch(self,val):
        dbcursor = self.dbcursor

        query="INSERT INTO deliverylist VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query,val)
        dbConnector.db.commit()

    def get_ref_id(self,name):
        dbcursor = self.dbcursor
        query="SELECT ref_id from products_directory WHERE product_name=%s LIMIT 1"
        dbcursor.execute(query,(name,))
        result=dbcursor.fetchone()
        return result

    def get_batch_code(self,code):
        dbcursor = self.dbcursor
        query="SELECT BatchCode from deliverylist WHERE deliverylist.BatchCode=products.batch_code LIMIT 1"

        dbcursor.execute(query,(code,))
        result=dbcursor.fetchall()
        return result

    def addto_DeliveryItems(self,items):
        dbcursor = self.dbcursor
        query="INSERT INTO delivery_items (list,Product_Id,	qty,qty_in,	qty_out,remark) VALUES(%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query,items)
        dbConnector.db.commit()

    def addMany_Del(self,vals):
        dbcursor = self.dbcursor
        query = "INSERT INTO products (ProductID,ref_id,ProductName,quantity,price,status,batch_code,expiry_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

        dbcursor.executemany(query, vals)
        dbConnector.db.commit()

    def delete_del(self, id):
        dbcursor=self.dbcursor
        query1="DELETE FROM products WHERE ProductID=%s"
        dbcursor.execute(query1, (id,))
        dbConnector.db.commit()

    def delete_del_batch(self,batch):
        dbcursor=self.dbcursor
        query1="DELETE FROM products WHERE batch_code=%s"
        query2="DELETE FROM deliverylist WHERE BatchCode=%s"
        dbcursor.execute(query1, (batch))
        dbcursor.execute(query2, (batch))
        dbConnector.db.commit()

    def delete_ProdRef(self,id):
        dbcursor=self.dbcursor
        query=("DELETE FROM products_directory WHERE ref_id=%s")
        dbcursor.execute(query,(id,))
        dbConnector.db.commit()

    def viewCode(self,productID):
        dbcursor = self.dbcursor
        query = "SELECT ProductID,ProductName,price,Quantity FROM products WHERE ProductID=%s"
        value=[productID]
        value=tuple(value)

        dbcursor.execute(query,value)
        result=dbcursor.fetchone()
        dbConnector.db.commit()

        if (dbcursor.rowcount==0):
            return "empty"
        else:
            return result

    def viewName(self,productID):
        dbcursor = self.dbcursor
        query = "SELECT ProductID,ProductName,price,Quantity FROM products WHERE ProductName=%s"
        value=[productID]
        value=tuple(value)

        dbcursor.execute(query,value)
        result=dbcursor.fetchone()
        dbConnector.db.commit()

        if (dbcursor.rowcount==0):
            return "empty"
        else:
            return result

    def returnall(self):
        dbcursor=self.dbcursor
        query="SELECT * FROM products_directory"
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result

    def return_one(self,name):
        dbcursor=self.dbcursor
        query="SELECT * FROM products_directory WHERE product_name=%s LIMIT 1"
        value=[name]
        value=tuple(value)
        
        dbcursor.execute(query,value)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result

    def editStatus(self,stat,id):
        dbcursor = self.dbcursor
        query = "UPDATE products SET status=%s WHERE ProductID=%s"
        val=(stat,id)

        dbcursor.execute(query, val)
        dbConnector.db.commit()
        



    def viewALL(self,val):
        dbcursor = self.dbcursor
        query = "SELECT id, item, price, qty FROM products_onhand WHERE item LIKE {}".format("\'%"+val+"%\'")
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result