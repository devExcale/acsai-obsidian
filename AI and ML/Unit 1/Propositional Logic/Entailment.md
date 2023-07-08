$\def \M#1{{ \mathcal M({#1}) }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \seqop#1#2#3{{ {#2}_1 #1 {#2}_2 #1 \cdots #1 {#2}_{#3} }}$

## Entailment

Entailment is *logical consequence*. 

Given two sentences $\phi, \psi$, it is said that $\phi$ entails $\psi$ iff $\M\phi \subseteq \M\psi$, i.e. the set of all models of $\phi$ is a subset of the set of all models of $\psi$.

$$\large
	\phi \vDash \psi
	\quad \Longleftrightarrow \quad
	\M \phi \subseteq \M \psi
$$

Similarly, given a set of sentences $\set\seq \phi n$ and a sentence $\psi$ such that $\psi$ is a logical consequence of $\set\seq \phi n$, i.e. $\M{\seq \phi n} \subseteq \M \psi$, it can be  said that $\seq \phi n$ are the **assumptions** and $\psi$ is the **conclusion**.

$$\large
	\set\seq \phi n \vDash \psi
$$

> [!tip] Implication vs Entailment
> 
> At a first glance, implication and entailment might describe the same thing, but they work on different levels:
> 
> - Implication is a *logical operator* that returns true if the LHS proposition actually implies the RHS proposition;
> - Entailment isn't an operator, but it is a symbol to describe the relation between propositions (i.e. if LHS true then RHS true, otherwise no claim).
> 
> Rephrasing the two concepts, it could even be said that the *implication operator* returns true if the RHS is *entailed* by the LHS, false otherwise.

Because of the entailment definition, the assumptions are *stricter sentences* w.r.t. the conclusion: the assumptions rule out more models than the conclusion do.

## Tautology

Tautology, sometimes called *validity*, refers to those sentences that are satisfied by **all** models (i.e. true for all models).

Let $n$ be the number of propositional symbols in a sentence $\phi$, then a sentence is a tautology (or is valid) if $|\M \phi| = 2^n$, i.e. the number of all possible models given $n$ propositions. Another way to check if a sentence is a tautology is to reduce the sentence to $True$ using [logical equivalences](/AI%20and%20ML/Unit%201/Propositional%20Logic/Logical%20Operations.md#Equivalences).

A tautology is marked by writing the sentence(s) on the RHS of the entailment symbol, with nothing on the LHS.

$$\large
	\vDash \seq \phi n
$$

> [!example] Example
> 
> $\phi = \text{"To be or not to be"}$ isn't a dilemma, it's a tautology ($\vDash \phi$).
> 
> $\phi = \beta \lor \lnot\beta$ can be reduced, by the complement rule, to $\phi = True$, which shows that $\phi$ is indeed a tautology. It can also be checked, by a truth table, that $|\M \phi| = 2$, which is the number of all possible models

## Contradiction

Contradiction is the opposite of tautology, it's a sentence that won't be satisfied by any model (i.e. false for all models).

A sentence $\phi$ is a contradiction if $|\M \phi| = 0$, i.e. there are no models of $\phi$ such that $\phi$ is true in it.

A contradiction is marked by writing the sentence(s) on the RHS of the negated entailment symbol, with nothing on the LHS.

$$\large
	\nvDash \seq \phi n
$$

> [!example]
> 
> The AND complement of any proposition is a contradiction.
> 
> $\phi = \beta \land \lnot\beta$, by the complement rule, can be reduced to $\phi = False$, which shows that there's no model in which $\phi$ is satisfied and hence $\phi$ is a contradiction.

## Equivalences

Given some sentences $\seq \phi n, \psi$, the following entailments / tautologies / contradictions express the same concept, it could be said (by misuse of the term) that they're *equivalent*.

$$\large
\displaylines{
	\seq \phi n \vDash \psi \\
	\seqop{\land} \phi n \vDash \psi \\
	\vDash (\seqop{\land} \phi n) \Rightarrow \psi \\
	\vDash (\phi_1 \Rightarrow (
		\cdots \Rightarrow (\phi_n \Rightarrow \psi) \cdots
	)) \\
	\nvDash \seqop{\land} \phi n \land \lnot\psi
}
$$