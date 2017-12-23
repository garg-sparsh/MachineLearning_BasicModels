import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Decision_Tree_Regression/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

from sklearn.tree import DecisionTreeRegressor
decisionTree = DecisionTreeRegressor(random_state=0)
decisionTree.fit(X,Y)

y_pred = decisionTree.predict('6.5')

print(y_pred)

x_grid = np.arange(min(X),max(X),step=0.1)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(X,Y,color = 'red')
plt.plot(x_grid,decisionTree.predict(x_grid), color = 'blue')
plt.show()