# Finite Automaton

A **deterministic finite automaton** (*DFA*) is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$ where

1. $Q$ is a finite set called **states**,
2. $\Sigma$ is a finite set called the **alphabet**,
3. $\delta : Q \times \Sigma \rightarrow Q$ is the **transition function**,
4. $q_0 \in Q$ is the **start state**,
5. $F \subseteq Q$ is the set of **accept states**, also called **final states**.

Finite Automaton are a kind of automata, with one main difference: the return values are replaced by the final states.

![Deterministic Finite Automaton](?TK)

When an automaton receives an input string, it moves from the initial state according to the input characters, read one by one, and the transition function.

- If the arrival state (the last state after execution) is an accepted (or final) state, then it is said that the automaton **accepts** the input;
- otherwise, it **rejects** the input.

## Nondeterministic Finite Automaton

A **nondeterministic finite automaton** (*NDA*) is a finite automaton where multiple next states may exist for any given state and input.

Formally, a **nondeterministic finite automaton** is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$ where

1. $Q$ is a finite set called **states**,
2. $\Sigma$ is a finite set called the **alphabet**,
3. $\delta : Q \times \Sigma_\varepsilon \rightarrow \mathcal P(Q)$ is the **transition function**,
4. $q_0 \in Q$ is the **start state**,
5. $F \subseteq Q$ is the set of **accept states**, also called **final states**.

> [!note] Notation
> 
> - $P(Q)$ determines the set of all possible subsets of a set $Q$; it is called the **power set** of $Q$.
> - $\Sigma_\varepsilon$ determines the union of an alphabet $\Sigma$ with the empty string, i.e. $\Sigma \cup \set\varepsilon$.

![Nondeterministic Finite Automaton](?TK)

The crucial difference between DFA and NFA is in the **transition function**:
- In a DFA, the transition function takes a *state* and an *input symbol* and produces the *next state*;
- In an NFA, the transition function takes a *state* and an *input symbol* or the *empty string* and produces the *set of possible next states*.

## Language of Automaton

The **language of an automaton** $M$, written $L(M)$, is the set of all input [strings](Foundations%20of%20Computer%20Science/Languages/Strings.md) that lead the automaton from its starting state to a final one.

> [!note] Deterministic Finite Automaton
> 
> Let $M = (Q, \Sigma, \delta, q_0, F)$ be a DFA and let $w = w_1 w_2 \cdots w_n$ be a string where each $w_i$ is a member of the alphabet $\Sigma$. Then, $M$ accepts $w$ if a sequence of state $r_0, r_1, \ldots, r_n$ in $Q$ exists with three conditions:
> 
> 1. $r_0 = q_0$,
> 2. $\delta(r_i, w_{i+1}) = r_{i+1}, \ \text{for } i = 0, \ldots, n-1$
> 3. $r_n \in F$

> [!note] Nondeterministic Finite Automaton
> 
> Similarly, let $M = (Q, \Sigma, \delta, q_0, F)$ be a NFA and let $w = w_1 w_2 \cdots w_m$ be a string where each $w_i$ is a member of the alphabet $\Sigma$. Then, $M$ accepts $w$ if a sequence of state $r_0, r_1, \ldots, r_m$ in $Q$ exists with three conditions:
> 
> 1. $r_0 = q_0$,
> 2. $r_{i+1} \in \delta(r_i, w_{i+1}), \ \text{for } i = 0, \ldots, m-1$
> 3. $r_m \in F$
> 
> Notice that it may be that $m \ge |w|$, because some of the $w_i$ may be $\varepsilon$; in fact, $m = |w|$ if and only if $w_i \neq \varepsilon \ \forall w_i$.

It is said that $M$ **recognizes** a language $A$ if $A = \set{w \mid M \text{ accepts } w}$, or $A \subseteq L(M)$.

##