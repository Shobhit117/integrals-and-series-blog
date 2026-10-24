Title: An integral involving the squared arctangent of sine squared
Date: 2026-10-24 10:09 +0530
Slug: an-integral-involving-the-squared-arctangent-of-sine-squared
Author: Shobhit Bhatnagar
Category: Feynman's Trick
Tags: feynmans-trick, trigonometric-integrals, definite-integrals
Summary: Integration by parts followed by differentiation under the integral sign reduces a squared-arctangent trigonometric integral to an elementary antiderivative.
Status: published

In this post we combine integration by parts with differentiation under the integral sign to evaluate

$$
\int_0^{\frac{\pi}{2}} \frac{\arctan^2 (\sin^2 \theta)}{\sin^2 \theta}\,d\theta = \pi \log\left( \frac{2+\sqrt{2}}{4}\right) \sqrt{\frac{\sqrt{2}+1}{2}}+\frac{\pi^2}{4}\sqrt{\frac{\sqrt{2}-1}{2}}.
$$

## Integration by parts and introducing a parameter

Let $I$ denote the integral. Integrating by parts with $u = \arctan^2(\sin^2 x)$ and $dv = \frac{dx}{\sin^2 x}$ (so $v = -\cot x$ and $du = \frac{4\sin x \cos x \arctan(\sin^2 x)}{1+\sin^4 x}\,dx$), the boundary term $\bigl[-\cot x \arctan^2(\sin^2 x)\bigr]_0^{\pi/2}$ vanishes at both endpoints because $\cot(\pi/2) = 0$ and $\cot x \arctan^2(\sin^2 x) = O(x^3)$ as $x \to 0^+$. Thus,

$$
I = \int_{0}^{\frac{\pi}{2}}\frac{\arctan^2(\sin^2 x)}{\sin^2 x}\,dx = 4\int_0^{\frac{\pi}{2}}\frac{\cos^2 x\arctan(\sin^2 x)}{1+\sin^4 x}\,dx.
$$

To eliminate the remaining arctangent, introduce a parameter $\alpha \in [0,1]$:

$$
f(\alpha) = \int_0^{\frac{\pi}{2}}\frac{\cos^2 x\arctan(\alpha \sin^2 x)}{1+\sin^4 x}\,dx,
$$

so that $f(0) = 0$ and $I = 4f(1)$. Differentiating inside the integral with respect to $\alpha$ and decomposing into partial fractions in $\sin^4 x$ gives

$$
\begin{aligned}
f'(\alpha) &= \int_0^{\frac{\pi}{2}}\frac{\cos^2 x}{1+\sin^4 x}\cdot\frac{\sin^2 x}{1+\alpha^2 \sin^4 x}\,dx \\
&= \frac{1}{1-\alpha^2}\int_0^{\frac{\pi}{2}}\frac{\cos^2 x\sin^2 x}{1+\sin^4 x}\,dx - \frac{\alpha^2}{1-\alpha^2}\int_0^{\frac{\pi}{2}}\frac{\cos^2 x\sin^2 x}{1+\alpha^2 \sin^4 x}\,dx.
\end{aligned}
$$

Define the auxiliary integral

$$
g(\alpha) = \int_0^{\frac{\pi}{2}}\frac{\cos^2 x\sin^2 x}{1+\alpha^2 \sin^4 x}\,dx.
$$

Then $f'(\alpha) = \frac{g(1) - \alpha^2 g(\alpha)}{1 - \alpha^2}$, and integrating from $\alpha = 0$ to $\alpha = 1$ yields

$$
I = 4f(1) = 4\int_0^1\frac{g(1)-\alpha^2 g(\alpha)}{1-\alpha^2}\,d\alpha. \tag{1}
$$

## Evaluating the auxiliary integral $g(\alpha)$

Substituting $t = \tan x$ (so $\sin^2 x = \frac{t^2}{1+t^2}$, $\cos^2 x = \frac{1}{1+t^2}$, and $dx = \frac{dt}{1+t^2}$) and applying partial fractions, we obtain

$$
\begin{aligned}
g(\alpha) &= \int_0^{\frac{\pi}{2}}\frac{\cos^2 x\sin^2 x}{1+\alpha^2 \sin^4 x}\,dx \\
&= \int_0^\infty \frac{t^2}{\bigl((1+\alpha^2)t^4+2t^2+1\bigr)(t^2+1)}\,dt \\
&= -\frac{1}{\alpha^2}\int_0^\infty\frac{1}{1+t^2}\,dt + \frac{1}{\alpha^2}\int_0^\infty\frac{1+(1+\alpha^2)t^2}{(1+\alpha^2)t^4+2t^2+1}\,dt.
\end{aligned}
$$

The first integral is $\frac{\pi}{2}$. For the second integral, put $r = \sqrt[4]{1+\alpha^2}$ and $s = rt$. Then

$$
\begin{aligned}
\int_0^\infty\frac{1+r^4 t^2}{r^4 t^4+2t^2+1}\,dt
&= \frac{1}{r}\int_0^\infty \frac{1+r^2 s^2}{s^4 + \frac{2}{r^2}s^2 + 1}\,ds \\
&= \frac{1+r^2}{2r}\int_0^\infty \frac{1 + \frac{1}{s^2}}{\left(s - \frac{1}{s}\right)^2 + 2 + \frac{2}{r^2}}\,ds,
\end{aligned}
$$

where the last step averages the integral with its image under $s \mapsto 1/s$. Substituting $w = s - \frac{1}{s} \in (-\infty, \infty)$ gives a standard Cauchy integral:

