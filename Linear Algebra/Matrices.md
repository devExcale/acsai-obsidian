# Matrices

A matrix is a special structure composed of numbers, it is composed of $n$ rows and $m$ columns. It is a like a *table* with custom properties, every cell is a real value.

$$\begin{bmatrix}
1 & 2 &  3 &  4\\
5 & 6 &  7 &  8\\ 
8 & 9 & 10 & 11\\
\end{bmatrix}
\text{ is a 3x4 matrix} $$

## Matrix Multiplication

Matrices can be multiplied with either other matrices or vectors.

The result of matrix multiplication is a new matrix that has the same number of rows as the first matrix and the same number of columns as the second matrix. To calculate the entries of the resulting matrix, we take the [dot product](?TK) of each row of the first matrix with each column of the second matrix.

$$\large
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ \end{bmatrix} \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \\ \end{bmatrix} = \begin{bmatrix} 58 & 64 \\ 139 & 154 \\ \end{bmatrix}
$$

> [!tip] Rows and Columns
> 
> When multiplying two matrices, the number of columns of the first matrix must match the number of rows of the second matrix.

## Inverse of a Matrix

The inverse of a matrix $A$, denoted as $A^{-1}$, is the matrix such that the product of A and its inverse gives the identity matrix.

$$\large
	A A^{-1} = A^{-1} A = I
$$

Geometrically, the inverse of a matrix $A$ is a matrix that reverses the linear transformation applied by $A$. If $A$ applies an irreversible transformation (space collapses on a lower dimension, i.e. when the determinant is $0$), then $A^{-1}$ doesn't exist and $A$ is said to be *singular*.

## Diagonal Matrix

A diagonal matrix is a special type of square matrix where all the non-diagonal elements are zero, but the values on the diagonal can be anything.

$$\large
	\begin{bmatrix}
		d_1 & 0 & \cdots & 0 \\
		0 & d_2 & \cdots & 0 \\
		\vdots & \vdots & \ddots & \vdots \\
		0 & 0 & \cdots & d_n
	\end{bmatrix}
$$

> [!tip] Identity Matrix
> 
> The **identity matrix** is a special case of diagonal matrix, where all the entries in the diagonal are $1$.
> 
> $$\large
> 	I = \begin{bmatrix}
> 		1 & 0 & \cdots & 0 \\
> 		0 & 1 & \cdots & 0 \\
> 		\vdots & \vdots & \ddots & \vdots \\
> 		0 & 0 & \cdots & 1
> 	\end{bmatrix}
> $$
> 
> The identity matrix has the special property that multiplying a vector or another matrix by the identity will result in the starting vector or matrix, i.e. the identity matrix is the only matrix which does not morph the space.

## Symmetric Matrix

A symmetric matrix is a square matrix that is equal to its transpose, i.e.

$$\large
	A = A^T
	\Longleftrightarrow
	a_{ij} = a_{ji} \quad \forall i,j
$$

> [!note] Eigenvectors
> 
> If matrix is symmetric, then all the [eigenvectors](/Linear%20Algebra/Eigenvectors.md) will be **orthogonal** one to each other.

## Orthogonal Matrix

An orthogonal matrix is a square matrix in which all the column vectors are **orthonormal** to each other.

> [!tip] Rotation
> 
> If all the column vectors in an orthogonal matrix are unit vectors (i.e. magnitude $1$), then the matrix represents a pure rotation without any other transformation.

Orthogonal matrices have another property: the transpose of an orthogonal matrix is equal to it's inverse.

$$\large
	Q^T = Q^{-1}
$$

> [!example] Rotation Matrix
> 
> The previous identity can be proven using the formula for the rotation matrix: a rotation by $\theta$ can be reversed by rotating by $-\theta$.
> 
> $$\large
> 	\text{Let } Q(\theta) =
> 	\begin{bmatrix}
> 		\cos\theta & -\sin\theta \\
> 		\sin\theta & \cos\theta
> 	\end{bmatrix},
> $$
> $$\large
> 	\begin{aligned}
> 	\text{then } Q^{-1}(\theta) &= Q(-\theta) \\
> 	&= \begin{bmatrix}
> 		\cos(-\theta) & \sin(-\theta) \\
> 		\sin(-\theta) & \cos(-\theta)
> 	\end{bmatrix} \\
> 	&= \begin{bmatrix}
> 		\cos\theta & \sin\theta \\
> 		-\sin\theta & \cos\theta
> 	\end{bmatrix} \\
> 	&= Q^T(\theta)
> 	\end{aligned}
> $$

