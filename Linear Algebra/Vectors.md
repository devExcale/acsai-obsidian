# Vectors

A vector is a mathematical object that either represents a physical quantity or position with magnitude and direction.

A vector can be written as a **linear combination** (*sum of the multiples*) of the components of a basis set of vectors. The basis vectors are usually unit vectors in the direction of the coordinate axes.

> [!info] Cardinal Basis
> 
> In the Cartesian coordinate system, the basis vectors are $\hat{i}$, $\hat{j}$, and $\hat{k}$. They all have length of 1 and are in the direction of the $x$-axis, $y$-axis and $z$-axis respectively.
> 
> This basis is called **Cardinal Basis**.

## Magnitude

The magnitude (or *norm*) of a vector is the physical length from the tail of the vector to its head, it can be calculated using the Pythagorean theorem.

For a vector
$\vec{v} = \begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}$, the magnitude is $|\vec{v}| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$.

## Operations

### Vector Addition

Vectors can be added and subtracted by summing or subtracting their components. 

$$\large
	\vec u + \vec v =
	\begin{bmatrix}
		u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n
	\end{bmatrix}
$$

$$\large
	\vec u - \vec v =
	\begin{bmatrix}
		u_1 - v_1 \\ u_2 - v_2 \\ \vdots \\ u_n - v_n
	\end{bmatrix}
$$

### Scalar Multiplication

Vectors can be multiplied by a scalar. The result of multiplying a vector $\vec{v}$ by a scalar $\lambda$ is a new vector with the same direction but different magnitude. The resulting magnitude is the previous magnitude multiplied by the scalar.

$$\large
	\lambda \vec v =
	\begin{bmatrix}
		\lambda v_1 \\ \lambda v_2 \\ \vdots \\ \lambda v_n
	\end{bmatrix}, \quad
	|\lambda \vec v| = \lambda |\vec v|
$$

### Dot Product

Also called *inner product*, geometrically the dot product represents a vector's *orthogonal projection* on another vector.

*TK geometric meaning*

The dot product can be computed by summing the product of the two vectors' components with the same indices, i.e.

$$\large
	\vec u \cdot \vec v =
	\sum_{i=1}^n u_i v_i =
	u_1 v_1 + u_2 v_2 + \cdots + u_n v_n
$$

There exists another formula to compute the dot product, which is deeply connected to the angle between the two vectors and their length.

$$\large
	\vec u \cdot \vec v = \cos\theta |\vec{u}| |\vec{v}|
$$

From the previous formula, a ratio ([cosine similarity](?TK)) and a new formula to find the angle between two vectors can be found.

$$\large
	\theta = \arccos \frac
		{\vec u \cdot \vec v}
		{|\vec u| |\vec v|}
$$

# Matrix-Vector Multiplication

A vector can be multiplied by a matrix, resulting in a new vector. The $i$-th component of the new vector is calculated by computing the dot product between the $i$-th row of the matrix and the operand vector.

$$\large
	A \vec v =
	
	\begin{bmatrix}
		a_{11} & a_{12} & \dots & a_{1n} \\
		a_{21} & a_{22} & \dots & a_{2n} \\
		\vdots & \vdots & \ddots & \vdots \\
		a_{m1} & a_{m2} & \dots & a_{mn} \\
	\end{bmatrix}
	
	\begin{bmatrix}
		v_1 \\ v_2 \\ \vdots \\ v_n
	\end{bmatrix} =
	
	\begin{bmatrix}
		a_{11}v_1 + a_{12}v_2 + \dots + a_{1n}v_n \\
		a_{21}v_1 + a_{22}v_2 + \dots + a_{2n}v_n \\
		\vdots \\
		a_{m1}v_1 + a_{m2}v_2 + \dots + a_{mn}v_n \\
	\end{bmatrix}
$$

> [!info] Geometric Meaning
> 
> Matrix-Vector multiplication has a special geometric meaning: multiplying a vector by a matrix applies on the vector the [linear transformation](/Linear Algebra/Transformations/Linear Transformations.md) represented by the matrix.
