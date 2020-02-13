import numpy as np
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pickle
import matplotlib.pyplot as plt 

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
    bias_array_list = []
    coef_list = []
    prediction_list = []
    varience_list = []
    reg = linear_model.LinearRegression()

    for j in range(10):
        X_temo = np.array(X_train_number[j])
        X_temo = X_temo[:, np.newaxis]
        X_poly = poly.fit_transform(X_temo)
        
        X_teme = X_test[:, np.newaxis]
        X_test_poly = poly.fit_transform(X_teme)
        
        reg.fit(X_poly,Y_train_number[j]);
        
        coef_list.append(reg.coef_)
        temp = reg.predict(X_test_poly)
        prediction_list.append(temp)

    coef = np.array(coef_list)
    prediction = np.array(prediction_list)

    for j in range(X_test.shape[0]):
        X_specific_sample = prediction[:,j]
        # print(X_specific_sample)
        # print(y_test[j])
        expec = np.sum(X_specific_sample)
        expec = expec/10
        X_specific_sample = (X_specific_sample - expec)
        X_specific_sample**=2
        X_specific_sample/=10
        var = np.sum(X_specific_sample)
        varience_list.append(var)
        # print(abs(expec - y_test[j]))
        bias_array_list.append(abs(expec - y_test[j]))

    bias = np.array(bias_array_list)
    varience = np.array(varience_list)
    final_sum = np.sum(bias)
    final_sum = final_sum/X_test.shape[0]
    fi_sum = np.sum(varience)
    fi_sum = fi_sum/X_test.shape[0]
    final_varience_list.append(fi_sum)
    final_bias_list.append(final_sum)

final_bias = np.array(final_bias_list)
final_varience = np.array(final_varience_list)
x_cor = [i for i in range(1,11)]
plt.plot(x_cor,final_varience)
plt.xlabel('degree of model')
plt.ylabel('Varience')
plt.show()
print(final_bias)
print(final_varience)