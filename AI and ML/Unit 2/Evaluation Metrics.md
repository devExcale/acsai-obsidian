# Evaluation Metrics

When evaluating the performance of a classification model, several metrics can be used to assess its effectiveness. Here are some commonly used evaluation metrics for binary classification.

## Score

The score of a binary classifier refers to the numerical value or probability assigned to each instance that indicates its likelihood of belonging to the positive class. The score can be used as a measure of confidence or certainty in the classification decision made by the model.

![Binary Classification Score Line](/assets/binary_score_model.png)

## Threshold

In binary classification, a score threshold is a predefined value used to convert the continuous scores assigned by a binary classifier into a categorical prediction; by comparing the score of an instance to the threshold, the classifier determines whether to classify it as belonging to the positive class or the negative class.

When the score of an instance exceeds the threshold, it is classified as positive; otherwise, it is classified as negative. The threshold can be set at different levels depending on the desired trade-off:

- A lower threshold results in more positive predictions, potentially increasing the sensitivity but also increasing the risk of false positives;
- A higher threshold leads to fewer positive predictions, potentially increasing the specificity but also increasing the risk of false negatives.

![Binary Classification Score Threshold](/assets/score_model_threshold.png)

## Confusion Matrix

A confusion matrix is a useful tool to visualize and evaluate the performance of a classifier. It provides a comprehensive summary of the classifier's predictions and their agreement with the actual class labels.

![Binary Confusion Matrix](/assets/confusion_matrix.png)

A binary classifier confusion matrix is a 2x2 matrix that consists of four elements:

- True Positive $[tp]$: The number of instances correctly classified as positive.
- False Positive $[fp]$ The number of instances incorrectly classified as positive.
- True Negative $[tn]$: The number of instances correctly classified as negative.
- False Negative $[fn]$: The number of instances incorrectly classified as negative.

The elements on the diagonal represent correct predictions; the elements on the off-diagonal represent wrong predictions.

> [!info] Optimal Classifier
> 
> An optimal classifier's confusion matrix will be a diagonal matrix: there won't be wrong predictions, so the off-diagonal elements will always be null.

## Accuracy

Accuracy measures the overall correctness of the classifier's predictions. It quantifies the proportion of instances that are correctly classified out of the total number of instances in the dataset.

$$\large
	\text{Accuracy} =
	\frac{tp + tn}{tp + tn + fp + fn}
$$

The number of correct predictions refers to the count of instances that are correctly classified as either positive or negative, while the total number of predictions represents the total number of instances in the dataset.

> [!warning] Drawbacks
> 
> Accuracy provides a straightforward measure of how well the classifier performs in terms of overall correctness. However, it can be misleading in certain scenarios, especially when dealing with imbalanced datasets where the classes are not represented equally. In such cases, a high accuracy value can be achieved by simply predicting the majority class most of the time, while the classifier may struggle to correctly identify the minority class.

## Precision

Precision is used to assess the quality of the positive predictions made by a classifier. It quantifies the proportion of correctly predicted positive instances out of all instances predicted as positive.

$$\large
	\text{Precision}
	= \frac{tp}{tp + fp}
$$

- A high precision indicates that the classifier has a low rate of false positive predictions, meaning it is selective in labelling instances as positive.
- A low precision suggests that the classifier has a higher rate of false positive predictions, resulting in a higher number of instances being falsely labelled as positive.

> [!tip] Use Case
> 
> Precision is particularly useful in scenarios where the cost of false positive predictions is high, such as in medical diagnoses or spam email filtering. In these cases, precision helps assess the classifier's ability to avoid false alarms and provide accurate positive predictions.

## Recall

Recall, also known as sensitivity or true positive rate, is used to measure the classifier's ability to correctly identify positive instances out of all actual positive instances.

$$\large
	\text{Recall}
	= \frac{tp}{tp + fn}
$$

- A high recall indicates that the classifier is effective in capturing most of the positive instances and has a low rate of false negative predictions. It means that the classifier has a good ability to detect positive cases.
- A low recall suggests that the classifier has a higher rate of false negative predictions, resulting in missing a significant number of actual positive instances.

> [!tip] Use Case
> 
> Recall plays a crucial role in situations where identifying all positive instances is critical, such as in disease detection or fraud detection. In medical diagnoses, for example, a high recall ensures that the classifier minimizes the number of missed positive cases, enabling timely intervention and treatment.

## F-Measure

The F-measure is an evaluation metric that combines both precision and recall into a single score. It provides a balanced assessment of a classifier's performance by considering both the ability to avoid false alarms (i.e. precision) and the ability to capture positive instances (i.e. recall).

$$\large
	F_\beta =
	{
		(1 + \beta^2) \cdot \text{Precision} \cdot \text{Recall}
		\over
		\beta^2 \cdot \text{Precision} + \text{Recall}
	}
$$

The parameter β controls the weight assigned to precision and recall:
- when $\beta = 1$ it is called the F1-measure, which provides an equal balance between precision and recall;
- higher $\beta$ values gives more weight to recall;
- lower $\beta$ values gives more weight to precision.

The F-measure is useful when there is an imbalance between the positive and negative classes in the dataset, it provides a comprehensive evaluation of the classifier's performance by considering both false positives and false negatives.

## Positive Rates

Positive rates refer to the proportions associated with the positive class predictions made by a classifier.

- The **True Positive Rate** $[TPR]$ measures the proportion of actual positive instances correctly classified as positive by the classifier.

$$\large
	TPR = \frac{tp}{tp + fn}
$$

> [!note] True Positive Rate
> 
> The $TPR$, which is actually the *recall*, provides insights into how well the classifier captures positive instances and is particularly relevant when the goal is to minimize false negatives.

- The **False Positive Rate** $[FPR]$ measures the proportion of negative instances incorrectly classified as positive by the classifier.

$$\large
	FPR = \frac{fp}{fp + tn}
$$

> [!note] False Positive Rate
> 
> The $FPR$ helps assess the classifier's tendency to produce false alarms by misclassifying negative instances as positive.

## Receiver Operating Characteristic Curve

The *Receiver Operating Characteristic* curve is a graphical representation that illustrates the performance of a classifier by plotting the True Positive Rate against the False Positive Rate at various classification thresholds.

The curve is created by calculating the TPR and FPR for different threshold settings and plotting them on a graph. An optimal classifier would have an ROC curve that reaches the top-left corner of the graph, indicating high sensitivity and low false positive rate.

![ROC curve](/assets/roc_curve.png)

The *area under the ROC curve* (AUC) is commonly used as a metric to quantify the overall performance of the classifier. A higher AUC value indicates better classifier performance in distinguishing between positive and negative instances.

The ROC curve and AUC are useful tools for assessing the discriminative power of a binary classifier and comparing the performance of different models. They provide a comprehensive evaluation of the classifier's ability to balance true positives and false positives across different threshold values, allowing for an informed decision on the threshold selection based on the specific requirements of the problem at hand.