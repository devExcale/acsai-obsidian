# Languages

A language is, trivially, a set of [Strings](Foundations%20of%20Computer%20Science/Languages/Strings.md).

## Properties of Languages

A language is said to be **prefix-free** if no member is a proper prefix of another member. Similarly, it is said to be **suffix-free** if no member is a proper suffix of another member.

The **lexicographic** order of strings is the same dictionary order humans use.

The **shortlex order**, or simply **string order**, is a variant of the lexicographic order where shorter strings have precedence over longer strings.

> [!example] Binary Strings
> 
> The language of binary strings uses a *shortlex order*, because shorter strings have precedence over longer strings, and then comes lexicographic order.
> 
> $$\varepsilon \text{, 0, 1, 00, 01, 10, 11, 000, } \ldots$$

## Regular Languages

A language $L$ is said to be **regular** if there exists a finite automaton that accepts $L$.