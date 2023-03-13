# Eigenvectors

Eigenvectors are vectors that, when applying a [linear transformation](/Linear%20Algebra/Transformations/Linear%20Transformations.md), will get scaled but will remain on the same direction. Eigenvectors are represented by the following equation,

$$\large
	A \vec v = \lambda \vec v
$$

where:

- $A$ is the transformation matrix;
- $\vec v$ is the eigenvector;
- $\lambda$ is the scaling factor of the eigenvector.

> [!tip] How many eigenvectors
> 
> There can be at most $\text{rank}(A)$ eigenvectors in a transformation, but it isn't guaranteed to be exactly that number.
> 
> For example, take a generic [rotation matrix](Linear%20Algebra/Transformations/Linear%20Transformations.md#Rotation). Geometrically, it's impossible for a vector to be rotated and stay on the same direction as before; even though the rank of a rotation matrix is $2$, there are no eigenvectors.

## Finding Eigenvectors

Eigenvectors can be found via the following process.

$$\large \displaylines{
	A \vec v = \lambda \vec v \\
	A \vec v = \lambda I \vec v \\
	A \vec v - \lambda I \vec v = 0 \\
	(A - \lambda I) \vec v = 0 \\
	\det(A - \lambda I) = 0
} $$
