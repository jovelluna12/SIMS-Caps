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
        query = "SELECT ProductID,ProductName,price,quantity,order_date,expiry_date FROM products WHERE batch_code=%s"

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
        query = "UPDATE products SET ProductName=%s, price=%s, quantity=%s,expiry_date=%s ,status='Sellable' WHERE ProductID=%s"

        vals=(name, price,qty,expiry_date,id)

        dbcursor.execute(query, vals)
        dbConnector.db.commit()

    def confirm_all(self,val):
        dbcursor = self.dbcursor
        query = "UPDATE products SET ProductName=%s, price=%s, quantity=%s,expiry_date=%s ,status='Sellable' WHERE ProductID=%s"

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

    def addMany_Del(self,vals):
        dbcursor = self.dbcursor
        query = "INSERT INTO products VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        dbcursor.executemany(query, vals)
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
        query = "SELECT ProductID,ProductName,price,Quantity FROM products WHERE ProductName LIKE {}".format("\'%"+val+"%\' AND status='Sellable'")
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result