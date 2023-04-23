# Unsupervised Learning

Unsupervised learning is a type of [machine learning](/AI%20and%20ML/Unit%202/Machine%20Learning.md) in which an algorithm learns to make predictions or decisions by training on an unlabelled dataset, which consists of input data only, without classifying labels.

$$\large
	\underbrace{
		\set{ x_i }_{i=1}^N
	}_\text{known}
	\sim
	\underbrace { \mathcal D }_\text{unknown}
$$

The goal of unsupervised learning is to [group together](/AI%20and%20ML/Unit%202/Unsupervised%20Learning/Clustering.md) datapoints with common characteristics in an *unsupervised environment*, i.e. without initial classifiers such as labels, but using the provided training data only. Once an unsupervised model has been trained with a satisfactory accuracy, then the model can be queried to predict to which group a new input could belong to.

## Unsupervised Algorithms

- [K-means Clustering](/AI%20and%20ML/Unit%202/Unsupervised%20Learning/K-means%20Clustering.md)

- [Gaussian Mixture Model](/AI%20and%20ML/Unit%202/Unsupervised%20Learning/Gaussian%20Mixture%20Model.md)
