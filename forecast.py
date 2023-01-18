from sklearn.linear_model import SGDRegressor
import pandas as pd
import numpy as np
import dbConnector

global model

def forecast(x,y):
    dbcursor = dbConnector.dbcursor
    reg=SGDRegressor(max_iter=1000, tol=1e-3)
    reg.fit(x.values,y.values)

    query="SELECT products.ProductID,products.ProductName,SUM(products.quantity),products.price FROM products WHERE status='Sellable' GROUP BY products.ProductName;"
    dbcursor.execute(query)
    result=dbcursor.fetchall()
    
    x1=[]
    x2=[]

    for i in range(len(result)):
        x1.append(result[i][2])
        x2.append(result[i][3])

    
    X = np.column_stack((x1, x2))
    ans=round(reg.predict(X)[0])

    return result,ans
