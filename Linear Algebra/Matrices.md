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

TK