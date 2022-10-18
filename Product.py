import dbConnector

# Add , Edit, Delete and View Product
class product:
    def __init__(self):
    #     self.productName = productName
    #     self.quantity = quantity
    #     self.status = status
    #     self.Price = Price
        self.dbcursor = dbConnector.db.cursor()
    def viewAll(self):
        print("Viewing Product List")


    def add(self,ProductName,Quantity,status,price):
        dbcursor = self.dbcursor
        query="INSERT INTO products (ProductName,Quantity,status,price) VALUES(%s,%s,%s,%s)"
        value=(ProductName,Quantity,status,price)
        dbcursor.execute(query, value)
        dbConnector.db.commit()
        dbConnector.db.close()

    def addMany(self):
        print("Added new many Product")

    def delete(self,productID):
        print("Deleted Product", productID)


    def deleteMany(self,productID):
        print("Deleted Many Products")


    def update(self,productID):
        print("updating existing product",productID)


    def view(self,productID):
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

    def viewALL(self,val):
        dbcursor = self.dbcursor
        query = "SELECT ProductID,ProductName,price,Quantity FROM products WHERE ProductName LIKE {}".format("\'%"+val+"%\'")
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        dbConnector.db.commit()

        if (dbcursor.rowcount == 0):
            return "empty"
        else:
            return result