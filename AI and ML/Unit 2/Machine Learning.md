# Machine Learning

Machine Learning is a branch of Artificial Intelligence that teaches machines to learn and improve their performance on specific tasks by recognizing patterns in data. Compared to traditional algorithmic approaches, ML can analyse complex situations, adapt to new data and provide greater accuracy and efficiency.

The whole Machine Learning system is based on finding common patterns in the data, called **training set**, which then will be used to make a prediction on new input data.

> [!info] Output Prediction
> 
> The output prediction on the input data can take values of various types, based on the application of the ML algorithms; for example:
> 
> - Discrete labels $\rightarrow Y \subset \mathbb N$
> 
> - Continuous labels $\rightarrow Y \subseteq \mathbb R$
> 
> - Hyper-dimensional vectors, e.g. from the same space of the input data $\rightarrow Y \subset \mathbb R^d$

![Diagram of the Machine Learning workflow](/assets/Diagram - ML Approach (pad).png)

## Learning

Suppose that there exists a *loss function*, such that it has null value if the prediction is correct and grows the more the prediction is wrong. *Learning* is defined as lowering the loss (or *cost*) function when predicting both training and testing data.

$$\large
	\mathcal L( \underbrace{\hat y}_\text{pred.}, \underbrace{y}_\text{gt} )
	\quad \text{where} \quad
	\hat y = h_0(x)
$$

### Regression Loss Functions

- Squared error: $\mathcal L(\hat y, y) = (\hat y - y)^2$

- Absolute error: $\mathcal L(\hat y, y) = |\hat y - y|$

### Classification Loss Functions

- Binary error: *TK* piecewise function, 0 if correct, 1 if wrong

## Types of Machine Learning

- [Unsupervised Learning](/AI and ML/Unit 2/Unsupervised Learning/Unsupervised Learning.md)

- [Supervised Learning](/AI and ML/Unit 2/Supervised Learning/Supervised Learning.md)

- Deep Learning

- Reinforced Learning

## Model

A model is a representation of a system that *learns* from training data, it consists of a set of algorithms and statistical models that interpret the training data in some way such that it can make (hopefully correct) predictions and decisions when given new data.

Models can be distinguished into two categories:

- **Parametric models,** the training data is converted into a set of *parameters* $\theta$ that can be used to make predictions;
- **Non-parametric models,** the training data is stored directly and processed each time a prediction needs to be made, there are no parameters to be inferred.

> [!tip] Instance-based learning
> 
> Non-parametric models are sometimes referred to as *instance-based learning*, because learning for such models is simply storing training data.

## Fitting the Data

Efficiency, correctness and accuracy of a machine learning model all depend from how the model *fits the data*.

A model may fit the data in three ways:

- **Underfitting,** the model is too simple and lacks the ability to learn the patterns and structure present in the data, usually occurs when a model does not fit the training data well enough;

- **Overfitting,** the model is too complex and has learned too many of the noise and small details from the training data, it occurs when a model fits the training data too well;

- **Best fitting,** the model fits the training data well enough to capture the underlying patterns and structure without being biased by the noise and details. The best fitting model is neither underfitting nor overfitting and can accurately predict outcomes of unseen data.

![Graphical examples of over, under and best fitting](/assets/over_under_fit.png)

## Limits of Machine Learning

Machine learning isn't perfect: there are multiple limitations to it.

- **Bias**

The machine is learning from humans, and humans aren't perfect creatures. There could be some kind of bias (either historical or some other type) that could infect the predictions.

- **Noise**

Noise could be present in the data: input data could present some noise, which could make a prediction harder. Moreover, labels in training data may present some form of noise too, which if unproperly treated could shape the predictions to retain the noise.

- **Blackbox**

Most of the time, especially with complex and big models, the models themselves could pose as a blackbox: feed in the data and get out a prediction, but it may be insanely hard to grasp why the models made such a prediction.
