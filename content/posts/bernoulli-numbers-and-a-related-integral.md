Title: Bernoulli numbers and a related integral
Date: 2020-04-19 10:32:48 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: bernoulli-numbers-and-a-related-integral
Author: Shobhit Bhatnagar
Category: Euler Sums and Infinite Series
Tags: bernoulli-numbers, fourier-series, infinite-series, definite-integrals
Summary: From the defining recursion for Bernoulli polynomials to their Fourier expansions and an associated integral.
Status: published
WordPress_ID: 94

Bernoulli polynomials link a simple differential recursion to Fourier series and definite integrals. We begin with their defining conditions, derive the identities we need, and then apply them to an integral.

## Bernoulli polynomials

Define the sequence $\{B_r(x)\}_{r=0}^{\infty}$ by

$$
\begin{aligned}
B_0(x) &= 1 \\
B_r^\prime(x) &= r B_{r-1}(x) \quad \forall r\geq 1 \\
\int_0^1 B_r(x) dx &= 0 \quad \forall r\geq 1
\end{aligned}
$$

The first few Bernoulli Polynomials are:

$$
\begin{aligned}
B_0(x) & =1 \\
B_1(x) & =x-\frac{1}{2} \\
B_2(x) & =x^2-x+\frac{1}{6} \\
B_3(x) & =x^3-\frac{3}{2}x^2+\frac{1}{2}x \\
B_4(x) & =x^4-2x^3+x^2-\frac{1}{30} \\
\end{aligned}
$$

The numbers $B_n = B_n(0)$ are called the Bernoulli numbers. Integrating the relation $B_r^\prime(x)=rB_r(x)$ between 0 and 1 gives:

$$
B_r(1)-B_r(0) = \int_0^1 B_r^\prime (x) dx = r\int_0^1 B_{r-1}(x) dx = 0 \quad \forall r\geq 2
$$

This motivates us to define the periodic Bernoulli polynomials by

$$
\tilde{B}_r(x) = B_r(\langle x\rangle), \quad x\in\mathbb{R}, \; r\geq 2
$$

where $\langle x\rangle$ denotes the fractional part of $x$. We will now compute the Fourier series of $\tilde{B}_r(x)$, where $r\geq 2$. The $n$-th Fourier coefficient is given by:

$$
\begin{aligned}
a_n &= \int_0^1 \tilde{B}_r(x) e^{-2\pi i n x} dx= \int_0^1 B_r(x) e^{-2\pi i n x} dx
\end{aligned}
$$

Let's first consider the case when $n\neq 0$. Integration by parts, gives us:

$$
\begin{equation}\label{bernoulli-numbers-and-a-related-integral-eq-1}
\begin{aligned}
a_n &= -\frac{e^{-2\pi i n x}}{2\pi i n}B_r(x)\Big|_0^1 + \frac{1}{2\pi i n}\int_0^1 B_r^\prime (x) e^{-2\pi i n x} dx \\ 
&= \frac{1}{2\pi i n}\int_0^1 B_r^\prime (x) e^{-2\pi i n x} dx \\
&= \frac{r}{2\pi i n}\int_0^1 B_{r-1}(x) e^{-2\pi i n x} dx 
\end{aligned}
\end{equation}
$$

The repeated use of equation $\eqref{bernoulli-numbers-and-a-related-integral-eq-1}$ gives:

$$
\begin{aligned}
a_n &= \frac{r!}{(2\pi i n)^{r-1}} \int_0^1 B_1(x) e^{-2\pi i nx} dx \\
&= \frac{r!}{(2\pi i n)^{r-1}} \int_0^1 \left(x-\frac{1}{2} \right) e^{-2\pi i nx} dx \\
&= \frac{r!}{(2\pi i n)^{r-1}}\int_0^1 x e^{-2\pi i n x} dx \\
&= -\frac{r!}{(2\pi i n)^r}
\end{aligned}
$$

When $n=0$, we have $a_0 = \int_0^1 B_r(x)dx = 0$. Note that the Fourier series

$$
-r! \sum_{\substack{n=-\infty \\ n\neq 0}} \frac{e^{2\pi i n x}}{(2\pi i n)^r}
$$

converges absolutely for all $r\geq 2$. Therefore, it converges uniformly to $\tilde{B}_r(x)$ for all $r\geq 2$. This leads to the following bound:

$$
\begin{equation}\label{bernoulli-numbers-and-a-related-integral-eq-2}
|\tilde{B}_r(x)| \leq \frac{2r!}{(2\pi)^r}\sum_{n=1}^\infty \frac{1}{n^r} < \frac{4r!}{(2\pi)^r} \;\; \forall r\geq 2
\end{equation}
$$

Note that the above inequality also remains valid for $r=0$ and $r=1$. Now, let's consider the generating function:

$$
F(x,t) = \sum_{n=0}^\infty \frac{\tilde{B}_n(x) t^n}{n!}
$$

The inequality $\eqref{bernoulli-numbers-and-a-related-integral-eq-2}$ implies that:

$$
|F(x,t)| < 4 \sum_{n=0}^\infty \left(\frac{t}{2\pi}\right)^n
$$

Therefore, the series converges uniformly for all $t\in [0,2\pi]$ and all $x$. We, may, therefore differentiate term by term to obtain:

