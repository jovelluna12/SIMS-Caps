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
    def viewAll(self):
        print("Viewing Product List")


    def add(self,ProductID,ProductName,Quantity,price):
        dbcursor = self.dbcursor
        query="INSERT INTO products (ProductID,ProductName,Quantity,price) VALUES(%s,%s,%s,%s)"

        value=(ProductID,ProductName,Quantity,price)
        dbcursor.execute(query, value)
        dbConnector.db.commit()


    def addMany(self):
        print("Added new many Product")

    def delete(self,productID):
        print("Deleted Product", productID)


    def decreaseProductQuantity(self):
        print()

    # def updateProductQuantity(self,productID,quantity):
    #     dbcursor = self.dbcursor
    #     query = "UPDATE products SET Quantity=%s WHERE ProductID=%s"
    #
    #     for x in productID:
    #         for y in quantity:
    #             dbcursor.execute(query, (quantity[y],productID[x]))
    #
    #     dbConnector.db.commit()
    #     return "done"

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