from sklearn import metrics
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Load the iris dataset
dataset = datasets.load_iris()

# Fit a logistic regression model to the data
model = LogisticRegression(max_iter=200)
model.fit(dataset.data, dataset.target)

# Make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# Function to calculate the TP, FP, TN, FN for class 0


def calculate_performance_measures(expected, predicted, class_label):
    TP = FP = TN = FN = 0
    for exp, pred in zip(expected, predicted):
        if exp == class_label and pred == class_label:
            TP += 1  # True Positive
        elif exp != class_label and pred == class_label:
            FP += 1  # False Positive
        elif exp == class_label and pred != class_label:
            FN += 1  # False Negative
        elif exp != class_label and pred != class_label:
            TN += 1  # True Negative
    return TP, FP, TN, FN

# Function to calculate accuracy, precision, recall


def calculate_metrics(TP, FP, TN, FN):
    accuracy = (TP + TN) / (TP + FP + TN + FN)
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    return accuracy, precision, recall


# Calculate performance measures for class 0
class_label = 0
TP, FP, TN, FN = calculate_performance_measures(
    expected, predicted, class_label)
accuracy, precision, recall = calculate_metrics(TP, FP, TN, FN)

# Print the results
print(f"Class: {class_label}")
print(f"TP: {TP}, FP: {FP}, TN: {TN}, FN: {FN}")
print(
    f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}")

# For comparison, use sklearn's classification report and confusion matrix
print("\nSklearn Classification Report:")
print(metrics.classification_report(expected, predicted))
print("\nSklearn Confusion Matrix:")
print(metrics.confusion_matrix(expected, predicted))
