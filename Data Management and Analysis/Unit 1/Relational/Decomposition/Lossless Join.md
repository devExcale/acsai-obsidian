$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \rhojoin#1{{ m_\rho(#1) }}$
$\def \proj#1#2{{ \pi_{#1}({#2}) }}$

# Lossless Join

When [decomposing](/Data%20Management%20and%20Analysis/Unit%201/Relational/Decomposition/Decomposition%20of%20Relations.md) a relation, there could be a loss or altering of data when joining back all the decomposed instances.

A decomposition $\rho = \seq R n$ of a relation $R$ is said to have a lossless join if, for every legal instance $r$ of $R$, it holds that

$$\large
	r = \rhojoin r
$$

where $\rhojoin r$ represents the natural join of all sub-relations in $\rho$, i.e.

$$\large
	\rhojoin r = \, \bowtie_{i=1}^n \pi_{R_i}(r)
$$

## Properties of Decomposition Join

The natural join of all sub-relations in a decomposition $\rho$ has the following properties.

- $\large r \subseteq \rhojoin r$
- $\large \proj{R_i}{\rhojoin r} = \proj{R_i}{r}$
- $\large \rhojoin {\rhojoin r} = \rhojoin r$

## Checking Lossless Join

Given a decomposition $\rho = R_1, R_2, \cdots, R_n$, whether $\rho$ has a lossless join can be checked using the following algorithm.

> [!quote] Algorithm: $\clj X G$
> 
> $\text{Begin}$
> 
> $\quad \text{Let } r = (\text{a table with dim } n \times |R|)$
> 
> $\quad r_{iA} = (A \in R_i) \text{ ? } \alpha_A : \beta_{iA}$
> 
> $\quad \text{For every } X \rightarrow Y \in F \text{ then,}$
> 
> $\quad \text{if } \exists \ t_1, t_2 \text{ s.t. } t_1[X] = t_2[X] \land t_1[Y] \neq t_2[Y] \text{ do:}$
> 
> $\quad \quad \text{For every } A \in Y \text{ do:}$
> 
> $\quad \quad \quad \text{If } t_1[A] = \alpha_A \text{ do:}$
> 
> $\quad \quad \quad \quad t_2[A] = t_1[A]$
> 
> $\quad \quad \quad \text{Else do:}$
> 
> $\quad \quad \quad \quad t_1[A] = t_2[A]$
> 
> $\quad \quad \quad \text{Endif}$
> 
> $\quad \quad \text{Endfor } A \in Y$
> 
> $\quad \text{Endfor } X \rightarrow Y \in F$
> 
> $\quad \text{Repeat For } X \rightarrow Y \in F \text{ until r has aline with all } \alpha \lor r \text{ hasn't changed.}$
> 
> $\quad \text{If r has a row with all } \alpha \text{ then:}$
> 
> $\quad \quad \text{Lossless Join}$
> 
> $\quad \text{Else then:}$
> 
> $\quad \quad \lnot \text{Lossless Join}$
> 
> $\quad \text{Endif}$
> 
> $\text{End}$
