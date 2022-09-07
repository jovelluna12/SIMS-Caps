import dbConnector
class product:
    def __init__(self,productName,quantity,status,Price):
        self.productName = productName

        self.quantity = quantity
        self.status = status
        self.Price = Price

    def viewAll(self):
        print("Viewing Product List")

    def add(self,ProductName,Quantity,status,price):
        dbcursor = dbConnector.db.cursor()
        query="INSERT INTO products (ProductName,Quantity,status,price) VALUES(%s,%s,%s,%s)"
        value=(ProductName,Quantity,status,price)
        dbcursor.execute(query, value)
        dbcursor.close()
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
        print("Viewing details for ",productID)

