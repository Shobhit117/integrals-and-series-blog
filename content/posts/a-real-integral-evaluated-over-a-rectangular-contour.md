Title: A real integral evaluated over a rectangular contour
Date: 2026-10-24 10:03 +0530
Slug: a-real-integral-evaluated-over-a-rectangular-contour
Author: Shobhit Bhatnagar
Category: Contour Integration
Tags: contour-integration, residue-theorem, definite-integrals
Summary: Integrating a meromorphic function around a horizontal strip of height two pi evaluates a real integral mixing exponential and rational factors.
Status: published

When an integrand combines exponential functions with a rational factor such as $\frac{1}{x^2+\pi^2}$, a rectangular contour of height $2\pi$ can exploit the periodicity of $e^z$ in the imaginary direction while building the rational factor from the difference of two simple fractions. Using this technique, we will prove that for every $a \in \mathbb{R}$,

$$
\int_{-\infty}^\infty \frac{e^x}{e^{2x}+e^{2a}}\frac{1}{x^2+\pi^2}\,dx = \frac{2\pi e^{-a}}{4a^2+\pi^2}-\frac{1}{1+e^{2a}}.
$$

## Setting up the rectangular contour

Consider the complex function

$$
f(z) = \frac{e^z}{(e^{2z}+e^{2a})z}.
$$

Notice why $f(z)$ is well suited to the horizontal lines $\operatorname{Im} z = \pm \pi$: on those lines $e^{x \pm i\pi} = -e^x$ and $e^{2(x \pm i\pi)} = e^{2x}$, so the exponential factor $\frac{e^z}{e^{2z}+e^{2a}}$ takes the exact same value $-\frac{e^x}{e^{2x}+e^{2a}}$ on both horizontal edges, while the remaining factor $\frac{1}{z}$ produces

$$
\frac{1}{x-i\pi} - \frac{1}{x+i\pi} = \frac{2\pi i}{x^2+\pi^2}.
$$

Let $\Gamma$ be the positively oriented rectangle in the complex plane with vertices $R-i\pi$, $R+i\pi$, $-R+i\pi$, and $-R-i\pi$, where $R > |a|$:

![Positively oriented rectangular contour with vertices at plus or minus R plus or minus i pi enclosing three simple poles]({static}/images/contour-rectangle-shifted-poles.svg)

## Computing the residues inside the contour

Inside $\Gamma$, the denominator $(e^{2z}+e^{2a})z$ vanishes at three points, each of which is a simple pole of $f(z)$:

- At $z = 0$, the residue is

$$
\mathop{\operatorname{Res}}_{z=0} f(z) = \lim_{z \to 0} z f(z) = \frac{1}{1+e^{2a}}.
$$

- The solutions of $e^{2z} = -e^{2a} = e^{2a \pm i\pi}$ with $\operatorname{Im} z \in (-\pi, \pi)$ are $z_\pm = a \pm \frac{i\pi}{2}$. At a simple zero $z_0$ of $e^{2z}+e^{2a}$, differentiating the denominator gives $\frac{d}{dz}(e^{2z}+e^{2a})\big|_{z=z_0} = 2e^{2z_0} = -2e^{2a}$. Since $e^{a \pm i\pi/2} = \pm i e^a$, the residues at $z_\pm$ are

$$
\begin{aligned}
\mathop{\operatorname{Res}}_{z=a+\frac{i\pi}{2}} f(z)
&= \frac{e^{a+\frac{i\pi}{2}}}{-2e^{2a}\left(a+\frac{i\pi}{2}\right)} = -\frac{i e^{-a}}{2a+i\pi}, \\
\mathop{\operatorname{Res}}_{z=a-\frac{i\pi}{2}} f(z)
&= \frac{e^{a-\frac{i\pi}{2}}}{-2e^{2a}\left(a-\frac{i\pi}{2}\right)} = \frac{i e^{-a}}{2a-i\pi}.
\end{aligned}
$$

By the residue theorem,