$$
\frac{1+r^2}{2r}\int_{-\infty}^\infty \frac{dw}{w^2 + \frac{2(r^2+1)}{r^2}} = \frac{1+r^2}{2r}\cdot\frac{\pi}{\sqrt{\frac{2(r^2+1)}{r^2}}} = \frac{\pi\sqrt{1+r^2}}{2\sqrt{2}} = \frac{\pi\sqrt{1+\sqrt{1+\alpha^2}}}{2\sqrt{2}}.
$$

Therefore,

$$
g(\alpha) = -\frac{\pi}{2\alpha^2} + \frac{\pi \sqrt{1+\sqrt{1+\alpha^2}}}{2\sqrt{2}\alpha^2}. \tag{2}
$$

Substituting (2) into equation (1), the $-\frac{\pi}{2}$ terms cancel between $\alpha^2 g(\alpha)$ and $g(1)$, leaving

$$
I = \pi\sqrt{2}\int_0^1\frac{\sqrt{1+\sqrt{2}}-\sqrt{1+\sqrt{1+\alpha^2}}}{1-\alpha^2}\,d\alpha. \tag{3}
$$

## Integrating with respect to $\alpha$

Integral (3) admits an elementary antiderivative via the two successive substitutions $t = \sqrt{1+\alpha^2}$ (so $\alpha\,d\alpha = t\,dt$ and $\frac{d\alpha}{1-\alpha^2} = \frac{t\,dt}{(2-t^2)\sqrt{t^2-1}}$) and $u = \sqrt{t-1}$ (so $t = u^2+1$ and $dt = 2u\,du$):

$$
\begin{aligned}
&\int \frac{\sqrt{1+\sqrt{2}}-\sqrt{1+\sqrt{1+\alpha^2}}}{1-\alpha^2}\,d\alpha \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - \int \frac{\sqrt{1+\sqrt{1+\alpha^2}}}{1-\alpha^2}\,d\alpha \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - \int \frac{t\sqrt{1+t}}{(2-t^2)\sqrt{t^2-1}}\,dt \quad \left(t=\sqrt{1+\alpha^2}\right) \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - \int \frac{t}{(2-t^2)\sqrt{t-1}}\,dt \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - 2\int \frac{u^2+1}{2-(u^2+1)^2}\,du \quad \left(u=\sqrt{t-1}\right) \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - 2\int \frac{u^2+1}{(\sqrt{2}-1-u^2)(\sqrt{2}+1+u^2)}\,du \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - \int\frac{du}{\sqrt{2}-1-u^2} + \int\frac{du}{\sqrt{2}+1+u^2} \\
&= \sqrt{1+\sqrt{2}}\operatorname{arctanh}(\alpha) - \sqrt{\sqrt{2}+1}\operatorname{arctanh}\left( u \sqrt{\sqrt{2}+1}\right) + \sqrt{\sqrt{2}-1}\arctan\left(u\sqrt{\sqrt{2}-1} \right) + C.
\end{aligned}
$$

At the lower endpoint $\alpha = 0$, we have $u = 0$, so the antiderivative evaluates to $0$. As $\alpha \to 1^-$, we have $u = \sqrt{\sqrt{1+\alpha^2}-1} \to \sqrt{\sqrt{2}-1}$. For the $\arctan$ term, $u\sqrt{\sqrt{2}-1} \to \sqrt{2}-1 = \tan\left(\frac{\pi}{8}\right)$, so $\arctan(\sqrt{2}-1) = \frac{\pi}{8}$. For the difference of the two $\operatorname{arctanh}$ terms, set $c = \sqrt{\sqrt{2}+1}$ and use the factorization $1-\alpha^2 = (\sqrt{2}-1-u^2)(\sqrt{2}+1+u^2) = c^{-2}(1-c^2 u^2)(c^2+u^2)$:

$$
\begin{aligned}
\lim_{\alpha\to 1^-}\bigl(\operatorname{arctanh}(\alpha) - \operatorname{arctanh}(cu)\bigr)
&= \frac{1}{2}\lim_{\alpha\to 1^-}\log\left(\frac{1+\alpha}{1+cu}\cdot\frac{1+\alpha}{1+cu}\cdot\frac{1-c^2 u^2}{1-\alpha^2}\right) \\
&= \frac{1}{2}\lim_{u^2\to \sqrt{2}-1}\log\left(\frac{c^2}{c^2+u^2}\right) \\
&= \frac{1}{2}\log\left(\frac{\sqrt{2}+1}{2\sqrt{2}}\right) = \frac{1}{2}\log\left(\frac{2+\sqrt{2}}{4}\right).
\end{aligned}
$$

Putting everything together, we conclude that

$$
\begin{aligned}
I &= \pi\sqrt{2}\left\{\frac{\sqrt{\sqrt{2}+1}}{2}\log\left(\frac{\sqrt{2}+2}{4} \right) + \sqrt{\sqrt{2}-1}\arctan(\sqrt{2}-1)\right\} \\
&= \pi\sqrt{2}\left\{\frac{\sqrt{\sqrt{2}+1}}{2}\log\left(\frac{\sqrt{2}+2}{4} \right) + \frac{\pi}{8}\sqrt{\sqrt{2}-1}\right\} \\
&= \pi \log\left( \frac{2+\sqrt{2}}{4}\right) \sqrt{\frac{\sqrt{2}+1}{2}}+\frac{\pi^2}{4}\sqrt{\frac{\sqrt{2}-1}{2}}.
\end{aligned}
$$

In [a later post on Lobachevsky-type integrals]({filename}/posts/lobachevsky-type-logarithmic-integrals-via-partial-fraction-series.md), we show that the improper integral $\int_0^\infty \frac{\arctan^2(\sin^2 x)}{x^2}\,dx$ reduces to this exact same value.

