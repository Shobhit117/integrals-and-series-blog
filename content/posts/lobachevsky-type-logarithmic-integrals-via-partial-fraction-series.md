Title: Lobachevsky-type logarithmic integrals via partial-fraction series
Date: 2026-10-24 10:12 +0530
Slug: lobachevsky-type-logarithmic-integrals-via-partial-fraction-series
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: logarithmic-integrals, fourier-series, catalans-constant, polylogarithm, trigonometric-integrals
Summary: Periodizing improper integrals via the partial-fraction expansion of cosecant squared reduces trigonometric-logarithmic integrals on the half-line to finite intervals.
Status: published

Whenever an even, $\pi$-periodic function $f(t)$ is integrated against $\frac{1}{t^2}$ over the entire real line, splitting $\mathbb{R}$ into intervals of length $\pi$ and summing the translates $\frac{1}{(t+n\pi)^2}$ folds the integral onto $\left[0, \frac{\pi}{2}\right]$. We will use this Lobachevsky periodization method to prove that for $|a| < 1$ and $b > 0$,

$$
\int_{0}^{\infty} \ln \left(\frac{1+a \sin^{2} (bx)}{1-a \sin^{2} (bx)} \right) \frac{1}{x^{2}}\,dx = \pi b \left( \sqrt{1+a} - \sqrt{1-a} \right),
$$

and then record three related consequences.

## Folding the real line onto $\left[0, \frac{\pi}{2}\right]$

We make use of Euler's partial-fraction expansion for the squared cosecant:

$$
\sum_{n=-\infty}^\infty \frac{1}{(t+n\pi)^2} = \frac{1}{\sin^2 (t)}.
$$

Let $I$ denote the target integral. Using the evenness of the integrand and substituting $t = bx$, we decompose $\mathbb{R}$ into the intervals $\left[n\pi - \frac{\pi}{2}, n\pi + \frac{\pi}{2}\right]$ for $n \in \mathbb{Z}$:

$$
\begin{aligned}
I &= \frac{1}{2}\int_{-\infty}^\infty \ln \left(\frac{1+a \sin^{2} (bx)}{1-a \sin^{2} (bx)} \right)\frac{1}{x^2}\,dx \\
&= \frac{b}{2}\int_{-\infty}^\infty \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\frac{1}{t^2}\,dt \quad (t=bx) \\
&= \frac{b}{2}\sum_{n=-\infty}^\infty \int_{n\pi - \frac{\pi}{2}}^{n\pi + \frac{\pi}{2}} \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\frac{1}{t^2}\,dt \\
&= \frac{b}{2}\sum_{n=-\infty}^\infty \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\frac{1}{(t+n\pi)^2}\,dt \\
&= \frac{b}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\left( \sum_{n=-\infty}^\infty \frac{1}{(t+n\pi)^2} \right) dt \\
&= \frac{b}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\frac{1}{\sin^2(t)}\,dt \\
&= b \int_0^{\frac{\pi}{2}} \ln \left(\frac{1+a \sin^{2} (t)}{1-a \sin^{2} (t)} \right)\frac{1}{\sin^2(t)}\,dt.
\end{aligned}
$$

## Expanding in a power series in $a$

For $|a| < 1$, expand the logarithm using $\ln\left(\frac{1+u}{1-u}\right) = 2\sum_{k=0}^\infty \frac{u^{2k+1}}{2k+1}$ with $u = a\sin^2 t$, and apply Wallis's formula $\int_0^{\pi/2} \sin^{2m}(t)\,dt = \frac{\pi}{2}\frac{1}{2^{2m}}\binom{2m}{m}$ with $m = 2k$:

