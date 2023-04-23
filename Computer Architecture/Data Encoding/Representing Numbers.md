# Representing Numbers

###### Information Encoding

When dealing with information, we need a mean to picture the information and work with it. In computer science, information can be represented through sequences of symbols taken from a fixed alphabet.

Knowing this, we can define a *code* $C$, which is a set of words formed by the symbols of an alphabet $\Sigma$, called *support* of $C$.

We can use a *coding function* to transmute some kind of information into a uniform type of coded data.
A coding function is defined as $f : I \rightarrow C$, where $I$ is a set of words and $C$ is the set of encoded words (made up by the new alphabet).

***Ex.*** | *Car --> 00, Shuttle --> 01, Airplane --> 10*

We can also define a *decoding function*, to transmute back the coded data into understandable information.
A decoding function is defined as $g : C \rightarrow I$, with the same meanings as the coding function. Typically, this function is the inverse of the coding function.

***Ex.*** | *00 --> Car, 01 --> Shuttle, 10 --> Airplane*


###### Numbers Encoding

When we use our numbers, what we're implicitly doing is using a *positional numeric system*. With this system, we have an alphabet $\Sigma$ made up of $b$ distinct symbols, and every position in the sequence has a *weight*, a value. We can represent the total value of the number $N$ (of $m$ digits) with the formula

$$ \large N_b = \sum^{m-1}_{i=0} c_i b^i \quad c_i \in \Sigma $$

The same number, represented with different alphabets, can hold different value

***Ex.*** | *Decimal system ($b = 10,\, \Sigma = \{0,\cdots,9\}$)*

$$ \begin{align}
254_{10} &= 2 \cdot 10^2 + 5 \cdot 10^1 + 4 \cdot 10^0 \\
&= 200 + 50 + 4
\end{align}$$

***Ex.*** | *Septenary system ($b = 7,\, \Sigma = \{0,\cdots,6\}$)*

$$ \begin{align}
254_{7} &= (2 \cdot 7^2 + 5 \cdot 7^1 + 4 \cdot 7^0)_{10} \\
&= (98 + 35 + 4)_{10} \\
&= 137_{10}
\end{align}$$

These systems have some properties:

- **Representation interval**
The set of numbers we can represent with the current system. With $n$ digits in base $b$, the set of all representable numbers is $\{0,\cdots,b^n-1\}$, its size ($b^n$) is how many numbers we can represent.

- **Representation length**
The number of how many digits we need to represent a number $N$ in base $b$. This number is calculated with the formula $\lfloor{ \log_b N }\rfloor + 1$


###### Polynomial method

The formal formula for converting from base $a$ to base $b$ with this method (*Polynomial method*) is the following:

$$ \large N_{a} = \sum^{n-1}_{i=0} c_i a^i \quad c_i \in \{0, \dots, a-1\} $$

With this, we're expressing $N_a$ as a polynomium using the digits from the alphabet of $b$, then evaluating the expression using arithmetics in base $b$.

***Ex.*** | *Number from base-2 to base-10*

$$ \begin{align}
111001_2 &= (1 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0)_{10} \\
&= (32 + 16 + 8 + 0 + 0 + 1)_{10} \\
&= 57_{10}
\end{align} $$

This method, though, it's difficult to use if the final base $b$ is not base-10 (you'd have to use arithmetic rules you're not used to, arithmetics modulo $b$), so it'd be best to use other methods in this case.

***Ex.*** | *Number from base-7 to base-2*

$$ \begin{align}
3602_7 &= (10 \cdot 21^3 + 20 \cdot 21^2 + 0 \cdot 21^1 + 2 \cdot 21^0)_3 \\
\end{align} $$


###### Iterated divisions method

There exists a proven theorem, the theorem of the Euclidean Division, that states:

$$ \begin{gather}
\text{For every } D,d \in \mathbb{N}
\text{ there exists a unique pair } q,r \in \mathbb{N} \\
\text{ s.t. } D = q \cdot d + r
\text{, with } 0 \le r < d
\end{gather} $$

What this means, really, is that for every number $D$ and a divisor $d$ there is a quotient $q$ and a reminder $r$ :

$$ \begin{align}
q &= D \ \text{div} \ d \\
r &= D \ \text{mod} \ d
\end{align} $$

***Ex.*** | *Number 7, divisor 3*

$$ \begin{align}
q &= 7 \ \text{div} \ 3 = 2\\
r &= 7 \ \text{mod} \ 3 = 1
\end{align} $$

The proof is quite long, so [here](Iterated%20division%20proof.md) it is.

