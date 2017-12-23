import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 3 - Classification/Section 14 - Logistic Regression/Logistic_Regression/Social_Network_Ads.csv')
X = dataset.iloc[:, 2:4].values
Y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.75,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_scalar = StandardScaler()
x_test = sc_scalar.fit_transform(x_test)
x_train = sc_scalar.fit_transform(x_train)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
print(y_pred)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred) #to check the correctness of prediction





