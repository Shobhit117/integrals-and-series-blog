Title: A trigonometric integral via a semicircular contour
Date: 2026-10-24 10:06 +0530
Slug: a-trigonometric-integral-via-a-semicircular-contour
Author: Shobhit Bhatnagar
Category: Contour Integration
Tags: contour-integration, beta-function, gamma-function, trigonometric-integrals
Summary: A trigonometric substitution and integration around the right half of the unit disk reduce an inverse-sine integral to a beta function.
Status: published

Integrals containing nested inverse trigonometric functions often simplify dramatically after a change of variables that unwraps the inner function, followed by a passage to the unit circle in the complex plane. We will prove that for every $n \in \mathbb{N}$,

$$
\int_0^{\frac{\pi}{2}}\frac{\cos\left((2n-1)\arcsin\left(\frac{\sin x}{\sqrt{2}}\right) \right)}{\sqrt{1-\frac{\sin^2 x}{2}}}\,dx = \frac{\sqrt{\pi}}{2}\sin\left(\frac{n\pi}{2}\right)\frac{\Gamma\left(\frac{n}{2} \right)}{\Gamma\left(\frac{n+1}{2}\right)}.
$$

## Unwrapping the inverse sine

Let $I$ denote the integral. We begin with the substitution $\sin t = \frac{\sin x}{\sqrt{2}}$, so that $\cos t\,dt = \frac{\cos x}{\sqrt{2}}\,dx$. Since $\cos x = \sqrt{1 - 2\sin^2 t} = \sqrt{\cos(2t)}$ and $t$ runs from $0$ to $\frac{\pi}{4}$ as $x$ runs from $0$ to $\frac{\pi}{2}$, the factor $\sqrt{1 - \frac{\sin^2 x}{2}} = \cos t$ cancels against $\cos t\,dt$:

$$
I = \sqrt{2}\int_0^{\frac{\pi}{4}}\frac{\cos\bigl((2n-1) t\bigr)}{\sqrt{1-2\sin^2 t}}\,dt = \sqrt{2}\int_0^{\frac{\pi}{4}}\frac{\cos\bigl((2n-1) t\bigr)}{\sqrt{\cos(2t)}}\,dt.
$$

Next, substitute $\theta = 2t$ and use the evenness of the integrand on $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$:

$$
\begin{aligned}
I &= \frac{1}{\sqrt{2}} \int_{0}^{\frac{\pi}{2}}\frac{\cos\left(\frac{2n-1}{2}\theta\right)}{\sqrt{\cos \theta}}\,d\theta \\
&= \frac{1}{2\sqrt{2}} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{\cos\left(\frac{2n-1}{2}\theta\right)}{\sqrt{\cos \theta}}\,d\theta \\
&= \frac{1}{2\sqrt{2}} \operatorname{Re}\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{\exp\left(\frac{2n-1}{2}i\theta\right)}{\sqrt{\cos \theta}}\,d\theta.
\end{aligned} \tag{1}
$$

## Integrating around the right half of the unit disk

Now integrate the principal branch of

$$
f(z) = \frac{z^{n-1}}{\sqrt{1+z^2}}
$$

around the positively oriented contour in the right half-plane shown below:

![Right half-unit-disk contour bounded by the unit semicircle in the right half-plane and the imaginary axis with small circular indents at plus i and minus i]({static}/images/contour-right-semicircle.svg)

The contour consists of the right half of the unit circle $|z|=1$ ($-\frac{\pi}{2} < \arg z < \frac{\pi}{2}$), the segment of the imaginary axis between $+i$ and $-i$, and two small circular indents of radius $\epsilon$ avoiding the branch points at $z = \pm i$. Near $z = \pm i$, we have $|1+z^2| = |z-i||z+i| \sim 2\epsilon$, so $|f(z)| = O(\epsilon^{-1/2})$ while the arc length of each indent is $O(\epsilon)$. Thus the integrals along both indents are $O(\epsilon^{1/2})$ and vanish as $\epsilon \to 0^+$.

