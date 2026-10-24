Title: The Fourier transform of the hyperbolic secant
Date: 2026-10-24 10:04 +0530
Slug: the-fourier-transform-of-the-hyperbolic-secant
Author: Shobhit Bhatnagar
Category: Contour Integration
Tags: contour-integration, residue-theorem, fourier-series, infinite-series
Summary: Residue calculus on a rectangular contour shows that the hyperbolic secant is its own Fourier transform up to scaling.
Status: published

A classic property of the hyperbolic secant $\operatorname{sech}(\pi x) = \frac{1}{\cosh(\pi x)}$ is that, like the Gaussian, it is an eigenfunction of the Fourier transform. We will prove that for $a > 0$,

$$
\int_{-\infty}^\infty \frac{e^{ia x}}{\cosh(\pi x)}\,dx = \frac{1}{\cosh\left(\frac{a}{2}\right)}.
$$

Since $\cosh(\pi x)$ is an even function, the imaginary part $\int_{-\infty}^\infty \frac{\sin(ax)}{\cosh(\pi x)}\,dx$ vanishes by symmetry, so the formula is symmetric in $a$ and holds for all real $a \in \mathbb{R}$.

## Method 1: An expanding rectangular contour

Let $f(z) = \frac{e^{iaz}}{\cosh(\pi z)}$. The poles of $f(z)$ occur where $\cosh(\pi z) = 0$, namely at

$$
z_n = \frac{(2n+1)i}{2}, \qquad n \in \mathbb{Z},
$$

all of which lie on the imaginary axis with spacing $i$. For each positive integer $N \in \{1, 2, \dots\}$, define $B_N$ to be the positively oriented rectangle with vertices $-N$, $N$, $N+iN$, and $-N+iN$:

![Expanding rectangular contour B_N in the upper half-plane enclosing N poles on the imaginary axis]({static}/images/contour-rectangle-cosh-poles.svg)

Choosing the top edge at height $\operatorname{Im} z = N$ ensures that the contour passes halfway between the poles $z_{N-1} = \left(N-\frac{1}{2}\right)i$ and $z_N = \left(N+\frac{1}{2}\right)i$, enclosing exactly the $N$ simple poles $z_0, z_1, \dots, z_{N-1}$.

At $z_n = \frac{(2n+1)i}{2}$, we have $\frac{d}{dz}\cosh(\pi z)\big|_{z=z_n} = \pi\sinh\left(i\pi\left(n+\frac{1}{2}\right)\right) = \pi i (-1)^n$, so the residue is

$$
\mathop{\operatorname{Res}}_{z=\frac{(2n+1)i}{2}} \frac{e^{iaz}}{\cosh(\pi z)} = \frac{e^{-a\left(n+\frac{1}{2}\right)}}{\pi i (-1)^n} = \frac{(-1)^n e^{-\frac{a}{2}} e^{-an}}{\pi i}.
$$

Applying the residue theorem to $B_N$ and taking $N \to \infty$ gives a convergent geometric series (since $a > 0$ implies $e^{-a} < 1$):

$$
\begin{aligned}
\lim_{N\to \infty}\int_{B_N}\frac{e^{ia z}}{\cosh(\pi z)}\,dz
&= 2\pi i \sum_{n=0}^\infty \mathop{\operatorname{Res}}_{z=\frac{(2n+1)i}{2}} \frac{e^{ia z}}{\cosh(\pi z)} \\
&= 2\pi i \left(\frac{e^{-\frac{a}{2}}}{\pi i}\sum_{n=0}^\infty (-1)^n e^{-an}\right) \\
&= \frac{2e^{-\frac{a}{2}}}{1 + e^{-a}} \\
&= \frac{1}{\cosh\left(\frac{a}{2}\right)}.
\end{aligned}
$$

To verify that only the integral along the bottom edge $[-N, N]$ survives as $N \to \infty$, we estimate the other three sides:

- **Top edge** ($z = x + iN$, $-N \leq x \leq N$): Since $\cosh(\pi(x+iN)) = (-1)^N\cosh(\pi x)$ and $|e^{ia(x+iN)}| = e^{-aN}$,

$$
\left|\int_{-N}^{N} \frac{e^{ia(x+iN)}}{\cosh(\pi(x+iN))}\,dx\right| \leq e^{-aN}\int_{-\infty}^\infty \frac{dx}{\cosh(\pi x)} = e^{-aN} \to 0 \quad (N \to \infty).
$$

- **Vertical edges** ($z = \pm N + iy$, $0 \leq y \leq N$): By the reverse triangle inequality, $|\cosh(\pi(\pm N + iy))| \geq \sinh(\pi N)$, while $|e^{ia(\pm N + iy)}| = e^{-ay} \leq 1$, so

$$
\left|\int_0^N \frac{e^{ia(\pm N + iy)}}{\cosh(\pi(\pm N + iy))}\,i\,dy\right| \leq \frac{N}{\sinh(\pi N)} \to 0 \quad (N \to \infty).
$$

Consequently,

$$
\int_{-\infty}^\infty \frac{e^{ia x}}{\cosh(\pi x)}\,dx = \lim_{N\to \infty}\int_{B_N}\frac{e^{ia z}}{\cosh(\pi z)}\,dz = \frac{1}{\cosh\left(\frac{a}{2}\right)}.
$$

## Method 2: A fixed-height strip enclosing a single pole

We can also avoid summing an infinite series of residues by using a rectangle $\Gamma_R$ of fixed height $1$ with vertices $-R$, $R$, $R+i$, and $-R+i$. Since $\cosh(\pi(x+i)) = -\cosh(\pi x)$, the top edge is a constant multiple of the bottom edge:

$$
\int_{R+i}^{-R+i} \frac{e^{iaz}}{\cosh(\pi z)}\,dz = e^{-a}\int_{-R}^R \frac{e^{iax}}{\cosh(\pi x)}\,dx.
$$

The vertical sides are bounded by $\frac{1}{\sinh(\pi R)} \to 0$ as $R \to \infty$, and $\Gamma_R$ encloses only the single pole at $z_0 = \frac{i}{2}$. The residue theorem then gives

$$
(1 + e^{-a})\int_{-\infty}^\infty \frac{e^{iax}}{\cosh(\pi x)}\,dx = 2\pi i \mathop{\operatorname{Res}}_{z=\frac{i}{2}} \frac{e^{iaz}}{\cosh(\pi z)} = 2\pi i \left(\frac{e^{-\frac{a}{2}}}{\pi i}\right) = 2e^{-\frac{a}{2}},
$$

which immediately divides through to $\frac{1}{\cosh(a/2)}$ for every $a \in \mathbb{R}$ (and, by analytic continuation, for every complex $a$ in the strip $|\operatorname{Im} a| < \pi$).