$$
\begin{aligned}
I &= 2b \int_0^{\frac{\pi}{2}}\left(\sum_{k=0}^\infty \frac{a^{2k+1}\sin^{4k+2}(t)}{2k+1} \right)\frac{1}{\sin^2(t)}\,dt \\
&= 2b\sum_{k=0}^\infty \frac{a^{2k+1}}{2k+1} \int_0^{\frac{\pi}{2}} \sin^{4k}(t)\,dt \\
&= \pi b\sum_{k=0}^\infty \frac{a^{2k+1}}{(2k+1) 2^{4k}} \binom{4k}{2k}.
\end{aligned}
$$

To sum this series in closed form, recall the binomial expansion $(1-u)^{-1/2} = \sum_{n=0}^\infty \frac{1}{2^{2n}}\binom{2n}{n}u^n$. Taking the even part in $u$ gives

$$
\frac{(1-u)^{-1/2} + (1+u)^{-1/2}}{2} = \sum_{k=0}^\infty \frac{u^{2k}}{2^{4k}}\binom{4k}{2k},
$$

and integrating both sides from $u = 0$ to $u = a$ produces

$$
\sum_{k=0}^\infty \frac{a^{2k+1}}{(2k+1) 2^{4k}} \binom{4k}{2k} = \int_0^a \frac{(1-u)^{-1/2} + (1+u)^{-1/2}}{2}\,du = \sqrt{1+a} - \sqrt{1-a}.
$$

Therefore,

$$
I = \pi b \left( \sqrt{1+a}-\sqrt{1-a}\right).
$$

## Three companion identities

1. **A first-order Lobachevsky integral:** Using the partial-fraction expansion $\sum_{n=-\infty}^\infty \frac{(-1)^n}{t+n\pi} = \frac{1}{\sin t}$ in the same manner shows that for $|a| < 1$ and $b > 0$,

$$
\int_{0}^{\infty} \ln \left( \frac{1+a \sin(bx)}{1-a \sin(bx)} \right) \frac{dx}{x} = \pi \arcsin(a).
$$

2. **A dilogarithm integral:** Dividing the identity above (with $b=1$) by $a$ and integrating both sides from $a=0$ to $a=\frac{1}{\sqrt{2}}$ using $\int_0^z \ln\left(\frac{1+u}{1-u}\right)\frac{du}{u} = \operatorname{Li}_2(-z) - \operatorname{Li}_2(z)$ yields

$$
\int_0^\infty \frac{\operatorname{Li}_2\left(\frac{\sin x}{\sqrt{2}}\right)-\operatorname{Li}_2\left(-\frac{\sin x}{\sqrt{2}}\right)}{x}\,dx = \pi\int_0^{\frac{1}{\sqrt{2}}}\frac{\arcsin(a)}{a}\,da = \frac{\pi G}{2}+\frac{\pi^2 \ln(2)}{8},
$$

where $G$ is Catalan's constant (since substituting $a = \sin\theta$ and integrating by parts reduces $\int_0^{1/\sqrt{2}}\frac{\arcsin a}{a}\,da$ to $\frac{\pi}{8}\ln 2 + \frac{G}{2}$).

3. **Reducing an improper squared-arctangent integral:** Applying the same $\sum_{n=-\infty}^\infty \frac{1}{(x+n\pi)^2} = \frac{1}{\sin^2 x}$ reduction to $f(x) = \arctan^2(\sin^2 x)$ shows that $\int_0^\infty \frac{\arctan^2(\sin^2 x)}{x^2}\,dx = \int_0^{\pi/2} \frac{\arctan^2(\sin^2 x)}{\sin^2 x}\,dx$. By [our earlier evaluation of that trigonometric integral]({filename}/posts/an-integral-involving-the-squared-arctangent-of-sine-squared.md), we immediately obtain

$$
\int_0^\infty \frac{\arctan^2 (\sin^2 x)}{x^2}\,dx = \pi \log\left(\frac{2+\sqrt{2}}{4}\right)\sqrt{\frac{\sqrt{2}+1}{2}}+\frac{\pi^2}{4} \sqrt{\frac{\sqrt{2}-1}{2}}.
$$

