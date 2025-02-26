# Homework Assignment 4
# Matthew Hatami

# Question 1-3
df = read.csv("penguins.csv")
str(df)

# lets see how many rows of data we have for each species of penguins
species = table(df$species)
species
# so we have Adelie1:151, Chinstrap:152:219, Gentoo:220:342
# now lets create stratified indices for each species
set.seed(587)
adelie = array(sample(1:150, 150), c(10, 15))
set.seed(587)
chinstrap = array(sample(152:211, 60), c(10, 6))
set.seed(587)
gentoo = array(sample(220:339, 120), c(10,12))




# set the matrix
confMat = matrix(0, nrow=3, ncol=3) #since we have 3 species of penguin
rownames(confMat) = colnames(confMat) = c("Adelie", "Chinstrap", "Gentoo")
for (i in 1:10) {
  test_indices = c(adelie[i,], chinstrap[i,], gentoo[i,])
  test_partition = df[test_indices,]
  train_partition = df[-test_indices,]

  # now lets build the model
  model = naiveBayes(train_partition[,2:6], train_partition[,1])
  
  confMat = confMat + table(predict(model, test_partition[,2:6]), test_partition[,1])
}

confMat 





#################
##################################
###################################################
# Question 4

# let's work on sensitivity and specifity for each of the species:

sensitivity = diag(confMat) / rowSums(confMat)
specificity <- (sum(confMat) - rowSums(confMat) - colSums(confMat) + diag(confMat)) /
  (sum(confMat) - rowSums(confMat))

cat("Sensitivity for Adelie =", sensitivity["Adelie"], "\n")
cat("Specificity for Adelie =", specificity["Adelie"], "\n")
cat("Sensitivity for Chinstrap =", sensitivity["Chinstrap"], "\n")
cat("Specificity for Chinstrap =", specificity["Chinstrap"], "\n")
cat("Sensitivity for Gentoo =", sensitivity["Gentoo"], "\n")
cat("Specificity for Gentoo =", specificity["Gentoo"], "\n")


#################
##################################
###################################################
# Question 5
set.seed(500)
test_indices = sample(1:342, 10)
test_partition = df[test_indices,]
train_partition = df[-test_indices,]


# lets train the model
model = naiveBayes(train_partition[,2:6], train_partition[,1])

# lets predict
confMat = table(predict(model, test_partition[,2:6]), test_partition[,1])
confMat # it shows that his claim was true and the model predicted them all correctly

# although his/her claim about the 100% accuracy measures is true, this accuracy is not reliable.
# the most important reason for this is that the model is probably overfitting. given the large training data and
# small test sample, the model is most probably overfitting and will not generalize to unseen data well