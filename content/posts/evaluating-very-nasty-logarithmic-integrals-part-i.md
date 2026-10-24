Title: Evaluating very nasty logarithmic integrals: Part I
Date: 2020-08-01 09:15:41 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: evaluating-very-nasty-logarithmic-integrals-part-i
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: euler-sums, polylogarithm
Summary: The first part of a series on logarithmic integrals: harmonic-number sums, polylogarithms, and residues.
Status: published
WordPress_ID: 476

Logarithmic integrals often become more manageable when we express them as Euler sums. This first part develops that approach and then introduces contour integration as another way to evaluate the resulting sums. We will use identities from [An alternating Euler sum (A)]({filename}/posts/an-alternating-euler-sum.md) and [Euler sums involving squared harmonic numbers (B)]({filename}/posts/euler-sums-involving-square-of-harmonic-numbers.md).

## Integral #1

Our first integral is the following:

$$
\begin{aligned}
I &= \int_0^1 \frac{\log(t)\log(1-t)\log(1+t)}{t}dt
\end{aligned}
$$

We will use the integral $J = \int_0^1 \frac{\log(t)\log^2(1-t)}{t}dt$ as a starting point. Make the substitution $t\mapsto t^2$ in $J$ to obtain:

$$
\begin{aligned}
J &= 2\int_0^1  \frac{\log(t^2) \log^2(1-t^2)}{t}dt \\
&= 4\int_0^1 \frac{\log(t)\log^2(1-t)}{t}dt + 4\int_0^1 \frac{\log(t)\log^2(1+t)}{t}dt + 8\int_0^1 \frac{\log(t)\log(1-t) \log(1+t)}{t}dt \\
&= 4J + 4\int_0^1 \frac{\log(t)\log^2(1+t)}{t}dt + 8I
\end{aligned}
$$

Solving the above equation for $I$ gives us:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-i-eq-1}
I = -\frac{3}{8}J - \frac{1}{2} \int_0^1 \frac{\log(t)\log^2(1+t)}{t}dt
\end{equation}
$$

Applying integration by parts and using the generating function of the Harmonic number yields:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-i-eq-2}
\begin{aligned}
\int_0^1 \frac{\log(t)\log^2(1+t)}{t}dt &= -\int_0^1 \frac{\log^2(t)\log(1+t)}{1+t}dt \\
&= -\sum_{n=1}^\infty (-1)^{n+1} H_n \int_0^1 t^{n} \log^2(t) \; dt \\
&= -2\sum_{n=1}^\infty (-1)^{n+1} \frac{H_n}{(n+1)^3} \\
&= -2\sum_{n=0}^\infty (-1)^{n+1} \frac{H_{n+1}-\frac{1}{n+1}}{(n+1)^3} \\
&= 2\sum_{n=1}^\infty (-1)^{n+1} \frac{H_n}{n^3} - 2\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^4} \\
&= 2\text{Li}_4(-1) +  2\sum_{n=1}^\infty (-1)^{n+1} \frac{H_n}{n^3} 
\end{aligned}
\end{equation}
$$

A similar calculation shows that:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-i-eq-3}
J = 2\zeta(4) - 2\sum_{n=1}^\infty \frac{H_n}{n^3}
\end{equation}
$$

From [(A)]({filename}/posts/an-alternating-euler-sum.md), we know how to evaluate $\sum_{n=1}^\infty (-1)^{n+1} \frac{H_n}{n^3}$ and $\sum_{n=1}^\infty \frac{H_n}{n^3}$.

$$
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n}{n^3} &= \frac{\pi^4}{72} \\
\sum_{n=1}^\infty (-1)^{n+1}\frac{H_n}{n^3} &= \frac{11\pi^4}{360}+\frac{\pi^2}{12}\log^2(2)-\frac{\log^4(2)}{12}-\frac{7}{4}\log(2)\zeta(3) -2\text{Li}_4\left(\frac{1}{2}\right)
\end{aligned}
$$

Finally, putting everything together gives us:

$$
\boxed{I = -\frac{3\pi^4}{160}-\frac{\pi^2}{12}\log^2(2)+\frac{\log^4(2)}{12}+\frac{7}{4}\log(2)\zeta(3) +2\text{Li}_4\left(\frac{1}{2}\right)}
$$

## Integral #2

The next integral on our list is

$$
K = \int_0^1 \frac{\log(x)\log(1+x^2)\arctan(x)}{x}dx
$$

This integral was originally posted by the user FDP on math.stackexchange.com. [My solution](https://math.stackexchange.com/questions/3774212/evaluating-int-01-frac-ln-x-ln1x2-arctan-xxdx) is posted there as well.

Using integration by parts gives us:

$$
K = - \frac{1}{2}\int_0^1 \frac{\log^2(x)\log(1+x^2)}{1+x^2}dx - \int_0^1 \frac{x \log^2(x) \arctan(x)}{1+x^2}dx
$$

Now, we can use the following series expansions to reduce $K$ into Euler sums:

$$
\begin{aligned}
\frac{\arctan (x)}{1+x^2} &= \sum_{n=0}^\infty (-1)^n \tilde{H}_n x^{2n+1} , \quad |x| < 1\\
\frac{\log(1+x^2)}{1+x^2} &= \sum_{n=1}^\infty (-1)^{n+1} H_n x^{2n} , \quad |x| < 1 
\end{aligned}
$$

where $\tilde{H}_n = \sum_{i=0}^n \frac{1}{2i+1}$. This gives us:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-i-eq-4}
\begin{aligned}
K &= -\sum_{n=0}^\infty (-1)^n \tilde{H}_n\int_0^1 x^{2n+2} \log^2(x)\; dx-\frac{1}{2}\sum_{n=1}^\infty (-1)^{n+1} H_n\int_0^1 x^{2n}\log^2(x)\; dx \\
&= -2\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+3)^3} - \sum_{n=1}^\infty \frac{(-1)^{n+1} H_n}{(2n+1)^3} \\
&= -2\sum_{n=1}^\infty \frac{(-1)^{n+1} H_{2n}}{(2n+1)^3} 
\end{aligned}
\end{equation}
$$

