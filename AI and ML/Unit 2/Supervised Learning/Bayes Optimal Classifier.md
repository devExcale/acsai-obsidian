# Bayes Optimal Classifier

Theoretically, a complex and unknown generator $\mathcal D$ is assumed to provide output pairs $(x,y)$, where:

- $x \in \mathcal X$ is an element of the set we're interested in learning;
- $y \in \mathcal Y$ is a label assigned to the elements.

$\mathcal D$ can be referred to as a **probability distribution**, where the probability of $(x,y) \in \mathcal X \times \mathcal Y$ is the probability that the label $y$ is assignable to $x$.

Knowing the probability distribution $\mathcal D$, building a prediction function $h : \mathcal X \rightarrow \mathcal Y$ would be trivial. For an input $x$, the function should return the label $y$ such that the probability of $(x,y)$ is maximised, i.e.

$$\large
	h(x) = \arg \max_{ y \in \mathcal Y } \mathcal{D}(x,y)
$$
