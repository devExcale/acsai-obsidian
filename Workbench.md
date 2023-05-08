# Workbench

*Just a big TODO list of notes*


![hr](/assets/hr.png)


## AI ML U1

#### Agents

Goal based agent

Consequentialism

Instead of storing all possible percepts, the best solution is to start from a subset of it and then include others while learning.

#### Automata

- [ ] Finite-State LTS means that it has finite states and actions, Finite-State Automata means that it has to end at some point.

- [ ] Every non-deterministic automata can be represented as a deterministic automata, even though the states and actions may increase.

- [ ]  An FSA is deterministic if the outcome of an action is determined, non-deterministic if the outcome isn't determined (i.e. deterministic if for each state every action leads to one state only, non-deterministic otherwise).

#### Searching

- [ ] Graph search vs tree-like search

- [ ] Breadth-first search is complete (if there's a solution it will return it, otherwise it won't)

#### Logic-based Agents

- [ ] Entailment / Models


![hr](/assets/hr.png)


## AI ML U2

#### Training

A model can't be verified on the same dataset it has been trained on, because the model is kind of guaranteed to reach the expected output. To verify the correctness of a model, a dataset with different data is required, so that the model will try to guess the output on data it has never seen.

#### Pearson Correlation Coefficient

The formula calculates the arithmetic means of both x and y, then calculates how much the set of the points change wrt to the mean point. Then, it sums all contributions to calculate the correlation between x and y. 

#### Inductive Bias

Different people (and different AI's) have different experiences, which influences the resulting reasoning.

#### PCA

- [ ] Reconstruction Error

- [ ] Another PCA interpretation: find an orthogonal projection that minimises the reconstruction error

- [ ] What if the sample cardinality is smaller than the data dimensionality

- [ ] There is a way to retrieve the Principal Components from SVD

#### Matrix Calculus

- [ ] First derivative of vector to scalar: Gradient (Dx1)

- [ ] Second derivative of vector to scalar: Hessian (DxD, symmetric)

- [ ] First derivative of vector to vector (D->P): Jacobian (DxP)

- [ ] Second derivative of vector to vector (D->P): High-order Tensor (DxPxP)

- [ ] The hessian can be seen as the jacobian of the gradient

- [ ] Quadratic Forms: $x^T A x$ ($A$ symmetric) | If we call $Ax = b$, then $x^T b$ is the dot product between $x$ and itself after $A$ has been applied. Geometrically, it represents the shape of the *parabola* of the matrix

- [ ] Quadratic form can be applied to asymmetric square matrices too: let $B = \frac{1}{2} A + \frac{1}{2} A^T$, then $B$ is symmetric and the quadratic form can be applied to $B$. 

- [ ] Gradient is linear

- [ ] Lagrange multiplier

#### K-mean

- [ ] Furthest-first Heuristic: first is picked at random, others are picked iteratively based on decreasing distance (updated on each assignment)

#### Supervised Learning

- [ ] Empirical Risk Minimization
- [ ] Bias error
- [ ] Bias-Variance tradeoff (dartboard)
- [ ] Feature weighting (choosing dominant vs superficial features)

#### K-NN

- [ ] Advantages and disadvantages

- [ ] Split the data into training (60%), validation (20%), test (20%)

- [ ] The validation data is used to select or fix the hyper-parameter $k$

- [ ] The training loss function can be defined by classifying the training set itself given a parameter $k$

- [ ] Generally, the increasing order of errors should be train, validation, test

- [ ] **Remember** to estimate scaling / regularizing the data only with the training set, and then apply it to validation / test data too

#### Decision Trees

- [ ] Supervised w/parameters

- [ ] $p_k = \frac{|S_k|}{|S|}$ probability of picking one label

- [ ] **impurity:** misclassification in the data during the mode decision (1 - probab of picking the label picked) $1 - \max_{k \in Y}{p_k}$

- [ ] **Gini impurity:** sort of an *entropy of impurities*, it's computed as the sum of (prob picking) (prob not picking)

- [ ] Geany Imputiry function: $H(S) = \sum_{k \in Y} p_k (1 - p_k)$
- [ ] Etropy function: $- \sum_{k \in Y} p_k \log_2()$

- [ ] Entropy is derived from impurity: impurity is a general concept, entropy is impurity implemented

- [ ] Impurity of a tree: recursive weighted sum of the entropy of both sides of the current branch of the tree.

![hr](/assets/hr.png)


## Computer Vision and NLP

- [ ] CV images are stored in standard NumPy arrays


![hr](/assets/hr.png)


## Statistics

Forchetta: the range of values a variable could assume.

sample vs observation

Data are a random sample of characteristics 

Unit profile: connection between an individual and a unit group

Profile of a specific unit: combination of all values for a ?

Box plot

Response Variable
Explanatory Variable


![hr](/assets/hr.png)


## Data Management and Analysis U2

*Empty, for now...*

![hr](/assets/hr.png)
