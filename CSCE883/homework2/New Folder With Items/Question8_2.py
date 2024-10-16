import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Load the iris dataset
dataset = datasets.load_iris()

# Fit a logistic regression model to the data
model = LogisticRegression(max_iter=200)
model.fit(dataset.data, dataset.target)

# Make predictions and calculate probabilities
predicted = model.predict(dataset.data)
# Get the predicted probabilities for each class
probs = model.predict_proba(dataset.data)

# Assuming it's a binary classification for class 0 (Iris dataset is multiclass, but we can simplify for class 0 vs. others)
# To simulate a binary classification, let's consider class 0 vs all other classes
# Convert to binary classification problem
binary_target = (dataset.target == 0).astype(int)
probs_class_0 = probs[:, 0]  # Probabilities of belonging to class 0

# Calculate AUC
auc = metrics.roc_auc_score(binary_target, probs_class_0)
print(f"AUC: {auc:.2f}")

# Calculate and plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(binary_target, probs_class_0)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2,
         label=f'ROC curve (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
