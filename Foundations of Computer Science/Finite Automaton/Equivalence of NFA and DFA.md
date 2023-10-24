# Equivalence of NFA and DFA

It can be proven that, for every NFA $N$, there exists a DFA $M$ such that $L(N) = L(M)$; i.e. *their languages are the same*.

Let $N = (Q, \Sigma, \delta, q_0, F)$ be the NFA recognizing some language $A$. A DFA $M = (Q', \Sigma, \delta', q_0', F')$ can be constructed to recognize $A$.

If $N$ doesn't have any $\varepsilon$-transition, the following initialization can be used.

- $Q' = \mathcal P(Q)$
- $q_0' = \set{q_0}$
- $F' = \set{ R \in Q' \mid R \text{ contains an accept state of } N }$
- $\delta'(R, a) = \bigcup_{r \in R} \delta(r, a) \quad \forall(R,a) \in Q' \times \Sigma$

If $N$ has any $\varepsilon$-transition, the previous initialization can still be used, with the following changes.

- $q_0' = E(\set{q_0})$
- $\delta'(R, a) = \bigcup_{r \in R} E(\delta(r, a)) \quad \forall(R,a) \in Q' \times \Sigma$

> [!note] $\varepsilon$-closure
> 
> The $\varepsilon$-closure $E(R)$ of a set of states $R \subseteq Q$ is the set of all states $q \in Q$ that can be reached from $R$ by traveling along 0 or more $\varepsilon$ arrows.

> [!example] Equivalence example
> 
> As example, take the following image represent two equivalent automaton. On the left there is an initial NFA, on the right there is its equivalent DFA.
> 
> ![Automaton - Equivalence NFA](assets/Automaton%20-%20Equivalence%20NFA.jpg)
> 
> The NFA $N = (Q, \Sigma_\varepsilon, \delta, q_0, F)$ is the following.
> 
> - $Q = \set{1, 2, 3}$
> - $\Sigma_\varepsilon = \set{\varepsilon, a, b}$
> - $q_0 = 1$
> - $F = \set{1}$
> 
> The derived DFA $M = (Q', \Sigma, \delta', q_0', F')$ is the following.
> 
> - $Q' = \mathcal P(Q) = \set{\emptyset, \set{1}, \set{2}, \set{3}, \set{1,2}, \set{1,3}, \set{2,3}, \set{1,2,3}}$
> - $\Sigma = \Sigma_\varepsilon \setminus \set\varepsilon = \set{a, b}$
> - $q_0' = E(F) = E(\set 1) = \set{1,3}$
> - $F' = \set{\set{1}, \set{1,2}, \set{1,3}, \set{1,2,3}}$
> 
> Note that the DFA could be optimised (e.g. states $\set{1,2}$, $\set{1}$ could be removed), so an equivalent automaton is not always the optimal one.
