dataset = read.csv('/Users/sparshgarg/Documents/SantaClara/Machine Learning/Machine Learning_Udemy/Part 3 - Classification/Section 14 - Logistic Regression/Logistic_Regression/Social_Network_Ads.csv')
dataset = dataset[3:5]

set.seed(1234)
split = sample.split(dataset$Purchased, SplitRatio = 3/4)
training_set = subset(dataset,split==TRUE)
test_set = subset(dataset, split==FALSE)

training_set[, 1:2] = scale(training_set[, 1:2])
test_set[, 1:2] = scale(test_set[, 1:2])

