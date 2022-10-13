import random, dbConnector

def generateNum():
    PurchaseID = random.randint(1,9999)
    InvoiceNumber = random.randint(1, 9999)
    query = "SELECT purchasedproducts.PurchaseID,salestransaction.InvoiceNumber from purchasedproducts,salestransaction"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if PurchaseID == x and InvoiceNumber==x:
            PurchaseID = random.randint(1, 9999)
            InvoiceNumber = random.randint(1, 9999)
            break
        else:
            continue
    return PurchaseID, InvoiceNumber

def generatePurchaseID():
    PurchaseID = random.randint(1, 9999)
    query = "SELECT purchasedproducts.PurchaseID from purchasedproducts"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if PurchaseID == x :
            PurchaseID = random.randint(1, 9999)
            break
        else:
            continue

    return PurchaseID
