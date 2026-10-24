Title: Mellin transforms of sine and cosine via a quarter-circle contour
Date: 2026-10-24 10:05 +0530
Slug: mellin-transforms-of-sine-and-cosine-via-a-quarter-circle-contour
Author: Shobhit Bhatnagar
Category: Contour Integration
Tags: contour-integration, gamma-function, mellin-transform, trigonometric-integrals
Summary: Rotating the positive real axis to the positive imaginary axis via an indented quarter-circle contour evaluates the Mellin transforms of sine and cosine.
Status: published

Rotating the positive real axis onto the positive imaginary axis turns the oscillatory factor $e^{ix}$ into the rapidly decaying factor $e^{-y}$, converting oscillatory improper integrals into Euler's gamma integral. Using this idea, we will establish the formulas

$$
\begin{aligned}
\int_0^\infty x^{s-1} \sin(x)\,dx &= \begin{cases} \sin\left(\frac{\pi s}{2}\right)\Gamma(s), & s\in (-1,0)\cup (0,1), \\ \frac{\pi}{2}, & s=0, \end{cases} \\
\int_0^\infty x^{s-1} \cos(x)\,dx &= \cos\left(\frac{\pi s}{2}\right)\Gamma(s), \qquad 0 < s < 1.
\end{aligned}
$$

## Contour integration for $0 < s < 1$

Let $f(z) = z^{s-1} e^{iz}$, where $0 < s < 1$ and the principal branch of the logarithm ($-\pi < \arg z \leq \pi$) defines $z^{s-1} = e^{(s-1)\log z}$. We integrate $f(z)$ around the positively oriented indented quarter-circle contour shown below, and then let $R \to \infty$ and $\epsilon \to 0^+$:

![Quarter-circle contour in the first quadrant bounded by arcs C_epsilon and C_R and segments along the positive real and imaginary axes]({static}/images/contour-quarter-circle.svg)

Here $C_R$ and $C_\epsilon$ are quarter-circles centered at $z=0$ of radii $R$ and $\epsilon$, respectively, and $C_\epsilon$ avoids the branch point at $z=0$. Since $f(z)$ is analytic inside and on the contour, Cauchy's integral theorem gives

$$
\int_\epsilon^R f(z)\,dz + \int_{C_R} f(z)\,dz + \int_{iR}^{i\epsilon} f(z)\,dz + \int_{C_\epsilon}f(z)\,dz = 0. \tag{1}
$$

On the vertical segment from $iR$ down to $i\epsilon$, parameterizing by $z = iy$ ($y \in [\epsilon, R]$, $dz = i\,dy$) and using $(iy)^{s-1} i = i^s y^{s-1} = e^{\frac{i\pi s}{2}} y^{s-1}$ gives

$$
\int_{iR}^{i\epsilon}f(z)\,dz = -i \int_\epsilon^R f(iy)\,dy = -e^{\frac{i\pi s}{2}}\int_\epsilon^R y^{s-1} e^{-y}\,dy. \tag{2}
$$

## Bounding the circular arcs

On $C_R$, parameterize $z = R e^{i\theta}$ for $0 \leq \theta \leq \frac{\pi}{2}$. Then $\left|e^{i R e^{i\theta}}\right| = e^{-R\sin\theta}$, and by Jordan's inequality $\sin\theta \geq \frac{2\theta}{\pi}$ on $\left[0, \frac{\pi}{2}\right]$, we obtain

$$
\begin{aligned}
\left|\int_{C_R} f(z)\,dz\right|
&= R^s \left| \int_0^{\frac{\pi}{2}} e^{i R e^{i\theta}} e^{i\theta s}\,d\theta\right| \\
&\leq R^s \int_0^{\frac{\pi}{2}} \left| e^{i R e^{i\theta}} \right|\,d\theta \\
&\leq R^s \int_0^{\frac{\pi}{2}} e^{-R \frac{2\theta}{\pi}}\,d\theta \\
&= \frac{\pi}{2}R^{s-1} \left(1-e^{-R} \right).
\end{aligned}
$$

Since $s < 1$, we have $R^{s-1} \to 0$ as $R \to \infty$, so

