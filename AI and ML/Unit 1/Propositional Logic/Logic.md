$\def \M#1{{ \mathcal M({#1}) }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Logic

Propositional Logic is one of the most important concepts for reasoning with artificial intelligence. It is a whole mathematical model used to describe and infer the real world.

## Knowledge Base

The knowledge base, *KB*, is the core component of logic, it is a *set of sentences*. The sentences are not the homonymous ones used by humans, but rather they are a way to **assert** something about the world. Sentences can be either *given* as ground truth (**axioms**) or *inferred* from other sentences.

A knowledge base can be queried in two ways:
- **tell,** adding sentences to the KB;
- **ask,** retrieving sentences from the KB.

> [!info] Inferring
> 
> Inferring can happen when a KB has been told or asked anything.

## Model

A model refers to an *instance of the world* where all propositions of the model assume a certain value. In a world where all propositions can assume boolean values, there are a total of $2^N$ models, where $N$ is the number of propositions.

If a model satisfies a sentence $\alpha$, it is said that *$m$ satisfies $\alpha$* or *$m$ is a model of $\alpha$*. The notation $\M\alpha$ is used to indicate the set of all models of $\alpha$ (i.e. $m \in \M\alpha)$ is a model of $\alpha$).

## Syntax

Syntax defines which sentences are valid sentences and which are invalid, it describes the structure of sentences.

Legal sentences are discerned in **atomic sentences** and **complex sentences**:

- *atomic sentences* are sentences which are composed of a single *proposition symbol*, a proposition symbol indicates a single proposition that could be either *true* or *false*;
- *complex sentences* are sentences which are composed of atomic sentences and *operators*, operators define the relations between the atomic sentences.

> [!note] Operators
> 
> Syntax defines the sets of all proposition symbols and operators and the rules such that a sentence is valid or invalid, but it doesn't define how to apply operators and their result. That is left up to *semantics*.

## Semantics

Semantics define the rules for determining the truth of a sentence with respect to a particular model.

*TK*

## Operators

In boolean proposition logic, the operators are the following (in descending order of precedence).

1. **Negation** $[\,\lnot\,] \rightarrow$ negates a given proposition;
2. **And** $[\,\land\,] \rightarrow$ true if both the LHS and RHS propositions are true;
3. **Or** $[\,\lor\,] \rightarrow$ true if either one of or both the LHS and RHS propositions are true;
4. **Implication** $[\,\Rightarrow\,] \rightarrow$ is true unless the LHS is true and the RHS is false;
5. **Biconditional**$[\,\Leftrightarrow\,] \rightarrow$ it is true if both the LHS and RHS are equal (i.e. *true-true* or *false-false*).

Parenthesis can be used to change the natural order of the operators by first evaluating the operators inside the parenthesis and then the ones outside.

### Entailment

Entailment is the equivalent of *logical consequence*. 

Given two propositional formulae $\phi, \psi$, it is said that $\phi$ entails $\psi$ iff $\M\phi \subseteq \M\psi$, i.e. the set of all models of $\phi$ is a subset of the set of all models of $\psi$.

$$\large
	\phi \vDash \psi
	\quad \Longleftrightarrow \quad
	\M \phi \subseteq \M \psi
$$

Similarly, given a set of propositional formulae $\set\seq \phi n$ and a proposition formula $\psi$ such that $\psi$ is a logical consequence of $\set\seq \phi n$, i.e. $\M{\set\seq \phi n} \subseteq \M \psi$, it can be  said that $\seq \psi n$ are the **assumptions** and $\psi$ is the **conclusion**.

$$\large
	\set\seq \phi n \vDash \psi
$$