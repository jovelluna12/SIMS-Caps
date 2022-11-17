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

def generateID():
    ID = random.randint(1, 9999)
    query = "SELECT ProductCode from productsindelivery"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if ID == x :
            ID = random.randint(1, 9999)
            break
        else:
            continue
    return ID

def generateProductID():
    ID = random.randint(1, 9999)
    query = "SELECT ProductID from products"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if ID == x :
            ID = random.randint(1, 9999)
            break
        else:
            continue
    return ID

def generateBatchCode():
    ID = random.randint(1, 9999)
    query = "SELECT BatchCode from productsindelivery"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if ID == x :
            ID = random.randint(1, 9999)
            break
        else:
            continue
    return ID
