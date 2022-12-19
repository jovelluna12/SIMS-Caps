from sklearn import linear_model

def forecast(x,y):
    reg=linear_model.LinearRegression()

    reg.fit(x.values,y.values)
    ans=reg.predict([[200,10]])
    
    return int(ans)