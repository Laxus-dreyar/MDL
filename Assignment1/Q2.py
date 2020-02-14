import numpy as np
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pickle
import matplotlib.pyplot as plt 
import pandas as pd

xfile1 = open('Q2_data/X_train.pkl','rb')
xfile2 = open('Q2_data/X_test.pkl','rb')
yfile1 = open('Q2_data/Y_train.pkl','rb')
yfile2 = open('Q2_data/Fx_test.pkl','rb')

X_train_number = pickle.load(xfile1)
Y_train_number = pickle.load(yfile1)
X_test = pickle.load(xfile2)
y_test = pickle.load(yfile2)

final_bias_list = []
final_varience_list = []


for i in range(10):
    
    poly = PolynomialFeatures(degree=i+1)
    prediction_list = []
    reg = linear_model.LinearRegression()

    X_teme = X_test[:, np.newaxis]
    X_test_poly = poly.fit_transform(X_teme)
    
    for j in range(20):
        X_temo = np.array(X_train_number[j])
        X_temo = X_temo[:, np.newaxis]
        X_poly = poly.fit_transform(X_temo)
        
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