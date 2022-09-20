import dbConnector

def ViewEmp(EmpID):
    dbcursor = dbConnector.db.cursor()
    query = "SELECT * FROM employees where EmpID=%s"
    id=EmpID
    dbcursor.execute(query,id)
    result=dbcursor.fetchall()
    dbcursor.close()
    dbConnector.db.commit()
    dbConnector.db.close()
    return result

def AddEmp(EmpID, name, username, password, role):
    dbcursor = dbConnector.db.cursor()
    query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
    value = (EmpID, name, username, password, role)
    dbcursor.execute(query, value)
    dbcursor.close()
    dbConnector.db.commit()
    dbConnector.db.close()

def AddEmpMany(val):
    dbcursor = dbConnector.db.cursor()
    query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
    dbcursor.executemany(query,val)
    dbcursor.close()
    dbConnector.db.commit()
    dbConnector.db.close()

def EditEmp(id,name,username,password,role):
    dbcursor = dbConnector.db.cursor()
    query="UPDATE employees SET Name='%s', username='%s', password='%s',role='%s' WHERE EmpID=%s"
    value=(name,username,password,role,id)
    dbcursor.execute(query,value)
    dbcursor.close()
    dbConnector.db.commit()
    dbConnector.db.close()

def deleteEmp(id):
    dbcursor = dbConnector.db.cursor()
    query="DELETE FROM employees where EmpID=%s"
    value=(id,)
    dbcursor.execute(query,value)
    dbcursor.close()
    dbConnector.db.commit()
    dbConnector.db.close()