import numpy as np
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pickle
import matplotlib.pyplot as plt 

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
        expec = np.sum(X_specific_sample)
        expec = expec/10
        X_specific_sample = (X_specific_sample - expec)
        X_specific_sample**=2
        X_specific_sample/=10
        var = np.sum(X_specific_sample)
        varience_list.append(var)
        bias_array_list.append((expec - y_test[j])*(expec - y_test[j]))

    bias = np.array(bias_array_list)
    varience = np.array(varience_list)
    final_sum = np.sum(bias)
    final_sum = final_sum/X_test.shape[0]
    final_sum = math.sqrt(final_sum)
    fi_sum = np.sum(varience)
    fi_sum = fi_sum/X_test.shape[0]
    final_varience_list.append(fi_sum)
    final_bias_list.append(final_sum)

fig = plt.figure()
plt1 = fig.add_subplot(221) 
plt2 = fig.add_subplot(223)
fig.subplots_adjust(hspace=.5,wspace=0.5) 
final_bias = np.array(final_bias_list)
final_varience = np.array(final_varience_list)
x_cor = [i for i in range(1,11)]
plt1.plot(x_cor,final_bias)
plt1.set_title('Bias vs Degree of model')
plt2.plot(x_cor,final_varience)
plt2.set_title('Varience vs Degree of model')
plt.show()
print(final_bias)
print(final_varience)