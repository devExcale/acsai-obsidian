# Rational  Encoding
---

We can't use the integer system to represent rational numbers, so we have to invent other systems.

### Fixed Point Notation

It's still a positional system. The number is represented by $m+n$ digits:
- The first $m$ digits are the integer part
- The remaining $n$ are the fractional part

$$ \large \begin{gather}

c_{m-1} \cdots c_1 c_0, c_{-1} c_{-2} \cdots c_{-n}
\quad c_i \in \{0,\cdots,b-1\} \\

= \sum^{m-1}_{i=0} c_i b^i + \sum^{-n}_{i=-1} c_i b^i \\

= \sum^{m-1}_{i=0} c_i b^i + \sum^{n}_{i=1} \frac{c_{-i}}{b^i} \\

\end{gather} $$

So the rational number $N$ is a pair represented as $<N_i,N_f>$, made up from an integer part $N_i$ and a fractional one $N_f$.

###### Change of Base

To turn $<N_i,N_f>_a$ into $<N_i,N_f>_b$ :

**Integer part,** same procedure as naturals.
**Fractional part,** similar procedure:
- If the arrival base is 10, use the 
