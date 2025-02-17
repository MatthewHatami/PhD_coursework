# Question 1: Categorical data can't be used with k-means clustering since statistical variables such as mean can't be calculated for them


# Question 2: K-means clustering is not a deterministic method, it has a factor of randomness. the initial cluster centroids are chosen randomly
#             in this method, however, we can set a seed value (set.seed()) to get the same randomness, so that we can replicate the same results
#             in different machines or at different times in the same machine





##########################################################################################
######################################################
##################
# Question 3:
df = penguins
head(df) # from this line we can see the numeric columns in the dataset and separate them
df_numeric = df[,c("culmen_length_mm", "culmen_depth_mm", "flipper_length_mm", "body_mass_g")]

head(df_numeric) # checking if we have go the right columns



# now we can define the loop but before that we need to define a vector to store the within cluster sum of squares error
wcss = numeric(20)
for (k in 1:20){
  set.seed(1801) # to make the results repeatable as requested in the homework assignment
  kmeans_result = kmeans(df_numeric, centers=k)
  wcss[k]=kmeans_result$tot.withinss
}


# saving plots to the pdf
pdf("HW2Q3.pdf")
plot(1:20, wcss, type="b", pch=20, col="red",
     xlab="k - number of clusters",
     ylab="within cluster sum of squares"
     )
dev.off()


##########################################################################################
######################################################
##################
# Question 4: I would choose 4, because to my eyes, it's where the elbow is. Increasing the value of k further more,
#             does not improve the situation that much.




##########################################################################################
######################################################
##################
# Question 5:
# in previous question, I chose 4 for my k value, now I continue wiht that.
chosenK=4
set.seed(1801)
kmeans_results = kmeans(df_numeric, centers = chosenK)
clusters = kmeans_results
# lets create the plot now
pdf("HW2Q5.pdf")


plot(df_numeric[,1:4],
     col = kmeans_results$cluster, pch = 19, 
     main = "K-Means Clustering of Penguins Data")

dev.off()


##########################################################################################
######################################################
##################
# Question 6:

# Normalizing data and determining opticam K value using in-class functions
myShift = function(x) {x-min(x, na.rm=TRUE)}
myScale = function(x) {max(x, na.rm=TRUE) - min(x, na.rm=TRUE)}
myNorm = function(x) {myShift(x)/myScale(x)}

# now se can normalize the numeric dataset we built from penguins dataset
df_normalized = as.data.frame(lapply(df_numeric, myNorm))

withinSS = numeric(20) # build the vector to fill later

for (k in 1:20){
  set.seed(1801)
  normalizedKmeans_result=kmeans(df_normalized, centers=k) # this is to run the k-means with k clusters
  withinSS[k] = normalizedKmeans_result$tot.withinss
}

pdf("HW2Q6.pdf")
plot(1:20, withinSS, type="b", pch=19, xlab="k", ylab="within cluster sum of squares")
dev.off()



##########################################################################################
######################################################
##################
# Question 7:
# I would say either values of 4 or 6 are viable options to choose according to this graph. to be on the safe side, I will go with 6.
# the reason why I chose 6 is that although from 4 to 5 there is no much height difference, but from 5 to 6 there is a relatively deep
# fall there, and after that we can't see any large changes in the value of within cluster sum of squares. so it's safe to go with 6


##########################################################################################
######################################################
##################
# Question 8:
normalizedChosenK=4
set.seed(1801)
normalizedKmeans_results = kmeans(df_numeric, centers = normalizedChosenK)
clusters = normalizedKmeans_results
# lets create the plot now
pdf("HW2Q8.pdf")


plot(df_numeric[,1:4],
     col = normalizedKmeans_results$cluster, pch = 19, 
     main = "K-Means Clustering of Penguins Data")

dev.off()


##########################################################################################
######################################################
##################
# Question 9:

# computing distance with euclidan function
distance_matrix = dist(df_normalized, method = "euclidean")

# checking first few samples
print(distance_matrix)



##########################################################################################
######################################################
##################
# Question 10:

#  hierarchical clustering with ward.D2 method
hc = hclust(distance_matrix, method = "ward.D2")

# Save the plot to a PDF file
pdf("HW2Q10.pdf")

# Plot the hierarchical clustering dendrogram
plot(hc, main="Hierarchical Clustering Dendrogram", 
    sub="Method: ward.D2")

dev.off()


##########################################################################################
######################################################
##################
# Question 11:
hc_k = 5

clusters_hc=cutree(hc, hc_k)

# lets make the pdf and do the plot now
pdf("HW2Q11.pdf")
plot(hc, main="clusters outline", xlab="observations", sub="ward.D2 method")


rect.hclust(hc, k = hc_k, border ="red")

dev.off()



##########################################################################################
######################################################
##################
# Question 12:

# assigning penguins to clusters
hc_clusters = cutree(hc, k = hc_k)

# Save the plot to a PDF file
pdf("HW2Q12.pdf")

# Scatter plot of the four numeric features, colored by hierarchical clusters
plot(df_numeric[,1:4], 
     col = hc_clusters, pch = 19, 
     main = "Hierarchical Clustering of Penguins Data")

dev.off()




##########################################################################################
######################################################
##################
# Question 13:
# The difference between Questions 5 and 8 was normalizing the data. in the questions 3-5 we used raw data
# but in the questions 6-8, we used the normalized data and we repeated the same steps.
# normalization process helps us to make sure all feaures make equl contributions
