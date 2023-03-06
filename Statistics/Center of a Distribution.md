# Center of a Distribution

The center of a distribution can be defined in multiple ways, depending on the needs and on the kind of information we're looking for.

## Mean

The *arithmetic* mean is the sum the observations normalized by the number of observations.

$$\large
	\bar x = \frac{1}{n} \sum_{i=1}^n x_i
	= \frac{x_1 + x_2 + \cdots + x_n}{n}
$$

[Example of Mean ](?TK)

> [!warning] Extreme Values
> 
> The mean is affected by extreme values: changing one of the first/last values into something much lower/higher will greatly affect the mean.


### Properties of the Mean

1. The mean value is *internal*, i.e. $x_1 \le \bar x \le x_n$
2. The mean value is the fair value in the distribution, i.e. $\sum_{i=1}^n x_i = \sum_{i=1}^n \bar x$
3. The sum of all [deviations](?TK) is zero, i.e. $\sum_{i=1}^n (x_i - \bar x) = 0$
4. The mean function is a linear function

## Median

The median is the value in the middle of the ordered set of all observations, i.e. the $j$-th term in the ordered sequence $(x_i)_{i=1}^n$, where $j = \frac{n+1}{2}$.

> [!tip] Middle Values
> 
> If the cardinality of the sample is odd, then the median is the middle value; but if the cardinality is even, then the median is the average ([mean](#Mean)) of the two middle values, which may or may not be an observed value.

[Example of Median](?TK)

> [!warning] Extreme Values
> 
> The median isn't affected by extreme values: changing one of the first/last values into something much lower/higher will not affect the mean, as the mean is only affected by the middle value(s).
