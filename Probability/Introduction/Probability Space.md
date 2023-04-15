# Probability Space

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$

## Sample Space

$\Omega = \set{ \omega_1, \omega_2, \ldots }$ is called the **sample space**, while the elements are called **outcomes**. $\Omega$ denotes the set of all possible outcomes for an action.

> [!example] Sample Space
> Let the action be:
> - the toss of a coin, then $\Omega = \set{H, T}$;
> - the toss of two coins, then $\Omega = \set{HH, HT, TH, TT}$.

### Countable Spaces

A sample space $\Omega$ is said *countable* if there exists a bijection between $\Omega$ and a subset of $\bb{N}$.

Examples of countable spaces are:

- The set of outcomes of throwing a die;
- The set of natural numbers;
- The set of integer numbers;
- The set of outcomes of throwing a coin infinitely many times.

Examples of uncountable spaces are:

- The set of numbers between 0 and 1.
- The set of real numbers;

> [!tip] Integers Bijection
> TK

## Events

A subset $A \subseteq \Omega$ is called an **event**.

TK operations with events

> [!example] Events
> Let $\Omega = \set{1,2,\ldots,6}$ be the outcomes of throwing a die. Then, examples of events are:
> - $A = \set\text{N is even} = \set{2,4,6}$
> - $B = \set\text{N is 5} = \set{5}$
> - $C = A \cup B = \set\text{N is even or N is 5} = \set{2,4,5,6}$

For every event can be defined a **complementary event** such that:
- $A \cup A^c = \Omega$
- $A \cap A^c = \emptyset$
- $\Omega \setminus A = A^c$

> [!example] Complementary Events
> Let $\Omega$ denote the outcomes of throwing a die.
> Then $\Omega = \{1, 2, \ldots, 6\}$.
> 
> Examples of events are:
> - $A^c = \set\text{N is odd} = \set{1,3,5}$
> - $B^c = \set\text{N is not 5} = \set{1,2,3,4,6}$
> - $C^c = (A \cup B)^c = \set\text{N is neither even nor 5} = \set{1,3}$

## Observable Events

Let $\cal{F} = \set{ A : A \subseteq \Omega}$, then $\cal{F}$ contains all the possible events of a sample space. $\cal{F}$ is said to be the collection of observable events. If an event $A \in \cal{F}$, then $\P{A}$ is said to be the probability of the event.

> [!note] Properties of $\cal{F}$
>- $\Omega \in \cal{F}$
>- $\emptyset \in \cal{F}$
>- $A \in \cal{F} \Leftrightarrow A^c \in \cal{F}$
>- for any sequence of events $(A_n)_{n \ge 1} \in \cal{F}$, it holds $\bigcup\limits_{n=1}^\infty A_n \in \cal{F}$

## Probability Measure

A probability measure is a function that maps events to a value $\in [0, 1]$, it indicates the likely of a certain outcome or event to happen.

Formally, a function $\bb{P} : \cal{F} \rightarrow [0, 1]$ is called a probability measure if:
- $\P{\Omega} = 1$
- For any sequence of disjoint events $(A_n)_{n \ge 1}$ it holds
$$\P{ \bigcup\limits_{n=1}^\infty{ A_n } }
= \sum_{n=1}^\infty \P{A_n}$$

> [!note] Properties of Probability Measures
> - $0 \le \P{A} \le 1 \quad \forall A \in \cal{F}$
> - $\P{A^c} = 1 - \P{A}$
> - $\P{\emptyset} = 0$
> - $\P{A \cup B} = \P{A} + \P{B} - \P{A \cap B}$
> - $\P{A \cup B} = \P{A} + \P{B} \Leftarrow A \cap B = \emptyset$
> - $\P{A \cup B} \le \mathbb{P}(A) + \mathbb{P}(B)$
> - $A \subseteq B \Rightarrow \P{A} \le \P{B}$

## Probability Space

A probability space is defined by the triple $(\Omega, \cal{F}, \bb{P})$, where:

- $\Omega$ is the [sample space](#Sample%20Space);
- $\cal{F}$ is the set of all [observable events](#Observable%20Events);
- $\bb{P}$ is the [probability measure](#Probability%20Measure).

### Uniform Probability Space

The simplest case of probability space is that of a finite sample space $\Omega$ and equally likely outcomes:

$$
	\bb{P}( \set\omega ) = \frac{1}{ |\Omega| }
	\quad \forall \omega \in \cal{F}
$$

By definition of probability measure, because every set $\set{\omega_1}$ is disjoint from every other set $\set{\omega_2}$, this implies that

$$
	\P{A} = \frac{ |A| }{ |\Omega| }
	\quad \forall A \in \cal{F}
$$
