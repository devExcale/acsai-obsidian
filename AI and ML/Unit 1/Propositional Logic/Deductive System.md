$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Deductive System

A deductive system is a procedure through which it is possible to derive, infer or deduce sentences (*a.k.a. conclusions*) by iteratively applying rules on other sentences (*premises*).

A deductive system $\mathcal D$ is composed by a set of sentences (*a.k.a. axioms*) and a set of *inference rules*.

In a given deductive system $\mathcal D$, If a set $\Gamma = \seq \phi n$ of premises can deduce a conclusion $\psi$, it is said that $\psi$ is a **deductive consequence** of $\Gamma$, denoted by the following.

$$\large
	\Gamma \vdash_{\mathcal D} \psi
$$

Deductive consequence can be checked through propositional logic resolution.

> [!note] Soundness
> 
> A deductive system is said to be **sound** if, for any deductive consequence, an entailment with the same operands holds.
> 
> $$\large
> 	(\Gamma \vdash_{\mathcal D} \psi)
> 	\Longrightarrow
> 	(\Gamma \vDash \psi)
> 	\quad \forall \,\Gamma \vdash_{\mathcal D} \psi
> $$
> 
> By design, every deductive system should be sound.

> [!note] Completeness
> 
> A deductive system is said to be **complete** if, for any entailment in the propositional model, a deductive consequence with the same operands holds.
> 
> $$\large
> 	(\Gamma \vDash \psi)
> 	\Longrightarrow
> 	(\Gamma \vdash_{\mathcal D} \psi)
> 	\quad \forall \,\Gamma \vDash \psi
> $$
> 
> A deductive system doesn't necessarily need to be complete, but it's a good property to have.


## Inference rules

An **inference rule** is a schema in the following form,

$$\large
	\frac{\seq \phi n}{\psi}
	\quad \text{or} \quad
	\frac \Gamma \psi
$$

where $\Gamma = \seq \phi n$ are the premises and $\psi$ is the conclusion.

Any equivalence $\Gamma \equiv \psi$ can be used as an inference rule to deduce $\psi$ from $\Gamma$; moreover, some inference rules are the result of iteratively applying equivalences and other rules, they can be used to make processing faster (e.g. *modus pones*, *modus tollens*).

$$\large
\begin{aligned}
	\text{And-Elimination}&: \quad
	\frac{\phi, \quad \psi}{\phi}, \frac{\phi, \quad \psi}{\psi} \\
	\text{Modus Pones}&: \quad
	\frac{\phi, \quad \phi \Rightarrow \psi}{\psi} \\
	\text{Modus Tollens}&: \quad
	\frac{\lnot\psi, \quad \phi \Rightarrow \psi}{\lnot\phi}
\end{aligned}
$$

## Propositional Logic Resolution

To check whether a set of premises $\Gamma$ entails a conclusion $\psi$, there are some steps to follow:

1. Remove any implication or biconditional through equivalences;
2. Convert the premises to a negated normal form;
3. Convert the premises to a conjunctive normal form;
4. Conjunct the premises with the negated conclusion;
5. Try to derive the empty clause through inference rules.

If an empty clause can be found, then $\psi$ is a deductive consequence of (entailed by) the premises $\Gamma$; otherwise, if all the possible clauses have been explored without finding an empty clause, $\psi$ isn't a conclusion of $\Gamma$.

