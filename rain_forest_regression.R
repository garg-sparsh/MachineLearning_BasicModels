dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Random_Forest_Regression/Position_Salaries.csv')
dataset = dataset[2:3]

library(randomForest)
set.seed(1234)
regressor = randomForest(x = dataset[1], y = dataset$Salary, ntree = 200)
y_pred = predict(regressor,data.frame(Level = 6.5))

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
library(ggplot2)
ggplot()+geom_point(aes(dataset$Level, dataset$Salary), colour = 'red')+
  geom_line(aes(x_grid, predict(regressor, newdata = data.frame(Level = x_grid)) ), colour = 'blue')