$$
\frac{\partial F(x,t)}{\partial x} = \sum_{n=1}^\infty \frac{\tilde{B}_{n-1}(x)}{(n-1)!}t^n = t F(x,t)
$$

Solving the above differential equation, we get $F(x,t) = G(t) e^{xt}$ where $G$ is some arbitrary function of $t$. Next, we integrate $F(x,t)$ between 0 and 1:

$$
\begin{aligned}
\int_0^1 F(x,t) dx &= G(t) \int_0^1 e^{xt} dx \\
&= G(t) \frac{e^t-1}{t}
\end{aligned}
$$

On the other hand, note that:

$$
\begin{aligned}
\int_0^1 F(x,t) dx &= \int_0^1 \sum_{n=0}^\infty \frac{\tilde{B}_n(x) t^n}{n!} dx \\
&= 1 + \sum_{n=1}^\infty \frac{t^n}{n!}\int_0^1 B_n(x) dx \\
&= 1
\end{aligned}
$$

Therefore, we obtain $G(t) = \frac{t}{e^t - 1}$ and

$$
\boxed{F(x,t) = \frac{t e^{xt}}{e^t-1}}
$$

An interesting property of the Bernoulli numbers is that $B_{2n+1}=0$ for all $n\geq 1$. To see this, consider:

$$
\frac{t}{e^t -1} + \frac{t}{2}= 1+\sum_{n=2}^\infty \frac{B_n t^n}{n!}
$$

Now, on the left hand side we have an even function of $t$. Therefore, the coefficients of the odd powers of $t$ on the right hand side are equal to 0. Using the Fourier series expansion, we can express the even-index Bernoulli numbers in terms of the Riemann zeta function:

$$
B_{2n} = \frac{2 (-1)^{n-1} (2n)!}{(2\pi)^{2n}} \zeta(2n)
$$

The Bernoulli polynomials satisfy the following recursive equation:

$$
{B}_n(x) = \sum_{k=0}^n \binom{n}{k} B_{n-k} x^k
$$

This can be proved by noting that:

$$
\begin{aligned}
\sum_{n=0}^\infty \frac{{B}_n(x) t^n}{n!} &= \frac{te^{xt}}{e^t-1} \\
&= e^{xt} \sum_{n=0}^\infty \frac{B_n t^n}{n!} \\
&= \sum_{m=0}^\infty \frac{(xt)^m}{m!} \sum_{n=0}^\infty \frac{B_n t^n}{n!} \\
&= \sum_{m=0}^\infty \sum_{n=0}^\infty \frac{B_n x^m t^{n+m}}{n! m!} \\
&= \sum_{n=0}^\infty \sum_{k=0}^n \frac{B_k t^n x^{n-k}}{k! (n-k)!} \\
&= \sum_{n=0}^\infty \frac{t^n}{n!}\sum_{k=0}^n \binom{n}{k} B_k x^{n-k}
\end{aligned}
$$

where $x\in [0,1]$. Now, compare the coefficients of $t^n$ to get the desired result. Plugging in $x=1$, gives the identity:

$$
\sum_{k=0}^{n-1} \binom{n}{k} B_k = 0
$$

Now, let's turn our attention to the integral:

$$
I=\int_0^{\frac{\pi}{2}}\frac{\sin(2nx)}{\sin^{2n+2}(x)}\cdot \frac{1}{e^{2\pi \cot x}-1} dx
$$

where $n\in\mathbb{N}$. We will use the following trigonometric identity:

$$
\frac{\sin(2nx)}{\sin^{2n}(x)} =(-1)^n \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r}\cot^{2r-1}(x)
$$

Substituting the above into the integral, gives:

$$
\begin{aligned}
I &= (-1)^n \int_0^{\pi\over 2}\left( \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r}\cot^{2r-1}(x)\right)\frac{\csc^2(x)}{e^{2\pi \cot x}-1}dx \\ 
&= (-1)^n \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r} \int_0^{\pi \over 2}\cot^{2r-1}(x)\frac{\csc^2(x)}{e^{2\pi \cot x}-1}dx \\ 
&= (-1)^n \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r} \int_0^\infty \frac{t^{2r-1}}{e^{2\pi t}-1}dt  \\ 
&= (-1)^n \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r}\frac{(2r-1)! \zeta(2r)}{(2\pi)^r }\\ 
&= (-1)^n \sum_{r=1}^{n}\binom{2n}{2r-1} (-1)^{r} (-1)^{r-1} \frac{B_{2r}}{4r}\\ 
&= \frac{(-1)^{n-1}}{4}\sum_{r=1}^{n}\binom{2n}{2r-1}\frac{B_{2r}}{r} \\
&= \frac{(-1)^{n-1}}{2(2n+1)}\sum_{r=1}^n \binom{2n+1}{2r} B_{2r} \\
&= \frac{(-1)^{n-1}}{2(2n+1)} \left[\sum_{r=0}^{2n} \binom{2n+1}{r} B_r - \binom{2n+1}{0}B_0 - \binom{2n+1}{1} B_1\right] \\
&= \frac{(-1)^{n-1}}{2(2n+1)} \left[-\binom{2n+1}{0}B_0 - \binom{2n+1}{1} B_1\right] \\
&= \frac{(-1)^{n-1}}{4}\cdot \frac{2n-1}{2n+1}
\end{aligned}
$$
