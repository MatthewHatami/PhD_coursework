df = read.csv("penguins.csv")

# let's take a look at the dataset first
df

# and lets check the summary of the df before getting started
summary(df)
penguins = read.csv("penguins.csv")
tree_model <- rpart(species ~ island + flipper_length_mm + culmen_length_mm + 
                      culmen_depth_mm + body_mass_g, 
                    data = penguins, 
                    method = "class", 
                    control = rpart.control(minsplit = 2, cp = 0.001))
pdf("HW5Qb.pdf")
print(fit)
par(mar=c(1,1,1,1))
plot(fit, uniform=TRUE)
text(fit, use.n=TRUE, all=TRUE, cex = 0.8)
dev.off()



new_penguin <- data.frame(island = "Biscoe", 
                          flipper_length_mm = 180, 
                          culmen_length_mm = 43, 
                          culmen_depth_mm = 18, 
                          body_mass_g = 4000)

prediction <- predict(tree_model, new_penguin, type = "class")
print(prediction)
# answer to part c: Adelie Chinstrap Gentoo






# question d
tree_model_grad <- rpart(species ~ island + flipper_length_mm + culmen_length_mm + 
                           culmen_depth_mm + body_mass_g, 
                         data = penguins, 
                         method = "class", 
                         control = rpart.control(minsplit = 5, cp = 0.01))

pdf("HW5Qd.pdf")
print(fit)
par(mar=c(1,1,1,1))
plot(fit, uniform=TRUE)
text(fit, use.n=TRUE, all=TRUE, cex = 0.8)
dev.off()




