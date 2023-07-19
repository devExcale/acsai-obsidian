# Spectral Decomposition

The spectral decomposition is a way, based on the [spectral theorem](#Spectral Theorem), to decompose a complex matrix into three simpler matrices. The decomposition is as follows,

$$\large
	A = Q \Lambda Q^T
$$

where:
- $A$ is a symmetric matrix;
- $Q$ is an orthogonal matrix ([rotation](/Linear Algebra/Transformations/Linear Transformations.md#Rotation)) composed of the eigenvectors of $A$;
- $\Lambda$ is a diagonal matrix ([scaling](/Linear Algebra/Transformations/Linear Transformations.md#Scaling)) composed of the eigenvalues of $A$.

The rotation matrices should apply rotations only, so the eigenvectors that compose $Q$ (and $Q^T$) should be normalised.

> [!tip] Decomposition Logic
> 
> The logic behind spectral decomposition is to find the eigenvectors of $A$, rotate them to the cardinal basis, apply the scaling given by the respective eigenvalues and then rotate the eigenvectors back to their original position.

> [!warning] Symmetric Matrix
> 
> Spectral Decomposition works only with symmetric matrices. This is because a symmetric matrix has orthogonal eigenvectors, which can align to the cardinal basis.
