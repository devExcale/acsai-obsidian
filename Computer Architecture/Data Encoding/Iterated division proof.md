# Iterated division proof
---

Let a number $N$ of $n$ digits in base $b$ be represented by the [Polynomial method](Representing%20Numbers.md#Polynomial%20method):

$$ \large \begin{align}
N_b &= c_0 + c_1 \cdot b^1 + c_2 \cdot b^2 + \cdots + c_{n-2} \cdot b^{n-2} + c_{n-1} \cdot b^{n-1} \\
&= c_0 + b \cdot ( c_1 + c_2 \cdot b^1 + \cdots + c_{n-2} \cdot b^{n-3} + c_{n-1} \cdot b^{n-2} )
\end{align} $$

We can see that, by dividing by $b$, we get a part of that number as quotient (the part in parenthesis), and another part (always less than $b$) as remainder ($c_0$).

Those remainders, put together in the reverse order in which we got them, give us the representation of the number in base-$b$.

$$ \large \begin{align}

N \text{ mod } b &= c_0 \\
N \text{ div } b &= c_1 + c_2 \cdot b^1 + \cdots + c_{n-2} \cdot b^{n-3} + c_{n-1} \cdot b^{n-2} = N^{(1)} \\
N^{(1)} \text{ mod } b &= c_1 \\
N^{(1)} \text{ div } b &= c_2 + c_3 \cdot b^1 + \cdots + c_{n-2} \cdot b^{n-4} + c_{n-1} \cdot b^{n-3} = N^{(2)} \\
N^{(2)} \text{ mod } b &= c_2 \\
N^{(2)} \text{ div } b &= c_3 + \cdots + c_{n-2} \cdot b^{n-5} + c_{n-1} \cdot b^{n-4} = N^{(3)} \\
&\ \ \vdots \\
N^{(n-1)} \text{ mod } b &= c_{n-1} \\
N^{(n-1)} \text{ div } b &= 0 \\

\end{align} $$

Iterating like this, what we get is a sequence of remainders that, using the polynomial system back, give us the number we've started from. Basically, this is the inverse of the polynomial system.

In fact, using the positional system the number is written as

$$ \large N_b = ( c_0 c_1 \cdots c_{n-2} c_{n-1} )_b $$