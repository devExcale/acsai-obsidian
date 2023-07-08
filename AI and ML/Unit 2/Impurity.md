$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$

# Impurity

Impurity, in a Machine Learning context, is a numerical value that represent how accurate a prediction-model is. It usually refers to models that use decision-making algorithms such as [decision trees](/AI%20and%20ML/Unit%202/Supervised%20Learning/Decision%20Trees.md), and it is analogous to a loss or cost function.

> [!tip] Classification
> 
> A good classification model should should aim to lower the impurity value.


Usually, impurity functions are denoted by $H(S)$, where $S$ is a dataset.

Let $S_k \subseteq S$ be subsets divided by label,

$$\large
	S_k = \set{(x,y) \in S \ | \ y = k}, \quad
	\bigcup_k S_k = S
$$

then, define $p_k$ to be the probability of picking a point of label $k$ from $S$.

$$\large
	p_k = \frac{|S_k|}{|S|}
$$

## Misclassification Impurity

The misclassification impurity measures the probability of mislabelling the label with the highest cardinality.

$$\large
	H(S) = 1 - \max_k(p_k)
$$

> [!example] Example
> 
> Given a set $S$ with 4 points, of which 3 have label $y_1$ and 1 has label $y_2$, then the misclassification impurity of $S$ is
> $$\large
> 	H(S) = 1 - \max{p_k}
> 	= 1 - \max\set{ \frac{3}{4}, \frac{1}{4} }
> 	= \frac{1}{4} = 25\%
> $$

## Gini Impurity

The Gini impurity is an advanced form of misclassification impurity, but it involves all classes instead of considering just the one with the highest cardinality.

$$\large
	G(S) = \sum_{k=1}^K p_k (1 - p_k)
$$

The Gini impurity represents the expectation of randomly classifying a point with the wrong label.

$$\large
\begin{aligned}
	\E{K \ne k}
	&= \E{1 - \P{K = k}} \\
	&= \E{1 - p_k} \\
	&= \sum_{k=1}^K (1 - p_k) p_k \\
	&= G(S)
\end{aligned}
$$

## Entropy

Entropy is defined as the amount of *randomness*, or *chaos*, that is present in a set. The formula that defines entropy is the following.

$$\large
	H(X) \doteq - \sum_{x \in X} p_x \log_2 p_x
$$

> [!abstract] Problem generalization
> 
> The entropy function is denoted as $H(X)$, and not $H(S)$, because we generalize the problem and suppose that $X$ is a random variable instead of a set of points and labels, but the only thing that changes is the notation.

Like Gini impurity, entropy computes some kind of expectation, but using a function $h(x)$ that measures the *excitement* of a single class. For convenience, $h(x)$ must abide to some properties.

The excitement of a class being picked should be inversely proportional to the likelihood of it happening:

- if a class is almost certain to be picked, then the excitement should be very small, $\P X \rightarrow 1 \Longrightarrow h(x) \rightarrow 0$;
- if a class is almost impossible to be picked, then the excitement should be very big, $\P X \rightarrow 0 \Longrightarrow h(x) \rightarrow \infty$.

If two pick events are independent, then we should be able to sum the excitement of both pickings to get the excitement of the joint picking: $h(x,y) = h(x) + h(y)$.

A function that satisfies all the previous properties is the $\log$ function of the inverse of the probability of picking the class, which is equal to the negative $log$ of the probability. 

$$\large
	h(x) = \log\frac{1}{p_x} = - \log p_x
$$

Hence, the entropy function computes the expectation of the excitement of each class.

$$\large
\begin{aligned}
	\E{h(x)} &= \sum_{x \in X} p_x \, h(x) \\
	&= - \sum_{x \in X} p_x \log_2 p_x \\
	&= H(X)
\end{aligned}
$$

> [!tip] Common cases for Entropy
> 
> Here are listed some common cases for entropy:
> 
> - If there is just one class, then $H(X) = 0$, i.e. there is no excitement because the only class present is always going to be picked.
> - If there are $N$ classes equiprobable, then all the classes will have the same excitement. The value of the entropy will be equal to the excitement of all classes, and can be computed by the formula $H(X) = \log_2(N)$.

### Relative Entropy

Given two distributions $P,Q$, the cross entropy $H(P,Q)$ is defined as follows.

$$\large
	H(P,Q) = -\sum_{x \in X} p_x \log q_x
$$

The cross-entropy represents the expected value of the excitement of the classes in $Q$ while using the weights of $P$.

> [!note] Note
> 
> Note that, usually, $H(P,Q) \neq H(Q,P) and k$


Given two distributions $P,Q$
