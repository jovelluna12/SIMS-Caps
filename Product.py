import dbConnector
class product:
    def __init__(self,productName,itemCode,quantity,status,Price):
        self.productName = productName
        self.itemCode = itemCode
        self.quantity = quantity
        self.status = status
        self.Price = Price

    def viewProductList(self):
        print("Viewing Product List")

    def addnewProduct(self):
        print("Added new Product")

    def deleteProduct(self,productID):
        print("Deleted Product", productID)

    def updateExistingProduct(self,productID):
        print("updating existing product",productID)

    def viewProductDetails(self,productID):
        print("Viewing details for ",productID)

