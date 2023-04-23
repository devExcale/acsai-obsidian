# Linear Transformations

A linear transformation can be seen as a function that *transforms* a vector space in some kind of way. Some transformations that can be applied on a vector space are [scaling](#Scaling), [rotating](#Rotation), [shearing](#Shearing).

[Matrix-Vector multiplication](Linear%20Algebra/Vectors.md#Matrix-Vector%20Multiplication) is used to apply a linear transformation; many transformations applied sequentially can be applied at the same time by multiplying the vector space by a single matrix, which can be computed by multiplying all the matrices together in the order of application.

$$\large
	CBA \vec v = M \vec v, \quad
	\text{where } M = C \times (B \times A)
$$

## Determinant

The determinant of a transformation (and of the respective matrix) represents the scaling factor of the transformation, it represents the ratio between the areas of the parallelograms spanned by the final basis and by the cardinal basis.

If the determinant is:

- **positive,** the transformation preserves orientation and stretches or shrinks the space;
- **negative,** the transformation reverses orientation and reflects the space;
- **zero,** the transformation collapses the space onto a lower-dimensional subspace.

## Translation

TK

## Scaling

A scaling transformation changes the size of an object. The scaling transformation multiplies each component of a vector $\vec v$ by $\alpha$, resulting in a new vector $\vec w = \alpha \cdot \vec v$.

The matrix representation of the scaling transformation has diagonal entries equal to the scaling factor $\alpha$ and all other entries equal to zero. In two dimensions, the scaling transformation matrix is as follows.

$$\large
	\begin{bmatrix}
	\alpha & 0 \\
	0 & \alpha
	\end{bmatrix}
$$

Scaling can also be applied to the single components separately by changing the component's relative entry in the matrix's diagonal. For example, the following matrix doubles only the vertical component of a two-dimensional vector space.

$$\large
	\begin{bmatrix}
	\alpha & 0 \\
	0 & \beta
	\end{bmatrix}
	
	\begin{bmatrix}
	x \\ y
	\end{bmatrix} =
	
	\begin{bmatrix}
	\alpha x \\ \beta y
	\end{bmatrix}
$$

## Rotation

A bidimensional vector space can be rotated by a given angle $\theta$ by multiplying the vector space by the following matrix.

$$\large
	\begin{bmatrix}
	\cos\theta & -\sin\theta \\
	\sin\theta & \cos\theta
	\end{bmatrix}
$$

The angle $\theta$ determines the amount of rotation applied to the vector. For example, rotating a vector by $90$ degrees counter-clockwise results in a new vector that is perpendicular to the original.

> [!tip] Preserving Distance and Angles
> 
> Rotation is a linear transformation that preserves distance and angles between vectors:
> - if two vectors were orthogonal before the transformation, they will still be orthogonal after the transformation;
> - if the angle between two vectors was $\alpha$ before the transformation, it will remain $\alpha$ after the transformation.

## Shearing

A *shear* is a linear transformation that "shears" the vector space in a certain direction. It is defined by a matrix of the form:

$$\large
	S_{xy} = \begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}
	\quad \text{or} \quad
	S_{yx} = \begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}
$$

where $k$ determines the amount and direction of the shear.

When applied to a vector, a shear transformation moves the components of the vector parallel to the direction of the shear, with the amount of movement proportional to the distance from the origin.

## All Transformation Together

All the previous transformations ([scaling](#Scaling), [rotation](#Rotation), [shearing](#Shearing)) can be applied at the same time by multiplying the vector space by the following matrix,

$$\large
	\begin{bmatrix}
		s_x\cos\theta & -c_x\sin\theta \\
		c_y\sin\theta & s_y\cos\theta
	\end{bmatrix}
$$

where:

- $s_x, s_y$ are the scaling factors;
- $\theta$ is the rotation angle;
- $c_x, x_y$ are the shearing factors.