$$
\begin{aligned}
\int_\Gamma f(z)\,dz
&= 2\pi i \left( \mathop{\operatorname{Res}}_{z=0} f(z) + \mathop{\operatorname{Res}}_{z=a+\frac{i\pi}{2}} f(z) + \mathop{\operatorname{Res}}_{z=a-\frac{i\pi}{2}} f(z)\right) \\
&= 2\pi i \left( \frac{1}{1+e^{2a}} - \frac{i e^{-a}}{2a+i\pi} + \frac{i e^{-a}}{2a-i\pi}\right) \\
&= 2\pi i \left( \frac{1}{1+e^{2a}} - \frac{2\pi e^{-a}}{4a^2 +\pi^2}\right).
\end{aligned} \tag{1}
$$

## Relating the contour integral to the real integral

Breaking $\Gamma$ into its four sides and parameterizing the bottom and top edges by $z = x \mp i\pi$ for $x \in [-R, R]$, we have

$$
\begin{aligned}
\int_\Gamma f(z)\,dz
&= \int_{-R-i\pi}^{R-i\pi} f(z)\,dz + \int_{R-i\pi}^{R+i\pi} f(z)\,dz + \int_{R+i\pi}^{-R+i\pi} f(z)\,dz + \int_{-R+i\pi}^{-R-i\pi} f(z)\,dz \\
&= \int_{-R}^{R} \bigl(f(x-i\pi)-f(x+i\pi)\bigr)\,dx + \int_{R-i\pi}^{R+i\pi} f(z)\,dz + \int_{-R+i\pi}^{-R-i\pi} f(z)\,dz \\
&= -2\pi i \int_{-R}^{R} \frac{e^x}{e^{2x}+e^{2a}}\frac{1}{x^2+\pi^2}\,dx + \int_{R-i\pi}^{R+i\pi} f(z)\,dz + \int_{-R+i\pi}^{-R-i\pi} f(z)\,dz.
\end{aligned} \tag{2}
$$

## Bounding the vertical segments

On the right vertical edge $z = R + iy$ with $y \in [-\pi, \pi]$, we have $|R+iy| \geq R$ and, by the reverse triangle inequality for $R > |a|$,

$$
|e^{2R+2iy} + e^{2a}| = e^{2R}|e^{2iy} + e^{2a-2R}| \geq e^{2R}(1 - e^{2a-2R}).
$$

Hence

$$
\begin{aligned}
\left| \int_{R-i\pi}^{R+i\pi} f(z)\,dz\right|
&= \left|\int_{-\pi}^\pi f(R+iy)\,i\,dy \right| \\
&\leq e^R \int_{-\pi}^\pi \frac{dy}{|R+iy|\cdot |e^{2R+2iy}+e^{2a}|} \\
&\leq \frac{e^{-R}}{R} \int_{-\pi}^\pi \frac{dy}{|e^{2iy}+e^{2a-2R}|} \\
&\leq \frac{e^{-R}}{R} \frac{2\pi}{1-e^{2a-2R}}.
\end{aligned} \tag{3}
$$

Similarly, on the left vertical edge $z = -R + iy$, we have $|e^z| = e^{-R}$ and $|e^{-2R+2iy} + e^{2a}| \geq e^{2a} - e^{-2R}$ for $R > |a|$, so

$$
\left|\int_{-R+i\pi}^{-R-i\pi} f(z)\,dz \right| \leq \frac{e^{-R}}{R}\frac{2\pi}{e^{2a}-e^{-2R}}. \tag{4}
$$

From bounds (3) and (4), both vertical integrals tend to $0$ as $R \to \infty$. Equating (1) and (2) in the limit $R \to \infty$ and dividing by $-2\pi i$ yields

$$
\int_{-\infty}^\infty \frac{e^x}{e^{2x}+e^{2a}}\frac{1}{x^2+\pi^2}\,dx = \frac{2\pi e^{-a}}{4a^2+\pi^2}-\frac{1}{1+e^{2a}}.
$$

