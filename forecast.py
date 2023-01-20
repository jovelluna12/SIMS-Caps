from tkinter.ttk import Combobox
from tkinter import messagebox
import Product
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np
import dbConnector


import tkinter as tk

def sample_data():
    dataset=pd.read_csv('SAMPLE_DATASET.csv')

    X=dataset.drop(['NumberofItemsSold'],axis=1).values
    Y=dataset[['NumberofItemsSold']].values
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, random_state=42)
    sgd_reg.fit(X_train, y_train)
    w = sgd_reg.coef_
    b = sgd_reg.intercept_
    
    return w, b

def forecast():

    dbcursor = dbConnector.dbcursor
    query="SELECT products.ProductID,products.ProductName,products.Quantity+SUM(purchasedproducts.Quantity ) as Quantity,products.price,SUM(purchasedproducts.Quantity ) AS NumberOfItemsSold FROM products, purchasedproducts,salestransaction WHERE STRCMP(purchasedproducts.Item , products.ProductName)=0 AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) GROUP BY purchasedproducts.Item;"
    dbcursor.execute(query)

    result=dbcursor.fetchall()
    df=pd.DataFrame(result,columns=["ProductID","item","Quantity","Price","NumberofItemsSold"])

    X=df.drop(['NumberofItemsSold',"item"],axis=1).values
    Y=df[['NumberofItemsSold']].values
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    if len(df)<300 and len(df)<300:
        w,b=sample_data()
    
    else:
        reg=SGDRegressor(max_iter=1000, tol=1e-3)
        reg.fit(X_train,X_test)
        w = reg.coef_
        b = reg.intercept_

    
    new_data=[int(prod_to_pred[0][0]),int(e2.get()),int(prod_to_pred[0][2])]
    prediction=b+np.dot(new_data,w)
    if messagebox.showinfo("Forecast Result","Forecasted Number of Sales\nNext Month for this Product is \n"+str(int(prediction))):
        root.destroy()


def GUI():
    def selected_code(event):
        if 'e2' not in globals():
            tk.Label(root, text="Quantity").pack()
            global e2
            e2 = tk.Entry(root)
            e2.pack()

            a=Product.product()
            global prod_to_pred
            prod_to_pred=a.return_one(e1.get())
            tk.Button(root,text="Forecast", command=forecast).pack()
            

    global root
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Forecast")

    a=Product.product()
    res=a.returnall()

    tk.Label(root, text="Product").pack()
    e1 = Combobox(root)
    e1["values"]=([x[1] for x in res])
    e1.pack()
    e1.bind("<<ComboboxSelected>>",selected_code)

    root.mainloop()
