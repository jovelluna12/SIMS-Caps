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

def generateInvoice():
    InvoiceNumber = random.randint(1, 9999)
    query = "SELECT salestransaction.InvoiceNumber from salestransaction"
    dbcursor = dbConnector.db.cursor()
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    for x in result:
        if InvoiceNumber==x:
            InvoiceNumber = random.randint(1, 9999)
            break
        else:
            continue
    return InvoiceNumber
    
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

def generatePurchaseID():
    ID = random.randint(1, 9999)
    query = "SELECT PurchaseID from purchasedproducts"
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
    query = "SELECT batch_code from products"
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

def generateEmpID():
    ID = random.randint(1, 9999)
    query = "SELECT EmpID from employees"
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

def generateVendorID():
    ID = random.randint(1, 9999)
    query = "SELECT id from vendor"
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
