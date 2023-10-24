$\def \M#1{{ \mathcal M({#1}) }}$

# Logical Operations

In boolean proposition logic, the operators are the following (in descending order of precedence).

1. **Negation** $[\,\lnot\,] \rightarrow$ negates a given proposition;
2. **And** $[\,\land\,] \rightarrow$ true if both the LHS and RHS propositions are true;
3. **Or** $[\,\lor\,] \rightarrow$ true if either one of or both the LHS and RHS propositions are true;
4. **Implication** $[\,\Rightarrow\,] \rightarrow$ is true unless the LHS is true and the RHS is false;
5. **Biconditional** $[\,\Leftrightarrow\,] \rightarrow$ it is true if both the LHS and RHS are equal (i.e. *true-true* or *false-false*).

Parenthesis can be used to change the natural order of the operators by first evaluating the operators inside the parenthesis and then the ones outside.

> [!note] Literal
> 
> A single propositional symbol, with or without a negation operator, is called a **literal**.

## Equivalences

A sentence $\phi$ is said to be equivalent to a sentence $\psi$ if $\M \phi = \M \psi$. It could also be said that the two sentences are equivalent if they [entail](/AI%20and%20ML/Unit%201/Propositional%20Logic/Entailment.md) each other, i.e. $\phi \vDash \psi$ and $\psi \vDash \phi$.

> [!note]
> 
> It can be proven, by means of a truth table or through other equivalences, that some sentences are equivalent to other sentences.

Most (if not all) properties of boolean operators (*and*, *or*, *not*) work under logical operators too, e.g.

- Associativity (*AND, OR*)
- Commutativity (*AND, OR*)
- Distributivity (*AND, OR*)
- De-Morgan (*AND / OR*)
- Involution (*NOT*)

The inverse and converse of implications don't hold, but a different kind of "opposite" (called **contraposition**) obtained by first inverting the implication and then conversing it does hold.

$$\large
	\alpha \Rightarrow \beta
	\ \equiv \ 
	\lnot\beta \Rightarrow \lnot\alpha
$$

**Implications can be removed:** implications are equivalent to the disjunction of the RHS and the negation of the LHS.

$$\large
	\alpha \Rightarrow \beta
	\ \equiv \ 
	\lnot\alpha \lor \beta
$$

**Biconditionals can be removed:** biconditionals tell that two implications are in place, LHS implies RHS and RHS implies LHS.

$$\large
\begin{aligned}
	\alpha \Leftrightarrow \beta
	\ &\equiv \ 
	(\alpha \Rightarrow \beta) \land (\beta \Rightarrow \alpha)
	\\ &\equiv \
	(\lnot \alpha \lor \beta) \land (\lnot \beta \lor \alpha)
	\\ &\equiv \
	(\lnot \alpha \land \lnot \beta) \lor (\alpha \land \beta)
\end{aligned}
$$

## Negated Normal Form

Negated Normal Form (*a.k.a. NNF*) is a sentence form where all the negations are pushed on the single symbols, rather than on complex sentences, and there are no implications nor equivalences.

Any sentence can be converted to NNF, if not already, by using a combination of equivalences on parts of the sentence until the sentence is in NNF.

## Conjunctive Normal Form

Conjunctive Normal Form (*a.k.a. CNF*) is a sentence form where the sentence is formed by conjunctions ($\land$) of disjunctions ($\lor$) of literals (either $a$ or $\lnot a$).

$$\large
	(\ell_{1,1} \lor \cdots \lor \ell_{1,n_1})
	\land \cdots \land
	(\ell_{m,1} \lor \cdots \lor \ell_{m,n_m})
$$

Any sentence can be converted to CNF, if not already, by converting the sentence into NNF and then distributing the disjunctions over the conjunctions.

$$\large
	\phi \lor (\psi \land \chi)
	\equiv
	(\phi \lor \psi) \land (\phi \lor \chi)
$$