# Gaussian Mixture Model

A Gaussian Mixture Model, a.k.a. *GMM*, is a statistical model that uses a mixture of Gaussian probability distributions to represent a pattern or set of data. It is often used for modeling complex data that cannot be accurately described by a single Gaussian distribution, and to cluster and classify datasets where the clusters can be approximated by Gaussian distributions.

In this model, a data point is assumed to be generated from one of several Gaussian distributions, each with its own mean and covariance matrix. The probability density function of a GMM is a weighted sum of Gaussian distributions, where each component represents a cluster or subpopulation of the data.

> [!info]
> 
> Each Gaussian distribution is called a **component**; the set of all means and covariances of the components are called the model's **parameters**.

The goal of a GMM is to estimate the parameters of each Gaussian component, the number of components and the mixing weights that determine the proportion of each component in the mixture. GMMs are commonly used in pattern recognition (clustering), image segmentation, speech recognition, and other applications where data is inherently multimodal or has complex structure.

> [!tip] Dimensionality Reduction
> 
> Another extremely helpful usage of GMM is dimensionality reduction: dimensionality reduction can be applied distinctively on each gaussian component, thus retaining the complex shape of the model.