We'll employ the contour integration method to evaluate the above Euler sum. It is a very powerful tool that can handle a large class of Euler sums (see, for e.g. [Euler sums and contour integral representations by Philippe Flajolet and Bruno Salvy](https://projecteuclid.org/euclid.em/1047674270)).

We'll integrate the function $f(z) = \pi \csc(\pi z) \frac{\gamma+\psi_0(-2z+1)}{(-2z+1)^3}$ around the positively oriented square, $C_N$, with vertices $\pm \left(N+\frac{1}{4} \right)\pm \left(N+\frac{1}{4} \right)i$. It is easy to see that

$$
\lim_{N\to \infty}\int_{C_N}f(z)\; dz = 0
$$

Hence, the sum of all residues of $f(z)$ at its poles is equal to $0$. A straightforward computation shows that the residues are:

$$
\begin{aligned}
\mathop{\text{Res}}\limits_{z=-n} f(z) &= (-1)^n \frac{H_{2n}}{(2n+1)^3} , \quad n\in \{0,1,2,\cdots\} \\
\mathop{\text{Res}}\limits_{z=\frac{2n+1}{2}} f(z) &= \frac{(-1)^{n+1} \pi}{16 n^3} , \quad n\in \{1,2,3,\cdots\} \\
\mathop{\text{Res}}\limits_{z=n} f(z) &= \frac{(-1)^{n+1}H_{2n-1}}{(2n-1)^3}- 3\frac{(-1)^{n+1}}{(2n-1)^4}, \quad n\in \{1,2,3,\cdots \}\\
\mathop{\text{Res}}\limits_{z=\frac{1}{2}} f(z) &= \frac{\pi \zeta(3)}{2}
\end{aligned}
$$

The list of local expansions of basic kernels given on page 6 of the above mentioned paper are quite useful for carrying out these computations. Now, adding up all the residues gives us:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-i-eq-5}
\begin{aligned}
\frac{\pi \zeta(3)}{2}+\sum_{n=1}^\infty \frac{(-1)^n H_{2n}}{(2n+1)^3} + \frac{\pi}{16}\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^3} + \sum_{n=1}
^\infty \frac{(-1)^{n+1}H_{2n-1}}{(2n-1)^3} -3\sum_{n=1}^\infty \frac{(-1)^{n+1}}{(2n-1)^4}&= 0\\
\implies \frac{\pi \zeta(3)}{2}+\sum_{n=1}^\infty \frac{(-1)^n H_{2n}}{(2n+1)^3} + \frac{\pi}{16}\left(\frac{3\zeta(3)}{4} \right) + \sum_{n=1}^\infty \frac{(-1)^n H_{2n}}{(2n+1)^3} -2 \sum_{n=1}^\infty \frac{(-1)^{n+1}}{(2n-1)^4} &= 0 \\
\implies -2\sum_{n=1}^\infty \frac{(-1)^{n+1}H_{2n}}{(2n+1)^3} + \frac{35\pi \zeta(3)}{64} -2\beta(4) = 0 \\
\implies \boxed{\sum_{n=1}^\infty \frac{(-1)^{n+1}H_{2n}}{(2n+1)^3} = -\beta(4) + \frac{35\pi \zeta(3)}{128}} 
\end{aligned}
\end{equation}
$$

where $\beta(s) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^s}$ is the Dirichlet beta function. Finally, plugging equation $\eqref{evaluating-very-nasty-logarithmic-integrals-part-i-eq-5}$ into $\eqref{evaluating-very-nasty-logarithmic-integrals-part-i-eq-4}$ gives us:

$$
\boxed{K = 2\beta(4) - \frac{35\pi \zeta(3)}{64}}
$$

Following are some more examples of Euler sums that can be evaluated using the contour integration method:

$$
\begin{aligned}
\sum_{n=0}^\infty\frac{(-1)^n\psi_2(n+1)}{2n+1} &= 8\beta(4)+\frac{\pi^2}{3}G-\frac{7\pi}{2}\zeta(3) \\
\sum_{n=0}^\infty\frac{(-1)^n\psi_1(n+1)}{(2n+1)^2} &= 6\beta(4)+\frac{\pi^2}{4}G-\frac{7\pi}{4}\zeta(3) \\
\sum_{n=1}^\infty \frac{(-1)^{n+1} H_n}{(2n+1)^3} &= -3\beta(4)+\frac{7\pi}{16}\zeta(3)+\frac{\pi^3}{16}\log(2)
\end{aligned}
$$

where $G=\beta(2)$ denotes the Catalan's constant. Some integrals that can be evaluated with the above Euler sums are:

$$
\begin{aligned}
\int_0^1 \frac{\log^2(x)\arctan(x)}{x\left(1-x^2 \right)}dx &=\beta(4)+\frac{7\pi \zeta(3)}{64}+\frac{\pi^3 \log(2)}{32} \\
\int_0^1\frac{\log(x)\arctan(x)\text{arctanh}(x)}{x}dx &= \frac{\pi^2}{16}G-\frac{7\pi\zeta(3)}{32} \\
\int_0^{\frac{\pi}{2}}\frac{x}{\sin x}\log^2\left(\frac{1+\cos x-\sin x}{1+\cos x+\sin x}\right)dx &= \frac{\pi^2}{6}G +4\beta(4)
\end{aligned}
$$
