# Nearest Neighbour

Nearest Neighbour, a.k.a. *k-NN*, is a [supervised](/AI%20and%20ML/Unit%202/Supervised%20Learning/Supervised%20Learning.md) machine learning algorithm used to predict classifications on data.

Let the input data live in a $D$ dimensional space, then the goal of k-NN is to infer the classification of the data by looking at the closest $k$ *neighbours* (data points) to the input in the space.

## Classifying

Given the training data $\mathcal D = \set{ (x_1, y_1), \ldots, (x_n, y_n)}$ and an input point $v$, the label $y_v$ of $v$ is inferred to be the label of the closest point to $v$.

$$\large \displaylines {
	x^* = \arg \min_{x_i \in \mathcal D} \text d (x_i, v) \\
	y_v = y^* \quad | \quad (x^*, y^*) \in \mathcal D
}$$

> [!note] Distance metric
> 
> In the mathematical representation of the algorithm, $\text d(\cdot, \cdot)$ refers to a suitable [distance metric](?TK).

Stopping a just one 

## Choosing K

Choosing the right hyper-parameter $k$ is important to avoid [underfitting and overfitting](/AI%20and%20ML/Unit%202/Machine%20Learning.md#Fitting%20the%20Data) the model.

- **Best constant predictor**

## Normalization

Normalizing the data is an important step before trying k-NN. By normalizing 

### Min-Max Normalization

### Normal Normalization

### Feature Normalization


---

k-NN has irregular and non-linear decision boundaries

the distance is important: euclidian distance treats each features as equally important, while some axis could be more important than others (e.g. points on two parallel lines)

min-max normalization: $\large \frac{x - x_{mean}}{x_{max} - x_{min}}$

## Feature Normalization

In high-dimensional spaces, there could be more irrelevant features 

Solving the problem is learning which are the good features and removing the bad features

---

Manifold -> Local PCA

k-NN, infinite data -> Bayes Optimal Classifierc
