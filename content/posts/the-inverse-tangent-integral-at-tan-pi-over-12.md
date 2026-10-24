Title: The inverse tangent integral at two minus root three
Date: 2026-10-24 10:10 +0530
Slug: the-inverse-tangent-integral-at-tan-pi-over-12
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: logarithmic-integrals, catalans-constant, fourier-series, trigonometric-integrals
Summary: Integration by parts and the Fourier series of log tangent evaluate the inverse tangent integral at tan(pi/12) in terms of Catalan's constant.
Status: published

The inverse tangent integral $\operatorname{Ti}_2(z) = \int_0^z \frac{\arctan x}{x}\,dx$ equals Catalan's constant $G = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2}$ at $z = 1 = \tan\left(\frac{\pi}{4}\right)$. At the half-angle argument $z = 2-\sqrt{3} = \tan\left(\frac{\pi}{12}\right)$, it satisfies a remarkable closed-form relation discovered by Ramanujan:

$$
\int_0^{2-\sqrt{3}}\frac{\arctan(x)}{x}\,dx = \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + \frac{2}{3}G.
$$

## Integration by parts and the Fourier series of $\ln(\tan\theta)$

Let $I$ denote the integral. Integrating by parts with $u = \arctan x$ and $dv = \frac{dx}{x}$, and then substituting $x = \tan\theta$ (using $\tan\frac{\pi}{12} = 2-\sqrt{3}$), we obtain

$$
\begin{aligned}
I &= \Bigl[ \ln(x)\arctan(x) \Bigr]_0^{2-\sqrt{3}} - \int_0^{2-\sqrt{3}}\frac{\ln (x)}{1+x^2}\,dx \\
&= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) - \int_0^{\frac{\pi}{12}} \ln(\tan\theta)\,d\theta.
\end{aligned} \tag{1}
$$

For $\theta \in \left(0, \frac{\pi}{2}\right)$, recall the standard Fourier cosine expansions

$$
\begin{aligned}
\ln(2\sin \theta) &= -\sum_{k=1}^\infty \frac{\cos(2k \theta)}{k}, \\
\ln(2\cos \theta) &= \sum_{k=1}^\infty (-1)^{k+1}\frac{\cos(2k\theta)}{k}.
\end{aligned}
$$

Subtracting the second series from the first cancels all even-indexed terms and doubles the odd-indexed terms ($k = 2m+1$):

$$
\ln(\tan\theta) = \ln(2\sin\theta) - \ln(2\cos\theta) = -2\sum_{k=0}^\infty \frac{\cos\bigl(2(2k+1)\theta\bigr)}{2k+1}.
$$

## Term-by-term integration and multisection of the series

Substituting the Fourier series of $\ln(\tan\theta)$ into equation (1) and integrating term by term gives

$$
\begin{aligned}
I &= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + 2\int_0^{\frac{\pi}{12}}\left(\sum_{k=0}^\infty \frac{\cos\bigl(2(2k+1)\theta\bigr)}{2k+1} \right) d\theta \\
&= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + 2\sum_{k=0}^\infty\frac{1}{2k+1}\int_0^{\frac{\pi}{12}} \cos\bigl(2(2k+1)\theta\bigr)\,d\theta \\
&= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + \sum_{k=0}^\infty\frac{\sin\left( (2k+1)\frac{\pi}{6}\right)}{(2k+1)^2}.
\end{aligned}
$$

To evaluate the remaining Dirichlet-type series, examine the periodic numerator $s_k = \sin\left((2k+1)\frac{\pi}{6}\right)$ as $k$ varies modulo $3$:

- When $k \equiv 0$ or $2 \pmod 3$ (so $2k+1$ is not divisible by $3$), $s_k = \frac{1}{2}(-1)^k$.
- When $k = 3m+1$ (so $2k+1 = 6m+3 = 3(2m+1)$ is an odd multiple of $3$), $s_{3m+1} = \sin\left((2m+1)\frac{\pi}{2}\right) = (-1)^m = -(-1)^k$.

On the full alternating sum $\sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} = G$, separating out the subsequence $k = 3m+1$ where $(-1)^{3m+1} = -(-1)^m$ gives

$$
\sum_{k \not\equiv 1 \pmod 3} \frac{(-1)^k}{(2k+1)^2} = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} + \sum_{m=0}^\infty \frac{(-1)^m}{(6m+3)^2} = G + \frac{G}{9}.
$$

Multiplying those terms by $\frac{1}{2}$ and adding the $k = 3m+1$ terms (which have coefficient $(-1)^m$) yields

$$
\begin{aligned}
I &= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + \frac{1}{2}\left( \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} + \sum_{m=0}^\infty \frac{(-1)^m}{(6m+3)^2}\right) + \sum_{m=0}^\infty \frac{(-1)^m}{(6m+3)^2} \\
&= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + \frac{1}{2}\left(G + \frac{G}{9}\right) + \frac{G}{9} \\
&= \frac{\pi}{12}\ln\left(2-\sqrt{3}\right) + \frac{2}{3}G.
\end{aligned}
$$

