# Foundations of Computer Science

#### Pumping Lemma

The Pumping Lemma is a fundamental concept in formal language theory, particularly in the context of regular languages. It is used to demonstrate that certain languages are not regular by showing that they cannot satisfy the requirements of the Pumping Lemma.

The Pumping Lemma states that for any regular language, there exists a constant "p" (the pumping length) such that any string in the language with a length of at least "p" can be divided into three parts, "xyz," where:

1. For any non-negative integer "i," the string "xy^iz" is also in the language.
2. The length of "xy" is at most "p" (i.e., the first part, "xy," is limited in size).
3. The string "y" is not empty (i.e., "y" contains at least one character).

The purpose of the Pumping Lemma is to provide a way to prove that certain languages are not regular. If a language cannot satisfy the conditions of the Pumping Lemma, it cannot be regular. This lemma is a valuable tool for demonstrating the limitations of regular languages and for classifying languages into different classes of formal languages, such as regular, context-free, or context-sensitive languages.

> [!example] \[Exercise] Non-regular language
> 
> *Prove that the language of all strings of $1$'s whose length is a perfect square is not regular.*
> 
> $$\large
> 	D = \set{ 1^{n^2} \mid n \in \mathbb N }
> $$
> 
> Fix any $p$ and consider $s = 1^{p^2}$. Let $s = xyz$, with $|y| > 0$ and $|xy| \le p$; hence, $|y| \le p$.
> 
> $$\large
> \displaylines {
> 	|xyyz| = |xyz| + |y| \\
> 	\begin{aligned}
> 		1. \Rightarrow \quad
> 		   &> |xyz| = p^2 \\
> 		2. \Rightarrow \quad 
> 		   &= |xyz| + |y| = p^2 + |y| \\
> 		   &\le p^2 + p < (p+1)^2
> 	\end{aligned}
> }
> $$
> 
> It is derived that $p^2 < |xyyz| < (p+1)^2$, which proves that $|xyyz|$ isn't a perfect square, so $xyyz \not\in D$.
