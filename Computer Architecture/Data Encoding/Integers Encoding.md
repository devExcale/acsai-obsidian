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

All the elementary operations in the same way as base-10, except for the subtraction. When we're subtracting one number from another, we always have to check that the first number is equal or greater than the second one, because we're working with naturals and we've yet to introduce negative numbers.


###### Binary Representation of Integers

There are multiple ways to represent integers in binary:
- Modulo and sign
- One's complement
- Two's complement

The first two make operations complicated (preliminary checks on sign and values), while the last one allows for immediate sum and difference, so the **two's complement** method is the most used.

In two's complement, the value of the sequence of digits $c_{n-1} \cdots c_1 c_0$ is given by the following expression:

$$ \large 
N_{2-compl} = -c_{n-1} b^{n-1} \sum^{n-2}_{i=0} c_i 2^i \quad c_i \in \{0,1\}
$$

To use this representation, it is important that we know the exact length of the sequence:

$$ \large \begin{gather}
1101_{2-compl} \text{ with 4 digits: } -2^3 + 2^2 + 1 = -3 \\
1101_{2-compl} \text{ with 5 digits: } 2^3 + 2^2 + 1 = 13
\end{gather} $$

The MSB is a sign indicator:
- If set to 0, we're multiplying by 0 the only negative value, so the number is going to be positive;
- If set to 1, the number is negative (the sum of all positive values is always smaller than the absolute value of the only negative coefficient, formally $\large { b^{n-1} > \sum^{n-2}_{i=0} c_i b^i }$)

**2-compl conversion**
To turn an integer $N$ from base-10 to base-2 in 2-compl with $n$ bits:
- If $N\ge0$, use [iterated divisions](/Representing Numbers.md#Iterated divisions method),
	- if less than $n$ bits are required, the number can be represented and we must 0-pad until $n$ bits are used;
	- otherwise the number cannot be represented using $n$ bits.
- If $N<0$, use iterated divisions on $-N$,
	- if less than $n$ bits are required, the number can be represented and we must 0-pad until $n$ bits are used, the number is the opposite of what we've got now;
	- otherwise the number cannot be represented using $n$ bits.

Given a number $N_{2-compl}$, its opposite can be found by performing a bitwise complement of $N$ and then adding 1. 

[//]: # (TODO: Will do 2-compl opposite proof some other time)

***Ex.*** | *Numbers in 2-compl with 4 bits*

$$ \begin{array}{rll}

9: & \quad \text{ 9 is coded as 1001, requires 4 bits}
&\rightarrow \neg\text{ repr.}\\
5: & \quad \text{ 5 is coded as 101, requires 3 bits}
&\rightarrow 0101\\
-3: & \quad \text{-3 is coded as 0011, requires 4 bits}
&\rightarrow 1101 \\
-9: & \quad \text{ 9 is coded as 1001, requires 4 bits}
&\rightarrow \neg\text{ repr.}\\

\end{array} $$

[//]: # (TODO: 2-compl arithmetics)
