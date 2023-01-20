from tkinter.ttk import Combobox
from tkinter import messagebox
import Product
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd
import numpy as np
import dbConnector

import tkinter as tk
    
def forecast():
    dbcursor = dbConnector.dbcursor
    query="SELECT products.ProductID,products.ProductName,products.Quantity+SUM(purchasedproducts.Quantity ) as Quantity,products.price,SUM(purchasedproducts.Quantity ) AS NumberOfItemsSold FROM products, purchasedproducts,salestransaction WHERE STRCMP(purchasedproducts.Item , products.ProductName)=0 AND DATE(salestransaction.DatePurchased) >= (DATE(NOW()) - INTERVAL 30 DAY) GROUP BY purchasedproducts.Item;"
    dbcursor.execute(query)

    result=dbcursor.fetchall()
    df=pd.DataFrame(result,columns=["ProductID","item","Quantity","Price","NumberofItemsSold"])

    size=df.shape[0]
    if size<100:
        dataset=pd.read_csv('SAMPLE_DATASET - Sheet1 (2).csv')
        X=dataset.drop(['190'],axis=1).values
        Y=dataset[['190']].values
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)

        new_data=[int(prod_to_pred[0][0]),int(e2.get()),int(prod_to_pred[0][2])]

        predicted = regr.predict([new_data])
    
    else:
        X=df.drop(['NumberofItemsSold',"item"],axis=1).values
        Y=df[['NumberofItemsSold']].values
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)
        new_data=[int(prod_to_pred[0][0]),int(e2.get()),int(prod_to_pred[0][2])]
        predicted = regr.predict([new_data])
    
    if messagebox.showinfo("Forecast Result","Forecasted Number of Sales\nNext Month for this Product is \n"+str(int(predicted))):
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
