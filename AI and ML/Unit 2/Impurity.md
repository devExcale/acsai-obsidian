$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$

# Impurity

Impurity, in a Machine Learning context, is a numerical value that represent how accurate a prediction-model is. It usually refers to models that use decision-making algorithms such as [decision trees](AI%20and%20ML/Unit%202/Supervised%20Learning/Decision%20Trees.md), and it is analogous to a loss or cost function.

> [!tip] Classification
> 
> A good classification model should should aim to lower the impurity value.


An impurity function is denoted by $H(S)$, where $S$ is a dataset. Let $S_k \subseteq S$ be subsets divided by label,

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

Like Gini impurity, entropy computes some kind of expectation, but using a function $h(x)$ that measures the *impact* of a single class. For convenience, $h(x)$ must abide to some properties.

The entropy of an event should be inversely proportional to the likelihood of it happening:
- if an event is almost certain to happen, then the entropy should be very small, $\P X \rightarrow 1 \Longrightarrow h(x) \rightarrow 0$;
- if an event is almost impossible to happen, then the entropy should be very big, $\P X \rightarrow 0 \Longrightarrow h(x) \rightarrow \infty$.

If two events are independent, then we should be able to sum the entropy of both events to get the entropy of the joint events: $h(x,y) = h(x) + h(y)$.

A function that satisfies all the previous properties is the $\log$ function. 

$$\large
	h(x) = \log\frac{1}{p_x} = - \log p_x
$$

Hence, the entropy function computes the expectation of the TK of each event.

$$\large
\begin{aligned}
	\E{h(x)} &= \sum_{x \in X} p_x \, h(x) \\
	&= - \sum_{x \in X} p_x \log_2 p_x \\
	&= H(X)
\end{aligned}
$$