Since $f(z)$ is analytic inside the indented region, Cauchy's theorem equates the integral over the right semicircle to the integral upwards along the imaginary axis from $-i$ to $+i$. Parameterizing the imaginary axis by $z = iy$ with $y \in (-1, 1)$ and $dz = i\,dy$ gives

$$
\begin{aligned}
\int_{\left\{z\in \mathbb{C} :\; |z|=1, \; -\frac{\pi}{2}<\arg z < \frac{\pi}{2} \right\}}\frac{z^{n-1}}{\sqrt{1+z^2}}\,dz
&= \int_{-i}^i \frac{z^{n-1}}{\sqrt{1+z^2}}\,dz \\
&= i^{n}\int_{-1}^1 \frac{y^{n-1}}{\sqrt{1-y^2}}\,dy \\
&= \begin{cases}
2 i^n \int_0^1 \frac{y^{n-1}}{\sqrt{1-y^2}}\,dy, & n\text{ odd},\\
0, & n\text{ even}.
\end{cases}
\end{aligned} \tag{2}
$$

Notice that when $n = 2k+1$ is odd, $i^n = i(-1)^k = i\sin\left(\frac{n\pi}{2}\right)$, whereas when $n$ is even, $\sin\left(\frac{n\pi}{2}\right) = 0$. Hence, for every $n \in \mathbb{N}$, equation (2) can be written in the unified form

$$
\int_{\left\{z\in \mathbb{C} :\; |z|=1, \; -\frac{\pi}{2}<\arg z < \frac{\pi}{2} \right\}}\frac{z^{n-1}}{\sqrt{1+z^2}}\,dz = 2i\sin\left(\frac{n\pi}{2}\right)\int_0^1 \frac{y^{n-1}}{\sqrt{1-y^2}}\,dy. \tag{2'}
$$

## Parameterizing the semicircular arc

On the right unit semicircle, set $z = e^{i\theta}$ for $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$, with $dz = i e^{i\theta}\,d\theta$. Since $1 + e^{2i\theta} = 2e^{i\theta}\cos\theta$ and $\cos\theta > 0$ on $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, the principal square root is $\sqrt{1+e^{2i\theta}} = \sqrt{2\cos\theta}\,e^{\frac{i\theta}{2}}$. Therefore,

$$
\begin{aligned}
\int_{\left\{z\in \mathbb{C} :\; |z|=1, \; -\frac{\pi}{2}<\arg z < \frac{\pi}{2} \right\}}\frac{z^{n-1}}{\sqrt{1+z^2}}\,dz
&= i\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{e^{in \theta}}{\sqrt{1+e^{2i\theta}}}\,d\theta \\
&= i\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{e^{\frac{2n-1}{2}i \theta}}{\sqrt{e^{i\theta}+e^{-i\theta}}}\,d\theta \\
&= \frac{i}{\sqrt{2}}\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{e^{\frac{2n-1}{2}i \theta}}{\sqrt{\cos \theta}}\,d\theta.
\end{aligned} \tag{3}
$$

Combining equations (1), (2'), and (3), and finally setting $\xi = y^2$ ($d\xi = 2y\,dy$) to reduce the remaining integral to Euler's beta function $B\left(\frac{n}{2}, \frac{1}{2}\right)$, we conclude that

$$
\begin{aligned}
I &= \sin\left(\frac{n\pi}{2}\right)\int_0^1 \frac{y^{n-1}}{\sqrt{1-y^2}}\,dy \\
&= \frac{1}{2}\sin\left(\frac{n\pi}{2}\right)\int_0^1 \xi^{\frac{n}{2}-1}(1-\xi)^{-\frac{1}{2}}\,d\xi \\
&= \frac{\sqrt{\pi}}{2}\sin\left(\frac{n\pi}{2}\right)\frac{\Gamma\left(\frac{n}{2} \right)}{\Gamma\left(\frac{n+1}{2}\right)}.
\end{aligned}
$$

