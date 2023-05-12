$\def \M#1{{ \mathcal M({#1}) }}$

# Logical Operators

In boolean proposition logic, the operators are the following (in descending order of precedence).

1. **Negation** $[\,\lnot\,] \rightarrow$ negates a given proposition;
2. **And** $[\,\land\,] \rightarrow$ true if both the LHS and RHS propositions are true;
3. **Or** $[\,\lor\,] \rightarrow$ true if either one of or both the LHS and RHS propositions are true;
4. **Implication** $[\,\Rightarrow\,] \rightarrow$ is true unless the LHS is true and the RHS is false;
5. **Biconditional** $[\,\Leftrightarrow\,] \rightarrow$ it is true if both the LHS and RHS are equal (i.e. *true-true* or *false-false*).

Parenthesis can be used to change the natural order of the operators by first evaluating the operators inside the parenthesis and then the ones outside.

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

**Biconditions can be removed:** biconditions tell that two implications are in place, LHS implies RHS and RHS implies LHS.

$$\large
	\alpha \Leftrightarrow \beta
	\ \equiv \ 
	(\alpha \Rightarrow \beta) \land (\beta \Rightarrow \alpha)
$$
