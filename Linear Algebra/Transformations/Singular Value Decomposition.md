# Singular Value Decomposition

The singular value decomposition is a method to decompose a complex transformation into a series of three simpler transformations, i.e. two [rotations](/Linear%20Algebra/Transformations/Linear%20Transformations.md#Rotation) and a [scaling](/Linear%20Algebra/Transformations/Linear%20Transformations.md#Scaling).

Any matrix $A$, regardless of rank and dimensions, can be decomposed in the following way,

$$\large
	A = U \Sigma V^*
$$

where:
- $U,V$ are orthogonal matrices that represent two rotations;
- $V^*$ is the transpose of $V$;
- $\Sigma$ is a diagonal matrix that represents the scaling.

> [!tip] Transpose of V
> 
> The transpose of $V$ is written as $V^*$ as a reminder that $V$ is orthogonal, i.e. 
> $$V^* = V^T = V^{-1}$$

## Geometric Meaning of SVD

The SVD stems from the following reasoning, similarly to [spectral decomposition](/Linear%20Algebra/Transformations/Spectral%20Decomposition.md): we want to find a set of orthogonal vectors $v_i$ such that, when transformed by $A$, they will stay orthogonal, even if scaled ($\sigma_i \vec u_i$).

$$\large
	A \vec v_i = \sigma_i \vec u_i
$$

Compacting the sets of vectors in matrices, the following identity can be obtained, from which the final formula can be obtained by multiplying by $V^*$ on the right on both sides.

$$\large
\begin{aligned}
	A V &= U \Sigma \\
	A &= U \Sigma V^*
\end{aligned}
$$

The previous formula gives another intuition in the geometric representation of SVD: we want to find a rotation 

## Singular Vectors and Values

- The column vectors of $U$ and $V$ are said to be the **left** and **right** (respectively) **singular vectors** of $A$;
- $\Sigma$ is said to contain the **singular values** of $A$.

The meaning of singular vectors and values are similar to the meaning of eigenvectors for [spectral decomposition](/Linear%20Algebra/Transformations/Spectral%20Decomposition.md):
- the singular vectors are orthogonal vectors that will stay orthogonal once the transformation $A$ has been applied, the right singular vectors $\vec v_i$ will be mapped in the direction of the respective left singular vectors $\vec u_i$;
- the singular values $\sigma_i$ are the factors which scale the left singular vectors $\vec u$ to align with the transformed right singular vectors $v_i$ ($A v_i =\sigma_i u_i$).

### Left Singular Matrix

The left singular matrix $U$ can be computed by performing a [spectral decomposition](/Linear%20Algebra/Transformations/Spectral%20Decomposition.md) on $AA^T$, i.e. $U$ is composed by the eigenvectors of the symmetric matrix $AA^T$, ranked in descending order of their respective eigenvalues.

> [!quote] Proof
> 
> The following series of identities proves that $U$ and $\Sigma$ can be found by performing a spectral decomposition on $AA^T$.
> 
> $$\large
> \begin{aligned}
> 	A A^T &= U \Sigma V^* (U \Sigma V^*)^T \\
> 	&= U \Sigma \underbrace{V^* V}_I \underbrace{\Sigma^T}_\Sigma U^T \\
> 	&= U \Sigma \Sigma U^T \\
> 	&= U \Sigma^2 U^T
> \end{aligned}
> $$

> [!tip] Left Singular Matrix as a Rotation
> 
> The fact that $U$ can be found by a spectral decomposition guarantees that $U$ is an orthogonal matrix, meaning it represents a rotation.

### Right Singular Matrix

The right singular matrix $V$ can be computed by performing a [spectral decomposition](/Linear%20Algebra/Transformations/Spectral%20Decomposition.md) on $A^T A$, i.e. $V$ is composed by the eigenvectors of the symmetric matrix $A^T A$, ranked in descending order of their respective eigenvalues.

> [!quote] Proof
> 
> The following series of identities proves that $V$ and $\Sigma$ can be found by performing a spectral decomposition on $A^T A$.
> 
> $$\large
> \begin{aligned}
> 	A^T A &= (U \Sigma V^*)^T U \Sigma V^* \\
> 	&= V \underbrace{\Sigma^T}_\Sigma \underbrace{U^T U}_I \Sigma V^* \\
> 	&= V \Sigma \Sigma V^T \\
> 	&= V \Sigma^2 V^T
> \end{aligned}
> $$

> [!tip] Right Singular Matrix as a Rotation
> 
> The fact that $V$ can be found by a spectral decomposition guarantees that $V$ is an orthogonal matrix, meaning it represents a rotation.

### Singular Values Matrix

The singular values matrix $\Sigma$ can be computed by performing a [spectral decomposition](/Linear%20Algebra/Transformations/Spectral%20Decomposition.md) on either $A A^T$ or $A^T A$. In both spectral decompositions, the scaling matrix $\Lambda$ is the square of $\Sigma$; given that $\Sigma$ is diagonal, the singular values $\sigma_i$ can be found by taking the square root of the eigenvalues $\lambda_i$ contained in $\Lambda$.

$$\large
\begin{aligned}
	\Sigma^2 &= \Lambda \\
	\sigma_i^2 &= \lambda_i \\
	\sigma_i &= \sqrt \lambda_i
\end{aligned}
$$

## Data Meaning of SVD

TK