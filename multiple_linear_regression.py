import pandas as pd
import numpy as np

dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Multiple_Linear_Regression/50_Startups.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:] #to avoid dummy variable trap

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

#backward elimination
import statsmodels.formula.api as sm
X = np.append(arr=np.ones((50,1)).astype('int'), values= X,axis=1)
X_opt = X[:, [0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog=Y,exog=X_opt).fit()
X_opt = X[:, [0,1,3,4,5]]
regressor_ols = sm.OLS(endog=Y,exog=X_opt).fit()
X_opt = X[:, [0,3,4,5]]
regressor_ols = sm.OLS(endog=Y,exog=X_opt).fit()
X_opt = X[:, [0,3,5]]
regressor_ols = sm.OLS(endog=Y,exog=X_opt).fit()
print(regressor_ols.summary())