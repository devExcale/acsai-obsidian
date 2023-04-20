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

![Diagram of the Machine Learning workflow](/assets/Diagram%20-%20ML%20Approach%20(pad).png)

## Types of Machine Learning

- [Unsupervised Learning](/AI%20and%20ML/Unit%202/Unsupervised%20Learning/Unsupervised%20Learning.md)

- [Supervised Learning](/AI%20and%20ML/Unit%202/Supervised%20Learning/Supervised%20Learning.md)

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

## Limits of Machine Learning

Machine learning isn't perfect: there are multiple limitations to it.

- **Bias**

The machine is learning from humans, and humans aren't perfect creatures. There could be some kind of bias (either historical or some other type) that could infect the predictions.

- **Noise**

Noise could be present in the data: input data could present some noise, which could make a prediction harder. Moreover, labels in training data may present some form of noise too, which if unproperly treated could shape the predictions to retain the noise.

- **Blackbox**

Most of the time, especially with complex and big models, the models themselves could pose as a blackbox: feed in the data and get out a prediction, but it may be insanely hard to graps why the models made such a prediction.