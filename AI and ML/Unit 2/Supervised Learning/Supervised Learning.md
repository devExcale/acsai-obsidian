# Supervised Learning

Supervised learning is a type of [machine learning](/AI and ML/Unit 2/Machine Learning.md) in which an algorithm learns to make predictions or decisions by training on a labelled dataset, which consists of input data and the corresponding output label.

$$\large
	\underbrace{
		\set{ x_i, y_i }_{i=1}^N
	}_\text{known}
	\sim
	\underbrace { \mathcal D }_\text{unknown}
$$

The goal of supervised learning is to learn a mapping function from the input variables to the output variables. Once the mapping function is learned, it can be used to make predictions on new, unseen data.

> [!info] Prediction Types
> 
> Based on the label, there exist two types of supervised learning prediction:
> - **Classification,** when the label is a discrete value, either *binary* ($0,1$) or *multi-class* ($1, \ldots, N$);
> - **Regression,** when the output is a continuous value.
>  
> ![regr_vs_class](/assets/regr_vs_class.webp) 

## Supervised Algorithms

- [Nearest Neighbour](/AI and ML/Unit 2/Supervised Learning/Nearest Neighbour.md)
