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
        query = "SELECT ProductID,ProductName,price,quantity,deliverylist.datepurchased,expiry_date FROM products,deliverylist WHERE products.batch_code=%s AND deliverylist.BatchCode=products.batch_code "

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
        print(type(vals))
        print(vals)

        dbcursor.executemany(query, vals)
        dbConnector.db.commit()

    def return_to_sender(self,prod_id,batch_code,ref,qty,remark):
        dbcursor = self.dbcursor
        batch=batch_code[0]
        query="INSERT INTO return_to_sender(ProductID,BatchCode,ref_id,qty,remarks) VALUES(%s,%s,%s,%s,%s)"
        dbcursor.execute(query,(prod_id,batch,ref,qty,remark,))
        dbConnector.db.commit()

    def add_deliveryBatch(self,val):
        dbcursor = self.dbcursor
        query="INSERT INTO deliverylist VALUES(%s,%s,%s,%s)"
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
        query = "SELECT ProductID,ProductName,price,batch_code,Quantity FROM products WHERE ProductName LIKE {}".format("\'%"+val+"%\' AND status='On Hand'")
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result