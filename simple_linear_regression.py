import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Simple_Linear_Regression/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values
print(X)
print(Y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_train,y_train,edgecolors='red')
plt.plot(x_train,regressor.predict(x_train), color = 'blue')
plt.title("Salary vs experience")
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_test,y_test,edgecolors='red')
plt.plot(x_train,regressor.predict(x_train), color = 'blue')
plt.title("Salary vs experience")
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

