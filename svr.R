dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/SVR/Position_Salaries.csv')

dataset = dataset[2:3]
library(e1071)
regressor = svm(formula = Salary ~., data = dataset, type = 'eps-regression')

y_pred = predict(regressor, data.frame(Level=6.5))

library(ggplot2)
ggplot()+geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red')+
  geom_line(aes(x = dataset$Level,y = predict(regressor,newdata = dataset)), colour = 'blue')

