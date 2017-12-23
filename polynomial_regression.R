dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Polynomial_Regression/Position_Salaries.csv')
dataset = dataset[2:3]
lin_reg = lm(formula = Salary ~ Level, data = dataset) #linear regression

dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary~.,data = dataset)


library(ggplot2)
#Linear Regression plot
ggplot()+geom_point(aes(dataset$Level,dataset$Salary),colour = 'red')+
  geom_line(aes(dataset$Level,predict(lin_reg, newdata = dataset)), colour = 'blue')

#Polynomial Regression plot
ggplot()+geom_point(aes(dataset$Level,dataset$Salary),colour = 'red')+
  geom_line(aes(dataset$Level,predict(poly_reg,newdata = dataset)),colour = 'blue')

y_lin = predict(lin_reg, data.frame(Level = 6.5))
y_pol = predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4 ))