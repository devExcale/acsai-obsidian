# Latex Definitions

*A collection of latex macros I use*

---

$$\large
\displaylines{
	\text{[Probability]} \\
	\mathbb P(\cdot)
}
$$

```tex
$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
```

---


$$\large
\displaylines{
	\text{[Expectation]} \\
	\mathbb E(\cdot)
}
$$

```tex
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
```

---

$$\large
\displaylines{
	\text{[Random Variable]} \\
	\mathbb X(\cdot)
}
$$

```tex
$\def \X#1{{ \mathbb{X} \left(#1\right) }}$
```

---

$$\large
\displaylines{
	\text{[Variance]} \\
	\text{Var}(\cdot)
}
$$

```tex
$\def \Var#1{{ \text{Var} \left(#1\right) }}$
```

---

$$\large
\displaylines{
	\text{[Covariance]} \\
	\text{Cov}(\cdot)
}
$$

```tex
$\def \Cov#1{{ \text{Cov} \left(#1\right) }}$
```

---

$$\large
\displaylines{
	\text{[Indicator]} \\
	\mathbb{1}_{A} (\cdot)
}
$$

```tex
$\def \Ind#1#2{{ \mathbb{1}_{#1} \left( {#2} \right) }}$
```

---

$$\large
\displaylines{
	\text{[Bold]} \\
	\mathbb{A,B,C}
}
$$

```tex
$\def \bb#1{{ \mathbb{#1} }}$
```

---

$$\large
\displaylines{
	\text{[Calligraphy]} \\
	\mathcal{A,B,C}
}
$$

```tex
$\def \cal#1{{ \mathcal{#1} }}$
```

---

$$\large
\displaylines{
	\text{[Normal Distribution]} \\
	\mathcal N (\cdot, \cdot)
}
$$

```tex
$\def \ND#1#2{{ \mathcal N \left( {#1},{#2} \right) }}$
```

---

$$\large
\displaylines{
	\text{[Sequence]} \\
	 A_1, A_2, \ldots, A_B
}
$$

```tex
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
```

---

$$\large
\displaylines{
	\text{[Sequence - Functions]} \\
	 A_1(B), A_2(B), \ldots, A_C(B)
}
$$

```tex
$\def \seqf#1#2#3{{ {#1}_1({#2}_1), {#1}_2({#2}_2), \ldots, {#1}_{#3}({#2}_{#3}) }}$
```

---

$$\large
\displaylines{
	\text{[Sequence - w/Operator]} \\
	 B_1 \odot B_2 \odot \ldots \odot B_C
}
$$

```tex
$\def \seqop#1#2#3{{ {#2}_1 #1 {#2}_2 #1 \cdots #1 {#2}_{#3} }}$
```

---

$$\large
\displaylines{
	\text{[Independence]} \\
	\unicode{x2AEB}
}
$$

```tex
$\def \indep{{ \mathrel\unicode{x2AEB} }}$
```

---

$$\large
\displaylines{
	\text{[Propositional Logic Model]} \\
	\mathcal M(\cdot)
}
$$

```tex
$\def \M#1{{ \mathcal M({#1}) }}$
```

---
