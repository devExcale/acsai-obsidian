$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \Var#1{{ \text{Var} \left(#1\right) }}$
$\def \Cov#1#2{{ \text{Cov} \left(#1,#2\right) }}$
$\def \bb#1{{ \mathbb{#1} }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \seqop#1#2#3{{ {#2}_1 #1 {#2}_2 #1 \cdots #1 {#2}_{#3} }}$
$\def \indep{{ \mathrel\unicode{x2AEB} }}$

# Covariance

The covariance of two random variables $X,Y$ is a measure of how much the changes of $X$ and $Y$ are related.

The covariance of two random variables $X,Y$, both with finite mean $\E X, \E Y$, is given by the following formula.

$$\large
	\Cov X Y = \E{ [X - \E X][Y - \E Y] }
$$

> [!tip] Covariance of two Random Variables
> 
> The covariance of two distributions tell how much the two distributions are related:
> - if the covariance is positive then there's a proportional trend;
> - if the covariance is negative then there's an inversely proportional trend.

## Properties of the Covariance

1. $\Cov X Y = \E{XY} - {\E X}{\E Y}$

2. $\Cov X X = \Var X$

3. $c \in \bb R \Rightarrow \Cov X c = 0$

4. $c \in \bb R \Rightarrow \Cov{cX}{Y} = c \, \Cov X Y$

5. $c \in \bb R \Rightarrow \Cov{X + c}{Y} = \Cov X Y$

6. $X,Y,Z \text{ r.v.} \Rightarrow \Cov{X + Z}{Y} = \Cov X Y + \Cov Z Y$

7. $\Var{X + Y} = \Var X + \Var Y + 2 \Cov X Y$

8. $X,Y \text{ indep.} \Rightarrow \Cov X Y = 0$
