#R Homework Assignment 1 - Due Tuesday 2/4 by 11:59pm
dataset = read.csv('popest2024.csv')
stateData = dataset[dataset$SUMLEV==40, ]
stateData[0:5,0:9 ]

######## Question 1 & 2 ######## 
# rank based on the average of international immigration in 2023 and 2024
IntMigRanked = stateData[order(-(stateData$INTERNATIONALMIG2024)), ] 
IntMigRanked[0:5,5 ] # first 5 rows
IntMigRanked[(nrow(IntMigRanked)-4):nrow(IntMigRanked), "NAME"] # last 5 rows
IntMigRanked[1:5, "NAME"] # first 5 rows

# to print with concatenation (Note: we should only put characters in Cat command, therefore use as.character)
cat("The most internatioanl migration from 7/1/2023 to 6/30/2024 belongs to: "
    , as.character(IntMigRanked[1, "NAME"])) #prints result of question 1

# Question 2
cat("The least internatioanl migration from 7/1/2023 to 6/30/2024 belongs to: "
    , as.character(IntMigRanked[(nrow(IntMigRanked)), "NAME"])) #prints result of question 2





######## Question 3 & 4 ######## 
# similar to questions 1 & 2, I can rank the dataset based on the field "RDEATH2024" and then find the first and last coloumns
# however, I will try to use two new commands (which.max() and which.min()) that I just learnt

cat("The highest death rate belongs to: " , as.character(stateData$NAME[which.max(stateData$RDEATH2024)]))
cat("The lowest death rate belongs to: " , as.character(stateData$NAME[which.min(stateData$RDEATH2024)]))






######## Question 5 & 6 ########
cat("The mean state-level population in 2024: ", mean(stateData$POPESTIMATE2024)) #prints result of question 5
cat("The median state-level population in 2024: ", median(stateData$POPESTIMATE2024))#prints result of question 6




######## Question 7 ########

stateData$NAME[stateData$NPOPCHG_2024<0]
cat(sum(stateData$NPOPCHG_2024<0), "states had a negative change in population from 7/1/2023 to 7/1/2024") #prints results of question 7
cat("states with negative change in their population in that period are: ", as.character(stateData$NAME[stateData$NPOPCHG_2024<0])) #additional informaiton for question 7



######## Question 8 ########
pdf()
hist(stateData$RBIRTH2024, 
     breaks=16, xlab = "State Birth Rates per 1000 people",
     main = "Distribution of State Birth Rates for 2024")
dev.off()


######## Question 9 ########
pdf("international_domestic_migration.pdf")
plot(x=stateData$INTERNATIONALMIG2024, y=stateData$DOMESTICMIG2024,
     main="Domestic vs. Internatoinal Comparison",
     xlab = "International Migration 2024",
     ylab = "Domestic Migration 2024")
#grid(nx = NULL, ny = NULL, col = "gray", lty = "dotted") #uncomment this to get the grids on
#text(stateData$INTERNATIONALMIG2024, stateData$DOMESTICMIG2024, labels = stateData$NAME, pos = 4, cex = 0.8, col = "darkgreen") #uncomment this to see the labels on the points
dev.off()



######## Question 10 ########
region2 = stateData[stateData$REGION == 2, ]
cat(sum(region2$DOMESTICMIG2024 > 0), " states in region 2 had positive domestic migration in the given period")
cat("states: ", as.character(region2$"NAME"[region2$DOMESTICMIG2024>0]), "are states in region 2 with positive domestic immigration")
region2$"NAME"[region2$DOMESTICMIG2024>0]



######## Question 11 ########
region1 = stateData[stateData$REGION == 1, ]
cat("the mean for international migration for states in region 1 is: ", mean(region1$INTERNATIONALMIG2024))




######## Question 12 ########
region4 = stateData[stateData$REGION == 4, ]
cat("the median for international migration for states in region 4 is: ", median(region4$INTERNATIONALMIG2024))




######## Question 13 ########
region3 = stateData[stateData$REGION == 3, ]
region2 = stateData[stateData$REGION == 2, ]
sum(region3$INTERNATIONALMIG2024>max(region2$INTERNATIONALMIG2024))
region3$NAME[region3$INTERNATIONALMIG2024>max(region2$INTERNATIONALMIG2024)]


