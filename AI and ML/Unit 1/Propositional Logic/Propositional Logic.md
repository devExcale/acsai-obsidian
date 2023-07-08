$\def \M#1{{ \mathcal M({#1}) }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Propositional Logic

Propositional Logic is one of the most important concepts for reasoning with artificial intelligence. It is a whole mathematical model used to describe and infer the real world.

## Knowledge Base

The knowledge base, *KB*, is the core component of logic, it is a *set of sentences*. The sentences are not the homonymous ones used by humans, but rather they are a way to **assert** something about the world. Sentences can be either *given* as ground truth (**axioms**) or *inferred* from other sentences.

A knowledge base can be queried in two ways:
- **tell,** adding sentences to the KB;
- **ask,** retrieving sentences from the KB.

> [!info] Inferring
> 
> Inferring can happen both when a KB has been told or asked something, it isn't constrained to when it is asked only-.

## Model

A model refers to an *instance of the world* where all propositions of the model assume a certain value. In a world where all propositions can assume boolean values, there are a total of $2^N$ models, where $N$ is the number of propositions.

If a model satisfies a sentence $\alpha$, it is said that *$m$ satisfies $\alpha$* or *$m$ is a model of $\alpha$*. The notation $\M\alpha$ is used to indicate the set of all models of $\alpha$ (i.e. $m \in \M\alpha)$ is a model of $\alpha$).

## Syntax

Syntax defines which sentences are valid sentences and which are invalid, it describes the structure of sentences.

Legal sentences (**propositional formulae**) are discerned in **atomic sentences** and **complex sentences**:

- *atomic sentences* are sentences which are composed of a single *proposition symbol*, a proposition symbol indicates a single proposition (a fact about the world) that can assume a *truth value* (whose domain is defined by semantics);
- *complex sentences* are sentences which are composed of atomic sentences and *operators*, operators define the relations between the atomic sentences.

> [!note] Symbols and Operators
> 
> Syntax defines the sets of all proposition symbols and operators and the rules such that a sentence is valid or invalid, but it doesn't define how interpret symbols or how to apply operators and their result. That is left up to *semantics*.

## Semantics

Semantics define the rules for determining the truth of a sentence with respect to a particular model. In the simplest logic model, semantics define that a proposition can assume just one of two truth values: *true* or *false*.

Semantics then define some other rules:

- The only *pre-existent sentences* are $\top$  (a.k.a. *top*) and $\bot$ (a.k.a. *bottom*), with values *True* and *False* respectively for every model;
- The truth value of every proposition symbol must be assigned to the model directly, it can't be supposed outside the model;
- The rules for all [operators](AI%20and%20ML/Unit%201/Propositional%20Logic/Logical%20Operations.md).

## Evaluation

Two functions are defined to query the values of symbols and sentences: the **interpretation** function and the **valuation** function.

The **interpretation function** takes in input a propositional symbol and returns the truth value of that symbol on the underlying model.

$$\large
	\iota : PL \rightarrow \set{T,F}
$$

The interpretation functions isn't the same for all models, but rather it is dependant on the model: it returns the truth values for the symbols in the model, i.e. given a model such that $\set{\alpha=T,\beta=F}$, then $\iota(\alpha) = T$ and $\iota(\beta) = F$.

The **valuation function** (under $\iota$) takes in input a sentence, it evaluates the truth value of the sentence and it returns it.

$$\large
	v^\iota : \mathcal L_{PL} \rightarrow \set{T,F}
$$