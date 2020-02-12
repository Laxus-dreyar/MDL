import numpy as np
import math
from sklearn import linear_model
import pickle

dbfile = open('Q1_data/data.pkl','rb')
db = pickle.load(dbfile)
le = db.shape[0]
li_X = []
li_y = []
for i in range(int(le)):
    li_X.append([1,db[i][0]])
    li_y.append(db[i][1])
X = np.array(li_X)
y = np.array(li_y)
print(X)
print(y)
reg = linear_model.LinearRegression().fit(X,y)
coef = reg.coef_
print(coef)
predicted = reg.predict(X)
Bias = predicted
print(predicted)
for i in range(100):
    Bias[i] = abs(Bias[i] - y[i])
    print(Bias[i])