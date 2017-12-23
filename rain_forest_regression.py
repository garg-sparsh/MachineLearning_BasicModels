import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Random_Forest_Regression/Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300, random_state=0)
regressor.fit(X,Y)
y_pred = regressor.predict('6.5')
print(y_pred)
x_grid = np.arange(min(X),max(X),0.01)
x_grid = x_grid.reshape(len(x_grid),1)

plt.scatter(X,Y)
plt.plot(x_grid,regressor.predict(x_grid))
plt.show()






