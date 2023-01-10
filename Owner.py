import Employee
import dbConnector
import pandas as pd
import forecast


class Owner(Employee.Employee):
    def __init__(self):
        self.dbcursor = dbConnector.dbcursor
    
    def viewallEmp(self):
        query="SELECT * FROM employees"
        cursor = self.dbcursor
        cursor.execute(query)
        result = cursor.fetchall()
        dbConnector.db.commit()
        return result

    def selectEmp(self,id):
        query = "SELECT * FROM employees where EmpID=%s"
        cursor = self.dbcursor
        cursor.execute(query, id)
        result = cursor.fetchall()
        dbConnector.db.commit()

        return result

    def AddEmp(self,EmpID,name, username, password, role):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        value = (EmpID, name, username, password, role)
        dbcursor.execute(query, value)
        dbConnector.db.close()

    def AddEmpMany(self,val):
        dbcursor = self.dbcursor
        query = "INSERT INTO employees (EmpID,name,username,password,role) VALUES(%s,%s,%s,%s,%s)"
        dbcursor.executemany(query, val)
        dbConnector.db.close()

    def EditEmp(self,id,name,username,password,role):
        dbcursor = self.dbcursor
        query = "UPDATE employees SET Name=%s, username=%s, password=%s,role=%s WHERE EmpID=%s"
        value = (name, username, password, role, id)
        dbcursor.execute(query, value)
        dbConnector.db.commit()

    def deleteEmp(self,id):
        dbcursor = dbConnector.db.cursor()
        query = "DELETE FROM employees where EmpID=%s"
        query2="DELETE FROM attendance WHERE employee=%s"
        value = (id,)
        dbcursor.execute(query2, value)
        dbcursor.execute(query, value)
        dbConnector.db.commit()