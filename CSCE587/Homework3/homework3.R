# Homework Assignment 3
# Matthew Hatami

## Part A - Simple Linear Regression
# Part A: Question 1
df <- read.csv("hw3data.csv")
summary(df)
pdf("HW3PAQ1.pdf")
plot(df$hrsTreatment,df$secResponse,
     xlab = "hrsTreatment",
     ylab = "secResponse",
     main = "hrsTreatment vs. secResponse")

dev.off()

#################
##################################
###################################################
# Part A: Question 2
# There appears to be a linear relationship between two columns of the dataset
# by increasing the value of "hrsTreatment" the value of "secResponse" tend to decrease
# so I'd say there is a negative correlation between them
# this can be modellled by a linear regression model. 
# logisitic regression isn't suitable here since it uses Sigmoid function
# to model categorical data, this is not the case here.


#################
##################################
###################################################
# Part A: Question 3
linReg <- lm(secResponse ~ hrsTreatment, data=df)
summary(linReg)

#################
##################################
###################################################
# Part A: Question 4

intercept <- coef(linReg)[1]
intercept

slope <- coef(linReg)[2]
slope

# the model predicts that secResponse will decrease by 3.94 with each additional hour of treatment
#################
##################################
###################################################
# Part A: Question 5
pdf("HW3PAQ5.pdf")
par(mfrow = c(2,2))
plot(linReg)
dev.off()

#################
##################################
###################################################
# Part A: Question 6

# Residuals vs. Fitted graph: on x axis we have predicted values and in y axis we have residuals, which is the difference
# between predictions and real values. if the model works perfectly, all the residuals should be zero, but this can't be 
# the case in reality. However, if the residuals are randomly scattered around zero in this graph, we can say that the 
# model is making acceptable predictions. if residuals have a pattern the model might not be appropriate, and we might need
# a more complex model such as a polynomial regression.


#################
##################################
###################################################
# Part A: Question 7
linReg2 = lm(secResponse ~ hrsTreatment + minExercise, data = df)
summary(linReg2)

#################
##################################
###################################################
# Part A: Question 8
r2_linReg = summary(linReg)$r.squared
r2_linReg2 = summary(linReg2)$r.squared

print(paste("Single Regression R^2:", r2_linReg))
print(paste("Double Regression R^2:", r2_linReg2))

cor(df$hrsTreatment, df$minExercise)

# adding the second parameter (minExercise) improved the r-square value from 0.67 to 0.95 which is significant
# it shows that having this second parameter is titally worthwhile.


## Part B - Logistic Regression
# Part B: Question 1

pdf("HW3PBQ1.pdf")
plot(df$hrsTreatment, df$hitTarget,
     main = "hrsTreatment vs. hitTarget",
     xlab = "hrsTreatment",
     ylab = "hitTarget")
dev.off()

#################
##################################
###################################################
# Part B: Question 2
cor(df$hrsTreatment, df$hitTarget)
# running the above line, we can see that the correlation coefficient for these two variables is ~0.82, which
# indicates a relatively strong correlation, so we can model their relationship
# However, given the scatter plot produced in Question 1, hitTarget is a binary variable (it only takes 0 and 1)
# since it's a categorical data, we can use logistic regression model for modeeling their relationship.


#################
##################################
###################################################
# Part B: Question 3
max(df$hitTarget) - df$hitTarget
df$missedTarget <- max(df$hitTarget) - df$hitTarget
summaryStat <- summary(df[,c("missedTarget", "hitTarget", "hrsTreatment")])
print(summaryStat)


