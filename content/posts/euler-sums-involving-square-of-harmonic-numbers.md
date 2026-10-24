Title: Euler sums involving squared harmonic numbers
Date: 2020-07-23 17:33:33 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: euler-sums-involving-square-of-harmonic-numbers
Author: Shobhit Bhatnagar
Category: Euler Sums and Infinite Series
Tags: euler-sums, polylogarithm, logarithmic-integrals, infinite-series
Summary: Generating functions for squared harmonic numbers provide evaluations of Euler sums and logarithmic integrals.
Status: published
WordPress_ID: 444

The [previous post on Euler sums]({filename}/posts/an-alternating-euler-sum.md) evaluated sums containing $H_n$ and $H_n^{(2)}$. We now turn to squares of harmonic numbers. Their generating function leads to the integral $\int_0^x \frac{\log^3(1-t)}{t}dt$, from which several further evaluations follow.

## A generating function for squared harmonic numbers

Our starting point is the identity

$$
\sum_{n=1}^\infty (H_n)^2 x^n = \frac{\log^2(1-x)+\text{Li}_2(x)}{1-x} ,\quad -1\leq x < 1
$$

This can be derived by plugging $H_n = \int_0^1\frac{1-t^n}{1-t}dt$ and interchanging the sum and the integral. We can rewrite the above equation using the fact that $\sum_{n=1}^\infty H_n^{(2)} x^n = \frac{\text{Li}_2(x)}{1-x}$.

$$
\begin{equation}\label{euler-sums-involving-square-of-harmonic-numbers-eq-1}
\sum_{n=1}^\infty (H_n)^2 x^n = \frac{\log^2(1-x)}{1-x} + \sum_{n=1}^\infty H_n^{(2)} x^n , \quad -1\leq x < 1
\end{equation}
$$

## 1. Evaluation of $\int_0^x \frac{\log^n(1-t)}{t}dt$

In this section, we will derive a formula for the integral $\int_0^x \frac{\log^n(1-t)}{t}dt$ where $n$ is a positive integer. First, we'll consider the case when $0\leq x < 1$. We have:

$$
\begin{equation}\label{euler-sums-involving-square-of-harmonic-numbers-eq-2}
\begin{aligned}
\int_0^x \frac{\log^n (1-t)}{t}dt &= \int_0^{-\log(1-x)} \frac{t^n e^{-t}}{1-e^{-t}}dt \quad (t\mapsto 1-e^{-t}) \\
&= \sum_{j=1}^\infty \int_0^{-\log(1-x)}t^n e^{-jt} dt \\
&= -\sum_{j=1}^\infty \left[e^{-jt}\sum_{i=0}^n \frac{(-1)^{n-i}\log^{n-i}(1-x)}{j^{i+1}}n^{\underline{i}} \right]_0^{-\log(1-x)} \\
&= - \sum_{j=1}^\infty \left( (1-x)^j \sum_{i=0}^n \frac{(-1)^{n-i}\log^{n-i}(1-x)}{j^{i+1}}n^{\underline{i}}-\frac{n!}{j^{n+1}} \right) \\
&= n! \zeta(n+1) + \sum_{i=0}^n (-1)^{n-i+1} n^{\underline{i}}\log^{n-i}(1-x) \text{Li}_{i+1}(1-x) \end{aligned}
\end{equation}
$$

A similar calculation shows that for $-1\leq x < 0$, we have:

$$
\begin{equation}\label{euler-sums-involving-square-of-harmonic-numbers-eq-3}
\begin{aligned}
\int_x^0 \frac{\log^n(1-t)}{t}dt &= -\frac{\log^{n+1}(1-x)}{n+1} - n! \zeta(n+1) + \sum_{i=0}^{n} n^{\underline{i}}\log^{n-i}(1-x)\text{Li}_{i+1}\left(\frac{1}{1-x}\right) \end{aligned}
\end{equation}
$$

## 2. Sums with $(H_n)^2$

We can divide equation $\eqref{euler-sums-involving-square-of-harmonic-numbers-eq-1}$ by $x$ and integrate both sides to get some interesting results.

$$
\begin{align}
\sum_{n=1}^\infty \frac{(H_n)^2}{n}x^n &= -\frac{\log^3(1-x)}{3}-\log(1-x)\text{Li}_2(x)+\text{Li}_3(x), \quad -1\leq x < 1\label{euler-sums-involving-square-of-harmonic-numbers-eq-4}\\
\sum_{n=1}^\infty \frac{(H_n)^2}{n^2}x^n &= \text{Li}_4(x) + \frac{\text{Li}_2^2(x)}{2}-\frac{1}{3}\int_0^x \frac{\log^3(1-t)}{t}dt, \quad -1\leq x \leq 1\label{euler-sums-involving-square-of-harmonic-numbers-eq-5}
\end{align}
$$

Equation $\eqref{euler-sums-involving-square-of-harmonic-numbers-eq-4}$ was derived using results from section 4 of [this post]({filename}/posts/an-alternating-euler-sum.md).

One can now plug in $x=-1$ in equation $\eqref{euler-sums-involving-square-of-harmonic-numbers-eq-5}$ to get:

$$
\boxed{\sum_{n=1}^\infty \frac{(H_n)^2}{n^2}(-1)^{n+1} = \frac{41\pi^4}{1440} + \frac{\pi^2 \log^2(2)}{12}-\frac{\log^4(2)}{12}-\frac{7}{4}\log(3)\zeta(3)-2\text{Li}_4\left(\frac{1}{2}\right)}
$$

Of course, equation $\eqref{euler-sums-involving-square-of-harmonic-numbers-eq-3}$ was used to evaluate $\int_{-1}^0 \frac{\log^3(1-t)}{t}dt$.