So, to convert a number $N_a$ in base $b$ :
1. Repeatedly divide $N_a$ for $b_a$ (**$\large b$ must be expressed in base $\large a$ and the division must be done in base $\large a$**);
2. The remainders of the division, converted in base $b$, give us the digits, from less signifying to most one, of  $N_a$ expressed in base $b$.

***Ex.*** | *675 (base-10) to base-4*

$$ \begin{align}
657 &: 4 = 164 &&\text{ remainder } 1 \\
164 &: 4 = 41  &&\text{ remainder } 0 \\
 41 &: 4 = 10  &&\text{ remainder } 1 \\
 10 &: 4 = 2   &&\text{ remainder } 2 \\
  2 &: 4 = 0   &&\text{ remainder } 2 \\
\end{align} $$
$$ \rightarrow 675_{10} = 22101_4 $$

***Ex.*** | *317 (base-10) to base-16*

$$ \begin{align}
317 &: 16 = 19 &&\text{ remainder D } (13) \\
 19 &: 16 = 1  &&\text{ remainder } 3 \\
  1 &: 16 = 0  &&\text{ remainder } 1 \\
\end{align} $$
$$ \rightarrow 317_{10} = 13\text{D}_4 $$

This method, though, it's difficult to use if the starting base $b$ is not base-10 (you'd have to use arithmetic rules you're not used to, arithmetics modulo $b$), so it'd be best to use other methods in this case.


###### Mixed method

To convert a number $N_a$ in base $b$, where $a,b\ne10$, it'd be best to use both methods at once: first convert from base-$a$ to base-10, then convert the result to base-$b$.

***Ex.*** | *102202 (base-3) to base-5*

$$ 102202_3 = (3^5 + 2 \cdot 3^3 + 2 \cdot 3^2 + 2)_{10} = 317_{10} $$

$$ \begin{align}
317 &: 5 = 63 &&\text{ remainder } 2 \\
 63 &: 5 = 12 &&\text{ remainder } 3 \\
 12 &: 5 = 2  &&\text{ remainder } 2 \\
  2 &: 5 = 0  &&\text{ remainder } 2 \\
\end{align} $$

$$ \rightarrow 102202_3 = 2232_5 $$


###### Particular bases

When converting from base-$a$ to base-$b$, we can have particular cases where $b = a^k$ or $a = b^k$

In the case base-$a$ --> base-$a^k$ we have that

$$ \large \begin{align}
c_{n-1} \cdots c_1 c_0 \text{ mod } a^k &= c_{k-1} \cdots c_0 \\
c_{n-1} \cdots c_1 c_0 \text{ div } a^k &= c_{n-1} \cdots c_k \\
\end{align} $$

So, if $b = a^k$ and ${ N_a = c_{n-1} \cdots c_1 c_0 }$, then the number in base-$b$ is

$$ \large
(c_{n-1} \cdots c_{hk})_b
\cdots
(c_{3k-1} \cdots c_{2k})_b
(c_{2k-1} \cdots c_k)_b
(c_{k-1} \cdots c_{2k})_b
$$

***Ex.*** | *453 (base-10) to base-100*  ($10^2$)

$$ \large \begin{align}
403_{10} \text{ mod } 100 &= 3 \\
403_{10} \text{ div } 100 &= 4 \\
\end{align} $$
$$ \large \rightarrow 403_{10} = 43_{100}$$

***Ex.*** | *1000111101 (base-2) to base-4* ($2^2$)

$$ \large \begin{array}{rcccccl}
 ( & 10 & 00 & 11 & 11 & 01 & )_2 \\
=( &  2 &  0 &  3 &  3 &  1 & )_4 \\
\end{array} $$


***Ex.*** | *1000111101 (base-2) to base-8* ($2^3$)

$$ \large \begin{array}{rccccl}
 ( & 1 & 000 & 111 & 101 & )_2 \\
=( & 1 &  0  &  7  &  5  & )_8 \\
\end{array} $$

In the case base-$a^k$ --> base-$a$ we just have to convert the single digits into the lower base:

$$ \large (c_{n-1})_b \cdots (c_2)_b (c_1)_b (c_0)_b $$

***Ex.*** | *8315 (base-9) to base-3* ($3^2$)

$$ \large \begin{array}{rccccl}
 ( &  8 &  3 &  1 &  5 & )_9 \\
=( & 22 & 10 & 01 & 12 & )_3 \\
\end{array} $$


***Ex.*** | *8D3A (base-16) to base-2* ($2^4$)

$$ \large \begin{array}{rccccl}
 ( &    8 &    D &    3 &    A & )_{16} \\
=( & 1000 & 1101 & 0011 & 1010 & )_2    \\
\end{array} $$
