dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 2 - Regression/Multiple_Linear_Regression/50_Startups.csv')
dataset$State = factor(x = dataset$State, levels =  c('New York','California','Florida'), labels = c(1,2,3))

library(caTools)
set.seed(123)
split = sample.split(dataset,SplitRatio = 4/5)
training_set = subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = dataset) #to test the whole dataset to check the most
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset) #to test the whole dataset to check the most
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = dataset) #to test the whole dataset to check the most
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend, data = dataset) #to test the whole dataset to check the most
summary(regressor)

y_pred = predict(regressor,newdata = test_set)
