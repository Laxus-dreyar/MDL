import numpy as np
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pickle
import matplotlib.pyplot as plt 
import pandas as pd

dbfile = open('Q1_data/data.pkl','rb')
db = pickle.load(dbfile)
le = db.shape[0]
X = db[:,0]
y = db[:,1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
X_train_number_list = []
Y_train_number_list = []

for i in range(10):
    X_train,X_temp,y_train,y_temp = train_test_split(X_train,y_train,test_size = 0.1)
    X_train_number_list.append(X_temp)
    Y_train_number_list.append(y_temp)

X_train_number = np.array(X_train_number_list)
Y_train_number = np.array(Y_train_number_list)
final_bias_list = []
final_varience_list = []

for i in range(10):
    
    poly = PolynomialFeatures(degree=i+1)
    prediction_list = []
    reg = linear_model.LinearRegression()

    for j in range(10):
        X_temo = np.array(X_train_number[j])
        X_temo = X_temo[:, np.newaxis]
        X_poly = poly.fit_transform(X_temo)
        
        X_teme = X_test[:, np.newaxis]
        X_test_poly = poly.fit_transform(X_teme)
        
        reg.fit(X_poly,Y_train_number[j]);
        temp = reg.predict(X_test_poly)
        prediction_list.append(temp)


    prediction = np.array(prediction_list)

    expec = np.mean(prediction,axis = 0)
    bias = np.subtract(expec,y_test)
    bias**=2

    varience = np.var(prediction,axis=0)

    bias_avg = np.mean(bias)
    bias_avg = math.sqrt(bias_avg)

    var_avg = np.mean(varience)

    final_varience_list.append(var_avg)
    final_bias_list.append(bias_avg)

final_bias = np.array(final_bias_list)
final_varience = np.array(final_varience_list)
x_degree = [i for i in range(1,11)]
data = {'Degree':x_degree,
        'Bias':final_bias,
        'Variance':final_varience}
df = pd.DataFrame(data)
print(df[['Degree','Bias','Variance']])
final_bias_2 = final_bias**2
plt.plot(x_degree,final_bias_2,label = '$bias^2$')
plt.plot(x_degree,final_varience,label = '$varience$')
plt.xlabel('degree')
plt.legend()
plt.show()