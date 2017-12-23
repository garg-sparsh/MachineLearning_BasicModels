dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/SVR/Position_Salaries.csv')
dataset = dataset[2:3]

library(rpart)
regressor = rpart(formula = Salary ~., data = dataset,control = rpart.control(minsplit = 1))
y_pred = predict(regressor, data.frame(Level = 6.5))

x_grid = seq(min(dataset$Level),max(dataset$Level),0.01)

library(ggplot2)
ggplot()+geom_point(aes(dataset$Level, dataset$Salary), colour = 'red')+
  geom_line(aes(x_grid, predict(regressor, newdata = data.frame(Level = x_grid))), colour = 'blue')
