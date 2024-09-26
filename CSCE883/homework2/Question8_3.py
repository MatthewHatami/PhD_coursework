from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, LeaveOneOut

# Load the iris dataset
dataset = datasets.load_iris()

# Fit a logistic regression model to the data
model = LogisticRegression(max_iter=200)

# 1. Cross-Validation Error (Using 5-Fold CV as an example)
cv_scores = cross_val_score(
    model, dataset.data, dataset.target, cv=5, scoring='accuracy')

# Calculate the cross-validation error
cv_error = 1 - cv_scores.mean()
print(f"5-Fold Cross-Validation Accuracy: {cv_scores.mean():.2f}")
print(f"5-Fold Cross-Validation Error: {cv_error:.2f}")

# 2. Leave-One-Out Cross-Validation (LOO-CV) Error
loo = LeaveOneOut()
loo_scores = cross_val_score(
    model, dataset.data, dataset.target, cv=loo, scoring='accuracy')

# Calculate the leave-one-out cross-validation error
loo_error = 1 - loo_scores.mean()
print(f"Leave-One-Out Cross-Validation Accuracy: {loo_scores.mean():.2f}")
print(f"Leave-One-Out Cross-Validation Error: {loo_error:.2f}")
