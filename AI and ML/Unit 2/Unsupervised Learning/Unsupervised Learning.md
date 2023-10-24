# Unsupervised Learning

Unsupervised learning is a type of [machine learning](/AI and ML/Unit 2/Machine Learning.md) in which an algorithm learns to make predictions or decisions by training on an unlabelled dataset, which consists of input data only, without classifying labels.

$$\large
	\underbrace{
		\set{ x_i }_{i=1}^N
	}_\text{known}
	\sim
	\underbrace { \mathcal D }_\text{unknown}
$$

The goal of unsupervised learning is to [group together](/AI and ML/Unit 2/Unsupervised Learning/Clustering.md) datapoints with common characteristics in an *unsupervised environment*, i.e. without initial classifiers such as labels, but using the provided training data only. Once an unsupervised model has been trained with a satisfactory accuracy, then the model can be queried to predict to which group a new input could belong to.

## Unsupervised Algorithms

- [K-means Clustering](/AI and ML/Unit 2/Unsupervised Learning/K-means Clustering.md)

- [Gaussian Mixture Model](/AI and ML/Unit 2/Unsupervised Learning/Gaussian Mixture Model.md)
