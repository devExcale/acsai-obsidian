# Integers Encoding
---

###### Binary Representation of Naturals

A natural number $N$ in base 2 with $n$ bits is represented by the formal formula

$$ \large 
N_2 = \sum^{n-1}_{i=0} c_i 2^i \quad c_i \in \{0,1\}
$$

The bit $\large c_0$ is called **LSB** (Less Signifing Bit, holds the lowest value), the bit $\large c_{n-1}$ is called **MSB** (Most Signifying Bit, holds the highest value).

***Ex.*** | *Binary integer to decimal*

$$ \begin{align}
111001_2 &= (1 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0)_{10} \\
&= 57_{10}
\end{align} $$
