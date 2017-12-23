dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data.csv')
dataset$Age = ifelse(is.na(dataset$Age),ave(dataset$Age,FUN = function(x) mean(x,na.rm = TRUE)),dataset$Age)

dataset$Country = factor(dataset$Country,levels = c('France','Spain','Germany'),labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,levels = c('No','Yes'),labels = c(0,1))

library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split ==FALSE)

training_set[, 2:3] = scale(training_set[, 2:3] )
test_set[, 2:3]  = scale(test_set[, 2:3] )