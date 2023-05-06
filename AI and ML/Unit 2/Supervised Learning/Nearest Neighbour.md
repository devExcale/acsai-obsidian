$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Nearest Neighbour

Nearest Neighbour, a.k.a. *k-NN*, is a [supervised](/AI%20and%20ML/Unit%202/Supervised%20Learning/Supervised%20Learning.md) machine learning algorithm used to predict classifications on data.

Let the input data live in a $D$ dimensional space, then the goal of k-NN is to infer the classification of the data by looking at the closest $k$ *neighbours* (data points) to the input in the space.

> [!abstract] Assumption
> 
> k-NN works on the assumption that the label of a point should be similar to the label of other nearby points.

## Classifying

Given the training data $\mathcal D = \set{ (x_1, y_1), \ldots, (x_n, y_n)}$ and an input point $v$, the label $y_v$ of $v$ is inferred to be the label of the closest point to $v$,

$$\large \displaylines {
	x^* = \arg \min_{x_i \in \mathcal D} \text d (x_i, v) \\
	y_v = y^* \quad | \quad (x^*, y^*) \in \mathcal D
}$$

where $\text d(\cdot, \cdot)$ refers to a suitable [distance metric](/AI%20and%20ML/Unit%202/Distance%20Metrics.md).

Predicting the label by looking to just the closest datapoint would [overfit](/AI%20and%20ML/Unit%202/Machine%20Learning.md#Fitting%20the%20Data) the model, so the predicted label is decided by the mode of the closest $k$ datapoints to the input.

> [!warning] Multiple Modes
> 
> If the mode are multiple labels (i.e. the distribution is *multimodal*), then the algorithm can choose the label with the most *weight* (i.e. the sum of the distances is the lowest) or just choose one at random.


## Choosing K

Choosing the right hyper-parameter $k$ is important to avoid [underfitting or overfitting](/AI%20and%20ML/Unit%202/Machine%20Learning.md#Fitting%20the%20Data) the model. One heuristic rule of thumb is to set $k = \sqrt{|\mathcal D|}$.

A stable way to choose $k$ is to divide the dataset into three parts:
- **training,** which is stored to be used by the k-NN algorithm;
- **validation,** which is used to fix $k$;
- **testing,** which is used to test the resulting model.

> [!tip] Splitting the dataset
> 
> A good ratio to split the dataset into training / validation / testing would be 60% / 20% / 20%, but it's not a fixed rule. 


$k$ is chosen in an empirical way:
1. pick a range of possible values for $k$ (e.g. 1 - 20);
2. compute the accuracy (or the loss) on the validation set for each value in the $k$-range;
3. pick the $k$ value from the range such that the accuracy is the highest (or the loss is the lowest).

> [!info] Overfit
> 
> Setting $k=1$ will *overfit* the model, because the model would choose the label on too few information (i.e. just the closest point). This could create area patches that are too specific to the training data.
> 
> ![KNN - K equals 1](/assets/knn_k1.png)

> [!info] Underfit
> 
> Setting $k = |\mathcal D|$ will *underfit* the model, because the model would *always* choose the label with the highest frequency. This is called the *best constant predictor*.
> 
> ![KNN - Best Constant Predictor](/assets/knn_best_constant.png)

[Data Normalization](/AI%20and%20ML/Unit%202/Preprocessing/Data%20Normalization.md)