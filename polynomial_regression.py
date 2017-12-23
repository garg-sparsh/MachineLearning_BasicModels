import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Polynomial_Regression/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,Y)
y_pred = regressor.predict(X)

#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
#poly_reg.fit(X,Y)

multi_reg = LinearRegression()
multi_reg.fit(X_poly,Y)
y_multi = multi_reg.predict(X_poly)

plt.scatter(X,Y,color = 'red')
plt.plot(X,y_pred, color = 'blue')
plt.show()

plt.scatter(X,Y,color = 'red')
plt.plot(X,y_multi,color = 'purple')
plt.show()