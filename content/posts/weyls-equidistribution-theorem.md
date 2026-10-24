Title: Weyl's Equidistribution Theorem
Date: 2020-02-05 16:39:57 +0000
Modified: 2025-11-13 15:49:54 +0000
Slug: weyls-equidistribution-theorem
Author: Shobhit Bhatnagar
Category: Number Theory
Tags: 
Summary: Weyl's criterion connects uniform distribution modulo one with exponential sums and averages of Riemann-integrable functions.
Status: published
WordPress_ID: 37

Weyl's criterion lets us test uniform distribution by checking exponential sums. We will prove the equivalence between this test, interval counts, and averages of Riemann-integrable functions. A sequence of real numbers $x_1, x_2, \cdots$ is said to be equidistributed (mod 1) if for every sub-interval $(a,b)\subset [0,1]$, we have

$$
\lim_{N\to \infty}\frac{|\{1\leq n\leq N:\; \langle x_n \rangle\in (a,b)\}|}{N} = b-a
$$

where $\langle x \rangle$ denotes the fractional part of $x$. Weyl's equidistribution criterion states that the following statements are equivalent:

1. $x_1, x_2, \cdots$ are equidistributed (mod 1).
2. For each non-zero integer $k$, we have

    $$
    \lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^N e^{2\pi i k x_n}=0
    $$

3. For each Riemann integrable function $f:[0,1]\to\mathbb{C}$, we have

    $$
    \lim_{N\to \infty}\frac{1}{N}\sum_{n=1}^N f(\langle x_n \rangle) = \int_0^1 f(x) dx
    $$

## Proof: (1) ⇒ (3)

Let $I=[a,b)\subseteq [0,1]$ and note that

$$
\frac{|\{1 \leq n \leq N: \langle x_n \rangle\in [a,b) \}|}{N}=\frac{1}{N}\sum_{n=1}^N \chi_{[a,b)}(\langle x_n \rangle)
$$

where $\chi_{[a,b)}(x)$ equals 1 if $x\in [a,b)$ and 0 otherwise. This shows that (3) holds for the case when $f$ is a characteristic function. Now, let $\lambda_1, \lambda_2\in \mathbb{R}$ and $f_1$, $f_2$ be functions for which (3) holds. Then,

$$
\begin{aligned}\lim_{N\to \infty}\frac{1}{N}\sum_{n=1}^N (\lambda_1 f_1 + \lambda_2 f_2)(\langle x_n \rangle) &= \lim_{N\to \infty} \frac{\lambda_1}{N}\sum_{n=1}^N f_1(\langle x_n\rangle) + \lim_{N\to \infty}\frac{\lambda_2}{N}\sum_{n=1}^Nf_2(\langle x_n\rangle) \\ &= \lambda_1\int_0^1 f_1(x) dx + \lambda_2 \int_0^1 f_2(x) dx \\ &= \int_0^1 (\lambda_1 f_1 + \lambda_2 f_2)(x) dx\end{aligned}
$$

Thus, (3) holds for all linear combinations of characteristic functions of subintervals of $[0,1]$.

Now, let $f:[0,1]\to \mathbb{R}$ be an integrable function, and let $\epsilon >0$. Choose step functions $f_1$ and $f_2$ such that:

- $f_1\leq f\leq f_2$ pointwise
- $\int_0^1 (f_2(x)-f_1(x))dx < \frac{\epsilon}{2}$
- There exists $N_0$ such that $\left|\int_0^1 f_1(x)dx - \frac{1}{N}\sum_{n=1}^N f_1(\langle x_n\rangle) \right| < \frac{\epsilon}{2}$ and $\left|\int_0^1 f_2(x)dx - \frac{1}{N}\sum_{n=1}^N f_2(\langle x_n\rangle) \right| < \frac{\epsilon}{2}$ for all $N\geq N_0$

It follows that for $N\geq N_0$,

$$
\begin{aligned}
\int_0^1 f(x) dx - \frac{1}{N}\sum_{n=1}^N f(\langle x_n\rangle) &\leq \int_0^1 f(x) dx - \frac{1}{N}\sum_{n=1}^N f_1(\langle x_n\rangle) \\
&< \int_0^1 f(x) dx -\int_0^1 f_1(x) dx +\frac{\epsilon}{2} \\
&< \int_0^1 (f_2(x)-f_1(x)) dx + \frac{\epsilon}{2} \\
&< \epsilon
\end{aligned}
$$

In a similar way, we can prove that

$$
\int_0^1 f(x) dx - \frac{1}{N}\sum_{n=1}^N f(\langle x_n\rangle) > -\epsilon \quad \forall\; N\geq N_0
$$

Therefore, we have

$$
\left|\int_0^1 f(x) dx - \frac{1}{N}\sum_{n=1}^N f(\langle x_n\rangle) \right| < \epsilon \quad \forall\; N\geq N_0
$$

To see that (3) holds when $f$ is complex valued, we need only consider the real and imaginary parts separately.

## (2) ⇒ (3)

First let $f$ be continuous and $1$-periodic. Trigonometric polynomials uniformly approximate such functions on the circle. For any $\epsilon>0$, choose

$$
p(x)=\sum_{|k|\leq m}c_k e^{2\pi i kx},\qquad \|f-p\|_\infty<\epsilon.
$$

By (2), the average of $p(x_n)$ tends to its constant coefficient $c_0=\int_0^1p(x)\,dx$. Thus

$$
\limsup_{N\to\infty}\left|\frac1N\sum_{n=1}^N f(\langle x_n\rangle)-\int_0^1 f(x)\,dx\right|\leq2\epsilon.
$$

Letting $\epsilon\to0$ proves the assertion for continuous periodic $f$.

To pass to interval indicators, fix an arc $I$ of the circle. For any $\epsilon>0$, choose continuous periodic functions $g_-$ and $g_+$, with short linear ramps near the endpoints, such that

$$
g_-\leq\chi_I\leq g_+,\qquad \int_0^1(g_+-g_-)\,dx<\epsilon.
$$

Their integrals bracket the length of $I$. Applying the result just proved to $g_-$ and $g_+$ squeezes the limiting interval frequency to that length. The same construction with a small neighborhood of a single point shows that endpoint visits have density zero, so the choice of open, closed, or half-open endpoints does not affect the result. This proves (1). The argument in (1) ⇒ (3) now extends the conclusion to all Riemann-integrable functions.

Periodicity is essential in the first approximation step: a continuous function on $[0,1]$ whose endpoint values differ cannot be uniformly approximated there by trigonometric polynomials.

The implications **(3) ⇒ (1)** and **(3) ⇒ (2)** are obvious.

## References

- Hannigan-Daley, Brad. Equidistribution and Weyl’s criterion. Retrieved from *http://individual.utoronto.ca/hannigandaley/equidistribution.pdf*. Accessed 5 Feb. 2020.
- Stein, Elias M. and Shakarchi, Rami. *Fourier Analysis: An Introduction*. Princeton University Press, 2003
