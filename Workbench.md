# Workbench

*Just a big TODO list of notes*


![hr](assets/hr.png)


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


![hr](assets/hr.png)


## AI ML U2

#### Training

A model can't be verified on the same dataset it has been trained on, because the model is kind of guaranteed to reach the expected output. To verify the correctness of a model, a dataset with different data is required, so that the model will try to guess the output on data it has never seen.

#### Pearson Correlation Coefficient

The formula calculates the arithmetic means of both x and y, then calculates how much the set of the points change wrt to the mean point. Then, it sums all contributions to calculate the correlation between x and y. 

#### Inductive Bias

Different people (and different AI's) have different experiences, which influences the resulting reasoning.

#### PCA

- [ ] PCA: point cloud should be centred by subtracting mu

- [ ] PCA: point cloud should be divided by sigma to round the cloud

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

#### Classification vs Regression

- [ ] Regression: turning a hyper-dimensional vector into a scalar
- [ ] Classification: map subsets of hyper-dimensional vectors into a discrete set of scalars 

#### Parametric vs Non-parametric

- [ ] Parametric: the conversion from a vector to the result scalar is given from some set of parameters $\theta$, the model has to be *trained* guess $\theta$
- [ ] Non-parametric: the conversion from a vector to the result scalar doesn't need any set of parameters, the model doesn't have to be trained
- [ ] Example of non-parametric: knn, decision trees


![hr](assets/hr.png)


## Computer Vision and NLP

- [ ] CV images are stored in standard NumPy arrays


![hr](assets/hr.png)


## Statistics

Forchetta: the range of values a variable could assume.

sample vs observation

Data are a random sample of characteristics 

Unit profile: connection between an individual and a unit group

Profile of a specific unit: combination of all values for a ?

Box plot

Response Variable
Explanatory Variable


![hr](assets/hr.png)


## Data Management and Analysis U2

*Empty, for now...*

![hr](assets/hr.png)