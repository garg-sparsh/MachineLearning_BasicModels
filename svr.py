import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/SVR/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2:].values

from sklearn.preprocessing import StandardScaler
sc_xscalar = StandardScaler()
X = sc_xscalar.fit_transform(X)
sc_yscalar = StandardScaler()
Y = sc_yscalar.fit_transform(Y)

from sklearn.svm import SVR
regressor = SVR(kernel='rbf',degree=4)
regressor.fit(X,Y)

y_pred = sc_yscalar.inverse_transform(regressor.predict(sc_xscalar.transform(np.array([['6.5']]))))
print(y_pred)

plt.scatter(X,Y, color='red')
plt.plot(X,regressor.predict(X),color = 'blue')
plt.show()
