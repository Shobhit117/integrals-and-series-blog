Title: A logarithmic sine integral via a keyhole contour
Date: 2026-10-24 10:07 +0530
Slug: a-logarithmic-sine-integral-via-a-keyhole-contour
Author: Shobhit Bhatnagar
Category: Contour Integration
Tags: contour-integration, residue-theorem, logarithmic-integrals
Summary: Integrating a complex power around a keyhole cut along the negative real axis evaluates a rational integral involving the sine of a logarithm.
Status: published

Integrals on $(0, \infty)$ containing $\sin(\ln x)$ or $\cos(\ln x)$ are the imaginary and real parts of $\int_0^\infty x^i R(x)\,dx$, since $x^i = e^{i\ln x} = \cos(\ln x) + i\sin(\ln x)$. By placing a keyhole branch cut along the negative real axis $(-\infty, 0]$ for an even rational function $R(z)$, the integrals along the upper and lower banks of the cut both fold onto $(0, \infty)$ with different constant factors $e^{-\pi}$ and $e^{\pi}$. We will use this method to prove

$$
\int_0^\infty \frac{\sin(\ln x)}{x^2+4}\,dx = \frac{\pi \sin(\ln 2)}{4\cosh\left(\frac{\pi}{2}\right)}.
$$

## The keyhole contour

Consider the function

$$
f(z) = \frac{e^{i\log z}}{4+z^2},
$$

where the branch of the logarithm is chosen with $-\pi < \arg z \leq \pi$, so the branch cut lies along the negative real axis $(-\infty, 0]$. We integrate $f(z)$ around the positively oriented keyhole contour shown below:

![Keyhole contour cut along the negative real axis with outer circle C_R, inner semicircle C_epsilon around the origin, and simple poles at plus 2i and minus 2i]({static}/images/contour-keyhole-negative-real.svg)

Here $C_R$ is a large circle of radius $R > 2$ and $C_\epsilon$ is a small semicircle of radius $\epsilon < 2$, both centered at the origin. On the circle $|z| = r$, we have $\left|e^{i\log z}\right| = e^{-\arg z} \leq e^\pi$, so

$$
\left|\int_{C_R} f(z)\,dz\right| \leq \frac{2\pi R e^\pi}{R^2 - 4} \to 0 \quad (R \to \infty)
\qquad\text{and}\qquad
\left|\int_{C_\epsilon} f(z)\,dz\right| \leq \frac{\pi\epsilon e^\pi}{4 - \epsilon^2} \to 0 \quad (\epsilon \to 0^+).
$$

Thus, in the limits $R \to \infty$ and $\epsilon \to 0^+$, only the two horizontal segments just above and just below the negative real axis contribute to the contour integral.

## Computing the residues at $\pm 2i$

Inside the contour, $f(z)$ has simple poles at $z = 2i$ and $z = -2i$. Using the branch $-\pi < \arg z \leq \pi$, we have $\log(2i) = \ln 2 + i\frac{\pi}{2}$ and $\log(-2i) = \ln 2 - i\frac{\pi}{2}$. Hence,

$$
\begin{aligned}
\mathop{\operatorname{Res}}_{z=2i} f(z)
&= \lim_{z\to 2i} (z-2i) \frac{e^{i\log z}}{z^2+4} \\
&= \frac{e^{i\log(2i)}}{4i} \\
&= \frac{e^{i\ln 2 - \frac{\pi}{2}}}{4i},
\end{aligned}
$$

and similarly,

$$
\mathop{\operatorname{Res}}_{z=-2i} f(z) = -\frac{e^{i\log(-2i)}}{4i} = -\frac{e^{i\ln 2 + \frac{\pi}{2}}}{4i}.
$$

## Evaluating the integral along the branch cut

On the upper bank of the negative real axis (traversed from $-\infty$ to $0$), $\arg z = +\pi$, so $\log z = \ln|x| + i\pi$ and $e^{i\log z} = e^{-\pi}e^{i\ln|x|}$. On the lower bank (traversed from $0$ to $-\infty$), $\arg z = -\pi$, so $\log z = \ln|x| - i\pi$ and $e^{i\log z} = e^{\pi}e^{i\ln|x|}$. Substituting $t = -x > 0$ (and relabeling $t$ as $x$) on both banks, the residue theorem gives

$$
\begin{aligned}
\int_{-\infty}^0 \frac{e^{i(\ln|x|+i\pi)}}{4+x^2}\,dx + \int_0^{-\infty} \frac{e^{i(\ln|x|-i\pi)}}{4+x^2}\,dx
&= 2\pi i \left(\mathop{\operatorname{Res}}_{z=2i} f(z) + \mathop{\operatorname{Res}}_{z=-2i} f(z)\right) \\
\implies e^{-\pi}\int_0^\infty \frac{e^{i\ln x}}{4+x^2}\,dx - e^{\pi}\int_0^\infty \frac{e^{i\ln x}}{4+x^2}\,dx
&= 2\pi i \left( \frac{e^{i\ln 2}}{4i}e^{-\frac{\pi}{2}}- \frac{e^{i\ln 2}}{4i}e^{\frac{\pi}{2}}\right) \\
\implies -2\sinh(\pi) \int_0^\infty \frac{e^{i\ln x}}{4+x^2}\,dx
&= -\sinh\left(\frac{\pi}{2}\right) \pi e^{i\ln 2}.
\end{aligned}
$$

Using the double-angle identity $\sinh(\pi) = 2\sinh\left(\frac{\pi}{2}\right)\cosh\left(\frac{\pi}{2}\right)$ to simplify the ratio of hyperbolic sines, we obtain

$$
\int_0^\infty \frac{e^{i\ln x}}{4+x^2}\,dx = \frac{\pi e^{i\ln 2}}{4\cosh\left(\frac{\pi}{2}\right)}.
$$

Taking the imaginary part of both sides yields the desired evaluation:

$$
\int_0^\infty \frac{\sin(\ln x)}{x^2+4}\,dx = \frac{\pi \sin(\ln 2)}{4\cosh\left(\frac{\pi}{2}\right)}.
$$

Equating the real parts simultaneously gives the companion cosine integral:

$$
\int_0^\infty \frac{\cos(\ln x)}{x^2+4}\,dx = \frac{\pi \cos(\ln 2)}{4\cosh\left(\frac{\pi}{2}\right)}.
$$