$$
\lim_{R\to \infty}\left|\int_{C_R} f(z)\,dz\right| = 0. \tag{3}
$$

By the exact same estimate on $C_\epsilon$ (or simply noting $\left|e^{i\epsilon e^{i\theta}}\right| \leq 1$ so the integral is bounded by $\frac{\pi}{2}\epsilon^s$), the condition $s > 0$ ensures that $1 - e^{-\epsilon} = O(\epsilon)$ and hence

$$
\left|\int_{C_\epsilon} f(z)\,dz\right| \leq \frac{\pi}{2}\epsilon^{s-1} \left(1-e^{-\epsilon} \right) = O(\epsilon^s) \to 0 \quad \text{as} \quad \epsilon \to 0^+. \tag{4}
$$

Combining equations (1), (2), (3), and (4) in the limits $R \to \infty$ and $\epsilon \to 0^+$ yields

$$
\begin{aligned}
\int_0^\infty x^{s-1} e^{ix}\,dx
&= e^{\frac{i\pi s}{2}} \int_0^\infty y^{s-1} e^{-y}\,dy \\
&= \left(\cos\left(\frac{\pi s}{2}\right) + i \sin\left(\frac{\pi s}{2}\right) \right) \Gamma(s).
\end{aligned}
$$

Separating the imaginary and real parts gives, for $0 < s < 1$,

$$
\int_0^\infty x^{s-1} \sin(x)\,dx = \sin\left(\frac{\pi s}{2}\right)\Gamma(s), \tag{5}
$$

$$
\int_0^\infty x^{s-1} \cos(x)\,dx = \cos\left(\frac{\pi s}{2}\right)\Gamma(s). \tag{6}
$$

## Extending the sine integral to $-1 < s \leq 0$

Because $\sin x = O(x)$ near $x=0$, the sine integral $I(s) = \int_0^\infty x^{s-1} \sin(x)\,dx$ converges on the wider strip $-1 < s < 1$. We have already proved that $I(s) = \sin\left(\frac{\pi s}{2}\right)\Gamma(s)$ for $0 < s < 1$.

Now suppose $-1 < s < 0$. Integrating by parts with $u = \sin x$ and $dv = x^{s-1}\,dx$ gives

$$
I(s) = \left[ \frac{x^s \sin(x)}{s} \right]_0^\infty - \frac{1}{s}\int_0^\infty x^s \cos(x)\,dx.
$$

At the upper limit $x \to \infty$, $|x^s \sin x| \leq x^s \to 0$ because $s < 0$; at the lower limit $x \to 0^+$, $x^s \sin x \sim x^{s+1} \to 0$ because $s > -1$. Moreover, since $0 < s+1 < 1$, we can apply equation (6) with $s+1$ in place of $s$, together with the functional equation $\Gamma(s+1) = s\Gamma(s)$:

$$
\begin{aligned}
I(s) &= -\frac{1}{s} \int_0^\infty x^{(s+1)-1} \cos(x)\,dx \\
&= -\frac{1}{s} \cos\left(\frac{\pi}{2}(s+1) \right)\Gamma(s+1) \\
&= \sin\left(\frac{\pi s}{2}\right)\Gamma(s).
\end{aligned}
$$

Finally, the case $s=0$ is the classic Dirichlet integral

$$
I(0) = \int_0^\infty \frac{\sin(x)}{x}\,dx = \frac{\pi}{2},
$$

which matches the removable singularity of $\sin\left(\frac{\pi s}{2}\right)\Gamma(s)$ at $s=0$:

$$
\lim_{s\to 0} \left[ \sin\left(\frac{\pi s}{2}\right)\Gamma(s) \right] = \lim_{s\to 0} \left[ \frac{\sin\left(\frac{\pi s}{2}\right)}{s}\Gamma(s+1) \right] = \frac{\pi}{2}.
$$

In [a companion post]({filename}/posts/evaluating-a-logarithmic-fresnel-integral-by-differentiating-under-the-integral-sign.md), we differentiate this identity at $s=0$ to evaluate a logarithmic Fresnel integral.

